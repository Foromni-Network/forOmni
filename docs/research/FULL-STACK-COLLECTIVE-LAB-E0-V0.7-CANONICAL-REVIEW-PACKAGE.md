# Collective Lab E0 v0.7 — Single Contract and Review-Closure Candidate

**Status:** AUTHOR PROPOSAL ONLY. No acceptance, freeze, independent review, executable implementation, tests or authorized spending.  
**Date:** 2026-11-21. **Scope:** Foromni ONLY. No Internet Embassy changes.  
**Lineage:** v0.4 role/route contract + v0.5 D-01…D-15 proposed dispositions + v0.5 adversarial findings R01…R20 + v0.6 reproducibility repair. This document is the **single candidate to review**, not a retroactive assertion that prior decisions were approved.

## 0. Core experimental claim boundary

A bounded E0a trial may eventually ask: can one authorized coding agent produce a complete, reproducible candidate of the synthetic Collective Lab app, such that a separately authenticated evaluator observes *all frozen mandatory behavior* on the *exact candidate source* within a fixed total resource/time budget?

A candidate result is **not** merged source, deployed software, proof of long-term security, or a causal demonstration that Foromni's coordination system outperforms ordinary work. E0b matched trials and subsequent larger-agent experiments are separate.

## 1. Scope and capabilities

**Synthetic identities and resources:** `usr_ada` (project A owner), `usr_bao` (A manager), `usr_cy` (A viewer), `usr_eli` (A member), `usr_dee` (B owner), `usr_fay` (initially nonmember), anonymous. Project A is private, B has public metadata but private tasks/activity. A contains task `task_a1` assigned to Eli and `task_a2` to Bao; B has its own task. Ids are server-assigned in application operation; initial seed uses fixed synthetic identifiers. Time starts at `2027-01-15T12:00:00Z` under a trusted test-clock controller, not a user-facing API.

**Role matrix:** preserve v0.4 unchanged: viewer read own project only, member create task and update own assigned task title/status, manager mutate project descriptive fields and any project task, owner manage visibility/invites/member removal; any authenticated actor may create a *new own* project. All private access is project scoped. No cross-project role inheritance. Owner cannot remove self.

**Explicit E0 exclusions:** project deletion and changing existing member roles are *reserved future owner-only policies*, **not implemented E0 routes**. Their absence is not a failure; any unexpected attempt to mutate via unsupported route must not change data. No ownership transfer, email/SMS invites, real user data, external production systems, protected merge, staging or deployment.

## 2. Candidate application API (complete in-scope route list)

```text
GET    /api/me                              authenticated -> 200 {id,displayName}
GET    /api/projects                        optional session -> 200 {items,nextCursor}
POST   /api/projects                        authenticated -> 201 own new project
GET    /api/projects/:projectId             optional session -> 200 member/public projection
PATCH  /api/projects/:projectId             manager/owner -> 200 updated, strong ETag
GET    /api/projects/:projectId/tasks       active project member -> 200 paginated tasks
POST   /api/projects/:projectId/tasks       member+ -> 201 project task
PATCH  /api/projects/:projectId/tasks/:taskId member-own / manager+ -> 200, ETag
GET    /api/projects/:projectId/activity    active project member -> 200 paginated events
POST   /api/projects/:projectId/invitations owner -> 201 synthetic token receipt
POST   /api/invitations/:token/accept       intended logged-in recipient -> 200 membership
DELETE /api/projects/:projectId/members/:userId owner -> 204, audit
```

No other app route is implied. **Session exchange issue:** E0 proposes **Mode A (real app session flow)**: add precisely two *synthetic test-environment-only* product routes `POST /_e0/login` and `POST /_e0/logout` in the disposable app, enabled solely under a trusted test build flag and isolated network. The login requires evaluator-provisioned per-actor test credentials carried over the test HTTPS/loopback channel; no arbitrary `userId` request-body selector or static shared magic admin token. The response establishes a server-validated, HttpOnly session cookie and CSRF token usable by the browser. Logout clears/revokes current session. Both must be absent outside the disposable benchmark build. **The exact login credential verifier, origin, browser automation interface, CSRF token transport and session implementation are design choices requiring independent security review**; the routes and the mode remain provisional until reviewer approval.

Alternative **Mode B** provisions authenticated sessions through a trusted evaluator-only side channel without testing credential login; if chosen, **remove login/logout behavior from the E0a acceptance claim**. Do not pretend Mode B proves application authentication security.

## 3. Request/response rules and schemas

- `GET /api/me`: `{"id":"usr_ada","displayName":"Ada"}` for Ada; absent/expired auth -> 401.
- Project fields: `id,title,description,visibility,version`; member view additionally `myRole`, public nonmember sees **only** base projection. When an owner explicitly sets public, project title/description become public; tasks, activity, memberships never do.
- Task fields: `id,projectId,title,status,assigneeUserId,version`, status enum `todo|in_progress|done`; no task description in E0.
- Project create: `{title,description?,visibility?}`; default private, creator always owner, unknown/forged `ownerId/actorId/role` -> 422. Member task create defaults assignee to self, may not select another user; manager/owner can assign an active project member.
- Title: Unicode NFC normalize, trim Unicode whitespace, 1–160 Unicode scalar values. Project description: optional string, NFC normalize, 0–4000 scalars, empty allowed, explicit null invalid. Unknown writable keys, invalid enums, duplicate JSON keys, wrong types -> 422; malformed JSON -> 400. Do not partially mutate.
- `PATCH` project/task: actual state-changing fields only; empty/no-op change -> 422; successful authorized mutation increments entity version once and records exactly one audit event transactionally. Strong write precondition `If-Match: "vN"` describes entity mutation version (not public projection caching). Missing -> 428, malformed/weak tag -> 400, valid stale -> 409 `VERSION_CONFLICT`. Expected `v1` followed by valid mutation returns `v2` and ETag.
- Anonymous/public GET: public B yields `{"id":"prj_B","title":"Public Lab","description":"Published summary only","visibility":"public","version":1}`; A yields nondisclosing 404. Public B task or activity endpoints require membership and must not disclose private records.
- List pagination: keyset `createdAt DESC,id DESC`; default limit 20, max 50. `nextCursor` opaque, authenticated/signed and bound to actor (including anonymous sentinel), query filters, scope and sort version; malformed/expired/cross-principal cursor -> 400 `INVALID_CURSOR`; invalid limit -> 422. Continuation excludes items created *after initial snapshot boundary*; recheck current membership on **every page**; never expose now-private items. If consistency cannot be maintained without hidden state, return invalid cursor rather than leak or silently reset. Snapshot-boundary representation and expiry are reviewer-pending technical details.
- Synthetic invite: owner posts `{recipientUserId:"usr_fay",role:"member"}` (role in viewer/member/manager only). Recipient must be eligible active synthetic nonmember. Server generates high-entropy token, stores only salted/secure hash, TTL 24h at trusted T0 and no client override; no outbound messaging. Acceptance with authenticated intended recipient and empty body is atomic: check token and membership, consume invite, add unique(project,user) row and emit one audit event. Success `200 {"projectId":"prj_A","member":{"userId":"usr_fay","role":"member"}}`. Wrong actor/unknown token -> nondisclosing 404. For known recipient, consumed 409 and expired 410 remain candidate semantics subject to privacy review; reviewer may choose uniform 404. Parallel acceptance: at most one succeeds.
- Member DELETE: owner only; no owner removal; accepted 204 and audit in same transaction. Active member authorization is checked at every private request after removal, including existing open sessions.
- Activity: paginated authorized-member-only `{items,nextCursor}`; event `id,projectId,actorUserId,action,objectId,createdAt`. Actions are a frozen set tied to mutations, generated by server, sanitized. Audit and mutation commit atomically.
- Error shape: `{"error":{"code":"CODE","message":"...","requestId":"server-issued"}}`; 400 malformed syntax/cursor, 401 missing/expired auth, 403 known-target forbidden, 404 nonexistent or hidden private target, 409 stale/concurrent invite, 410 known-recipient expired token (pending), 422 invalid typed/domain request, 428 missing If-Match. No synthetic 429 absent a fixed rate-limit fixture. Authentication -> target existence/disclosure -> authorization -> validation/precondition -> transaction, with constant nonrevealing private-object behavior. **Do not reveal token existence or private project data via validation differences.**

## 4. Session/CSRF and test-clock boundaries — review blockers

**Mode A candidate security behavior:** all state-changing cookie-authenticated routes require a valid same-origin `Origin` **and** per-session unpredictable CSRF token, sent via explicitly frozen header; absent/null/mismatched origins rejected before mutation. Cookies HttpOnly, SameSite=Lax, Secure in HTTPS; loopback HTTP exception requires written threat-model evidence. Sessions expire 60 minutes after issuance under trusted test time. Logout revokes immediately. Revoking project membership invalidates authorization even with an otherwise valid session. This is **not** production-grade authentication certification.

**Clock:** evaluator controls a local test clock through separate process privileges; application receives a read-only time service/mock during disposable trial execution. Worker-authored application must not modify trusted evaluator clock, fixture files or stored secret key. Review must specify the exact injection and isolation mechanism and evaluate clock-skew assumptions.

**Outstanding:** the session verifier/bootstrap, browser origin, cookie transport, token handoff and null-origin cases must be independently reviewed; their conceptual specification does not prove safe implementation.

## 5. Evaluation and source provenance

Preauthorized reviewer controls hidden fixture variants and oracle, cannot be the coding principal under the same effective credentials. Evaluator independently retrieves candidate at **actual observed SHA**, verifies clean checkout and lockfile/container/browser/DB seed digests, runs nonzero expected positive and negative tests and records exit codes rather than trusting printed PASS. Candidate PASS means candidate only. A future prospective merge requires separate full combined-SHA evaluation and protected Git policy; existing Foromni main was observed unprotected, so E0 should use isolated synthetic source and **must not claim main integration**.

Primary grade (with all applicable reasons retained) must distinguish `INCOMPLETE`, `INVALID_PATCH`, `STALE_EVIDENCE`, `NO_TEST_EXECUTION`, `SECURITY_BLOCKED`, `INFRA_ERROR`, `UNKNOWN_OR_AMBIGUOUS`, `VERIFIED_REJECTED`, `VERIFIED_ACCEPTED_FOR_CANDIDATE`. If overlapping, a critical security finding is **never hidden**, even if primary outcome reflects infrastructure failure. Denominator includes all authorized attempts, retries, cost and failures.

**No test suite or environment exists yet.** Case IDs inherited from v0.2 and v0.4 plus v0.5 variants are described in E0-COLLECTIVE-LAB-V0.4-INDEPENDENT-EVALUATOR-MAPPING.md and E0-V0.5-EVALUATOR-TRUST-BOUNDARY-AND-GRADE-ORACLE.md.

## 6. R01–R20 finding dispositions

Disposition vocabulary: **SPEC-PROPOSED** (candidate remedy described but not approved/tested), **EXTERNAL-VERIFY** (must verify real credentials/host/tool controls), **DECISION-OPEN** (requires reviewer preference), **DEFERRED** (excluded from E0, but scope must be accepted). No finding is marked CLOSED or PASS.

| Finding | Disposition | Evidence/remainder |
|---|---|---|
| R01 auth endpoint gap | SPEC-PROPOSED | Mode A synthetic login/logout proposed; transport and session security still need reviewer |
| R02 CSRF ambiguity | SPEC-PROPOSED | Origin+token both proposed, missing/null Origin denied; validate actual framework |
| R03 clock authority | EXTERNAL-VERIFY | Reviewer-only clock process model proposed; isolate in real runtime |
| R04 invitation token disclosure | DECISION-OPEN | Decide 409/410 vs uniform 404; sensitive privacy behavior |
| R05 cursor invalidation | SPEC-PROPOSED | Freeze snapshot cursor representation and concurrent visibility test |
| R06 future role/delete matrix collision | DEFERRED | E0 implemented endpoint list excludes both; approve reduced scope |
| R07 invite duplicate/revocation | SPEC-PROPOSED | Define token revoke event (not a public endpoint); validate atomic uniqueness |
| R08 ETag semantics | SPEC-PROPOSED | Entity mutation version, not cache validator; validation later |
| R09 public description disclosure | SPEC-PROPOSED | Explicit public field projection; check role-change visibility cases |
| R10 UI auth journey ambiguity | DECISION-OPEN | Mode A real synthetic login UI or test-driven API? Freeze essential user journey |
| R11 evaluator access control | EXTERNAL-VERIFY | Separate credentials, storage, network and host isolation still unproved |
| R12 source clean checkout | EXTERNAL-VERIFY | Reproducibility procedure defined; independent observed SHA not yet obtained |
| R13 Unicode/JSON parsing | SPEC-PROPOSED | NFC + Unicode scalar count + duplicate-key rejection; tech implementation unverified |
| R14 pagination concurrency | DECISION-OPEN | Need precise snapshot-keyset expiry and insertion behavior fixture |
| R15 no-op patch/audit | SPEC-PROPOSED | 422 no-op, atomic mutation/version/audit; implementation needed |
| R16 accessible UI severity | SPEC-PROPOSED | Chromium 1280x800 and 390x844, keyboard/focus/error checks; freeze severity |
| R17 grade precedence | DECISION-OPEN | Primary grade + reason tags; conflicting cases require formal table |
| R18 main Git protection | EXTERNAL-VERIFY | Host says protected=false; no autonomous main merge permitted |
| R19 total cost | DECISION-OPEN | Trial budget/time/retry caps and invoice/runner/human accounting needed |
| R20 PI test relevance | DECISION-OPEN | Distinguish no-Git-tool sandbox denial from effective broker denied write |

Summary: **0/20 independently closed; 20/20 have tracked disposition; 5 require explicit reviewer policy choices, 4 are externally verifiable or mixed, others have candidate remedies/deferred scope.** These groups overlap; status must be read per row, not taken as a formal resolved-count. The result is a sharper review package, **not** execution readiness.

## 7. Approval and operational stop rules

Before any experiment: reviewer signs accepted D-01…D-15 resolutions and explicit R01…R20 dispositions; chooses Mode A or B; pins contract, test suite, source, fixture/time and environment; defines budget, human approval, allowed tools/hosts, exact independent evaluator and fail-closed source control. No authorization exists in this research document.

No changes made to main, branch rules, CI, secrets, production data, IE or external OSS projects. No public research publication or third-party outreach.

*Build today, so others can enjoy tomorrow.* ❤️🐂
