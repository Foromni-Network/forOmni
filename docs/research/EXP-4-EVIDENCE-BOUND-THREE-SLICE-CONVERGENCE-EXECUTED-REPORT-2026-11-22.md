# EXP-4 — Three-Slice Evidence-Authenticated Handoff Convergence: Executed Research Report

**Date:** 2026-11-22. **Scope:** Foromni research branch `research/global-agent-roadmap-execution`; local synthetic Python experiment. No Internet Embassy changes. **Status:** local executable verification PASS (13/13 software tests); real separate QA principal, source observer, provider agents, enforced credentials and live cost telemetry **NOT demonstrated**.

## Experimental question and hypothesis

**Question:** Can the three-task EXP-3 pipeline (A evidence, B project/task access, C selection) converge after introducing an evaluator-authenticated synthetic receipt format that binds project, task, attempt, agent, evaluator, source, suite, verdict and cost, without mistakenly promoting unauthenticated or duplicate evidence?

**Hypothesis:** synthetic unmodified receipts will be accepted by a keyed MAC, mutated or incorrectly keyed receipts rejected, same-attempt replay rejected, task-scope/revocation gates held, and a single conservative selection emitted with no grant. This is an **exploratory deterministic software experiment**, not a blinded trial or a claim of statistical superiority. The assistant authored the implementation and tests. It does not satisfy truly independent QA custody.

**Control:** EXP-3 executed previously (reproduced locally this turn from uploaded exact evidence archive): `10/10 PASS`; earlier EXP-3 code compared evaluator and worker *strings* and trusted unverified count inputs.  
**Treatment:** EXP-4 adds HMAC-SHA256 envelope validation, unique `(project, task, attempt)` on valid receipts, evaluated negative verdicts counted in denominator/cost, and current synthetic owner permission/epoch/revocation check. Both use synthetic candidate A=2/2 and B=35/40. Differences make this a **feature/regression comparison**, not a controlled estimate of algorithm efficiency.

## Pipeline / three tasks

```
A provenance.py
  source+suite+project-bound evaluator-MAC receipts; valid attempt dedupe
      |
      v
B gate.py
  owner consent + scoped project/task/capability/action + current epoch
      |
      v
C selection.py
  Wilson 95%-lower-bound heuristic for eligible candidate records
      |
      v
converge.py
  one candidate suggestion, verification reasons and synthetic cost totals
  explicit authority=NONE, effective_grant=null, execution=NOT_RUN
```

## Environment, artifacts and exact reproduction

**Environment:** Python 3.13.5, standard library only, local container; `HMAC` uses a *public demonstration key embedded in the test fixture*, not a secret or operational signing key. Its purpose is to prove serialization/validation behavior under known-key assumptions, not secure authentication in production.

**Exact Git tree:** [EXP-4 source](../../research/exp4_evidence_handoff_convergence), on branch `research/global-agent-roadmap-execution`.

| File | Git blob of final tested bytes |
|---|---|
| `provenance.py` | `07a49b8a7b10bb127c81278bfd4a68988de3958e` |
| `gate.py` | `61d66970f86cf0325d5c1f5eaecfe758705ff400` |
| `selection.py` | `1704751e32e69824a6ed5a442fa3dd08b78952fb` |
| `converge.py` | `d9d12379f94521e67089b4795ff775e37317bb50` |
| `tests/test_convergence.py` | `e88f12bbeea1f619e616c242ed60e0cc8646c0b4` |

The file blobs were compared against local Git's `git hash-object` results after final test changes; all five match. The archive provided with the response contains the locally run files and test output.

**Reproduce from the checked-out research branch:**
```bash
cd research/exp4_evidence_handoff_convergence
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v
```

## Observed outcome

- Baseline re-run: `10 tests`, `OK`.
- EXP-4 initial suite: `12 tests`, `OK`; suite was improved after inspection.
- Final EXP-4 re-run: **`13 tests`, `OK`, 0 errors/failures** in approximately 0.015 s; time is incidental and **not a scientific throughput benchmark**.
- Integrated fixture: A = 2 accepted of 2; B = 35 accepted of 40, with five explicit signed `REJECT` outcomes and synthetic cost 10 cents per evaluated attempt. B selected; B total synthetic recorded cost = 400 cents, **not actual billing**; project-B candidate excluded. Output `authority: NONE`; `effective_grant: null`.
- Negative checks actually executed: modified signed field, wrong validation key, unknown evaluator name, equal evaluator/worker IDs, wrong project, stale source, duplicate *signed attempts* with conflicting verdict, rejected verdict denominator and cost, revoked/suspended grant, mismatched project and epoch, blocked protected action, zero-eligible abstention and stale-only abstention.

## AAR: What the experiment proves / fails to prove

**SUPPORTED:** the 3 modules interface cleanly, source/provenance fields are covered by an HMAC in the synthetic format, tampering and conflicting signed duplicate-attempt evidence are rejected in the tested functions; synthetic policy filters/revocations apply before ranking; integration yields one non-authoritative recommendation; all 13 local executable assertions passed.

**NOT SUPPORTED:** that any real evaluator is independent or cannot be impersonated, that source digest corresponds to actual code on GitHub, that submitted receipts came from executed QA rather than fabricated calls to the test issuer, that operator signing keys are isolated, that denial occurs at a real tool gateway or across a network, that a true agent worked on a software task, that costs were billed or reconciled, that the rank predicts real completion performance, or that production releases/merges are protected.

**Important weaknesses discovered:**
1. HMAC verification requires safe key separation. The test key is visible to test code; a rogue signer knowing it can create syntactically valid receipts. Production needs separate evaluator credentials/issuer and authenticated source observation.
2. Counting one valid signed receipt per `(project, task, attempt)` is necessary but not sufficient. Need issuer-owned accepted-task/attempt registry and durable global uniqueness, including across restarts, parallel processes and aliases.
3. A stale/invalid receipt is rejected but no security alert or quarantine/reason-based investigation has been implemented.
4. A valid signed `ACCEPT` event here is still a synthetic claim; no evaluator actually checked a candidate program during receipt issuance.
5. Policy input is a caller-authored dataclass, not real owner-approved grant; no action-time delegated credentials, lease fencing, external database or independent identity check.
6. Relative ranking remains uncalibrated to task difficulty, recency, global fairness or total billed cost; number of cases is not number of agent runs.
7. All work was authored under one developer principal and committed on the existing research branch, not produced by three separately authenticated autonomous agents, and no protected/shared integration branch merge occurred.

## Scientific decision and next gate

**Verdict:** `EXP4_LOCAL_SYNTHETIC_PIPELINE_PASS`, `RECEIPT_INTEGRITY_FIXTURE_PASS`, `AUTHENTIC_EVALUATOR_CUSTODY_NOT_PROVEN`, `PRODUCTION_TASK_AUTHORITY_NOT_PROVEN`.

The next useful discriminating experiment is **actual source-bound evaluator execution** with a separate isolated signing service and verified source checkout/attempt registry, then negative-case replay across process boundaries. Once those pass, benchmark three independently attributable agent task handoffs and gated integration under owner-approved permissions, preserving FOR-007 frozen scope.

**No protected merges, production auth changes, API spending or deployments.**
