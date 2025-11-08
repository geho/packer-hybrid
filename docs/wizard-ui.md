# Wizard UI Overview

This document outlines the simplified flow for the `packer-hybrid wizard` experience. The full Mermaid diagram lives in `openspec/changes/refactor-misplaced-specs/specs/cli/spec.md` under _Requirement: Wizard Template Consistency_.

```
Wizard Input -> Normalize Answers -> Render templates/wizard -> Present Text/Curses/Django UI -> Write configs/<env>/*.auto.pkrvars.hcl
```

For the detailed flow (including branching and validation), see the linked spec section.
