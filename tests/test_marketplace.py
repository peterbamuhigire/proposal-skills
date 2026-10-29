import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from scripts.check_marketplace import inventory, validate, ROOT


class MarketplaceTest(unittest.TestCase):
    def test_current_package(self):
        self.assertEqual(validate(ROOT), [])

    def test_hard_boundary(self):
        with patch('scripts.check_marketplace.inventory', return_value=(5000, 5000)):
            self.assertEqual(validate(ROOT), [])
        for values in ((5001, 5000), (5000, 5001)):
            with patch('scripts.check_marketplace.inventory', return_value=values):
                self.assertIn('hard 5000 file limit exceeded', validate(ROOT))

    def test_unreadable_tree_refused(self):
        def denied(*args, **kwargs):
            kwargs['onerror'](PermissionError('fixture denial'))
            return iter(())
        with patch('scripts.check_marketplace.os.walk', denied):
            self.assertTrue(any('incomplete' in x for x in validate(ROOT)))

    def test_git_cache_and_symlink_entries_counted(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / '.git').mkdir(); (root / '.git/object').touch()
            (root / 'source').touch(); (root / 'link').symlink_to(root / '.git', target_is_directory=True)
            self.assertEqual(inventory(root), (3, 2))

    def test_manifest_identity_paths_and_skill_symlink_refused(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'skills/one').mkdir(parents=True)
            skill = root / 'skills/one/SKILL.md'
            skill.write_text('fixture')
            (root / '.claude-plugin').mkdir()
            manifest = root / '.claude-plugin/plugin.json'
            plugin = {'name': 'example', 'version': '1', 'skills': ['./skills/one/']}
            manifest.write_text(json.dumps(plugin))
            (root / '.claude-plugin/marketplace.json').write_text(json.dumps({'plugins': [{'name': 'example', 'version': '1', 'source': './'}]}))
            (root / 'AGENTS.md').write_text('portable')
            (root / 'README.md').write_text('portable')
            self.assertEqual(validate(root), [])
            plugin['name'] = 'wrong'
            manifest.write_text(json.dumps(plugin))
            self.assertTrue(validate(root))
            plugin['name'] = 'example'
            plugin['skills'].append('./skills/one/')
            manifest.write_text(json.dumps(plugin))
            self.assertTrue(validate(root))
            plugin['skills'] = ['../outside/']
            manifest.write_text(json.dumps(plugin))
            self.assertTrue(validate(root))
            plugin['skills'] = ['./skills/one/']
            manifest.write_text(json.dumps(plugin))
            skill.unlink()
            skill.symlink_to(root / 'README.md')
            self.assertTrue(validate(root))
