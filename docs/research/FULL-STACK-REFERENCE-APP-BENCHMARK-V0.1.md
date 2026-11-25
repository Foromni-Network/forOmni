# Fixed Full-Stack Reference Application for Autonomous Agent Experiments v0.1

**Status:** Research fixture specification; no app has been built or tests executed.  
**Date:** 2026-11-21 · **Scope:** Foromni research only, separate from IE.  
**Companions:** END-TO-END-AINO-EXPERIMENT-READINESS-AND-EVIDENCE-PLAN.md; CONVERGENCE-WORK-PACKET-TYPED-CONTRACT-V0.2.md; AI-WORKFORCE-HOSTING-AND-SYNERGY-ARCHITECTURE.md.

## Benchmark problem and invariants

A small **fictional** global-collective project workspace called `Collective Lab`. A visitor views public projects; a synthetic member can log in, maintain an allowed profile, create a project, invite another **synthetic** member, create/assign/update tasks and view activity. Access must be role-scoped and tenant/project private by default. Design for mobile accessibility and straightforward maintainability.

This is a reproducible **controlled full-stack benchmark**, not an actual Foromni product commitment. All test users and data are synthetic. The specification must be frozen across comparisons; no cohort may quietly skip auth, persistence, QA or accessibility.

## Functional vertical slices

| Slice | Scope | Acceptance criteria and boundary |
|---|---|---|
| V0 foundation | Responsive shell, routes, UI states | Keyboard navigation, mobile viewport, accessible form labels and error/loading states |
| V1 identity | Synthetic signup/login/session and members | Reject anonymous private reads; server verified identity; session expiry; no real email sending |
| V2 projects | Project create/list/view/edit | Public projects visible to visitors only when explicitly published; private projects scoped to owner/member |
| V3 tasks | CRUD, assignment, status and activity | Only project members with allowed role can create/change/assign; record attribution and timestamps |
| V4 API contract | Typed member/project/task APIs | UI/provider version agreement, unknown fields/invalid permissions properly rejected |
| V5 durability | Database migrations and persistence | Clean setup; restart persistence; migration compatibility, rollback/repair plan |
| V6 resilience | Errors, retry, unauthenticated, stale changes | Fail clearly without showing false success; optimistic concurrency or appropriate conflict handling |
| V7 integrated delivery | Combined source, CI, staging rehearsal | Exact merge group verified; synthetic staging behavior repeatable; no public deployment |

**No slice is green.** The spec defines what future experiments should attempt, not currently available app features.

## Suggested API contract v1 (technology-neutral)

- `GET /api/projects`: only projects visible to requester by visibility and membership.
- `POST /api/projects`: authenticated creation; owner recorded by server.
- `GET /api/projects/{id}`: private access denied unless member.
- `PATCH /api/projects/{id}`: owner/manager only, version-safe updates.
- `GET /api/projects/{id}/tasks`: project member only when private.
- `POST /api/projects/{id}/tasks`: allowed project role.
- `PATCH /api/projects/{id}/tasks/{taskId}`: allowed role with audit event.
- `GET /api/me`: authenticated identity and allowed profile data.
- `GET /api/projects/{id}/activity`: scoped event history with no raw secrets.

Do not accept client-provided `owner_id` as authority. Use stable JSON error contract (e.g. code/message/request_id) and define pagination, filtering and concurrency precisely before executing trials. Browser UI may rely on generated API types or consumer/provider checks.

## Data and access model (conceptual)

`users(id, display_name, created_at)`  
`projects(id, owner_user_id, title, description, visibility, version, created_at)`  
`memberships(project_id, user_id, role, joined_at)`  
`tasks(id, project_id, assignee_user_id?, title, status, version, created_at, updated_at)`  
`activity(id, project_id, actor_user_id, action, target_type, target_id, created_at)`

Roles: `owner`, `manager`, `member` and `viewer`. Server-side enforcement: owner can administer membership, manager can edit tasks and assign within project, member can create/update tasks as explicitly allowed, viewer reads permitted scope only. Define exact role matrix and fixture permissions before a trial; ambiguity is a research blocker, not a license for each team to pick easier rules.

### Synthetic test personas

- Ada: project A owner; project B non-member.
- Bao: project A manager.
- Cy: project A viewer.
- Dee: project B owner; project A non-member.
- Unauthenticated visitor: public-only content.

Do not route real user records or production secrets into these experiments.

## Frozen acceptance checks (proposed)

- A visitor can view only published projects; no private task or activity data leaks.
- Ada can create/manage project A; cannot modify project B.
- Bao can create/assign/update project A tasks per approved matrix.
- Cy cannot mutate project A tasks.
- Dee cannot read or mutate project A private data.
- A malicious client request changing project ownership/foreign IDs cannot escalate access.
- API/member field contract can be consumed by UI; `name` vs `displayName` injection causes test failure until resolved.
- Refresh/restart preserves accepted projects/tasks and attribution.
- Mobile keyboard accessible forms and meaningful loading/error states tested.
- Combined branch result against current main is tested; stale source check alone cannot admit it.
- No step creates real accounts, sends mail, calls paid services or publishes the app.

Independent reviewers define exact checks and sealed adversarial cases before starting the benchmark. Do not rely solely on self-reported implementer screenshots.

## Failure-injection matrix

| Injection | Expected observed response |
|---|---|
| Backend field drift `displayName` → `name` | Consumer/provider or E2E failure, no accepted combined result |
| API permission check omitted | Cross-project private access tests fail, release denied |
| Database migration breaks old reader | Compatibility gate or staging run fails |
| One worker drops offline mid-task | Scoped lease fenced, work preserved as untrusted pending candidate |
| Main advances after isolated green | New prospective integration check required |
| CI returns unknown/timeouts | Health/QA UNKNOWN; no fabricated pass |
| Duplicate webhook / task claim | Idempotent processing or ownership dispute; no double acceptance |
| Budget limit reached during retry loop | Stop further paid tool calls, report incomplete |
| Reviewer shares implementer authority | Independence requirement fails |
| Founder declines release | Integrated/staged artifacts may remain; no production deployment |

## Fair cohort protocol

All cohorts receive exactly the same functional scope, acceptance oracle and safety requirements. Compare:
- 1 coding generalist + **external independent QA**;
- 3 implementer/coordinator agents + independent QA;
- 8 specialized workers + independent QA;
- adaptive 1→3→8 with the same evaluation rules.

Within each cohort, compare ordinary prompts against convergence-aware packets after freezing the required specifications. Keep model/provider/hardware differences controlled or explicitly vary one factor at a time. Count **all** model calls, orchestration overhead, infrastructure, CI, retries, human review and failed attempts. The eight-worker cohort may consume more cost; don't normalize by hiding that fact.

Primary: independently accepted integrated vertical slices per full dollar. Secondary: completion time, regression escape, source conflict/invalidation, human oversight hours, safety policy violations, onboarding/maintainability, recoverability and accessibility.

The largest valid result may be that one generalist plus strong CI outperforms a larger studio for small scopes. That is evidence to preserve rather than discard.

## Hosting/trial reproducibility envelope to freeze

- Host class: local sandbox, single VM or ephemeral remote; OS/kernel/container runtime and resource caps.
- Agent runtime/model release IDs, supported tools, token limits and API access policy.
- Network egress and private-data constraints, synthetic database snapshot, fixture seed.
- Convergence planner/control state and work packet version if treatment.
- Git branch protection, merge-queue/CI configuration and independent reviewer principal.
- Real task/source/merge SHA chain, event and evidence artifact digests.
- Operational logs/traces and per-task cost/provisioning records.
- Versioned scripts/commands needed to reproduce under equivalent approved conditions.

No actual host, paid vendor, environment or trial is selected or provisioned by this spec.

## Research completion criteria before the first authorized run

1. Approve the exact role matrix, API response shapes, migration and accessibility oracle.
2. Freeze the fixture, hidden negative cases and evaluation plan.
3. Choose an isolated host/runtime and reject unsafe shared privileged runners.
4. Define effective grant and QA independence enforcement.
5. Set objective budget ceiling and failure/stop conditions.
6. Secure explicit authorization for **specific** disposable experimental operations.
7. Publish independent verified results with negative cases and limitations, before making empirical marketing claims.

## Benefit to independent AINOs

A vendor-neutral full-stack fixture can become a common proving ground for AI-native organizations of different sizes, models and hosting arrangements. Publishing the exact assumptions, failure cases and operating costs helps others choose systems based on evidence rather than agent-count hype.

**No benchmark results exist yet.**

*Build today, so others can enjoy tomorrow.*
