# Research: From Massively Parallel Development to One Validated Mainline

**Status:** Research proposal; no implementation or deployment authorized  
**Date:** 2026-11-20  
**Scope:** Foromni only; no Internet Embassy task, code, branch, infrastructure, or integration changes  
**Related:** [Global Agent Roadmap Execution](GLOBAL-AGENT-ROADMAP-EXECUTION.md)  
**Thesis:** AINO coordination capacity is limited by *verified convergence throughput*, not feature-generation throughput.

## Executive recommendation

A worldwide workforce can create arbitrarily many candidate branches, but a dependable mainline requires **one serialized or safely coordinated admission authority**, small independently composable increments, continuously updated base revisions, exact-SHA validation of the *would-be merge result*, and reversible feature exposure. The target is not to merge every branch. It is to preserve every useful contribution, select compatible increments, and progressively integrate proven value.

**Recommended research hypothesis:** Foromni should publish an interoperable **Convergence Protocol** governing the complete journey:

`roadmap requirement → scoped contract → execution attempt → isolated artifact → candidate attestation → dependency-aware admission → synthetic merge result → integrated test → mainline → controlled enablement → release acceptance`.

This is a **logical lifecycle**, not a mandate for specific databases or GitHub status names.

The integration gateway must never be bypassed by a task agent's self-declared success. Git branch existence is neither the unit of value nor proof of completion. Projects beyond Git may use versioned artifacts with equivalent provenance semantics.

## 1. Why massive parallelism fails without convergence controls

1. **Shared mutable surface:** Uncoordinated work modifies the same schemas, contracts, files, dependencies or identity boundary.
2. **Stale bases:** A branch may be correct against commit A and invalid against current commit B.
3. **Transitive dependencies:** Feature X independently passes but cannot run without compatible Y and Z.
4. **Unverified combination:** Individual candidates pass, yet their union breaks runtime behavior.
5. **Unbounded branch age:** Long-lived feature lines compound conflicts, duplicate features and design drift.
6. **False progress:** Opening PRs and ticking tasks increases counts without changing the working system.
7. **Admission bottleneck:** One reviewer/test environment becomes the throughput ceiling; reviewers start bypassing gates.
8. **Opaque handoffs:** A successor cannot reliably reproduce implementation/test evidence.
9. **Confused release semantics:** Integration to main gets mistaken for exposure to users or production release.
10. **Economic misalignment:** Rewards favor code volume instead of accepted, useful, maintained results.

Control these *before* scaling agent count.

## 2. What established practice suggests

| Approach | Useful finding | Limit |
|---|---|---|
| Trunk-based development | Small, short-lived branches and regular integration reduce divergence and conflict | Requires stable validation, modular design, and feature isolation |
| Google large-scale codebase practices | One-version rules, review, CI, and limited development-branch lifetime support many teams | Google-specific organizational controls cannot simply be copied by a decentralized network |
| GitHub merge queue | Builds speculative merge groups against latest base and preceding queued changes; required checks gate admission | A queue does not verify task acceptance, business outcomes or agent authority |
| GitHub stacked PRs | Supports ordered dependent increments rather than one giant hard-to-review branch | Dependency-stack failure can block subsequent candidates; stacking does not eliminate coupling |
| Graphite stack workflows | Can coordinate rebasing and merging multi-PR stacks | Additional vendor/tool dependency and permission/approval implications |
| Feature flags and branch-by-abstraction | Incomplete but safe increments can integrate without becoming user-visible | Flags do not excuse untested data migrations, authorization flaws or incompatible contracts |
| Event sourcing + optimistic concurrency | Durable provenance and revision-aware transitions support reconciliation | Higher infrastructure, retention and projection complexity |

Primary references (as checked 2026-11-20):
- https://trunkbaseddevelopment.com/
- https://abseil.io/resources/swe-book/html/ch16
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue
- https://docs.github.com/en/pull-requests/reference/stacked-pull-requests
- https://www.graphite.com/docs/merge-pull-requests
- https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development
- https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing

**GitHub-specific caution:** If a repository uses GitHub merge queue with GitHub Actions, relevant required workflows must handle `merge_group` events; a PR-only check may not run on the prospective queued combination. Availability, permission and plan constraints must be verified for the target repository rather than assumed.

## 3. Separate the four planes

**A. Roadmap plane — what should exist.** Requirement identifiers, versions, business/user outcomes, acceptance criteria, priority, dependency DAG, release intent.

**B. Execution plane — who is doing what.** Agent/human worker identity, capabilities, task lease/fencing token, budgets, branches, checkpoints, handoffs, attempt outcomes.

**C. Convergence plane — what may safely join.** Candidate artifact IDs, source/base SHA, dependency and API compatibility, independently reproduced acceptance, target base, synthetic merge commit/hash, required checks, admission verdicts, integration evidence.

**D. Exposure/release plane — what users can access.** Feature flags, tenant/permission rollout, migrations, deployment digest, monitoring, rollback, founder approval if consequential.

A failure in one plane must not silently modify the others. Mainline integration does **not** automatically mean public launch. A task may be functionally complete but remain unreleased, or integrated but behind a disabled flag.

## 4. Candidate contract: minimum required record

Every proposed integration candidate should carry:

- `candidate_id`, `project_id`, `task_id`, `task_version`.
- `attempt_id`, `author_actor_id`, `reviewer_actor_id`, `provenance`.
- `repo_id`, `base_sha`, `head_sha`, `artifact_digest`, `pr_url` (or non-Git equivalent).
- Changed interfaces/files and declared dependency IDs/versions.
- Claimed user behavior, acceptance criterion IDs and matching evidence links.
- Required build/typecheck/unit/integration/security/acceptance checks with observed outcomes.
- Feature flag, migration and rollback plans where relevant.
- Requested target stage, sandbox namespace, trust policy and cost/time budget.
- Prior candidate or superseding/rebased relationship.
- Clear `unknown` values for untested properties; never infer passing.

The candidate's **source SHA** and the eventual **merge-result SHA** are distinct evidence targets. A reviewer can approve the source while requiring full reruns on a new synthesized merge group. No admission when required evidence is missing or mismatched.

## 5. Dependency graph and conflict classification

Construct an admission graph using task dependencies, schema/API compatibility, shared-resource/ownership conflicts, and order constraints.

- **Independent candidates:** can undergo parallel checks, then still must pass merge-group verification against evolving mainline.
- **Ordered dependency stack:** use smallest safe increment first, then downstream candidates after its acceptance; rebase and retest as needed.
- **Mutually incompatible changes:** queue one design decision, reject or rework competing contracts; do not blindly merge both.
- **Migration-sensitive changes:** apply expand/contract sequencing; ensure backward compatibility and rollback or forward-recovery plan.
- **Cross-cutting security/auth changes:** require explicit risk review and system-level checks; no blanket bypass to accelerate throughput.
- **Non-code artifacts:** use equivalent versioned schemas, content digests, approvals and target environment checks.

**Batch design:** Coherent compatibility groups, not all PRs created in the same hour. Admission batch records must fix exact revisions, ordering, required checks and release policy.

A branch that remains stale should be rebased/reconciled or intentionally closed with reusable work archived, not indefinitely counted as pending integration.

## 6. Proposed convergence protocol (research-only pseudocode)

```text
submit(candidate):
  verify actor authorization and task/revision binding
  verify source artifact provenance and acceptance contract
  resolve dependencies, conflicts, current base and required policies
  if missing info: hold in review with evidence request
  if incompatible: return to repair with specific conflict report
  place eligible candidate in dependency-aware admission queue

admit(candidate, observed_current_main):
  verify queue ticket and serialized/optimistically fenced admission
  assemble candidate onto current main (+ required earlier accepted candidates)
  generate synthetic merge-result SHA/artifact digest
  run all required checks on precisely that result
  independently assess acceptance and policy gates
  if base changes during checks: invalidate/requeue or use proven merge-queue semantics
  if any check fails: quarantine candidate; attach logs and repair owner
  else: merge via protected authority; record actual resulting mainline SHA
  re-run required post-merge integration/sandbox checks
  record integrated outcome or rollback/recovery event (never silently green)
```

**Critical invariant:** No stale claim, self-attested CI log, or prior mainline snapshot grants merge authority. Protected merge is a separately authorized action.

## 7. Rate and throughput economics

For a stable system, **accepted-integration throughput** must approach viable submitted work volume, or queue age will grow without bound.

Measure at least:
- Candidates authored/day vs independently accepted/day vs truly integrated/day.
- **Acceptance yield** = accepted candidates / submitted candidates.
- **Integration yield** = passing post-merge outcomes / admitted candidates.
- Queue latency percentiles and **oldest eligible candidate age**.
- Time since last meaningful task advance; stuck handoffs.
- Merge conflict/rebase frequency, stale-SHA invalidation rate.
- Failed merges, rollbacks, escaped regressions and recovery time.
- Cost of checks/retries and **cost per independently accepted deliverable**.
- Feature-enabled/released outcome separately from code-integrated count.
- Dependency-graph blocked node count and critical-path age.
- Recovered or superseded work vs discarded work.

Avoid rewarding branch count, PR count, passing self-authored tests, or status updates.

**Control-theory intuition:** If the arrival rate of eligible work exceeds the sustainable admission/validation service rate, an ever-growing backlog is inevitable. Limiting in-flight work and introducing admission backpressure is part of the design, not failure.

## 8. Safety invariants for a worldwide agent workforce

1. Mainline changes only through protected, independently verified admission.
2. No executor can be their own protected-gate verifier.
3. Every decision binds exact task version, source revision and target merge result.
4. Admission remains valid only for its checked base/dependency set.
5. Every failure is visible with repair ownership; no disappearing failed candidates.
6. Stale leases and retries never grant current write authority.
7. Integration is not deployment; deployment is not permission to expose a feature.
8. External agents receive constrained access; no unrestricted credential exchange.
9. Every integration event is auditable and reversible when feasible.
10. Policy and license compatibility gates cannot be skipped for throughput.
11. Global worker participation must not require a single model vendor, central workforce account, or shared internal prompt history.
12. Foromni must not move IE code or tasks across the boundary.

## 9. Stress tests before building a broad application

Proposed **tabletop cases** (documentation only until a separate pilot is approved):

1. 100 candidates opened simultaneously, 20 modifying the same interface.
2. Independent candidate A passes against main v1; main changes to v2 before merge.
3. Feature A depends on B, but B fails QA.
4. Stacked PR base is changed; all downstream checks invalidated.
5. A merge queue accepts a combined group whose integration test reveals a cross-feature bug.
6. Two independently passing database migrations conflict.
7. A read-only agent claims full test success and requests merging permissions.
8. Repeated webhook delivery produces duplicate admission tickets.
9. Integration controller crashes after merge but before recording the event.
10. Feature safely integrated behind a flag but unsafe when enabled for real users.
11. Revoked worker/compromised credential attempts to approve prior work.
12. 10,000 tasks are generated faster than testing capacity: verify backpressure, triage and prioritization.
13. Independent contributor in a different time zone loses access or goes offline; handoff preserves progress.
14. A release fails after successful integration; post-release incident doesn't erase historic acceptance evidence.

**Proof criteria:** No unverified mainline admissions in adversarial trials; no stale-SHA approvals; no accidental production release; deterministic reconciliation from events; measurable useful-completion throughput; recoverable interruption; finite queue age under controlled arrival rates.

These are proposed tests, not executed or passed tests.

## 10. Decision sequencing

**C0 — Research and formal definitions (NOW):** Specify invariants, candidate contract, dependency graph, authority matrix, evidence binding, admission protocol, metrics and cases above. No runtime implementation.

**C1 — Tabletop design review:** Three independent reviewers attempt to falsify the protocol with conflicting candidates, expired permissions, stale bases, integration failures and approval bypasses.

**C2 — Technical spike (separate authorization):** Synthetic work only, constrained sandbox: 3 worker agents, 10 tasks, overlapping changes, 2 QA workers, 1 protected merge controller, invalidated SHAs, one crash recovery test.

**C3 — Expansion pilot (separate authorization):** Scale to 25–100 candidate submissions, multiple independent worker runtimes, compatibility batches, realistic tests and recorded costs. Require all protection gates.

**C4 — Product architecture choice:** Use measured results to choose GitHub-first integration with merge queue and project views, a Foromni-owned event ledger, or durable orchestration; do not commit to a new orchestration stack merely because it is fashionable.

**C5 — Major ecosystem build (later authorization):** Only after validated convergence infrastructure exists.

## 11. Immediate next research artifacts

- A versioned `Convergence Candidate` JSON Schema proposal.
- Exact admission state/authority matrix distinguishing developer, independent QA, merge controller, release owner.
- Compatibility graph rules and batch manifest example.
- Adversarial event fixture sets with expected (fail-closed) outcomes.
- A measurement design for throughput, backpressure, queue health and cost per accepted feature.
- A decision record contrasting GitHub merge queue, stacked PRs, feature flags and custom event-ledger architecture.

## Founder-level research question

**Can 100 independent agents contribute more actual tested, integrated product value than 10 agents, without degrading stability or increasing the share of unverifiable work?**

Until we can measure an affirmative answer in controlled tests, scaling feature generation is the wrong optimization.

---

**Conclusion:** Foromni's foundational utility is not a roadmap board and not a global prompt router. It is **verified convergence from independently produced work into a shared, trustworthy mainline**.
