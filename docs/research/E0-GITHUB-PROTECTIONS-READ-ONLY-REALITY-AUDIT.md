# E0 GitHub Control Reality Audit — Read-Only Findings (2026-11-21)

**Status:** Actual API metadata reviewed; incomplete permission coverage explicitly recorded. **No branch rules, settings, secrets, CI, PR state, merges, or source code were modified by this audit.**
**Project:** Foromni only; `Foromni-Network/forOmni`. No Internet Embassy access.
**Method:** Authenticated GitHub read endpoints via connected integration. Repository controls can change after observation; this is not an ongoing monitoring assertion.

## 1. Observed facts, not assumptions

| Audit item | Observed response | Confidence / limit |
|---|---|---|
| Main ref | `main@46cffd81e73b0c957c1814b4b5ab5d346fe7ca99` | GitHub branch GET at observation time |
| Main `protected` | `false` | Explicit boolean returned by branch endpoint |
| Main protection summary | `enabled:false`, required checks `enforcement_level:off`, empty contexts/checks | Branch GET returned embedded summary |
| Repository rulesets list | `[]` | Empty result **visible through this integration**; do not claim unseen organization-level policies absent |
| Detailed branch protection GET | HTTP 403 `Resource not accessible by integration` | **Unknown** finer controls/admin inspection; cannot audit with this connection |
| Research PR #3 | Open, head `research/global-agent-roadmap-execution`, base `main`; `mergeable:null` from this API response | A null mergeability field is unknown/not computed, **not** a positive or negative mergeability result |
| `.github/CODEOWNERS` at research branch | 404 | File not found at exact path checked; other supported CODEOWNERS paths not exhaustively examined |
| `.github/workflows/ci.yml` at research branch | 404 | Exact file absent; cannot infer all possible CI workflows absent from one filename |
| `.github` directory listing at both main and research | 404 | No such directory visible in queried refs; different roots/workflow arrangement might exist |
| Research branch detailed protection | Not verified | Direct branch endpoint query using encoded slash failed URL validation in connector; do not infer protection state |

**Critical finding:** The main branch is **not protected by the visible GitHub branch protection configuration**. The first E0 integration design must therefore use a *disposable, isolated source destination and a trusted human/QA review process* rather than assume platform protection currently exists. Avoid autonomous branch merges into main.

**Limit:** This audit cannot prove who can write via installation/user credentials, whether other apps or org governance provide compensating controls, or whether a future repository ruleset will work. Treat those as separate verifications by an owner with appropriate privileges.

## 2. What must be checked by an authorized repository administrator before source automation

- Confirm current repository/org rulesets and how they apply to `main`, candidate refs and merge queues.
- Decide whether protected `main` should require independently controlled status checks and PR reviews, disallow force push, constrain bypass grants and optionally signed commits.
- Verify source branch write principal and whether it can write arbitrary files/refs; validate GitHub App token issuance scope and expiry under an isolated test identity.
- Verify status-check author ownership; no implementation worker should be able to post the check identity that admits its own changes.
- Verify required checks target the *prospective* merge-group/combined source, not a previously green branch.
- Confirm protection/CI controls are available on the intended repository and plan, not merely supported in GitHub's documentation.
- Inspect ruleset/branch enforcement using permitted admin tooling or GitHub UI; record authenticated actor, effective rules, timestamps and evidence.
- Test bypass, rejected merge, stale SHA and lost-ACK behavior **only with separately authorized synthetic operations**.

## 3. P0 control options that avoid an accidental permission escalation

**Research-only, now:** continue source-linked documents on the existing research branch; no runner/merge integration.

**First optional E0 trial after approval:** preferred disposable local Git repository or explicit isolated trial repository, with an agent producing patch artifacts and a separately trusted process doing controlled Git writes and source read-back. Do not grant agent `main` write or treat current Foromni main as a protected benchmark target.

**Later organization-grade source convergence:** establish actual GitHub rulesets/branch protections, permissions and independent status checks before autonomous merging. If org-level admin audit is unavailable, fail closed for protected integration claims.

## 4. Remaining unsupported statements

We **cannot yet** say: `main` is protected; codeowners reviews are enforced; required CI is configured; GitHub merge queue is active; agent-specific GitHub writes are path-restricted; independent QA credentials exist; a protected deployment lane exists; or E0 is execution-ready.

This document is an observation record, not a request to purchase capabilities or a green-light to change repository settings.

## 5. Research status implications

- **Git / protected integration readiness:** `NOT_READY` for autonomous merges on actual Foromni main.
- **Provisional workaround:** isolated synthetic candidate patch + human-controlled read-back and QA, pending trial authorization.
- **Exact E0 plan remains incomplete:** independently owned tests, runtime/sandbox and credentials, reproducibility, costs, and human authorization are outstanding.
- **Follow-up:** a repository owner/admin must later review and explicitly authorize any GitHub protection or deployment setting changes.

Source: GitHub repository branches, rulesets, pull-request and contents GET responses obtained 2026-11-21. No screenshots or external system changes performed.

*Build today, so others can enjoy tomorrow.* ❤️🐂
