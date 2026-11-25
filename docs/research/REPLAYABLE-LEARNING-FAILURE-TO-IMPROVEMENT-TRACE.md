# Replayable Learning Case: Integration Failure → Verified Improvement Proposal

**Status:** Research tabletop fixture; no agents, experiments, merges or deployments were run.  
**Date:** 2026-11-21 · **Project:** Foromni only, independent of IE.  
**References:** AI-WORKFORCE-CONTINUOUS-LEARNING-AND-EXPERIMENTS.md; CROSS-DOMAIN-CONVERGENCE-CONTRACT-V0.2.md; CONVERGENCE-CONTRACT-V0.1.md.

## Hypothetical source event: Integration contract mismatch

A synthetic autonomous team builds a membership feature. UI worker expects `member.displayName`, API worker implements `member.name`. Both isolated branches are green, but an integration test over the combined tree fails. Agents cannot mark their own work complete, nor can a learning agent remove a test to make the dashboard green.

**The observation:** Combined end-to-end test rejects result at merge-group `MG-1` under fictional main `M-7`.  
**Not observed:** No live Foromni failure, actual real-world frequency, statistically significant experiment, or accepted change. Illustrative SHAs are never usable Git object IDs.

## Event trace — all events are FICTIONAL

| Order | Event / actor | Evidence expected | Authorized projection |
|---|---|---|---|
| E01 | Frontend agent submits `C-FE` against shared spec v2 | API expectation `displayName`, source `S-FE-1` | Candidate submitted, not accepted |
| E02 | Backend agent submits `C-BE` against shared spec v2 | Response `name`, source `S-BE-1` | Candidate submitted, not accepted |
| E03 | Independent gate tests merged `MG-1` | Failing consumer/provider check and error trace | Integration blocked; no main ref change |
| E04 | Reliability agent reads authenticated failure | Exact merge-group revision, check ID, status | Observation recorded; reason inferred only |
| E05 | Analyst proposes cause `H-1` | Mismatch in interface fields, competing hypotheses | Hypothesis proposed, not independently proven |
| E06 | Coordinator proposes two remediations | A: shared API contract before implementation; B: post-hoc adapter | Options awaiting evaluation, no rule changed |
| E07 | Trusted experiment authority approves a **synthetic** A/B evaluation plan only | Scope, cost ceiling, fixtures, independent judge, stop rules | Plan authorized for future test; no actual test performed |
| E08 | Experimental arms (CONTROL: freeform handoff, TREATMENT: versioned API contract) are defined | Same product brief, model pool, test set, QA cost, risk policy | Protocol complete, results unknown |
| E09 | Independent reviewer inspects expected outcomes | Exact evidence, cost denominator, negative-case accounting | No adoption based solely on a plausible proposal |
| E10 | Human/authorized owner reviews potential operational improvement | No elevated branch rights, no removal of acceptance checks | Adoption still pending measured evidence |
| E11 | Proposed decision remains `INCONCLUSIVE_NOT_TESTED` | Event trace + protocol available | No change to authoritative workflow |

This trace deliberately stops **before** claiming a trial has occurred. A real execution would append authenticated observation events, blinded evaluation outcomes, a reviewer verdict, a scoped adoption/rejection decision and post-adoption monitoring.

## Hypotheses & pre-registration

**H-A (candidate):** Stable, explicit consumer/provider API schema in the task handoff reduces integration mismatch/rework versus freeform instructions.

**H-B (candidate):** A compatibility adapter built only at integration time may be cheaper for small tasks but risks duplicating inconsistent semantics.

**Null possibility:** For short and tightly coupled work, extra API negotiation may add overhead without improving verified delivery rate.

**Primary metric:** independently verified integrated vertical slices per total authorized dollar of model + test + repair + review work.

**Guardrails:** no privilege bypass, no hidden benchmark data exposure, no reduction in independent QA checks, no unacceptable regressions, no increasing escaped tenant/auth failures.

**Secondary measures:** time from approved objective to tested combined slice; invalidated runs; task handoff completeness; cost/energy as available; branch conflicts; human review time. Measure variance across repeated trials.

**Preconditions before running:** founder authorization for a disposable experiment, versioned benchmark fixture, grant-bound agent runtimes, independent reviewer with sealed holdout, fixed compute budget and transparent failure records.

## Decision table: evidence vs claimed result

| Situation | Independent decision | Why |
|---|---|---|
| Worker says "tests passed" but no trusted CI run | Hold | Model claim is not observed evidence |
| Both worker branches green; combined merge-group fails | Block merge | Integration result is authoritative for compatibility |
| API contract proposal is plausible but untested | Research candidate | Hypothesis is not proof |
| Experiment improves throughput but increases unauthorized accesses | Reject/stop | Safety constraints supersede optimization |
| Experiment improves one task type only | Conditional/scope-limited adoption candidate | Generalization is not established |
| Experiment wins on repeated sealed tests with no guardrail degradation | Eligible for independent review and bounded authorization | Still needs policy approval and monitoring |
| Improvement rolled out and integration failures worsen | Revert within authorized scope, open incident | Monitoring and recovery are part of learning |
| Agent suggests lowering acceptance to show more completions | Deny unapproved rule change | Optimization cannot redefine its own success |

## Event envelope sketch (NOT validated schema)

```json
{
  "event_id": "EVT-DEMO-05",
  "event_type": "learning_hypothesis_proposed",
  "objective_id": "OBJ-DEMO",
  "task_ids": ["TASK-FE", "TASK-BE"],
  "source_event_ids": ["EVT-DEMO-03", "EVT-DEMO-04"],
  "observed_merge_group": "MG-1",
  "proposer": "agent/analyst",
  "hypothesis_revision": 1,
  "possible_causes": [
    "API field naming drift",
    "stale interface specification"
  ],
  "proposal": "evaluate versioned API-contract handoff",
  "evidence_state": "NOT_TESTED",
  "decision": "PENDING_REVIEW",
  "policy_revision": "DEMO-P1",
  "privacy_class": "synthetic"
}
```

## Replay consistency oracle

A second analyst reading only the trace must arrive at:
- two submitted candidates;
- a failed combined integration attempt, not an accepted or released product;
- an unverified but plausible root-cause hypothesis;
- an experiment design awaiting execution and independent assessment;
- no new permissions, protected-branch changes or governance rules;
- a learning record with uncertainties, alternatives, revision history and nonproduction content.

## Evidence and dissemination

The trace can support an **edutainment simulation** now, labeled hypothetical. It cannot support claims like "Foromni experiments proved convergence contracts raise throughput by 40%." If a future trial is executed, publish exact method, immutable version references, repeat counts, failures and independent conclusions before converting its results to public campaigns.

**Next:** formal machine-readable schemas and replay validator under separate implementation authorization; then run the experiment before making numerical claims.

*Build today, so others can enjoy tomorrow.*
