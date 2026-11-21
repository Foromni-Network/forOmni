# Convergence-First Controller: Build for Integration Before Writing Code

**Status:** Foromni research proposal; not implemented, benchmarked or selected for production.  
**Date:** 2026-11-21  
**Project boundaries:** Foromni only. Internet Embassy may be investigating a related controller independently; this file does not inspect, copy, modify, connect or infer the status of IE's implementation. Any comparative study requires separate authorization and clean ownership/permissions.  
**Related:** CONVERGENCE-CONTRACT-V0.1.md, SCALING-THE-CONVERGENCE-CONTROLLER.md, AI-WORKFORCE-AUTHORITY-EVENT-CONTRACT-V0.1.md, AI-FULL-STACK-END-TO-END-WORKED-TRACE.md.

## The architectural shift

**Reactive integration:** Agents independently build whole features, then a merger discovers incompatible work, stale branches, overlapping ownership, and missing end-to-end evidence.

**Convergence-first engineering:** Before a worker writes code, a controller helps translate the objective into **small, integration-ready vertical slices** with explicit task ownership, interface dependencies, required evidence, target baseline, and a planned admission path. Agents receive verified context and short-lived branch instructions. After implementation, a *separate enforcement plane* independently validates and safely integrates only eligible results.

This is not a promise to remove all conflicts. It aims to prevent predictable integration failure, reduce late rework, and make other failures diagnosable and recoverable. A controller's planning advice must not automatically grant source-control rights.

## 1. Two interlocking controller functions

### A. Convergence planner (pre-development, agent-assisted)
- Interpret owner-approved objective, scope and acceptance.
- Inspect **authoritatively observed** repository baseline, file/module ownership, API contracts, dependency DAG, active tasks and blocked candidate inventory.
- Check whether an existing ready/in-progress/partially integrated task already addresses the requested feature; prefer repair/continuation over duplication.
- Propose small, backward-compatible vertical slices and precise changed interfaces.
- Assign isolated workspace/branch and narrowly scoped ownership *through an authorized coordinator*.
- Produce a candidate-ready **work packet** with current source/base SHA and definition of done.
- Recommend shared contract fixtures, feature flags, branch-by-abstraction or expand/contract changes when appropriate.
- Plan independent QA and a protected admission route before dispatch.
- Recheck for task/base drift when worker accepts packet.

### B. Convergence gate (post-development, policy enforced)
- Authenticate candidate, task revision, actual branch head, dependencies and grant.
- Verify artifact integrity and independently observed QA claims, including consumer/provider interfaces.
- Construct or delegate an exact prospective merge result against current main / eligible preceding candidates.
- Enforce protected checks, scoped permissions, merge-group revision identity, policy version and acceptance evidence.
- Queue or batch compatible candidates; isolate conflicts for repair; avoid stale-read admission.
- Observe actual resulting main SHA after merge; reconcile ledger outages and duplicated messages.
- Distinguish integrated source from staged, released, healthy and beneficial outcomes.

**Key insight:** A planning agent can help agents *build with convergence in mind*, but the final gate must be trustworthy even when planners and builders make mistakes or collude.

## 2. Work packet v0.1: preflight handoff proposal

```json
{
  "contract_version": "foromni.convergence-first.packet.v0.1-DRAFT",
  "objective_id": "OBJ-EXAMPLE",
  "task_id": "TASK-EXAMPLE",
  "task_revision": 3,
  "baseline": {
    "repository": "example/example",
    "target_ref": "refs/heads/main",
    "expected_main_sha": "PLACEHOLDER_NOT_A_GIT_SHA"
  },
  "ownership": {
    "attempt_id": "ATT-EXAMPLE",
    "scope": ["src/features/members/*"],
    "branch": "work/TASK-EXAMPLE/ATT-EXAMPLE",
    "lease_epoch": 2
  },
  "integration": {
    "vertical_slice": "Member directory can render from a stable API",
    "interfaces_owned": ["GET /api/members"],
    "interface_contract_revision": "api-r4",
    "depends_on": ["TASK-SCHEMA"],
    "compatibility_policy": "backward-compatible",
    "feature_flag_required": false
  },
  "acceptance": {
    "criteria_revision": "criteria-r3",
    "required_evidence": ["provider-contract-check", "consumer-contract-check", "end-to-end-test", "independent-qa"],
    "protected_admission_policy": "gate-r2"
  },
  "authorization": {
    "permitted_actions": ["read_scoped_repo", "write_isolated_branch", "run_disposable_tests", "open_pr"],
    "protected_merge_allowed": false,
    "effective_grant": "NOT_ISSUED"
  },
  "packet_status": "DRAFT_UNVERIFIED"
}
```

This illustrative JSON is **not** an authenticated grant, enforced file lock, executable schema or confirmed Git snapshot. Real implementation must validate SHA shape/digests, policy revisions, exact ownership and independently observed ref state. Path patterns alone cannot enforce exclusive writes when two modules affect one shared API or an agent holds unrestricted write tokens.

## 3. Developer-facing preflight lifecycle

1. **Discover:** Obtain latest approved objective and existing task IDs; refuse unsupported "start a new duplicate" directives.
2. **Model dependencies:** Declare API/schema and migrations first, with owners and compatibility constraints.
3. **Split vertically:** Prefer an independently mergeable change that leaves main valid, possibly hidden behind a correctly scoped feature flag.
4. **Check baseline:** Fetch current base SHA, interface version and dependencies, not an old prompt's assumptions.
5. **Reserve safely:** Allocate isolated attempt branch and effective scoped grants; branch/file claims are advisory without server-side enforcement.
6. **Generate:** Worker implements *within* packet; may propose scope changes but cannot unilaterally redefine acceptance.
7. **Self-check:** Worker runs allowed local tests, captures exact commands/source SHA, and provides known failures, without self-awarding independent acceptance.
8. **Reconcile early:** Detect overlapping interfaces or drift while development is underway; update work packets only through authorized revision events.
9. **Independent QA:** Check acceptance against exact candidate and combined context.
10. **Protected publish:** Queue, revalidate current merge group, merge once, read back actual SHA and continue to staging policy.

**Avoid false rigidity:** An agent may discover that the original architecture was wrong. It should submit a bounded proposal to revise contract/owners, preserving useful work and raising only the required decision—not force the wrong design.

## 4. Where convergence prevention works, and where it cannot

| Failure | Early intervention | Protected downstream check |
|---|---|---|
| Two agents invent duplicate modules | Existing task/ownership index and explicit task UUID | Reject conflicting candidate scope |
| UI expects `displayName`; API returns `name` | Versioned consumer/provider contract, jointly reviewed schema | Pact-like provider/consumer verification and E2E |
| Shared schema migration breaks older frontend | Expand/contract migration, compatibility requirements | Schema/backward compatibility gates |
| Two branches edit same file | Isolated branch, overlap warning, shared contract steward | Git conflict resolution plus retest |
| Different files break shared behavior | Declared interface ownership and dependency graph | Merge-group integration tests; Git clean merge is insufficient |
| Baseline changes during long-running attempt | Drift notifications and bounded work packets | Exact prospective merged result against current main |
| Agent says "all tests pass" | Evidence requirements in original task packet | Trusted CI observations and independent reviewer |
| Merge bot crashes after ref update | Durable action/idempotency design | Read actual Git ref, reconcile before retry |
| Too many active candidates | WIP caps and dependency-based routing | Fair queue/backpressure, not bypass of gates |
| Release looks safe despite broken customer workflow | Owner-defined observable outcomes before development | Staging, runtime and stakeholder acceptance separate |

## 5. Adopt/extend/reject: candidate existing components

**Adopt where suitable**
- **GitHub branch protection + native merge queue** for protected admission, current-base/queued-change checks and merge_group validation; verify settings and edition before claiming protection. https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue
- **Zuul** for demanding dependency-aware speculative gating; high operational footprint warrants justification. https://zuul-ci.org/docs/zuul/latest/gating.html
- **Pact** or equivalent consumer-driven testing to verify API expectations rather than merely textual merge compatibility. https://docs.pact.io/getting_started/verifying_pacts
- **Short-lived trunk-focused work and branch-by-abstraction** as engineering practices for integration-oriented slices, not as a requirement that workers push directly to unprotected main. https://trunkbaseddevelopment.com/
- **OpenTelemetry** for source-attributed logs, timing and trace identifiers, not proof of correctness. https://opentelemetry.io/docs/

**Extend**
- Portable objective/task/attempt identity and evidence binding across agent providers.
- Dependency/contract-aware preflight packet; task/branch ownership mapped to real enforcement.
- Safe re-planning on changing code, model handoffs and missing reviewers.
- Outcome/permission/QA audit linking work packets to protected main SHA.
- Adaptive queue capacity and objective-level progress projection.

**Reject or postpone**
- Building a new Git forge, full CI engine, task-board UI or merge queue before proving a genuine gap.
- Giving LLM planners unrestricted credentials to rewrite main, protections, or QA policy.
- Pretending a path claim is an atomic lock or a self-reported test is independent evidence.
- Assuming a single centralized controller should control independently governed collectives.

## 6. Critical authority matrix

| Operation | AI planner | AI implementer | Independent QA | Trusted policy service | Protected merger | Human/collective owner |
|---|---|---|---|---|---|---|
| Propose roadmap task/owner | Propose | Propose | Comment | Validate scope | No | Approve material change |
| Read permitted repo evidence | Yes | Yes | Yes | Verify grant | Yes | Establish boundaries |
| Write isolated task branch | No by default | With grant | Separate fixtures only | Authorize/deny | No | Set risk controls |
| Change interface agreement | Propose | Propose | Evaluate | Enforce revision | No | Approve when material |
| Assert candidate completed | Propose | Submit evidence | No self-verdict | Do not trust self-report | No | No automatic completion |
| Independent acceptance | No | No | Check and submit verdict | Validate independence | Enforce gate | Resolve high-impact exception |
| Merge protected main | No | No | No | Authorize eligible action | Execute | Govern policy |
| Production/public release | No | No | Verify artifact | Enforce policy | No | Accountable approval |

## 7. Four testable hypotheses and baseline design

**H1 — Early contract:** Same full-stack scope/models/budget/test suite. Work packet with explicit API/schema, source and owner revision versus unstructured task prompt + ordinary PR workflow. Hypothesis: fewer late-stage incompatible interfaces.

**H2 — Small vertical slices:** Same accepted feature requirements. Early compatible feature-flagged increments versus long parallel feature branches. Hypothesis: lower rebase/stale-test churn at potentially increased planning/CI overhead.

**H3 — Controller-aware staffing:** Fixed 8-agent studio versus adaptive agent recruitment gated by dependency and verification capacity. Hypothesis: higher verified outcomes per total cost on some task mixes.

**H4 — Preflight duplicate detection:** Agent task scheduler with existing-task dedupe and repair routing versus freeform new-task generation. Hypothesis: fewer duplicated implementations without suppressing necessary alternatives.

For fair comparison, hold effective permissions, review quality, test suite, compute budget and actual outcome criteria constant. Report failed tasks, reviewer labor, model costs, integration reruns and time-to-verifiable merged slice. Pre-register outcome metrics and note contamination/carryover.

**No experiment has run.**

## 8. Smallest proposed synthetic experiment (requires separate authorization to run)

A disposable two-feature app with a shared member API:
- 3 autonomous worker instances, independently controlled QA;
- one backend/API task, one frontend consuming it, one unrelated accessibility task;
- intentional mismatch in the **control scenario**;
- treatment receives a precise versioned API/branch/acceptance packet;
- each candidate uses isolated branch, trusted tests and protected integration;
- run repeated matched trials with both methods and record all costs/failures;
- scoring: end-to-end accepted slices / total cost; unauthorized main writes target zero; secondary: mismatch count, rework time, stale tests and reviewer escalation.

Study design must prevent a trick win: both arms need equivalent functional requirements, and the treatment cannot be credited merely for generating a prettier task template. If the treatment exposes the answer to a hidden test, the comparison is invalid.

## 9. Important operational nuance

"Convergence branch" can mean an integration workspace or temporary Git ref. **The Convergence Contract is not that branch**, and neither alone guarantees success. A branching strategy, compatible interface contracts, explicit ownership, verified combined checks and protected merge rights must all agree.

The controller should be helpful *before* development and restrictive only when an action is outside the approved contract. Avoid turning it into a global serialized planner that blocks independent work. Use many parallel bounded workers, strong local ownership, and a short coordinated publication step per protected target.

## 10. Research follow-up (no build authority)

- Draft *contract readiness rubric* with machine-checkable preflight rejection reason codes.
- Map each checklist field to upstream tool support and unfilled gaps, including the cost of operating Zuul versus GitHub-native.
- Formal schema for packet v0.1, evidence refs and dependency revisions.
- Work through a synthetic replan/handoff where frontend/back-end assumptions drift after a mainline merge.
- Compare IE's practical lessons **only if independently shared and authorized**, with provenance, ownership and no code transfer.
- Preserve a learner-friendly edutainment episode: **"Don't Build the Puzzle Before Agreeing on the Edges"**, labeled as conceptual teaching, not a proven Foromni implementation.

**Bottom line:** Convergence is not a cleanup job after the coders finish. It starts when a goal is decomposed into compatible, verifiable contributions. A trusted controller makes that discipline operational without giving agents permission to approve themselves.

*Build today, so others can enjoy tomorrow.*
