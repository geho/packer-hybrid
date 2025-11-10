import pathlib
import unittest

SPEC_PATH = pathlib.Path(__file__).resolve().parents[2] / "openspec" / "specs" / "hybridcore-logs" / "spec.md"


class HybridcoreLogsSpecTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = SPEC_PATH.read_text(encoding="utf-8")

    def test_sink_table_present(self) -> None:
        self.assertIn("register_sink(\"syslog\")", self.text)
        self.assertIn("cloud shippers", self.text)

    def test_retention_mapping_present(self) -> None:
        self.assertIn("HYBRIDCORE_LOG_MAX_DAYS", self.text)
        self.assertIn("--log-keep", self.text)

    def test_diag_integration_present(self) -> None:
        self.assertIn("diag log scrub", self.text.lower())
        self.assertIn("scrub manifest", self.text.lower())

    def test_context_table_present(self) -> None:
        self.assertIn("correlation_id", self.text)
        self.assertIn("canonical context schema", self.text.lower())


if __name__ == "__main__":
    unittest.main()
