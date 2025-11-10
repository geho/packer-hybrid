import pathlib
import unittest

SPEC_PATH = pathlib.Path(__file__).resolve().parents[2] / "openspec" / "specs" / "hybridcore-packer" / "spec.md"


class HybridcorePackerSpecTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = SPEC_PATH.read_text(encoding="utf-8")

    def test_incremental_hash_manifest_requirement_present(self) -> None:
        self.assertIn("Incremental Hash Manifests", self.text)
        self.assertIn("artifacts/<builder>.hash.json", self.text)

    def test_result_schema_table_present(self) -> None:
        self.assertIn("Result Schema & Exit Codes", self.text)
        self.assertIn("retry policy", self.text.lower())

    def test_diag_integration_present(self) -> None:
        self.assertIn("Diagnostics & Retention Integration", self.text)
        self.assertIn("state/packer/logs", self.text)


if __name__ == "__main__":
    unittest.main()
