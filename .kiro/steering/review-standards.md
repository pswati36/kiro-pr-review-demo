---
inclusion: always
---
# Team review standards (demo)
- Python: type hints on public functions; no bare `except:`
- AWS: no hardcoded account IDs, regions or ARNs; least-privilege IAM
- Lambda: handlers must log a correlation ID and handle timeouts
