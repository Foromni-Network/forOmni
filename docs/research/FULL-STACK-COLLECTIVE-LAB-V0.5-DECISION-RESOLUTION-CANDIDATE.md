# Collective Lab v0.5 — Fifteen-Decision Resolution Candidate

**Status:** RESEARCH PROPOSAL; all D-01–D-15 have a **recommended** disposition, not reviewer-approved decisions. **Not frozen, implemented, tested or authorized.**
**Date:** 2026-11-21. **Scope:** Foromni only. Internet Embassy untouched.
**Inputs:** FULL-STACK-COLLECTIVE-LAB-UNIFIED-CONTRACT-V0.4-REVIEW-CANDIDATE.md (complete v0.4 role matrix/endpoints and acceptance IDs); FULL-STACK-REFERENCE-APP-CONFORMANCE-V0.2.md; FULL-STACK-REFERENCE-APP-API-FIXTURE-FREEZE-PROPOSAL-V0.3.md. v0.5 is an amendment/decision proposal; retain v0.4 as the base spec until all dispositions are approved.

## 1. Decision reconciliation table

| Decision | Recommended precise choice | Reason / independent oracle | Approval status |
|---|---|---|---|
| **D-01 Additional invite recipient** | Add **Fay** (`usr_fay`), initially not a member of either project, as a seventh synthetic test principal; all IDs server-owned opaque values | Invitation acceptance must demonstrate newly granted membership without conflating an existing A/B role | Proposed |
| **D-02 Deterministic clock** | Set fixture `T0 = 2027-01-15T12:00:00Z`; test clock injected only into disposable environment; all event times and expiry comparisons in UTC; tests may advance clock via trusted evaluator only | Predictable invitation expiry, stable ordering and replay | Proposed |
| **D-03 Project deletion** | **Exclude DELETE project operation from first E0 implementation and grader**; preserve original owner-only policy as a future reserved capability, and return 404/405 for unsupported route consistently (reviewer select one; recommend 404 to avoid declaring route) | Avoid adding a destructive workflow not specified in v0.2; make omission explicit | Proposed |
| **D-04 Public projection** | Public nonmember can see exactly `id,title,description,visibility,version`; no `myRole`, memberCount, task names/activity, private membership or audit metadata; omit `myRole` if unauthenticated | Stable auditable privacy boundary | Proposed |
| **D-05 Cursor invalidation** | `GET` lists default `limit=20`, max 50, stable `createdAt DESC,id DESC`; opaque signed cursor binds viewer identity (anonymous sentinel), scope, filter and sort revision; malformed, expired or cross-scope cursor => 400 `INVALID_CURSOR`, never reset silently | Prevent invisible page-shifting and cross-user information disclosure | Proposed |
| **D-06 Project creation visibility** | Allow optional `visibility: public/private` on project creation **only for newly self-owned projects**; default private. Server sets authenticated creator as owner; no client actor or owner fields | Preserves v0.2 endpoint; public setting by rightful owner is coherent | Proposed |
| **D-07 Task description** | **Exclude task description** from E0 task request, stored canonical task and response; v0.3 0–4000 guideline applies to project `description` only for E0; if task description is submitted, reject unknown field 422 | Avoid silently extending v0.2 task representation | Proposed |
| **D-08 Invitation parameters** | Owner supplies `recipientUserId` (must refer to eligible synthetic identity) and role `viewer/member/manager`; not owner. Token server-generated high entropy, stored hashed; lifetime **24h fixed**; no caller TTL override, no outbound messaging | Narrow and replayable acceptance behavior; no owner privilege via invites | Proposed |
| **D-09 Invitation acceptance** | Authenticated matching recipient POSTs with empty body; on success **200** `{projectId,member:{userId,role}}`; token consumption, membership and successful audit event in **one** transaction; second/concurrent accept returns 409 `INVITE_CONSUMED`; wrong user 404 (non-disclosing); expired 410 only if token belongs to authenticated recipient (otherwise 404) | Defines conflict and privacy consistently; ensures one-use under races | Proposed |
| **D-10 Role change** | **Exclude member-role PATCH from E0 implementation**; retain owner-only policy intent as reserved future capability; grader must not assume route exists | Keeps E0 focused on v0.2 documented endpoints, prevents invented route | Proposed |
| **D-11 Input limits** | Both project and task titles trim to **1–160 Unicode code points**; project description is optional **0–4000** characters (empty string permitted); explicit `null` description => 422; no task description; reject unknown writable fields and unsafe types before mutation | Single predictable validator across tasks/projects; preserve E0 shape | Proposed |
| **D-12 Optimistic concurrency** | Current entity version starts at 1, PATCH requires a quoted **strong ETag** in `If-Match: "vN"`; missing => **428 PRECONDITION_REQUIRED**; syntactically invalid => 400; valid but stale => **409 VERSION_CONFLICT** (preserves v0.2); successful mutation increments exactly once and returns current ETag | Specific, testable contract; note alternative conventional 412 rejected for this benchmark only | Proposed |
| **D-13 Error catalogue** | Shared `{error:{code,message,requestId}}`; 400 malformed syntax/cursor, 401 unauthenticated, 403 known-object unauthorized, 404 inaccessible private or missing, 409 stale/replay, 410 valid recipient's expired invite, 422 invalid domain field, 428 missing If-Match; 429 **not in E0** absent frozen fixture. Reject unexpected body keys with 422; no sensitive server details | Makes wrong-authority and bad-input failure distinguishable | Proposed |
| **D-14 Session/auth** | Synthetic local deterministic session provider behind one server-verified session abstraction, cookie-bound `HttpOnly`, `SameSite=Lax`, `Secure` on HTTPS (for strictly local HTTP test, exception documented); fixed TTL = **60min** from controlled clock; revocation/logout invalidates subsequent requests; unsafe methods require same-origin + CSRF token or same-origin Origin validation with robust null/absent policy; freeze implementation choice and test-origin matrix before trial | Behavioral-equivalent disposable auth avoids needing real user/third-party provider; security design pending independent review | Proposed, SECURITY REVIEW REQUIRED |
| **D-15 UI/browser** | E0 minimum **Chromium** at desktop `1280×800` and mobile `390×844`; essential flows with keyboard only, visible focus, labels/error association, reachable modal dismissal; zero critical/blocker accessibility failures; noncritical findings recorded and reviewed, not silently ignored. No claim of broad WCAG conformance from limited E0 smoke tests | Reproducible essential-flow viewport and severity rules without overclaiming | Proposed |

**Decision status:** **15/15 disposition proposals drafted; 0/15 independently approved or frozen.** The D-03 and D-10 recommendations deliberately distinguish reserved owner-only powers from implemented E0 routes. An evaluator may test that unsupported routes do not accidentally provide destructive/privileged operations; it must not require implementing a nonexistent route.

## 2. Canonical E0 API roster after proposed dispositions

```text
GET    /api/me
GET    /api/projects
POST   /api/projects
GET    /api/projects/:projectId
PATCH  /api/projects/:projectId
GET    /api/projects/:projectId/tasks
POST   /api/projects/:projectId/tasks
PATCH  /api/projects/:projectId/tasks/:taskId
GET    /api/projects/:projectId/activity
POST   /api/projects/:projectId/invitations
POST   /api/invitations/:token/accept
DELETE /api/projects/:projectId/members/:userId
```

No delete-project or member-role-change endpoint in E0. Preserve v0.4 role matrix otherwise. Every project-scoped route must evaluate the active session's **current project membership**, not a cached claim. Public project *metadata* is not public task data.

### Example positive and negative expectations

- `GET /api/projects/prj_B` anonymous => public projection only; `GET /api/projects/prj_B/tasks` anonymous => 401.
- `GET /api/projects/prj_A` anonymous or Dee => 404 without private attributes.
- `POST /api/projects/prj_A/tasks` as Cy => 403, no row or success audit.
- `PATCH /api/projects/prj_A/tasks/task_a1` as Eli with `If-Match: "v1"` updating `title` => 200, version 2. Changing `assigneeUserId` as Eli => 403 and unchanged DB.
- `POST /api/projects` as Dee with `{title:"Demo",visibility:"public"}` => self-owned public project. With `ownerId:"usr_ada"` => 422.
- `PATCH` without `If-Match` => 428; stale `"v1"` after actual version advances => 409; never silently overwrite.
- `POST /api/projects/prj_A/invitations` as Ada targeting Fay for member, then Fay accepts => 200 and exactly one membership+audit. Concurrent replay => one winner, loser 409.
- `POST /api/invitations/:token/accept` as Dee for Fay's invite => non-disclosing 404 with no mutation; expired token belonging to Fay => 410.
- Cross-user opaque cursor => 400 without allowing access to a private row.
- A browser session invalidated by project removal cannot continue to read formerly private A details merely through client cache.

All values are proposed synthetic expected outputs, NOT observed API behavior.

## 3. Potential collisions and reviewer cautions

1. **Expiry control is security-sensitive:** a test clock must not be controllable by the untrusted coding worker in the trusted QA environment. Synthetic session TTL does not imply production-safe auth.
2. **Invite errors and information leaks:** privileged recipient-specific 410 may leak token status if token space is guessable; high entropy, rate controls and comparison behavior must be independently reviewed. Uniform 404 is a viable alternative if preferred.
3. **Cookie CSRF:** SameSite alone is not comprehensive CSRF protection. D-14 cannot be frozen without selecting a robust strategy for missing/null Origin and the actual framework.
4. **File/test isolation:** not enough for reviewer to have a separate prompt; actual filesystem/repo tokens must prevent the candidate worker from altering hidden QA fixtures.
5. **Cursor tokens:** signing and binding scope is a proposal, not proof. Current membership must be checked on each page request.
6. **Failure code semantics:** 409 stale version is intentionally inherited from v0.2 even though standard conditional-request patterns often use 412. Benchmark arms require *one* choice, not mix.
7. **Deleted project and role change:** preserved as owner-only **policy intentions**, explicitly deferred from first vertical slice. Future implementation scope expansion requires revising the same benchmark contract for both trial arms before execution.
8. **Workload consistency:** both control and convergence cohorts must receive identical preapproved requirements and independent oracle. Do not let one arm know hidden tests or receive easier seeds.

## 4. Exact change-control gate

A proposed freeze must record:
`contract_version=v0.5-accepted`, all 15 decisions and rationale, reviewer/owner identity, reviewed contract commit SHA, immutable reference fixture and suite hashes, server/browser/package versions, resource budget, known excluded features and expected denial behavior. If a decision changes after baseline begins, revise contract version and rerun/rebalance all affected arms. No cherry-picked successful results carry over.

**Current conclusion:** Requirements are now decision-ready **on paper**. Neither reviewer independence, API implementation, security of D-14, fixture correctness, nor source-host controls has been demonstrated. E0 remains **NOT READY FOR EXECUTION**.

*Build today, so others can enjoy tomorrow.* ❤️🐂
