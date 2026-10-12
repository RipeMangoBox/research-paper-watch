#!/usr/bin/env python3
"""Import a reviewed public batch and optionally publish to the fixed GitHub repository."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
from paper_watch import ROOT, SOURCES, catalogue, combine, date, import_batch, load, locked

REPOSITORY = 'RipeMangoBox/research-paper-watch'
ALLOWED = ('data/papers.json', 'README.md', 'dist/index.html')
REMOTES = ('https://github.com/' + REPOSITORY + '.git', 'https://github.com/' + REPOSITORY,
           'git@github.com:' + REPOSITORY + '.git')


def run(*args, capture=False):
    result = subprocess.run(args, cwd=ROOT, check=True, text=True,
                            stdout=subprocess.PIPE if capture else None)
    return result.stdout.strip() if capture else ''


def validate_batch(path, source, observed):
    # Validate before a network operation or any catalogue modification.
    combine(load(), catalogue(json.loads(path.read_text())), source, observed)


def publish(path, source, observed, push=False):
    with locked():
        validate_batch(path, source, observed)
        if not push:
            return import_batch(path, source, observed, dry_run=True)
        if run('git', 'remote', 'get-url', 'origin', capture=True) not in REMOTES:
            raise ValueError('origin must be the authorized research-paper-watch repository')
        if run('git', 'branch', '--show-current', capture=True) != 'main':
            raise ValueError('Publishing requires the main branch')
        if run('git', 'status', '--porcelain', capture=True):
            raise ValueError('Working tree must be clean; keep input batches in ignored incoming/')
        if run('gh', 'api', 'user', '--jq', '.login', capture=True) != 'RipeMangoBox':
            raise ValueError('The active GitHub account is not RipeMangoBox')
        run('git', 'pull', '--ff-only', 'origin', 'main')
        outgoing = set(filter(None, run('git', 'log', '--format=', '--name-only', 'origin/main..HEAD', capture=True).splitlines()))
        if not outgoing <= set(ALLOWED):
            raise ValueError('Unpushed commits include files outside the public catalogue outputs')
        result = import_batch(path, source, observed)
        # Do not spawn the locking CLI while holding this transaction's lock.
        from paper_watch import build
        build(check=True)
        run(sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v')
        run('node', '--test', 'tests/reader.test.cjs')
        changed = set(filter(None, run('git', 'diff', '--name-only', capture=True).splitlines()))
        if not changed <= set(ALLOWED):
            raise ValueError('Refusing to publish changes outside the public catalogue outputs')
        if changed:
            run('git', 'add', '--', *ALLOWED)
            staged = set(run('git', 'diff', '--cached', '--name-only', capture=True).splitlines())
            if not staged <= set(ALLOWED):
                raise ValueError('Unexpected staged files')
            run('git', 'commit', '-m', f'Update public papers: {source} {observed}')
        # Also retries an already-committed push after a previous network failure.
        run('git', 'push', 'origin', 'main')
        local = run('git', 'rev-parse', 'HEAD', capture=True)
        remote = run('git', 'ls-remote', 'origin', 'refs/heads/main', capture=True).split()[0]
        if local != remote:
            raise ValueError('Remote commit verification failed; no force push was attempted')
        return dict(result, pushed=True, commit=local, repository='https://github.com/' + REPOSITORY)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--source', required=True, choices=SOURCES)
    parser.add_argument('--date', required=True)
    parser.add_argument('--push', action='store_true', help='Commit and push only reviewed public catalogue outputs')
    args = parser.parse_args()
    try:
        print(json.dumps(publish(args.input.resolve(), args.source, date(args.date), args.push), ensure_ascii=False))
    except (ValueError, KeyError, TypeError, OSError, subprocess.CalledProcessError) as error:
        print('Publish stopped: ' + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
