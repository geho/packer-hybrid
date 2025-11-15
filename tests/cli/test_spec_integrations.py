import pathlib
import unittest

SPEC_PATH = pathlib.Path(__file__).resolve().parents[2] / "openspec" / "specs" / "cli" / "spec.md"


class CliSpecIntegrationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = SPEC_PATH.read_text(encoding="utf-8")

    def test_diag_references_security_spec(self) -> None:
        self.assertIn("specs/security/spec.md#requirement-secret-leak-detection", self.text)

    def test_status_schema_reference_present(self) -> None:
        self.assertIn("docs/cli-status-schema.json", self.text)

    def test_command_cross_links_present(self) -> None:
        self.assertIn("assessments/2025-11-14-remediation-migration/remediations/hybridcore-config-remediations.md", self.text)
        self.assertIn("assessments/2025-11-14-remediation-migration/remediations/hybridcore-templates-remediations.md", self.text)

    def test_template_validation_hooks_referenced(self) -> None:
        self.assertIn("specs/templates/spec.md#requirement-variant-naming-layout", self.text)
        self.assertIn("specs/templates/spec.md#requirement-checksum-cache-lifecycle", self.text)


if __name__ == "__main__":
    unittest.main()
