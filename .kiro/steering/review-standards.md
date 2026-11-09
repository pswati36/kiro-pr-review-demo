---
inclusion: always
---
# Team review standards (demo)
- Python: type hints on public functions; no bare `except:`
- AWS: no hardcoded account IDs, regions or ARNs; least-privilege IAM
- Lambda: handlers must log a correlation ID and handle timeouts
- Data access: DynamoDB access goes through `src/repo/` helpers, never `boto3.resource` directly in handlers

## Maintaining steering
- Steering describes the CURRENT way of working. Update rules in place; git keeps the history.
- A PR that changes a pattern described here must update this file in the same PR.
