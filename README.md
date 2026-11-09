# Kiro PR Review demo (GitHub Actions)

Every PR gets an automated, read-only code review from Kiro CLI in headless mode, posted as a PR comment.

```
PR opened → Actions → git diff → kiro-cli --no-interactive --agent pr-reviewer → PR comment (+ optional BLOCK gate)
```

## Setup (5 min)
1. Push this folder to a new GitHub repo.
2. Generate a Kiro API key (Kiro account settings) → repo **Settings → Secrets → Actions** → add `KIRO_API_KEY`.
3. Create a branch, copy `demo/sample_bad_change.py` into `src/`, open a PR.
4. Watch the **Kiro PR Review** check; the review appears as a comment and updates on every push.

## What's in it
| File | Purpose |
|---|---|
| `.github/workflows/kiro-pr-review.yml` | Triggers on PR, installs Kiro, runs review, posts/updates comment, optional fail gate |
| `.kiro/agents/pr-reviewer.json` | Custom agent: read + allow-listed git/grep shell only (cannot edit) |
| `.kiro/prompts/pr-reviewer.md` | Review checklist + fixed output format with verdict |
| `.kiro/steering/review-standards.md` | Team standards loaded into the reviewer |
| `demo/sample_bad_change.py` | Seeded issues: hardcoded key, pickle, bare except, hardcoded region, debug print |

## Steering drift check
Kiro also checks whether a PR changes a pattern that `.kiro/steering/` describes without updating the steering file in the same PR. The workflow passes the list of changed files and changed steering files to the reviewer, and drift findings appear in their own **Steering drift** section of the review comment.

To demo it, open a second PR that adds `demo/sample_drift_change.py` under `src/`. It switches DynamoDB access to a new pattern without editing `review-standards.md`, so Kiro should flag drift. Then push a commit that updates the Data access rule and watch the finding clear.

## Demo talking points
- **Same agent locally and in CI**: `kiro-cli chat --agent pr-reviewer` gives devs the identical review before pushing.
- **Governance**: read-only tools, shell allow-list, no fork-PR secrets, admin policies still apply to API-key sessions.
- **Team standards as code**: edit steering/prompt via PR; reviewed like any other code.
- **Context-lean**: diff only + one short steering file; no MCP servers loaded.

## Notes / verify before customer demo
- Confirm CLI flags against `kiro-cli chat --help` for your installed version (agent config keys can differ between CLI versions; run `/agent schema`).
- Large PRs: consider truncating the diff or reviewing per-file.
- Add more rules as `.kiro/skills/<name>/SKILL.md` (e.g. language-specific checks).
