#!/usr/bin/env python3
"""Offline public-paper catalogue: validate, merge, generate. Python 3.9+, stdlib only."""
import argparse
import copy
import datetime as dt
import fcntl
import hashlib
import html
import ipaddress
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from contextlib import contextmanager
from urllib.parse import parse_qsl, quote, unquote, urlencode, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ('vigen-seed', 'video-avatar', 'embodied-world', 'interactive-video')
CATEGORIES = ('视频生成基础', '少步蒸馏', '交互长视频', '流式系统', '具身与世界模型', '交互 Avatar')
PARTS = {'problem': '问题', 'method': '方法', 'value': '价值', 'limitation': '局限'}
FIELDS = {'id', 'title', 'short_name', 'published', 'category', 'tags', 'arxiv_id', 'doi',
          'paper_url', 'links', 'summary', 'evidence_urls', 'verified_at',
          'first_seen', 'last_seen', 'discovery_sources'}
ARXIV = re.compile(r'(?:\d{4}\.\d{4,5}|[a-z-]+(?:\.[A-Z]{2})?/\d{7})(?:v\d+)?$', re.I)


def date(value):
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
        raise ValueError('Dates must be YYYY-MM-DD')
    dt.date.fromisoformat(value)
    return value


def text(value, name, maximum=500):
    if not isinstance(value, str) or not value.strip() or len(value) > maximum:
        raise ValueError(f'Invalid {name}')
    if any(ord(c) < 32 for c in value) or '<' in value or '>' in value:
        raise ValueError(f'{name}: only plain single-line text is accepted')
    if re.search(r'(?i)(/Users/|/home/|file://|(?:gh[pousr]_|github_pat_)[A-Za-z0-9_]{10,}|sk-[A-Za-z0-9]{16,}|-----BEGIN .*PRIVATE KEY)', value):
        raise ValueError(f'{name}: local paths or credential-like strings are not public metadata')
    return value.strip()


def canonical_url(value):
    text(value, 'URL', 1500)
    u = urlsplit(value)
    host = (u.hostname or '').lower()
    if u.scheme not in ('https', 'http') or not host or u.username or u.password or u.port not in (None, 80, 443):
        raise ValueError('Only public HTTP(S) URLs without credentials or custom ports are accepted')
    if host in ('localhost',) or host.endswith(('.local', '.internal', '.localhost')) or '.' not in host:
        raise ValueError('Local URLs are not allowed')
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        address = None
    if address and not address.is_global:
        raise ValueError('Private network URLs are not allowed')
    query = []
    for key, val in parse_qsl(u.query, keep_blank_values=True):
        if re.search(r'(?i)(token|secret|signature|credential|api.?key|password|x-amz)', key):
            raise ValueError('Signed or credential-bearing URLs are not allowed')
        if not key.lower().startswith('utm_') and key.lower() not in ('ref', 'fbclid', 'gclid'):
            query.append((key, val))
    path = quote(unquote(u.path), safe='/@:._~-')
    if path != '/':
        path = path.rstrip('/')
    # HTTP and HTTPS identify the same public paper for deduplication.
    return urlunsplit(('https', host, path or '/', urlencode(sorted(query)), ''))


def arxiv(value):
    if not value:
        return None
    value = unquote(value.strip())
    if value.lower().startswith('arxiv:'):
        value = value[6:]
    if '://' in value:
        u = urlsplit(value)
        if (u.hostname or '').lower() not in ('arxiv.org', 'www.arxiv.org', 'export.arxiv.org'):
            return None
        value = re.sub(r'^/(abs|pdf|html)/', '', u.path).removesuffix('.pdf')
    if not ARXIV.fullmatch(value):
        return None
    return re.sub(r'v\d+$', '', value, flags=re.I).lower()


def doi(value):
    if not value:
        return None
    value = unquote(value.strip()).lower()
    value = re.sub(r'^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)', '', value)
    if not re.fullmatch(r'10\.\d{4,9}/[^\s]+', value):
        raise ValueError('Invalid DOI')
    return value


def normalize(raw, source=None, observed=None):
    if not isinstance(raw, dict) or set(raw) - FIELDS:
        raise ValueError('Unknown paper fields: export only the documented public schema')
    p = {k: text(raw.get(k), k, 500) for k in ('title', 'short_name')}
    p['published'] = date(raw['published']) if raw.get('published') else None
    p['category'] = raw.get('category')
    if p['category'] not in CATEGORIES:
        raise ValueError('Unknown category')
    tags = raw.get('tags', [])
    if not isinstance(tags, list) or len(tags) > 12:
        raise ValueError('tags must be a list of at most 12 strings')
    p['tags'] = sorted(set(text(t, 'tag', 60) for t in tags))
    paper_url = canonical_url(raw['paper_url'])
    explicit_arxiv = arxiv(raw.get('arxiv_id'))
    if raw.get('arxiv_id') and not explicit_arxiv:
        raise ValueError('Invalid arXiv ID')
    p['doi'] = doi(raw.get('doi'))
    candidates = {a for a in (explicit_arxiv, arxiv(paper_url),
                  arxiv(p['doi'][len('10.48550/arxiv.'):]) if p['doi'] and p['doi'].startswith('10.48550/arxiv.') else None) if a}
    if len(candidates) > 1:
        raise ValueError('Conflicting arXiv identities')
    p['arxiv_id'] = next(iter(candidates), None)
    url_doi = doi(unquote(urlsplit(paper_url).path[1:])) if urlsplit(paper_url).hostname in ('doi.org', 'dx.doi.org') else None
    if p['doi'] and url_doi and p['doi'] != url_doi:
        raise ValueError('Conflicting DOI identities')
    p['doi'] = p['doi'] or url_doi
    if p['doi'] and p['doi'].startswith('10.48550/arxiv.'):
        from_doi = arxiv(p['doi'][len('10.48550/arxiv.'):])
        if not from_doi or (p['arxiv_id'] and p['arxiv_id'] != from_doi):
            raise ValueError('Conflicting arXiv DOI')
        p['arxiv_id'] = from_doi
    p['paper_url'] = 'https://arxiv.org/abs/' + p['arxiv_id'] if p['arxiv_id'] else paper_url
    if p['arxiv_id']:
        p['id'] = 'arxiv:' + p['arxiv_id']
    elif p['doi']:
        p['id'] = 'doi:' + p['doi']
    else:
        p['id'] = 'url:' + hashlib.sha256(paper_url.encode()).hexdigest()[:20]
    links = raw.get('links', {})
    if not isinstance(links, dict) or set(links) - {'project', 'code', 'weights'}:
        raise ValueError('Unknown link fields')
    p['links'] = {k: canonical_url(links[k]) if links.get(k) else None for k in ('project', 'code', 'weights')}
    summary = raw.get('summary', {})
    if not isinstance(summary, dict) or set(summary) != set(PARTS):
        raise ValueError('Summary must contain problem, method, value, limitation')
    p['summary'] = {k: text(summary[k], k, 160) for k in PARTS}
    length = sum(len(v) for v in p['summary'].values())
    if not 80 <= length <= 160:
        raise ValueError(f'Summary must be 80–160 characters; got {length}')
    evidence = raw.get('evidence_urls')
    if not isinstance(evidence, list) or not evidence or len(evidence) > 20:
        raise ValueError('At least one primary-source evidence URL is required')
    p['evidence_urls'] = sorted(set(canonical_url(u) for u in evidence))
    p['verified_at'] = date(raw['verified_at'])
    observed = date(observed) if observed else None
    if observed and p['verified_at'] > observed:
        raise ValueError('Verification date cannot follow observation date')
    p['first_seen'] = date(raw.get('first_seen', observed))
    p['last_seen'] = date(raw.get('last_seen', observed))
    if p['first_seen'] > p['last_seen']:
        raise ValueError('first_seen must not follow last_seen')
    origins = raw.get('discovery_sources', [])
    if not isinstance(origins, list):
        raise ValueError('discovery_sources must be a list')
    p['discovery_sources'] = sorted(set(origins + ([source] if source else [])))
    if not p['discovery_sources'] or any(s not in SOURCES for s in p['discovery_sources']):
        raise ValueError('Unknown discovery source')
    return p


def identities(p):
    keys = {'url:' + canonical_url(p['paper_url'])}
    if p['arxiv_id']:
        keys.update(('arxiv:' + p['arxiv_id'], 'doi:10.48550/arxiv.' + p['arxiv_id']))
    if p['doi']:
        keys.add('doi:' + p['doi'])
    return keys


def merge(old, new):
    for key in ('arxiv_id', 'doi'):
        if old[key] and new[key] and old[key] != new[key]:
            raise ValueError('Identity collision: conflicting ' + key)
    # Newer verified metadata wins; null optional links never erase verified links.
    older, newer = (old, new) if new['verified_at'] >= old['verified_at'] else (new, old)
    p = copy.deepcopy(newer)
    for key in ('arxiv_id', 'doi', 'published'):
        p[key] = newer[key] or older[key]
    p['links'] = {k: newer['links'][k] or older['links'][k] for k in newer['links']}
    for key in ('tags', 'evidence_urls', 'discovery_sources'):
        p[key] = sorted(set(old[key] + new[key]))
    p['first_seen'] = min(old['first_seen'], new['first_seen'])
    p['last_seen'] = max(old['last_seen'], new['last_seen'])
    return normalize(p)


def catalogue(raw):
    if not isinstance(raw, dict) or set(raw) != {'schema_version', 'papers'} or raw['schema_version'] != 1 or not isinstance(raw['papers'], list):
        raise ValueError('Expected {schema_version: 1, papers: [...]}')
    return raw['papers']


def load(root=ROOT):
    papers = [normalize(p) for p in catalogue(json.loads((root / 'data/papers.json').read_text()))]
    seen = set()
    for p in papers:
        if seen & identities(p):
            raise ValueError('Duplicate paper in canonical catalogue: ' + p['id'])
        seen.update(identities(p))
    return papers


def combine(existing, incoming, source, observed):
    result = copy.deepcopy(existing)
    for raw in incoming:
        p = normalize(raw, source, observed)
        p['first_seen'] = min(p['first_seen'], observed)
        p['last_seen'] = max(p['last_seen'], observed)
        matches = [i for i, old in enumerate(result) if identities(p) & identities(old)]
        for i in reversed(matches):
            p = merge(result.pop(i), p)
        result.append(p)
    return sorted(result, key=lambda p: (p['published'] or '', p['id']), reverse=True)


def dump(papers):
    return json.dumps({'schema_version': 1, 'papers': papers}, ensure_ascii=False, indent=2) + '\n'


def atomic(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix='.paper-watch-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as handle:
            handle.write(value)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


@contextmanager
def locked(root=ROOT):
    with (root / '.watch.lock').open('a') as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        yield


def esc(s):
    return html.escape(s, quote=True)


def paper_badges(p):
    badges = []
    code = p['links']['code']
    if code:
        parsed = urlsplit(code)
        parts = parsed.path.strip('/').split('/')
        if parsed.hostname == 'github.com' and len(parts) >= 2:
            repo = '/'.join(parts[:2])
            badges.append(('Star', f'https://img.shields.io/github/stars/{quote(repo, safe="/")}.svg?style=social&label=Star', 'https://github.com/' + repo))
        else:
            badges.append(('Code', 'https://img.shields.io/badge/Code-181717.svg', code))
    label = 'arXiv' if p['arxiv_id'] else 'Paper'
    badges.append((label, f'https://img.shields.io/badge/{label}-b31b1b.svg', p['paper_url']))
    for key, label, color in [('project', 'Project', '9cf'), ('weights', 'Weights', 'yellow')]:
        if p['links'][key]:
            badges.append((label, f'https://img.shields.io/badge/{label}-{color}.svg', p['links'][key]))
    return badges


def paper_links(p):
    return ' '.join(f'<a href="{esc(url)}" rel="noopener noreferrer"><img src="{esc(image)}" alt="{label}" loading="lazy" height="20"></a>'
                    for label, image, url in paper_badges(p))


def markdown_link(label, url):
    label = esc(label).replace('[', '&#91;').replace(']', '&#93;')
    return f'[{label}](<{url}>)'


def render_readme(papers):
    out = ['# Research Paper Watch', '',
           '公开论文精选：视频生成、交互 Avatar、具身与世界模型。每篇附可折叠中文简介与一手来源。', '',
           f'**{len(papers)} 篇论文** · [在线阅读（支持快捷键）](https://ripemangobox.github.io/research-paper-watch/) · [下载离线阅读器 ZIP](https://ripemangobox.github.io/research-paper-watch/research-paper-watch.zip) · [唯一数据源](data/papers.json) · [导入与任务接入](docs/INTEGRATION.md)', '',
           '在线阅读页直接支持搜索、分类、E 全部展开、C 全部收起。离线 ZIP 解压后双击 index.html，无需安装或启动服务器。GitHub README 不运行自定义脚本：可点击简介，或 Tab 聚焦后按 Enter / 空格展开收起；E / C 请使用在线阅读页。', '',
           '日期为论文首次公开日期；空链接表示尚未核实。简介中的局限包含基于公开证据的阅读边界，不代表作者自述的缺陷。', '',
           '## 目录', '']
    for category in CATEGORIES:
        count = sum(p['category'] == category for p in papers)
        if count:
            anchor = category.lower().replace(' ', '-')
            out.append(f'- [{category}](#{anchor}) · {count}')
    for category in CATEGORIES:
        group = [p for p in papers if p['category'] == category]
        if not group:
            continue
        out += ['', f'## {category}', '']
        for p in group:
            out += [f'+ {markdown_link(p["title"], p["paper_url"])}<br>',
                    '  ' + ' '.join(f'[![{label}]({image})](<{url}>)' for label, image, url in paper_badges(p)),
                    f'  <br>{p["published"] or "日期待核实"} · {esc(" / ".join(p["tags"]))}', '',
                    '  <details>', '  <summary>brief</summary>', '']
            for key, label in PARTS.items():
                out.append(f'  - **{label}**：{esc(p["summary"][key])}')
            out += ['', '  来源：' + ' · '.join(f'<a href="{esc(u)}">[{i+1}]</a>' for i, u in enumerate(p['evidence_urls'])),
                    f'  核验：{p["verified_at"]}', '', '  </details>', '']
    out += ['## 维护', '', 'Python 3.9+，无第三方依赖。', '', '```bash',
            'python3 scripts/paper_watch.py validate', 'python3 scripts/paper_watch.py build --check',
            'python3 -m unittest discover -s tests -v', 'node --test tests/reader.test.cjs', '```', '',
            '数据和源码公开；不收录 PDF、私人笔记、实验记录或会话原文。推送到 main 后自动验证并部署在线阅读页及离线 ZIP。云端研究任务的接入状态见 [接入说明](docs/INTEGRATION.md)。', '',
            '组织形式参考 [Awesome-Video-Diffusion](https://github.com/showlab/Awesome-Video-Diffusion)。摘要为本项目独立撰写；论文、模型和源码的使用条件以各原始发布方为准。', '']
    return '\n'.join(out)


def render_html(papers, root=ROOT):
    cards = []
    for index, p in enumerate(papers, 1):
        searchable = ' '.join([p['title'], p['short_name'], p['category'], *p['tags'], *p['summary'].values(), p['arxiv_id'] or '', p['doi'] or ''])
        paragraphs = ''.join(f'<p><strong>{label}</strong>{esc(p["summary"][key])}</p>' for key, label in PARTS.items())
        citations = ' · '.join(f'<a href="{esc(u)}" rel="noopener noreferrer">来源 {i+1}</a>' for i, u in enumerate(p['evidence_urls']))
        cards.append(f'''<article class="paper" data-category="{esc(p['category'])}" data-search="{esc(searchable.lower())}">
<div class="paper-meta"><span>{esc(p['category'])}</span><time>{p['published'] or '日期待核实'}</time><span class="number">{index:02d}</span></div>
<h2><a href="{esc(p['paper_url'])}">{esc(p['short_name'])}</a></h2><p class="paper-title"><a href="{esc(p['paper_url'])}">{esc(p['title'])}</a></p>
<p class="links">{paper_links(p)}</p>
<details><summary>brief <span aria-hidden="true">＋</span></summary><div class="abstract">{paragraphs}<p class="evidence">{citations} · 核验 {p['verified_at']}</p></div></details>
</article>''')
    options = ''.join(f'<option value="{esc(c)}">{esc(c)}</option>' for c in CATEGORIES)
    template = (root / 'web/template.html').read_text()
    return template.replace('<!--STYLE-->', (root / 'web/style.css').read_text()).replace('<!--SCRIPT-->', (root / 'web/reader.js').read_text()).replace('<!--CARDS-->', '\n'.join(cards)).replace('<!--OPTIONS-->', options).replace('<!--COUNT-->', str(len(papers)))


def build(root=ROOT, papers=None, check=False):
    papers = load(root) if papers is None else papers
    papers = sorted(papers, key=lambda p: (p['published'] or '', p['id']), reverse=True)
    outputs = {'README.md': render_readme(papers), 'dist/index.html': render_html(papers, root)}
    for name, body in outputs.items():
        target = root / name
        if check:
            if not target.exists() or target.read_text() != body:
                raise ValueError('Generated file is stale: ' + name)
        else:
            atomic(target, body)


def import_batch(path, source, observed, root=ROOT, dry_run=False):
    before = load(root)
    incoming = catalogue(json.loads(Path(path).read_text()))
    after = combine(before, incoming, source, observed)
    # Render before any write: a template/schema failure cannot partially import data.
    readme, page = render_readme(after), render_html(after, root)
    changed = dump(before) != dump(after)
    if changed and not dry_run:
        atomic(root / 'data/papers.json', dump(after))
        atomic(root / 'README.md', readme)
        atomic(root / 'dist/index.html', page)
    return {'input': len(incoming), 'before': len(before), 'after': len(after),
            'added': len(after) - len(before), 'changed': changed, 'dry_run': dry_run}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('validate')
    builder = sub.add_parser('build'); builder.add_argument('--check', action='store_true')
    imp = sub.add_parser('import'); imp.add_argument('input', type=Path)
    imp.add_argument('--source', required=True, choices=SOURCES)
    imp.add_argument('--date', required=True); imp.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        with locked():
            if args.command == 'validate':
                print(json.dumps({'valid': True, 'papers': len(load())}))
            elif args.command == 'build':
                build(check=args.check); print('Generated files are current' if args.check else 'Generated README.md and dist/index.html')
            else:
                print(json.dumps(import_batch(args.input, args.source, date(args.date), dry_run=args.dry_run)))
    except (ValueError, KeyError, TypeError, OSError) as error:
        print('Error: ' + str(error), file=sys.stderr); return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
