# Scaling the Convergence Controller: Thousands of Agents, One Protected Mainline

**Status:** Research proposal v0.1, not approved or implemented  
**Date:** 2026-11-21  
**Project:** Foromni only. Do not modify or integrate Internet Embassy.  
**Companions:** CONVERGENCE-CONTRACT-V0.1.md, GIT-MERGE-MECHANICS-AND-INTEGRATION-CONTROLLER.md, MASSIVE-PARALLEL-TO-ONE-MAINLINE.md, CROSS-DOMAIN-CONVERGENCE-CONTRACT-V0.2.md.

## Central finding

The scalable architecture is **parallel work, parallel preliminary validation, selective speculative combined validation, but coordinated authoritative publication per target ref**. Do not allow every agent to push directly into a shared integration branch. Scale by reducing the size and coupling of changes, partitioning unrelated work, limiting work-in-progress, and investing test capacity only where it improves *accepted outcome* throughput.

A single controlled mainline publication path is not necessarily a bottleneck: time-consuming verification can run concurrently, while the final protected ref update is short. However, speculative checks can become stale as main advances, so indiscriminate parallelism increases wasted testing. Queue policy must balance these effects.

## What upstream systems actually do

**GitHub merge queue:** Organizes eligible PRs into speculative merge groups, validates groups with required checks, and merges when conditions hold. It supports configurable build concurrency, merge limits, status-check timeout and merge-group events. Required GitHub Actions workflows need the `merge_group` trigger. Public organization repositories qualify; private GitHub Enterprise Cloud plan conditions apply. Verify actual plan and ruleset policy before choosing. Source: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue

**Zuul dependent pipeline:** Tests speculative future combinations concurrently; dependency order and shared queues shape which revisions are tested. Zuul exposes queue configuration and dependency-aware pipelines. Source: https://zuul-ci.org/docs/zuul/latest/gating.html and https://zuul-ci.org/docs/zuul/latest/config/pipeline.html and https://zuul-ci.org/docs/zuul/latest/config/queue.html

**Prow Tide:** Maintains eligible GitHub PR pools and batches presubmit tests on up-to-date combinations, with pool status and retest scheduling. Source: https://docs.prow.k8s.io/docs/components/core/tide/ and https://docs.prow.k8s.io/docs/scaling/

**Important:** These handle Git/CI convergence, not Foromni's task claim fencing, independent acceptance, collective governance, or real-world beneficiary outcomes. Do not imply their scaling guarantees apply automatically to third-party agents.

## Six logical planes (only the last writer controls main)

1. **Intake:** accepts versioned candidate manifests; deduplicates `candidate_id` / artifact digests / stable idempotency keys; rejects malformed or unauthorized claims.
2. **Readiness:** tracks task dependency DAG, acceptance contract version, required reviewers, code owner, artifact SHA, risk tier, cost budget and data restrictions.
3. **Sharded preliminary verification:** runs safe static checks and independent validation in isolated, permission-constrained workers; caches results by exact relevant input digest and validator/toolchain versions.
4. **Queue scheduler:** clusters *compatible* candidates; partitions admission by repository/target branch and additional tightly coupled interfaces; respects dependency order and fairness; reserves scarce integration environments.
5. **Protected convergence gate:** synthesizes a combination against current main, binds all required checks to that exact prospective result, verifies authority and policy, and publishes through one protected merge controller/forge queue.
6. **Reconciler/observability:** reads actual main refs and CI results, replays durable events, detects missed webhooks/partial failures, reports blockers, restores truthful states and computes cost per accepted integration.

These are logical roles; no need for six new microservices at research stage. Start by mapping them to existing GitHub/Zuul/Prow components and a minimal Foromni ledger.

## Admissibility and scheduling policy

**Candidate prerequisites:**
- stable task ID, current spec/acceptance digest, contributor and independent verifier identities;
- exact source SHA, target ref, dependency set, changed interfaces and requested permissions;
- required quality checks and at least one proof of real task acceptance relevant to domain;
- declared feature flag/migration/rollback plan if risky;
- CI budget and resource class; unknown checks remain unknown, not passing.

**Order constraints:**
- topological task/dependency order;
- security-critical or user-blocking candidates can be prioritized by accountable owner;
- no queue starvation: cap aging; blocked candidates get explicit repair ownership and reason;
- fair-share quotas per organization/agent to prevent resource monopolization;
- incompatible candidates move to design reconciliation, never silently batched.

**Batch heuristic (proposal):** start with very small batches; co-batch only candidates with compatible dependency revisions and documented cross-feature checks; adapt batch size based on failure rate and rerun cost; bisect failing batches and retain every candidate/evidence record. No arbitrary 100-PR batch merely to maximize visible throughput.

## Reduce redundant work

- Validate cheap, deterministic checks early; reserve expensive integration tests for candidates that have passed the preconditions.
- Reuse checks only when their exact source/base/dependency/configuration scope remains valid; never reuse a green badge across changed relevant inputs.
- Group non-conflicting changes while testing their combined result; do not assume file-disjoint means semantically independent.
- Use predictable ephemeral test environments, quotas, and cost limits; execute untrusted PR code away from privileged control-plane credentials.
- Apply backpressure: when queue age, test contention, or failure retries exceed thresholds, divert agents to repair, documentation, review and dependency resolution rather than produce more incomplete candidates.
- Feature flags allow safe partial code integration when interfaces and migrations remain compatible, but flags do not substitute for tests.
- Use fewer, clearly owned APIs/interfaces and smaller change sets to reduce invalidation/rebase churn.

## Concurrency & consistency invariants

- Many agents may read/fetch identical refs at once without a special lock.
- Each task attempt owns one isolated workspace; shared branch writes require enforceable lease and expected-head checks.
- Only protected controller can publish to main under actual server-side permissions; a mere coordination note does not stop direct writes.
- Merge queue speculation verifies *combined* result on current eligible base; actual integrated SHA is read back after merge.
- Each admission event binds current task version, source SHA, prospective merge SHA, dependency digest, policy revision and independent verifier. Actual merged SHA may differ because of squash/rebase/merge method.
- Stale source/base/checks -> invalidate/requeue, not retroactive pass.
- Duplicate webhook deliveries and retries -> idempotent state projection; nondeterministic outcomes go to reconciliation.
- Timeout after successful merge but before ledger recording -> check Git main before retrying; never blindly repeat mutation.
- An upstream result for a different repo does not grant cross-repo authorization. Each independently governed collective owns its admission policy.

## Queueing and capacity model

Use simple measurable terms:

- `lambda`: incoming **eligible** candidates/unit time (not all authored branches).
- `mu`: independently verified + admitted candidates/unit time under current test capacity and branch serialization.
- `WIP`: candidates in active review/testing/merge stages.
- `queue_age_p95` and `oldest_eligible_age`.
- `invalidated_runs / total_runs` and `rebase_conflicts / active_candidates`.
- `accepted / submitted`, `integrated / accepted`, and `released / integrated` tracked separately.
- `cost_per_verified_integrated_outcome` including CI, inference, reviewer and retries.
- `reviewer_independence_failures`, `stale_SHA_admissions`, `unapproved_main_writes` targets zero in adversarial tests.

If sustained arrival exceeds achievable admission capacity, queue backlog will grow. A scheduler must limit intake/active WIP, expose expected wait states honestly, and route agents toward unblockers rather than chase vanity branch counts. This is a design implication, not a measured Foromni bottleneck.

A candidate may remain `ready_for_review` while integration is slow; it is **not** `completed`.

## Fault/recovery scenarios to tabletop

| Scenario | Required behavior |
|---|---|
| 1,000 simultaneous candidates, limited CI runners | Bounded active checks; explicit queued and blocked states; no bypass |
| Two workers modify same API via different branches | Dependency/contract conflict discovered and reconciled before admission |
| Test G1 passes while main changes | Invalidate G1 for affected merge result; requeue under new base |
| Five candidates batched; one fails | Preserve passed candidates and isolate failure with retest; no fake group pass |
| Queue controller fails mid-publication | Reconcile actual Git ref, no duplicate merges, resume safely |
| Webhook delivered multiple times/out of order | Deduplicate and version-check |
| Source branch force-pushed | Exact SHA evidence invalidated; new independent approval required |
| Worker loses lease | Deny stale authoritative writes; allow isolated artifact proposal |
| One tenant floods queue with low-value tasks | Fair share/backpressure; preserve priority for qualified work |
| Untrusted PR test attempts credential exfiltration | Sandboxed runner with no protected-control credentials |
| Required reviewer goes offline | Only gated candidate waits; unrelated compatible candidates progress |
| Merged code fails post-merge test | Incident/repair event; no fabricated integrated-success guarantee |
| Compatibility batch starves old single PR | Age-based scheduling and documented escalation |
| Model/provider goes unavailable | Reassign execution with permissions and evidence policy retained |

**These are proposed test cases, not run/tested results.**

## Architecture choice: prototype progression

**Phase 0 — Desk research:** Source-code-level study of GitHub merge queue, Zuul's dependent pipeline, and Tide pool selection. Inspect cancellation, concurrency quotas, stale results and failure isolation semantics. Select the minimum feature set.

**Phase 1 — Synthetic event replay (document-only):** Show candidate DAG, lease epochs, exact SHAs, queue events, job results and expected final projections for 3, 30, 300, and 3,000 candidates. Include two writers to one branch and one failed batch.

**Phase 2 — Disposable technical pilot (separate Founder authorization):** 20–30 synthetic tasks, 3+ worker providers including older/self-hosted, integration tests bound to merge-group SHAs, privilege separation and crash/replay tests. No IE code or credentials.

**Phase 3 — Scale benchmark (separate Founder authorization):** 100–1,000 simulated candidate submissions with controlled load, no production traffic; quantify accepted throughput, rerun waste, queue age and cost. Compare native GitHub with one Zuul/Prow path.

**Phase 4 — Stack decision:** Choose adopt/extend/reject based on metrics, security review and operating burden. Do not prematurely build a custom scheduler or Git host.

## Cross-domain perspective

Software mainline is one convergence adapter. For collective research, education, professional work or civic processes, the queue/admission metaphor remains useful but target state may be a published evidence-backed conclusion, accepted service milestone, documented decision or beneficiary-approved deliverable. Never make Git SHA or CI a universal criterion. Domain owners determine valid reviewers, consent, legitimacy and outcomes.

## Next research deliverable

A **scheduler/ledger event trace and authority matrix** that explicitly shows 10 incoming contributors, 3 parallel verification slots, 2 conflicting tasks, one stale SHA, one crash and one final mainline update. It should allow independent reviewers to produce the same state projection without assuming an implementation.

**Conclusion:** Build an assembly line of verified changes, not a bigger pile of speculative branches. The controller is primarily an authority/evidence protocol layered over mature CI/merge systems.

*Build today, so others can enjoy tomorrow.*
