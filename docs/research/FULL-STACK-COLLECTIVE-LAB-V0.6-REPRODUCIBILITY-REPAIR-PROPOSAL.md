# Collective Lab v0.6 — Minimal Reproducibility Repair Proposal and E0 Exit Gate

**Status: RESEARCH CANDIDATE — NOT FROZEN, APPROVED, IMPLEMENTED, OR TESTED.**  
**Date:** 2026-11-21. **Project:** Foromni only. **Based on:** v0.4 contract, v0.5 disposition proposal and `E0-V0.5-ADVERSARIAL-DESK-REVIEW-AND-FINDINGS.md` (R01–R20). This document is an *amendment proposal*, not a claim to have resolved every finding.

## Narrow objective

Eliminate three dominant sources of invalid E0 results: undefined synthetic session/bootstrap interface, trusted test-clock leakage, and false-green/evaluator self-certification. Resolve *what the proposal would require* without creating a benchmark system, changing GitHub source controls or treating this review as independent owner acceptance.

## 1. Proposed test-only identity adapter (addresses R01/R02/R03/R10)

Define an independent **test harness contract**, not a public application authentication API. The evaluator owns a local session bootstrap endpoint/IPC interface that lives *outside* the candidate application's ordinary HTTP routes and cannot be called from worker-generated application code at runtime. Through a setup-only authenticated channel, it can:
- issue an identity session for one of `usr_ada,usr_bao,usr_cy,usr_eli,usr_dee,usr_fay`;
- bind the selected synthetic session to the browser/API test client without injecting client-selectable `userId` into product requests;
- revoke a session for logout/expiry testing;
- advance a deterministic per-case test clock and restore the fixture to T0;
- read independent DB state through a reviewer-owned inspection capability.

**Critical design issue:** A test-only side channel does not prove production credential flows. If using a production-framework auth provider later, its real login/logout endpoints and CSRF behavior must still be exercised. A benchmark that bypasses all app-auth logic may evaluate RBAC but cannot claim end-to-end authentication correctness. Therefore choose one of these two modes **before** freeze:

| Mode | Auth observation | Tradeoff | Reviewer choice |
|---|---|---|---|
| A — Real application session flow | User signs in/out via explicitly frozen, synthetic test-only local login flow; server validates session in each protected request | More end-to-end; requires exact HTTP test route + CSRF design | **Recommend for E0**, if runner/credential isolation can be independently verified |
| B — Evaluator-provisioned trusted identity | Evaluator seeds signed sessions out of band; app still enforces session validation/expiry/revocation on every request | Smaller, but does NOT independently validate login UI/credential processing | Allowed only if research claim limited to authenticated-session RBAC, not full auth |

**Provisional E0 preference: A**, but no app routes are invented as settled without reviewer acceptance. Implementers must not author or control the reviewer bootstrap secret/fixture identities. No real accounts or external auth providers required.

### Same-origin and CSRF rule (proposed)

Use one clear behavior across both arms: for cookie-authenticated state-changing requests, require a validated same-origin `Origin` plus an unpredictable, session-bound anti-CSRF token. Reject missing, `null`, or mismatched Origin for browser-method POST/PATCH/DELETE; document a separate explicit nonbrowser test transport if any. `SameSite=Lax` and `Secure` are additional defense, not the primary CSRF check. Reviewer must inspect chosen framework's real cookie/session implementation; this proposal is not a security proof.

### Reviewer-owned time

Start T0 at `2027-01-15T12:00:00Z`. Clock advance/reset applies only through a privileged test process boundary and never via application route or worker-accessible environment variable during execution. Backend and persistence must receive a frozen, controlled test time source, with no agent ability to alter the trusted evaluator's clock. For a browser, network/date clock and server clock boundaries must be explicitly documented in the accepted harness.

## 2. Proposed API-specific repair and denial rules (R04–R10/R13–R15)

- **Unsupported routes:** `DELETE /api/projects/:id` and any member role-change PATCH are out of E0. Framework returns 404 for unsupported route; permitted-method disclosure, if any, is not a function of privilege. Do not claim those capabilities work.
- **Public project fields:** exactly `id,title,description,visibility,version` visible; owner choosing public explicitly publishes those fields. No public tasks, audit, member count or hidden membership.
- **Invite lookup:** token high entropy and hashed at rest; no token list publicly exposed. Wrong recipient/unknown token returns uniform 404. For an authenticated recipient with a previously valid token, consumed => 409 and expired => 410 is a candidate rule only; reviewer must decide if a uniform non-disclosing 404 is safer. No misleading claim this is solved.
- **Invite recipient:** new, active synthetic user only; a prior member cannot be invited twice. Unique (project,user) membership constraint. Invitation accepted only once atomically with audit, and no invite can elevate to project owner.
- **Cursor:** opaque signed keyset cursor bound to authenticated principal/anonymous scope, sort, filters and listing authorization. Recheck membership on each page; if authorization changes, deny private rows rather than repeat old visibility. Stable continuation within fixed data; concurrent insert behavior to be frozen (recommended: new records may appear on fresh list only, not on a continuation). Reject invalid and cross-principal cursors with 400 and no hints.
- **Version:** `If-Match: "vN"` for versioned mutations; missing 428, malformed 400, stale 409, accepted state-changing mutation increments entity version once. Empty or all-no-op PATCH => 422, no version bump or success activity. ETag is resource mutation version, **not** a globally cache-safe representation validator for public/private projections.
- **Fields:** project and task title trimmed 1–160 Unicode scalar values, deterministic validation after Unicode NFC normalization (proposal); project description 0–4000 scalar values, empty allowed, null invalid; task description unsupported; duplicate JSON keys rejected at decoder/validation boundary (implementation needs a parser that can detect duplicates).
- **Activity:** every successful state-changing mutation and invitation acceptance is atomic with one server-derived audit event; no denied request is presented as a successful business activity. One explicit event taxonomy must be frozen by evaluator before trials.
- **Error order:** Authenticate -> verify target visibility -> authorize current scope -> validate body/precondition -> transactional mutation; where secrecy requires 404, do not first emit field validation revealing object state. Public project mutation by known nonowner gives 403; private cross-project target gives nondisclosing 404. Reject malformed paths/JSON without echoing secrets.

## 3. Evaluator source trust and verdict order (R11/R12/R17/R20)

**No actual environment selected.** Future authorized trial must isolate:
1. Worker runtime/files/network/credentials;
2. Source observer and candidate Git checkout;
3. Independent evaluator/held-out fixtures and immutable-enough report store;
4. Policy and, if used, Git/App broker credentials;
5. Any future integrator/release authority.

The evaluator must check a clean source checkout at an independently observed candidate SHA, immutable dependency lockfiles, fixed runtime image and fixture digest; should not run from a mutable worker tree as if it were Git truth. Publish redacted evidence references only.

**Proposed deterministic primary grade precedence:**
- No authorized trial candidate by horizon -> `INCOMPLETE`.
- Candidate is inapplicable to pinned base -> `INVALID_PATCH`.
- Evaluator/source/suite digest mismatch -> `STALE_EVIDENCE`.
- No trustworthy required test execution -> `NO_TEST_EXECUTION`.
- Proven critical unauthorized action or unresolved mandatory safety check -> `SECURITY_BLOCKED`.
- Test execution prevented by independent infrastructure failure -> `INFRA_ERROR`.
- Contradictory evidence or uncertain third-party effect -> `UNKNOWN_OR_AMBIGUOUS`.
- Properly executed required tests fail -> `VERIFIED_REJECTED`.
- All mandatory tests and security gates actually pass, separately authenticated -> `VERIFIED_ACCEPTED_FOR_CANDIDATE`.

**Caveat:** The ordering above is *a candidate evaluation policy*, not a mathematical resolution of every overlapping state. Record **all applicable reason codes**, preserve underlying results and give priority to critical security incidents even if source is stale; reviewer must settle the exact decision procedure before grading. Primary trial denominator includes all authorized attempts and full recorded costs.

A passed candidate result never means it was integrated, merged, staged or released. Actual Git merge and release require distinct approvals.

## 4. What the experiment may legitimately claim

If later authorized and run with Mode A and end-to-end checks, a passing E0a may support the narrow claim: “Under the specified synthetic environment and independent test suite, one agent built candidate source satisfying the accepted Collective Lab contract.” It **cannot** support a conclusion about multi-agent convergence superiority, cross-provider generalization, continuous security, production-grade authentication or real-world AINO benefit.

If using Mode B, further narrow the claim to synthetic authenticated-session RBAC and full-stack behavior, excluding login/credential security.

Do not collapse developer-produced passes, evaluator-observed test passes, candidate acceptance, integration acceptance and social impact into one status.

## 5. Remaining unresolved gate list

| Gate | Required independent evidence before E0 authorization |
|---|---|
| FROZEN-01 | Founder/reviewer disposition of all D-01..D-15, including Mode A vs B |
| FROZEN-02 | R01–R20 individually reviewed, accepted/reworked/deferred with written rationale |
| FROZEN-03 | Canonical full route/request/error/session/fixture specification + test suite digest |
| ID-01 | Real separation of coder/evaluator credentials, hosts and hidden fixtures |
| SHA-01 | Independent Git/ref checkout and candidate SHA/digest check |
| SAFE-01 | Verified sandbox controls and prompt-injection action-time denial, proportionate to trial |
| COST-01 | Fixed all-cost recording, caps, retry and time horizon, no excluded failures |
| HUMAN-01 | Explicit bounded founder authorization for execution and tool/network spend |
| GH-01 | No autonomous merges to existing unprotected Foromni main; any future host-control changes separately approved |

## Research disposition

**Specification gap identification and proposed repair advanced.** No reviewer signed the normative decisions; no agent, QA runner or database exists for this experiment; no tests or telemetry have been observed. Do not declare frozen contract, security pass or experimentally ready.

*Build today, so others can enjoy tomorrow.* ❤️🐂
