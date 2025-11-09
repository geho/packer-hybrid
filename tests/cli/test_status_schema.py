import json
import pathlib
import unittest

SCHEMA_PATH = pathlib.Path(__file__).resolve().parents[2] / "docs" / "cli-status-schema.json"


class StatusSchemaTest(unittest.TestCase):
    def setUp(self) -> None:
        with SCHEMA_PATH.open(encoding="utf-8") as fh:
            self.schema = json.load(fh)

    def test_required_fields_present(self) -> None:
        required = set(self.schema.get("required", []))
        self.assertTrue({"version", "targets", "sources", "state", "issues"}.issubset(required))

    def test_version_property_exists(self) -> None:
        properties = self.schema.get("properties", {})
        self.assertIn("version", properties)
        self.assertEqual(properties["version"].get("type"), "string")


if __name__ == "__main__":
    unittest.main()
