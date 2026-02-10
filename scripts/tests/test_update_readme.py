import os
import tempfile
import shutil
import unittest

from scripts import update_readme


class TestUpdateReadme(unittest.TestCase):
    def test_generate_entry_contains_name(self):
        sample = {"blueprint": {"name": "Test BP", "domain": "automation", "description": "Desc"}}
        entry = update_readme.generate_entry("blueprints/automation/test.yaml", sample, "ru")
        self.assertIn("Test BP", entry)

    def test_collect_blueprints_multidoc(self):
        tmpdir = tempfile.mkdtemp()
        try:
            bp_dir = os.path.join(tmpdir, "blueprints")
            os.makedirs(bp_dir, exist_ok=True)
            file_path = os.path.join(bp_dir, "multi.yaml")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("""
blueprint:
  name: BP One
  domain: automation
  description: Doc1
---
blueprint:
  name: BP Two
  domain: script
  description: Doc2
""")

            groups = update_readme.collect_blueprints(blueprints_root=bp_dir)
            # expect two domains
            self.assertIn("automation", groups)
            self.assertIn("script", groups)
            self.assertTrue(any("bp one" in g[0] for g in groups["automation"]))
            self.assertTrue(any("bp two" in g[0] for g in groups["script"]))
        finally:
            shutil.rmtree(tmpdir)


if __name__ == "__main__":
    unittest.main()
