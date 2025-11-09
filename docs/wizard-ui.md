# Wizard UI Overview

This document outlines the simplified flow for the `packer-hybrid wizard` experience. Reference: [specs/cli/spec.md#requirement-wizard-template-consistency](openspec/specs/cli/spec.md#requirement-wizard-template-consistency).

```
Wizard Input -> Normalize Answers -> Render templates/wizard -> Present Text/Curses/Django UI -> Write configs/<env>/*.auto.pkrvars.hcl
```

```mermaid
%% sourced from openspec/specs/cli/spec.md#requirement-wizard-template-consistency
flowchart TD
  A["Gather Inputs"] --> B["Normalize Answers"]
  B --> C["Render templates/wizard"]
  C --> D["Text UI"]
  C --> E["Curses UI"]
  C --> F["Django UI"]
  D --> G["configs/<env>/*.auto.pkrvars.hcl"]
  E --> G
  F --> G
  G --> H["State & Validation"]
```

For the detailed flow (including branching and validation), see the linked spec section—the diagram above is kept in sync with the spec’s Mermaid source.
