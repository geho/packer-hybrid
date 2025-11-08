# Config Extendability Checklist

Follow [specs/hybridcore-config/config-extendability.md](openspec/specs/hybridcore-config/config-extendability.md) whenever onboarding new environments or inputs. The diagram reminds contributors to update the schema, refresh docs, add fixtures/tests, and surface results in code review before landing changes.

Quick steps:

1. Patch `schema/config.schema.json` with defaults/validation.
2. Document new vars in README/spec references.
3. Add golden fixtures + negative overlay tests.
4. Verify CI hash + overlay checks pass before requesting review.
