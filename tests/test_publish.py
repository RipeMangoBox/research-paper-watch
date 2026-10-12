import contextlib
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import publish as p


class PublishGuards(unittest.TestCase):
    def setUp(self):
        self.patches = [patch.object(p, 'locked', return_value=contextlib.nullcontext()),
                        patch.object(p, 'validate_batch'), patch.object(p, 'import_batch')]
        self.mocks = [patcher.start() for patcher in self.patches]
        for patcher in self.patches: self.addCleanup(patcher.stop)

    def test_dry_run_never_calls_git_or_network(self):
        with patch.object(p, 'run', side_effect=AssertionError('No commands in dry run')):
            p.publish(Path('batch.json'), 'interactive-video', '2026-10-12')
        self.mocks[2].assert_called_once_with(Path('batch.json'), 'interactive-video', '2026-10-12', dry_run=True)

    def test_wrong_repository_stops_before_import(self):
        with patch.object(p, 'run', return_value='https://github.com/other/private.git') as run:
            with self.assertRaisesRegex(ValueError, 'origin must'): p.publish(Path('batch.json'), 'video-avatar', '2026-10-12', True)
            self.assertEqual(run.call_count, 1)
        self.mocks[2].assert_not_called()

    def test_dirty_tree_stops_before_network(self):
        with patch.object(p, 'run', side_effect=[p.REMOTES[0], 'main', ' M private.txt']) as run:
            with self.assertRaisesRegex(ValueError, 'clean'): p.publish(Path('batch.json'), 'video-avatar', '2026-10-12', True)
            self.assertEqual(run.call_count, 3)
        self.mocks[2].assert_not_called()

    def test_wrong_account_stops_before_pull(self):
        with patch.object(p, 'run', side_effect=[p.REMOTES[0], 'main', '', 'other-user']) as run:
            with self.assertRaisesRegex(ValueError, 'account'): p.publish(Path('batch.json'), 'video-avatar', '2026-10-12', True)
            self.assertEqual(run.call_count, 4)
        self.mocks[2].assert_not_called()

    def test_unrelated_unpushed_commit_is_rejected(self):
        with patch.object(p, 'run', side_effect=[p.REMOTES[0], 'main', '', 'RipeMangoBox', '', 'private.txt']):
            with self.assertRaisesRegex(ValueError, 'Unpushed'): p.publish(Path('batch.json'), 'video-avatar', '2026-10-12', True)
        self.mocks[2].assert_not_called()


if __name__ == '__main__': unittest.main()
