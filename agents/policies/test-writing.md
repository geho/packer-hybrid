## Test Writing Principles

1. **Minimum Viable Coverage First**
   - Add tests only at meaningful checkpoints (feature complete, bug fixed). Avoid writing tests for half-finished behavior.
2. **Focus on Core Flows**
   - Cover primary user journeys and business-critical logic. Leave secondary helpers or edge cases for later unless the spec demands them now.
3. **Behavior Over Implementation**
   - Assert observable outcomes (responses, state changes, DB effects), not private functions or internal structures.
4. **Edge Cases When Justified**
   - Explicitly note any edge cases deferred so reviewers know the current limits.
5. **Readable, Intent-Revealing Names**
   - Use test names describing scenario and expectation (`returns_error_when_token_expired`).
6. **Mock External Systems**
   - Stub databases, APIs, queues, and file systems so tests run quickly and deterministically.
7. **Keep Tests Fast**
   - Target millisecond-level unit tests. If a test needs real IO, label it (e.g., “slow”, “integration”) and run it selectively.
8. **Record Gaps**
   - When you skip tests (time, scope), call it out in the PR summary or TODO so follow-up work can track it.
