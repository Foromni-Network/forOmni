# E0 Contract Reconciliation and Trial Authorization Package

**Status:** Research-only reconciliation; NOT an accepted API freeze, an approval, an executed test, or a release. Date: 2026-11-21. Scope: Foromni only.
**Sources:** FULL-STACK-REFERENCE-APP-CONFORMANCE-V0.2.md; FULL-STACK-REFERENCE-APP-API-FIXTURE-FREEZE-PROPOSAL-V0.3.md; E0-GITHUB-PROTECTIONS-READ-ONLY-REALITY-AUDIT.md; E0-INDEPENDENT-ACCEPTANCE-EVIDENCE-AND-GRADE-DECISION-TABLE.md.

## Findings: v0.2 vs v0.3

v0.2 establishes roles, exact endpoints and project-scoped permissions. v0.3 proposes concrete field bounds, cursor pagination, invitation expiry, versioned writes and deterministic fixtures. They are broadly complementary but v0.3 does not fully restate v0.2, and is NOT a replacement for its behavior matrix.

| Contract area | Confirmed alignment | Decision still required before freeze |
|---|---|---|
| Personas | Ada owner A; Bao manager A; Cy viewer A; Eli member A; Dee owner B; anonymous | Confirm fixture IDs and B public metadata projection |
| Project roles | v0.3 references v0.2 behavior matrix | Preserve member/manager/owner capabilities and explicit denial cases |
| Public visibility | Public metadata is distinguishable from member-only tasks/activity | Exact projection and unauthenticated output |
| Project creation | Authenticated actor is owner; private default | v0.2 permits optional visibility at creation, v0.3 example omits it: decide explicit accepted payload |
| Task writes | Member assigned-task restriction and version checks maintained | Full field schema, unknown/invalid fields, task description if supported |
| Lists | v0.3 suggests 20 default / 50 max, createdAt+ID ordering | Opaque cursor behavior, scope binding, invalid cursor status |
| Concurrency | v0.3 proposes integer entity version and strong ETag | Missing If-Match status, exact ETag format and compare semantics |
| Invitations | Opaque, hashed, recipient-bound, expiring one-use tokens | v0.3 24h TTL adoption; recipient identity/role and transaction atomicity |
| Membership | v0.2 owner-only delete endpoint; cannot remove owner | Revoked member session and cursor access behavior |
| Errors | v0.2 401/403/404/400/422/409, v0.3 common body | Exhaustive per-endpoint mapping, private resource non-disclosure |
| Activity | Authenticated server actor and timestamp | Ordering, server transaction and deterministic clock |
| QA/security | Independent exact-source positive and negative testing | Evaluator ownership, suite digest, security failures, resource budget |

**Recommendation:** Keep v0.2 for endpoint+role scope; accept/revise individual v0.3 decisions; then combine into reviewer-approved v0.4. The documents alone do not freeze E0.

## Mandatory independent behavioral checks before acceptance

- Identity: expired/anonymous denied, forged actor fields ignored.
- Privacy: Dee cannot access A; anonymous cannot discover private A.
- RBAC: Cy cannot mutate, Eli can only update own assigned task fields, Bao cannot alter owner controls.
- API: correct displayName shape, pagination, bad field errors and stale version conflict.
- Data: constraints, migration and persisted audit state after app process restart.
- Concurrency: two simultaneous writes do not overwrite silently; one invite cannot be accepted twice.
- UI: mobile/narrow viewport, keyboard navigation, loading and error state.
- Security: tool authorization survives README/PR prompt injection; worker never controls QA, protected main or credentials.
- Evidence: actual independent test execution on exact candidate SHA and prospective integration SHA, no stale green or empty test suite.
- Cleanup: disposable resources only, no external production data, no leftover credentials.

All cases are proposed, not implemented or executed.

## Authorization dossier: fields an owner must explicitly decide

| Field | Default pending approval |
|---|---|
| Objective, test oracle and version | Not frozen |
| Chosen isolated trial workspace/source commit | Not selected |
| Allowed source writes | None; no main merges |
| Worker runner, model and provider | Not selected |
| API credentials and authenticated worker identity | Not provisioned or audited |
| Network scope and access to real data | Deny by default; synthetic-only |
| Independent QA principal and evidence location | Not verified |
| Fixed build image, database seed and reset | Not pinned |
| Spend limit, retries, time horizon and stop conditions | No spending authorized |
| Threat model and prompt injection gate | Research requirements only |
| Teardown, retention and incident owner | Not assigned |
| Deployments, third-party outreach, publishing results | Not authorized |

A trial cannot be treated as approved because a document describes its potential workflow.

## Key readiness findings

1. GitHub main reports protected=false and required check enforcement off. Repository rulesets list was empty via this connection; detailed branch protection returned 403. **Autonomous merges to main are blocked as a recommended security decision**, although not currently host-enforced.
2. Current API contract is not formally frozen; some pagination, invitation, errors, versions and authentication decisions remain open.
3. Neither full-stack E0 implementation nor independent QA has been executed.
4. Worker sandbox isolation, principal enforcement, full-cost accounting, teardown and human authorization remain open.
5. Experiment design may advance through documentation; running tests, CI, new infrastructure or changing GitHub policy requires separate explicit authorization.

## Research-only next steps

- Review and consolidate v0.2/v0.3 into one versioned v0.4 candidate, preserving full behavior matrix.
- Specify evaluator trust boundary, suite and environment digests, real Git state checks, retention and missing-evidence rules.
- Ask an authorized repository administrator to examine protection/settings through appropriate access *before* ever enabling autonomous Git writes.
- Complete the founder-governed E0 authorization package with exact repo/runtime/provider/resource limits.
- Run an isolated one-agent baseline only once separately approved; do not conflate this with a proven AINO productivity improvement.

**Disposition: RESEARCH IMPROVED; E0 EXECUTION NOT READY. No tests, deployments or Git setting mutations carried out.**

*Build today, so others can enjoy tomorrow.* ❤️🐂
