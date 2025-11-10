```mermaid
flowchart TD
  OS["OS"] --> Platform["Platform"]
  Platform --> Variant["Variant"]
  Variant --> Builder["Builder manifest"]
  Builder --> Metadata["Metadata map entry"]
```
