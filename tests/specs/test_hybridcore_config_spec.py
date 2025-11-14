import pathlib
import unittest

SPEC_PATH = pathlib.Path(__file__).resolve().parents[2] / "openspec" / "specs" / "hybridcore-config" / "spec.md"


class HybridcoreConfigSpecTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = SPEC_PATH.read_text(encoding="utf-8")

    def test_references_templates_state_remediations(self) -> None:
        self.assertIn("assessments/2025-11-14-remediation-migration/remediations/hybridcore-templates-remediations.md", self.text)
        self.assertIn("assessments/2025-11-14-remediation-migration/remediations/hybridcore-state-remediations.md", self.text)

    def test_provisioning_mapping_table_present(self) -> None:
        self.assertIn("Provisioning Input Mapping", self.text)
        self.assertIn("openspec/specs/provisioning/spec.md", self.text)


if __name__ == "__main__":
    unittest.main()
