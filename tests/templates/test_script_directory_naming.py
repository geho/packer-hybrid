import pathlib
import re
import unittest


class ScriptDirectoryNamingTest(unittest.TestCase):
    def test_scripts_directory_names(self) -> None:
        scripts_root = pathlib.Path(__file__).resolve().parents[2] / "templates" / "scripts"
        if not scripts_root.exists():
            self.skipTest("templates/scripts directory not present in this checkout")

        allowed_roots = {"linux", "windows"}
        for child in scripts_root.iterdir():
            if child.is_dir():
                self.assertIn(child.name, allowed_roots, msg=f"Unexpected root dir {child}")
                for subdir in child.rglob("*"):
                    if subdir.is_dir():
                        self.assertRegex(
                            subdir.name,
                            r"^[a-z0-9-]+$",
                            msg=f"{subdir} must be lowercase kebab-case",
                        )


if __name__ == "__main__":
    unittest.main()
