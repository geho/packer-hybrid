## Validation Standards

1. **Layered Enforcement**
   - Perform critical validation on the server or backend job even if the client validates for UX. Never rely solely on client-side checks.
2. **Fail Fast**
   - Validate inputs at the earliest boundary (HTTP handler, queue consumer) and return actionable errors before costly work begins.
3. **Specific, User-Friendly Errors**
   - Return field-level messages that explain the issue and, when possible, how to fix it.
4. **Allowlists & Strong Typing**
   - Define accepted values/formats instead of trying to block every bad input. Use strict schemas/types where available.
5. **Sanitize & Escape**
   - Normalize or escape data before persistence or display to prevent SQL injection, XSS, command injection, etc.
6. **Business Rule Checks**
   - Ensure domain invariants (balances, date windows, quotas) are enforced alongside structural validation.
7. **Consistency Across Entry Points**
   - Shared validators/libraries should back APIs, background jobs, and admin tools alike so behavior doesn’t diverge.
8. **Logging & Monitoring**
   - Log validation failures with enough context (user ID, field, rule) for debugging, but avoid storing sensitive payloads.
