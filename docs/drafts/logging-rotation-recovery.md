# Logging Rotation & Recovery Runbook

Use [specs/hybridcore-logs/rotation-recovery.md](openspec/specs/hybridcore-logs/rotation-recovery.md) during incidents to understand how log files transition between `Active`, `ThresholdReached`, `Rotate`, `CorruptionDetected`, and `Recovery`.

1. Confirm whether rotation limits were exceeded (check the diagram’s `ThresholdReached` branch).
2. If a crash occurred mid-write, follow the `CorruptionDetected -> Recovery` flow to mark damaged files and force a fresh handler.
3. Verify CI artifacts list both the new log file and the flagged corrupted file before closing the incident.
