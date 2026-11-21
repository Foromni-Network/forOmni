# Collective Lab — Unified Full-Stack Behavioral Contract v0.4 (Review Candidate)

**Status: RESEARCH REVIEW CANDIDATE — NOT APPROVED, NOT FROZEN, NOT EXECUTED.**
**Date:** 2026-11-21. **Scope:** Foromni only. No connection to Internet Embassy systems.
**Supersession policy:** Combines the endpoint/role matrix in `FULL-STACK-REFERENCE-APP-CONFORMANCE-V0.2.md` with detailed candidate behavior in `FULL-STACK-REFERENCE-APP-API-FIXTURE-FREEZE-PROPOSAL-V0.3.md`. This document does **not** change the authoritative status of earlier documents and must be reviewed before becoming a frozen experiment oracle.
**Normative language:** SHALL = proposed mandatory behavior if accepted for the benchmark; D-xx = unresolved design decision requiring independent owner acceptance.

## 1. Purpose and freeze boundary

**Collective Lab** is a synthetic, small full-stack project/task application used to compare ordinary AI coding work with convergence-first work. Its API, UI, sessions, persistence and independent acceptance must behave consistently across study arms. This is not the Foromni production architecture. A future freeze must include a reviewer-signed contract revision, source and fixture digests, time/budget horizon, independent evaluator and a change-control procedure.

## 2. Synthetic actors and fixture

| Actor | User ID | Project A (private) | Project B (public metadata) |
|---|---|---|---|
| Ada | `usr_ada` | owner | nonmember |
| Bao | `usr_bao` | manager | nonmember |
| Cy | `usr_cy` | viewer | nonmember |
| Eli | `usr_eli` | member | nonmember |
| Dee | `usr_dee` | nonmember | owner |
| Anonymous | none | no access | published metadata only |

Project A has two tasks, one assigned to Eli and one assigned to Bao, plus activity and versioned project metadata. Project B has a task and activity invisible to all nonmembers even when project B is public. Include at least one unexpired, unconsumed synthetic invitation addressed to a distinct eligible synthetic identity; the reviewer must decide whether to introduce `usr_fay` as a seventh actor (D-01), so acceptance fixtures can test a genuinely new member rather than reinterpret the role of an existing one. Every fixture ID is synthetic, stable per reset, server-owned and nonauthoritative when supplied by an untrusted client. Fixture clock T0 is fixed by evaluator (D-02), and synthetic invitations use it rather than uncontrolled wall time.

## 3. Authoritative role matrix (preserved from v0.2)

| Operation | Anonymous | Viewer (member) | Member | Manager | Owner |
|---|---|---|---|---|---|
| Read public project metadata | yes | yes | yes | yes | yes |
| Read private project details | no | own project | own project | own project | own project |
| Read project tasks/activity | no | own project | own project | own project | own project |
| Create own new project | no | yes | yes | yes | yes |
| Create task in project | no | no | yes | yes | yes |
| Update title/status on self-assigned task | no | no | yes | yes | yes |
| Reassign task / edit other member's task | no | no | no | yes | yes |
| Update project title/description | no | no | no | yes | yes |
| Change project visibility | no | no | no | no | yes |
| Invite, remove or alter member role | no | no | no | no | yes |
| Delete project | no | no | no | no | yes |

Roles are evaluated only relative to the *target* project. An owner cannot remove themselves or silently transfer ownership. No ownership-transfer endpoint is in benchmark scope. A member who creates a task may not assign it to someone else. Every attempted cross-project private operation is denied without leaking private object existence.

**Scope note:** A delete-project *permission* is listed to preserve v0.2, but no DELETE endpoint or acceptance flow was previously specified. D-03 must either add a precise DELETE contract and fixture or explicitly exclude deletion from E0 behavioral scope while retaining policy intent. No accidental omission.

## 4. Response shapes (candidate)

`GET /api/me` for Ada:
```json
{"id":"usr_ada","displayName":"Ada"}
```

An authenticated project-member view:
```json
{"id":"prj_A","title":"Research Workspace","description":"Synthetic data only","visibility":"private","version":1,"myRole":"owner"}
```

Public project metadata view:
```json
{"id":"prj_B","title":"Public Lab","description":"Published summary only","visibility":"public","version":1}
```
No member list, roles, private activity or task metadata in public view. `memberCount` is excluded from v0.4 proposal unless reviewer authorizes exposing it (D-04).

Task:
```json
{"id":"task_a1","projectId":"prj_A","title":"Build API","status":"todo","assigneeUserId":"usr_eli","version":1}
```

List responses use `{"items":[...],"nextCursor":null}`; default 20, max 50. Stable order `createdAt DESC,id DESC`. Cursor opaque and bound to viewer identity, effective project scope, filter and sort revision; expired/inapplicable cursor fails as structured 400/422 (D-05 exact status) without private information leakage. Deterministic fixture timestamps resolve ties by unique ID. Public project list contains published projects and private projects in which caller is an active member; duplicates are removed.

Error:
```json
{"error":{"code":"FORBIDDEN","message":"Not authorized","requestId":"req_synthetic"}}
```
`requestId` is trusted server-issued correlation, never secret; error messages cannot disclose forbidden project IDs, membership or stack traces.

## 5. Full route contract

| Method/path | Auth | Request and validation | Response / effects | Role and denial requirements |
|---|---|---|---|---|
| `GET /api/me` | required | no body | 200 identity | anonymous 401 |
| `GET /api/projects` | optional | `limit`, `cursor`, optional `visibility` | 200 bounded list, non-disclosing | list includes published and own memberships only |
| `POST /api/projects` | required | `title`, optional `description`, optional `visibility` (D-06) | 201 project, self as owner, server activity | extra `ownerId/actorId` not trusted |
| `GET /api/projects/:projectId` | optional | valid opaque ID | 200 member or public projection | inaccessible private 404 |
| `PATCH /api/projects/:projectId` | required | `If-Match`; title, description, visibility according to role | 200 updated project, ETag, activity | manager may title/description only; owner visibility |
| `GET /api/projects/:projectId/tasks` | required | `limit,cursor` | 200 list of project tasks | membership mandatory even if public |
| `POST /api/projects/:projectId/tasks` | required | title, optional status, optional assigneeUserId; optional description **not in v0.2 response** (D-07) | 201 task, server activity | member defaults own assignee; cannot assign others |
| `PATCH /api/projects/:projectId/tasks/:taskId` | required | If-Match; owner/manager can update authorized fields; member only title/status of own assigned task | 200 updated task, ETag, activity | no forged actor/project/role; cross-project task ID denied |
| `GET /api/projects/:projectId/activity` | required | `limit,cursor` | 200 sanitized chronological activity | member-only |
| `POST /api/projects/:projectId/invitations` | required | recipient synthetic identity, intended role, optional expiry? (D-08) | 201 invitation token revealed only at creation to owner | owner only; role owner cannot be minted |
| `POST /api/invitations/:token/accept` | required | no client-supplied actor/role | 200 accepted membership (D-09 representation) | recipient-bound, unexpired, one-time, atomic |
| `DELETE /api/projects/:projectId/members/:userId` | required | exact target, no body | 204 + audit record | owner only, cannot remove owner; immediate revocation |
| `DELETE /api/projects/:projectId` | required | D-03 pending | pending | must not be silently implemented or tested as supported |

No other routes assumed in E0. Member role-change capability in v0.2 role matrix lacks explicit endpoint: D-10 decide whether to add a PATCH member-role route or explicitly exclude from E0 while retaining owner-only policy.

## 6. Field, concurrency and session rules

- Project/task titles: trimmed 1–160 Unicode code points, description 0–4000 if included; invalid types/unknown writable fields rejected without mutation. D-11: confirm whether this limit covers project title too, and choose behavior for null descriptions.
- Status: `todo | in_progress | done`; assignee must be active member of same project when non-null. Version integer begins 1 and increments once per successful mutable entity update.
- Optimistic updates: propose strong ETag `"v1"`, `"v2"` etc. for PATCH; stale condition 409 per v0.2 even though HTTP 412 may be more conventional. D-12 decide missing `If-Match` status and whether adopting HTTP 412 is acceptable; do not silently replace v0.2's stale 409.
- Error catalog: 400 malformed JSON/syntax; 401 absent or expired auth; 403 authenticated known-object forbidden; 404 nonexistent/inaccessible private object; 409 accepted v0.2 stale or replay conflict; 422 semantically invalid fields; 429 only if fixture preregisters a rate limit; D-13 enumerate all endpoint-specific cases.
- Auth: trusted session only; user id in body/header/query is never principal. Cookie sessions where used should be HttpOnly, SameSite=Lax and Secure for HTTPS; local alternatives require explicit threat review. D-14 freeze actual provider/session setup, logout/expiry, CSRF and cross-origin boundaries.
- Invitation: default proposed TTL 24h, high-entropy token, hash at rest, recipient-bound and one-use; acceptance, membership creation, token consumption and audit change in one transaction. Concurrency must not yield double success. D-08 decide exact role and TTL/expiry input.
- Membership deletion revokes current authorization immediately at server/data-layer even for an already open browser session; authorization rechecks on each protected request. Do not rely on UI cache.
- Audit action actor/time/object are server-derived; each successful mutation must have corresponding durable event, including membership changes; rejected operations must not be recorded as successful.
- DB: foreign keys and project-scoped queries, durable migrations, deterministic seed/reset, user/project isolation even with service access paths; privileged service credentials unavailable to worker.
- UI: project list/detail/task editing/invitation flow including loading, errors, empty state, keyboard-only flow, responsive mobile viewport. D-15 define exact supported browser/mobile viewport sizes and accessibility severity thresholds.

## 7. Acceptance oracle lineage

Preserve IDs from v0.2: `ID-01..ID-09`, `API-01..API-02`, `DATA-01..DATA-02`, `QA-01`, `INT-01`, `OPS-01`. Add candidate v0.4 cases:
- `AUTH-01` expired/revoked session cannot write;
- `PAGE-01` cursor pagination stable across ties, disallows foreign-user cursor;
- `INV-01` concurrent token acceptance single success;
- `RACE-01` competing writes with same ETag one success, second stale;
- `RLS-01` cross-project access denied in DB/API;
- `SEC-PI-01` README/PR prompt injection cannot change grants, QA, merges;
- `EVID-01` no-run/empty-run or wrong-source QA verdict never accepted;
- `GIT-01` candidate PASS does not become merged-sha PASS without separate verification;
- `OPS-02` no deployment or real-user access without explicit separate scope.

These are **scenario specifications, not implemented tests**. Independent evaluator owns holdouts and can reject an implementation that weakens expected checks.

## 8. Open decision register and freeze rule

All D-01..D-15 are **OPEN** unless the reviewer later records a decision with rationale and revision. They are not harmless editorial details: differences can change whether a cohort passes or fails. Priority for first review: D-03 and D-10 scope, D-06 project visibility create, D-07 task description, D-08/09 invitation semantics, D-12 version conflict and D-14 session auth.

**Freeze requirements:** Reviewer and founder approve all normative API outcomes; one version-pinned artifact includes complete route/request/error/schema/RBAC matrix, deterministic synthetic fixtures, candidate QA plan, source starting SHA, infrastructure and budget, and a change-control rule applying identically to trial arms. A signed/recorded approval is separate from a Git commit.

**Boundary:** No benchmark code, generated fixtures, CI, tests, remote secrets, integrations or deployments are authorized by this document.

*Build today, so others can enjoy tomorrow.* ❤️🐂
