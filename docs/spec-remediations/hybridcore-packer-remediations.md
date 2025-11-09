# Hybridcore Packer Remediations

## Open Topics

1. **Integrity** – Document future drift detection enhancements (incremental hashing) explicitly once design completed. _Plan_: add coverage for per-builder hash manifests and include CI examples.
2. **Completeness / Alignment** – The spec does not capture how packer orchestration reports status back to CLI/automation (error classes, retry codes). _Plan_: document the result schema and ensure tests assert structure before CLI consumes it.

## Closed Topics

1. **Cache/Parallelism** – Spec now covers cache invalidation rules and parallel limits.
2. **Alignment** – Drift detection requirement references templates/provisioners/state Open Issues.
