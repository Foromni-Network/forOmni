# E0 Acceptance Evidence and Grade Decision Table — Research v0.1

**Status:** Proposed independently reviewable evaluation contract. NOT a test suite, executable grader, real test result or approved benchmark.
**Date:** 2026-11-21. **Scope:** Foromni only; no Internet Embassy changes.
**Inputs:** FULL-STACK-REFERENCE-APP-CONFORMANCE-V0.2.md, FULL-STACK-REFERENCE-APP-API-FIXTURE-FREEZE-PROPOSAL-V0.3.md, EXTERNAL-CASE-STUDY-SWE-BENCH-ACCEPTANCE-EVIDENCE-AND-BENCHMARK-INTEGRITY.md, FULL-STACK-CONVERGENCE-TRIAL-PREREGISTRATION-V0.1.md, PROMPT-INJECTION-PIPELINE-SECURITY-GATE-RESEARCH.md.

## Core rule

A candidate can be **independently accepted** only after the correct current source/fixture was actually evaluated by a separate authorized principal, required positive and negative cases genuinely executed, and applicable hard security gates passed. A model's summary or a green cache label cannot create acceptance.

## Proposed evidence envelope (descriptive shape)

```json
{
  "schema": "foromni-e0-acceptance.v0.1-proposal",
  "objective_revision": "REVIEWED_SPEC_REQUIRED",
  "benchmark_case": "collective-lab/vertical-slice-01",
  "trial_arm": "CONTROL_OR_TREATMENT",
  "trial_id": "SYNTHETIC_EXAMPLE_ONLY",
  "task_id": "FROZEN_TASK_ID",
  "agent_attempts": ["ATTEMPT_IDENTIFIERS"],
  "base_source_sha": "EXACT_BASE_GIT_SHA",
  "candidate_source_sha": "EXACT_CANDIDATE_GIT_SHA",
  "evaluated_source_sha": "EXACT_EVALUATED_SHA",
  "prospective_merge_sha": null,
  "artifact_digest": "SHA256_OR_EXPLICIT_NOT_BUILT",
  "environment_digest": "VERSIONED_LOCK_IMAGE_RUNTIME_AND_FIXTURE",
  "suite_revision": "INDEPENDENT_SUITE_VERSION",
  "evaluator_principal": "TRUSTED_VERIFIED_PRINCIPAL",
  "test_execution": {
    "observed": false,
    "expected_test_cases": 0,
    "executed_test_cases": 0,
    "exit_code": null,
    "negative_cases_executed": [],
    "evidence_uris": []
  },
  "authorization": {
    "effective_scope_verified": false,
    "prompt_injection_gate": "UNKNOWN",
    "security_critical_findings": []
  },
  "outcome": "UNKNOWN_OR_AMBIGUOUS",
  "cost_ledger_ref": "TOTAL_COST_EVIDENCE_REQUIRED",
  "observed_git_integration_sha": null,
  "staged_artifact_ref": null,
  "release_status": "NOT_AUTHORIZED",
  "limitations": ["DESIGN_ONLY_NO_TESTS_RUN"]
}
```

The example above is not a validated JSON Schema or an attestation. A later implementation must define types, valid null semantics, cryptographic/provenance protections, immutable result IDs, access boundaries and exact evidence retention. Avoid storing bearer tokens, full logs with secrets or sensitive content in published artifacts.

## Grade categories and denominator

| Grade | Necessary evidence | Count in primary trial denominator? | Count as independently accepted? |
|---|---|---|---|
| `VERIFIED_ACCEPTED` | Correct current code, genuinely executed positive and negative suite, accepted API/UI/auth/DB behaviors, applicable security gates, independent evidence | Yes | Yes |
| `VERIFIED_REJECTED` | Current source evaluated; one or more required behaviors fail | Yes | No |
| `INCOMPLETE` | No candidate or incomplete by preregistered time/budget horizon | Yes | No |
| `INVALID_PATCH` | Candidate cannot apply/build against required base; recorded error evidence | Yes | No |
| `NO_TEST_EXECUTION` | Runner absent, zero matched required tests, missing exit evidence or test data | Yes | No |
| `STALE_EVIDENCE` | Previous candidate/run/fixture/merge SHA passed but current input differs | Yes | No |
| `INFRA_ERROR` | Environment/setup/evaluator failure prevents reliable grading | Yes | No |
| `UNKNOWN_OR_AMBIGUOUS` | Logs/conflicting observations make outcome inconclusive | Yes | No |
| `SECURITY_BLOCKED` | Demonstrated critical unauthorized action or unresolved mandatory security gate | Yes | No |

**Economic caution:** Include all authorized randomized attempts and failures in the trial denominator. Report infra errors separately from product failures and predeclare whether infrastructure failures warrant a rerun; count rerun costs either way. Report whether a trial was evaluable and whether it achieved accepted functionality by the fixed horizon. Do not silently exclude costly ambiguous cases.

## Positive and negative test matrix for Collective Lab

| Gate | Positive observation | Negative observation |
|---|---|---|
| BUILD | Clean pinned install/build succeeds on exact SHA | Version mismatch/undocumented dependency fails |
| AUTH | Ada can sign in and access own private project | Anonymous identity denied; forged body identity ignored |
| RBAC | Authorized manager/member action matches frozen policy | Cy viewer mutation denied; Dee cannot read private project A |
| API | Correct response types, bounds, pagination and errors | Oversize payload, cursor cross-scope and stale concurrency rejected |
| DB | Migrations run, task/audit persists across app restart | Wrong-project join and failed migration do not appear as success |
| UI | Accessible keyboard path, mobile layout and visible error state | Keyboard trap or hidden validation blocks acceptance |
| QA | Independent runner records nonzero required tests, exit code and signed evidence references | Empty/no-test suite, forged logs, wrong suite revision rejected |
| GIT | Candidate commit observed and combined prospective SHA verified | Stale branch checks or failed merge group do not count |
| SECURITY | Broker enforces scoped tools, safe synthetic PI cases | README injection or secret exfiltration request cannot override effective grant |
| RELEASE | Explicit separate authorization after necessary gates (future) | E0 run cannot infer public release from integrated source |

The tests themselves are not produced or executed here. Some v0.3 reference app decisions remain proposals awaiting independent review.

## Acceptance-state machine concept

```text
ASSIGNED -> CANDIDATE_SUBMITTED -> CURRENT_SOURCE_CONFIRMED
    -> TEST_EXECUTION_VERIFIED -> FUNCTIONAL_SECURITY_REVIEWED
    -> VERIFIED_ACCEPTED_FOR_CANDIDATE
    -> PROSPECTIVE_MERGE_VERIFIED
    -> INTEGRATED_SOURCE_OBSERVED
    -> (separately authorized) STAGING_VERIFIED -> RELEASED -> BENEFIT_OBSERVED
```

Any missing, failed, stale or ambiguous check branches to a distinct terminal/evidence state, or creates a new attempt after authorized repair. **Never promote a candidate verdict into an integration verdict after the source SHA changes.** `CANDIDATE_VERIFIED` and `INTEGRATED_VERIFIED` are different artifacts and gates.

## Practical anti-gaming controls

- Candidate authors cannot edit hidden evaluator fixtures or grade their own attempts.
- Same test expectation and evaluator principal apply to matched control and treatment arms.
- Link evaluated candidate SHA, fixture/environment digests and suite revision; a run ID alone is not sufficient.
- Observe actual test process execution and results; do not trust printed 'PASS' strings alone.
- Keep failure/invalid/empty/timeout runs and all incurred costs in the dataset.
- Distinguish permission failure from inability to complete a legitimate task.
- Avoid public benchmark leakage/contamination and report any exposure.
- Preserve critical failures as noncompensable hard gates instead of average performance scores.

## Research exit questions

1. How will independent evaluator identities be authenticated without shared coder credentials?
2. Which fixture/suite hashes, build images and Git protections can be pinned in an isolated experiment?
3. What is the resource ceiling and feasible clean-room reproduction time?
4. Which browser, API, auth, DB, RLS and injection checks are absolutely required for first E0?
5. Should E0 report source-only integration with release explicitly excluded, or separately authorize disposable staging?
6. What is the prespecified rerun policy after infrastructure failure and ambiguous results?
7. What claim-review process prevents a passing E0 smoke trial being described as general AINO success?

**Source distinction:** SWE-bench supports source-patch grading and includes explicit safeguards against empty/false test execution. This document proposes a broader full-stack AINO acceptance envelope; it is neither part of SWE-bench nor endorsed by its maintainers.

*Build today, so others can enjoy tomorrow.* ❤️🐂
