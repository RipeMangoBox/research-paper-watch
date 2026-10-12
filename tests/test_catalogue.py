import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from html.parser import HTMLParser

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import paper_watch as w


class CatalogueTests(unittest.TestCase):
    def setUp(self):
        self.seed = copy.deepcopy(w.load()[0])
        self.seed.update(first_seen='2026-10-12', last_seen='2026-10-12', verified_at='2026-10-12', discovery_sources=['vigen-seed'])

    def test_arxiv_versions_pdf_and_doi_match(self):
        for url in ['https://arxiv.org/pdf/2412.07772v4.pdf', 'https://export.arxiv.org/abs/2412.07772v2',
                    'https://doi.org/10.48550/arXiv.2412.07772']:
            p = copy.deepcopy(self.seed)
            p.update(arxiv_id=None, doi=None, paper_url=url)
            self.assertEqual(w.normalize(p)['id'], 'arxiv:2412.07772')

    def test_doi_case_and_canonical_url(self):
        a = copy.deepcopy(self.seed)
        a.update(arxiv_id=None, doi='https://DOI.org/10.1234/ABC', paper_url='https://publisher.example/paper?id=7&utm_source=feed#abstract')
        b = copy.deepcopy(a)
        b.update(doi='10.1234/abc', paper_url='https://doi.org/10.1234/abc')
        self.assertEqual(len(w.combine([w.normalize(a)], [b], 'interactive-video', '2026-10-12')), 1)
        self.assertEqual(w.canonical_url(a['paper_url']), 'https://publisher.example/paper?id=7')
        self.assertNotEqual(w.canonical_url('https://publisher.example/paper?id=8'), w.canonical_url(a['paper_url']))

    def test_url_only_tracking_and_fragment_deduplication(self):
        p = copy.deepcopy(self.seed)
        p.update(arxiv_id=None, doi=None, paper_url='https://paper.example/a/?utm_source=rss#top')
        q = copy.deepcopy(p); q['paper_url'] = 'http://paper.example/a'
        self.assertEqual(len(w.combine([w.normalize(p)], [q], 'video-avatar', '2026-10-12')), 1)

    def test_repeat_import_is_idempotent(self):
        once = w.combine([self.seed], [self.seed], 'video-avatar', '2026-10-12')
        twice = w.combine(once, [self.seed], 'video-avatar', '2026-10-12')
        self.assertEqual(once, twice)

    def test_three_sources_merge_without_duplicate(self):
        rows = [self.seed]
        for source in w.SOURCES[1:]:
            rows = w.combine(rows, [self.seed], source, '2026-10-13')
        self.assertEqual(len(rows), 1)
        self.assertEqual(set(rows[0]['discovery_sources']), set(w.SOURCES))
        self.assertEqual(rows[0]['first_seen'], '2026-10-12')
        self.assertEqual(rows[0]['last_seen'], '2026-10-13')

    def test_null_links_do_not_erase_verified_links(self):
        old = copy.deepcopy(self.seed); old['links']['weights'] = 'https://huggingface.co/example/model'
        new = copy.deepcopy(old); new['links']['weights'] = None
        result = w.combine([old], [new], 'interactive-video', '2026-10-13')[0]
        self.assertEqual(result['links']['weights'], old['links']['weights'])

    def test_stale_metadata_does_not_replace_newer_summary(self):
        old = copy.deepcopy(self.seed); old['verified_at'] = '2026-10-13'
        new = copy.deepcopy(self.seed); new['summary']['problem'] = '旧的说明不能覆盖已经核验的新内容。'
        result = w.combine([old], [new], 'interactive-video', '2026-10-13')[0]
        self.assertEqual(result['summary'], old['summary'])

    def test_conflicting_identifiers_fail(self):
        p = copy.deepcopy(self.seed)
        p.update(arxiv_id='2412.07772', paper_url='https://arxiv.org/abs/2506.08009')
        with self.assertRaises(ValueError): w.normalize(p)
        p.update(paper_url='https://arxiv.org/abs/2412.07772', doi='10.48550/arxiv.2506.08009')
        with self.assertRaises(ValueError): w.normalize(p)

    def test_private_urls_credentials_and_unexpected_fields_rejected(self):
        for url in ['file:///tmp/secret.pdf', 'http://localhost/a', 'https://127.0.0.1/a',
                    'https://192.168.0.1/a', 'https://user:password@example.org/a',
                    'https://example.org/a?token=secret', 'javascript:alert(1)']:
            with self.subTest(url=url), self.assertRaises(ValueError): w.canonical_url(url)
        p = copy.deepcopy(self.seed); p['private_notes'] = 'not a public field'
        with self.assertRaises(ValueError): w.normalize(p)
        p = copy.deepcopy(self.seed); p['summary']['problem'] = '文件在 /Users/someone/private 中。'
        with self.assertRaises(ValueError): w.normalize(p)

    def test_summary_length_and_required_evidence(self):
        p = copy.deepcopy(self.seed); p['summary'] = {k:'短' for k in w.PARTS}
        with self.assertRaises(ValueError): w.normalize(p)
        p = copy.deepcopy(self.seed); p['evidence_urls'] = []
        with self.assertRaises(ValueError): w.normalize(p)

    def test_rendered_content_escapes_plain_text(self):
        p = copy.deepcopy(self.seed); p['title'] = 'A & B "quoted"'
        page = w.render_html([w.normalize(p)])
        self.assertIn('A &amp; B &quot;quoted&quot;', page)
        self.assertNotIn('fetch(', page)

    def test_badges_and_reader_download_entry(self):
        p = copy.deepcopy(self.seed)
        p['links']['code'] = 'https://github.com/example/model/tree/main'
        badges = w.paper_badges(p)
        self.assertEqual(badges[0], ('Star', 'https://img.shields.io/github/stars/example/model.svg?style=social&label=Star', 'https://github.com/example/model'))
        p['links']['code'] = None
        self.assertNotIn('Star', [b[0] for b in w.paper_badges(p)])
        p.update(arxiv_id=None)
        self.assertIn('Paper', [b[0] for b in w.paper_badges(p)])
        page = w.render_html([p])
        self.assertIn('download="research-paper-watch.html"', page)
        self.assertIn('href="./index.html"', page)
        readme = w.render_readme([p])
        self.assertNotIn('raw.githubusercontent.com', readme)
        self.assertIn('research-paper-watch.zip', readme)
        self.assertIn('+ [', readme)

    def test_offline_package_contains_exact_standalone_reader(self):
        from package_reader import package
        from zipfile import ZipFile
        with tempfile.TemporaryDirectory() as tmp:
            root = self.temp_project(tmp)
            output = package(root)
            first = output.read_bytes()
            with ZipFile(output) as archive:
                self.assertEqual(archive.namelist(), ['index.html'])
                self.assertEqual(archive.read('index.html'), (root/'dist/index.html').read_bytes())
                self.assertIsNone(archive.testzip())
            self.assertEqual(first, package(root).read_bytes())

    def temp_project(self, temp):
        root = Path(temp)
        (root/'data').mkdir(); (root/'data/papers.json').write_text(w.dump([self.seed]))
        shutil.copytree(w.ROOT/'web', root/'web')
        w.build(root)
        return root

    def test_invalid_batch_is_atomic_and_dry_run_does_not_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.temp_project(tmp)
            before = {p: (root/p).read_bytes() for p in ['data/papers.json','README.md','dist/index.html']}
            batch = root/'batch.json'; batch.write_text(w.dump([self.seed]))
            w.import_batch(batch, 'video-avatar', '2026-10-13', root, dry_run=True)
            self.assertEqual(before, {p: (root/p).read_bytes() for p in before})
            invalid = copy.deepcopy(self.seed); invalid['evidence_urls'] = []
            batch.write_text(w.dump([self.seed, invalid]))
            with self.assertRaises(ValueError): w.import_batch(batch, 'video-avatar', '2026-10-13', root)
            self.assertEqual(before, {p: (root/p).read_bytes() for p in before})

    def test_concurrent_task_imports_preserve_all_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.temp_project(tmp)
            batch = root/'batch.json'; batch.write_text(w.dump([self.seed]))
            code = ('import sys; from pathlib import Path; sys.path.insert(0,sys.argv[1]); '
                    'import paper_watch as w; root=Path(sys.argv[2]); '
                    '\nwith w.locked(root): w.import_batch(root/"batch.json",sys.argv[3],"2026-10-13",root)')
            processes = [subprocess.Popen([sys.executable,'-c',code,str(w.ROOT/'scripts'),str(root),s]) for s in w.SOURCES[1:]]
            self.assertTrue(all(p.wait(timeout=15) == 0 for p in processes))
            self.assertEqual(set(w.load(root)[0]['discovery_sources']), set(w.SOURCES))
            w.build(root, check=True)

    def test_generated_details_and_accessible_controls(self):
        class Parser(HTMLParser):
            def __init__(self): super().__init__(); self.tags=[]
            def handle_starttag(self, tag, attrs): self.tags.append((tag, dict(attrs)))
        parser = Parser(); parser.feed(w.render_html(w.load()))
        self.assertEqual(sum(t=='details' for t,a in parser.tags), len(w.load()))
        buttons={a.get('id') for t,a in parser.tags if t=='button'}
        self.assertEqual(buttons, {'expand','collapse'})
        labels={a.get('for') for t,a in parser.tags if t=='label'}
        self.assertTrue({'search','category'} <= labels)
        w.build(check=True)


if __name__ == '__main__': unittest.main()
