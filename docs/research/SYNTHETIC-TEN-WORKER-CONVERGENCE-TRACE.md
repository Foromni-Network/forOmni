# Synthetic Convergence Scheduler Trace — Ten Contributors, Three Validation Slots

**Status:** RESEARCH TABLETOP, NOT EXECUTED. **Date:** 2026-11-21. **Project:** Foromni only.  
**Related:** SCALING-THE-CONVERGENCE-CONTROLLER.md; CONVERGENCE-CONTRACT-V0.1.md; CROSS-DOMAIN-CONVERGENCE-TABLETOP-TESTS.md.

## Goal

Make the proposed scheduler rules inspectable. Demonstrate how ten independent contributions compete for three verification slots and converge toward a protected mainline without allowing a stale SHA, incompatible contract, expired writer, or unreliable test to be mistaken for accepted integration. All IDs and SHAs below are **illustrative labels, not actual Git object IDs**.

## Fixture

- Protected `main` initially `M0`.
- Ten task candidates `C01..C10`, each with a stable task revision, author and separate verifier.
- Three independent validation slots `V1, V2, V3`. No other candidate can use them until released.
- `C01` is a small schema addition; `C02` updates the API based on C01; `C03` and `C04` change the same API in incompatible ways; `C05` is an independent accessibility fix; `C06` is a test-only increment; `C07` introduces a backwards-compatible adapter; `C08` has a stale SHA; `C09` is an isolated UI change; `C10` is docs.
- `C02` depends on `C01`. `C04` conflicts with `C03`; cannot both be admitted under the same agreed interface version. `C08` previously had evidence on source revision `S08a`, but current candidate head is `S08b`.
- Contributors may develop concurrently in their own branches. The protected admission controller alone can merge to `main`; the ledger has event IDs, idempotency keys and policy revisions.
- Illustrative verification checks: unit, contract, dependency, security, integration, independent task acceptance. The exact required set is policy- and task-specific.

## Deterministic event timeline

| Step | Incoming events and gate | Slot state (V1/V2/V3) | Expected authoritative result |
|---|---|---|---|
| T0 | All ten candidates submitted and authenticated; candidate manifests checked | idle/idle/idle | All in intake, no changes to main M0 |
| T1 | Readiness rejects `C08`'s old evidence; holds `C02` for C01 and `C04` for interface conflict review | C01/C05/C06 | C08=needs_reverification; C02=dependency_blocked; C04=design_conflict |
| T2 | C01 and C06 pass preliminary validation; C05 fails accessibility acceptance test | idle/C05/idle | C05=repair_required; failed test preserved, never green |
| T3 | C06 independently validated for M0; controller constructs merge-group G06(M0+C06), passes required gate and publishes | C07/C09/C10 | Main=M1; actual integrated SHA is read back and recorded; C06=integrated |
| T4 | C01 preliminary validation acceptable; merge-group G01(M1+C01) constructed, required gates pass | C07/C09/C10 | Main=M2; C01 integrated; C02 now eligible for next validation |
| T5 | C07, C09, C10 pass candidate checks against earlier context; M2 has advanced while checks ran | C02/C03/C08 | Prior candidate checks may be usable for source-local proofs, but integration checks must be regenerated for the actual M2 merge-group; no stale-mainline approval |
| T6 | Two controller replicas race to publish C10 at expected main M2 | C02/C03/C08 | At most one publication succeeds; other detects changed base/ref; Git result reconciled; main=M3 |
| T7 | Controller crashes after C10 merge but before writing ledger event; duplicate webhook arrives | C02/C03/C08 | Reconciler reads actual main M3, records single idempotent C10 admission, no second merge |
| T8 | C02 passes on new dependency C01 and current source; C03 passes tests but proposed interface is incompatible with C04 | idle/V2/idle | C03 can be considered under chosen interface policy; C04 held, not silently merged |
| T9 | C08 submits purported success based on obsolete S08a while source S08b changed | V1/V2/idle | Independent gate rejects prior check as STALE_SOURCE_SHA, requests new run; C08 remains unverified |
| T10 | C07, C09 receive fresh merge-group testing against actual main M3, then one is admitted at a time with readback | V1/idle/V3 | If gates pass, main advances M4 and M5; if not, candidate returns to review; no inference that both will pass |
| T11 | Agent for C05 loses lease and another agent takes over; original later submits | V1/idle/V3 | Old lease cannot mutate shared ref/status; useful patch may be resubmitted as new isolated attempt, tested again |
| T12 | Unresolved C04 awaits design decision; C08 awaits exact-source independent QA | queues visible | Blockers remain assigned; no fabricated completion; eligible unrelated work continues |

**Important:** This is an expected-state story, not a real benchmark. The order above is one legal scheduling strategy. It does not imply those candidates actually passed tests. To keep the trace logically precise, events saying “passes” stipulate a *hypothetical independent oracle outcome*.

## Scheduler rule sketch (research-only)

1. Admit to ready queue only if task revision, capability permissions, dependency graph, source identity and policy are consistent.
2. Reserve capacity for three independent validators; per-tenant WIP caps apply.
3. Schedule non-blocked candidates using weighted critical-path priority plus age/fairness; never starve low-priority eligible work indefinitely.
4. Cache safe source-local checks by exact input/environment/validator version, not by PR title or model name.
5. Construct merge-group for a particular candidate ordering and current base. Check combined SHA and dependencies, then publish through protected queue or conditional ref authority.
6. On any ambiguous controller crash, observe Git's true main ref and merge records before retrying.
7. Distinguish task execution status, verification, admission, integration, deployment, release and real-world benefit.
8. Preserve rejected/superseded artifacts, subject to consent, privacy and retention policy.

## Explicit concurrency oracle

- All ten workers may read M0 concurrently.
- No direct write to protected main by a worker.
- Isolated candidate branch writes need a current lease/fencing token *enforced by a trusted writer*, or use separate branch ownership.
- For one protected ref publication, only the valid queued action can advance current main; concurrent controllers must synchronize with actual forge rules/CAS semantics.
- Source SHA S08b cannot inherit S08a acceptance.
- Candidate C02 cannot pass dependency admission before actual C01 integration.
- C03 and C04 cannot both be assumed compatible solely because they each pass on a private branch.
- Replay duplicate webhook events must not duplicate integrations.
- Rollback/incident events add history; never erase previous provenance.

## Counterexample: why agent count alone fails

Suppose the ten candidates were generated instantly while only three independent tests run at a time and one protected merge gate exists. New task generation does not increase verified throughput. Increasing validators might improve throughput until merge-group invalidation or dependency contention becomes the limit. Excess branches exacerbate stale revisions and test reruns.

**Measurement plan:** queue age, rejected stale checks, wasted reruns, active slots, blocked dependency time, admissions/day, escaped regressions, independent verifier time, and fully loaded cost per accepted integrated result. No actual measurements recorded here.

## Independent review checklist

Can another reviewer:
- replay the event ordering to the same states,
- identify every required authority/policy decision,
- distinguish speculative checks from postmerge evidence,
- locate the idempotency points,
- explain why the C10 crash does not double-merge,
- explain why C05's expired writer cannot overwrite work,
- find which proposed transitions require user/stakeholder approval,
- identify where this story assumes rather than proves a Git hosting guarantee?

If any answer is unclear, revise the protocol before implementation.

## Open issues

- Exact implementation of exclusive lease/ref fencing (Git doesn't implement coordinator leases).
- Queue invalidation granularity: regenerate affected checks only under a precisely defined dependency/configuration model.
- How to ensure independent QA from separate principals, not two agents sharing one owner.
- Scheduler fairness across contributors, organizations, languages, time zones, and offline nodes.
- Cost/energy tradeoffs when speculative checks repeatedly invalidate.
- How to isolate untrusted contributions from privileged CI credentials.

## Sources

- GitHub merge queue and merge-group event: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue
- Zuul speculative dependent pipeline: https://zuul-ci.org/docs/zuul/latest/gating.html
- Git push safety: https://git-scm.com/docs/git-push

**Next study:** compare single-agent full-stack delivery versus multi-agent studios with the *same* acceptance and merge evidence protocol.
