# Open-Source AINO Case Study 04 — SWE-bench and Honest Acceptance Evidence

**Status:** Source-reviewed case study, not an executed benchmark, reproduced score or collaboration.  
**Date:** 2026-11-21. **Foromni only.** Internet Embassy is not part of this investigation.
**Source snapshot:** [SWE-bench/SWE-bench](https://github.com/SWE-bench/SWE-bench) at `02e7a74ffd0b707aab73d203fe87bdc7c76afc8e`.
**Research companions:** FULL-STACK-REFERENCE-APP-CONFORMANCE-V0.2.md; FULL-STACK-REFERENCE-APP-API-FIXTURE-FREEZE-PROPOSAL-V0.3.md; FULL-STACK-CONVERGENCE-TRIAL-PREREGISTRATION-V0.1.md; ECONOMETRICS-OF-CONVERGENCE-AND-COORDINATION-VARIANCE.md; OPEN-SOURCE-AINO-CASE-STUDY-FLYWHEEL-PROTOCOL.md.

## The question

**How can an AINO prove its coding agents produced independently accepted functionality, rather than clean-looking patches, self-reported success or a favorable subset of easy runs?**

SWE-bench offers a valuable source implementation for evaluating code patches against real GitHub issues and test suites in a reproducible harness. It does **not** automatically evaluate a multi-agent team operating a live full-stack application from objective to protected merge, staging, release, safe governance and beneficiary value. Foromni must preserve that distinction.

## 1. What the source actually provides

The current [README](https://github.com/SWE-bench/SWE-bench/blob/02e7a74ffd0b707aab73d203fe87bdc7c76afc8e/README.md) describes:
- Issue + original codebase -> candidate patch -> evaluation of whether required tests pass;
- Docker-based execution, local and cloud evaluation options, per-instance logs and a run-level report;
- several dataset variants, including Verified, Lite, Multimodal and Multilingual;
- the **SWE-bench Verified** subset described as 500 tasks reviewed for solvability;
- the latest README's **September 1, 2026** announcement for an open-source Multimodal v2 set of 480 tasks;
- a warning about nontrivial local hardware/storage costs;
- a significant caching caveat: result reuse keyed by `run_id` and `instance_id`, **not by patch content**. Use a fresh run ID to evaluate a different patch for the same instance.

The last caveat alone is a useful reminder: an evaluation artifact is only meaningful when the evaluated source and run identity correspond to the candidate being credited. A stale successful result reused for a new patch creates false evidence.

## 2. Notable defense against false-green grades

The repository's current [grading logic](https://github.com/SWE-bench/SWE-bench/blob/02e7a74ffd0b707aab73d203fe87bdc7c76afc8e/swebench/harness/grading.py) includes comments and checks addressing several failure classes:

1. If tests do not actually run, the evaluator should **not** infer resolution from an empty test-status map.
2. For `FAIL_TO_PASS` cases, skipped tests are not treated as a legitimate resolution.
3. `PASS_TO_PASS` cases help detect regressions in tests that already worked, with documented semantics for skipped cases.
4. Parsed test logs can be cross-checked against recorded test command exit status and evidence that an actual suite executed. Comments explicitly warn that test output can be printed or faked by source under test.

These mechanisms are code-inspected observations, **not a security audit or an assertion that every adversarial test-tampering technique is prevented**. The evaluator's own command execution, fixture controls, and sandbox trust remain important boundaries.

SWE-bench's [reporting module](https://github.com/SWE-bench/SWE-bench/blob/02e7a74ffd0b707aab73d203fe87bdc7c76afc8e/swebench/harness/reporting.py) separately tracks dataset total, submitted predictions, incomplete, empty patches, resolved, unresolved, errors and causes including likely infrastructure failure vs ambiguous failure. It explicitly retains failure/error cases in the dataset denominator rather than quietly dropping them.

The [evaluation guide](https://github.com/SWE-bench/SWE-bench/blob/02e7a74ffd0b707aab73d203fe87bdc7c76afc8e/docs/guides/evaluation.md) details per-run evidence files such as `report.json`, `test_output.txt`, `run_instance.log`, and the executed `eval.sh`. It distinguishes missing results from legitimate unresolved tests.

## 3. Mapping SWE-bench lessons to Foromni's full-stack acceptance oracle

| SWE-bench mechanism | What Foromni can learn | Additional AINO requirement |
|---|---|---|
| Frozen issue + codebase | Freeze objectives and starting source for comparison | Include all UI/API/auth/DB requirements and human-approved product intent |
| Patch application | Distinguish produced diff from meaningful functionality | Source must be integrated at exact current SHA under protected policy |
| Containerized evaluation | Reproduce environment and test setup | Auth providers, seeded tenants, DB migrations, browser and staging fixtures |
| Fail-to-pass / pass-to-pass | Detect fixed behavior and regressions | Role-matrix denials, cross-tenant leakage, accessibility, persistence and lifecycle |
| Test-execution evidence | Prevent no-test-run from scoring as success | Independent evaluator identity, sealed/maintained oracle and explicit policy observations |
| Distinct incomplete/errors | Preserve denominators and honest outcome accounting | Cost, elapsed time, human work, retries, agent count, release safety and lost acknowledgments |
| Run ID caching caveat | Don't reuse success for the wrong patch | Key claims to candidate SHA + environment/test suite revision, not just task/run label |
| Maintainer contribution path | Reproducible evaluation reports are useful public artifacts | Seek maintainer relevance before external issue or PR |

**Boundary:** SWE-bench's resolved score is an evaluation result for a specific patch/test instance, not proof that an AINO deployed a secure product or created downstream social value.

## 4. Proposed independent full-stack acceptance envelope

For each Foromni trial, require all of:
- `objective_id` and accepted `requirements_revision`;
- `benchmark_case_id`, difficulty stratum, assigned control/treatment and preregistered horizon;
- source `base_sha`, submitted candidate `candidate_sha`, exact combined `integration_sha` where reached;
- source-diff digest, runtime/lockfile/image/browser/schema seed digests;
- `evaluation_suite_revision` and independently authenticated `evaluator_principal`;
- test-execution positive evidence (exit status, nonzero expected tests run, relevant negative oracle);
- detailed `acceptance_outcome`: `VERIFIED_ACCEPTED`, `VERIFIED_REJECTED`, `INCOMPLETE`, `INFRA_ERROR`, `UNKNOWN_OR_AMBIGUOUS`, with no category silently excluded;
- records of full cost, end-to-end elapsed time, attempts and interventions;
- security-gate status and separate publish/deploy authority;
- actual GitHub observed merged SHA and real release/outcome events, only if they happened.

Report *both* accepted behaviors per all-inclusive cost and completion probability by a fixed horizon. Report conditional cost/latency distributions with explicit missingness/censoring. Where multiple features are required together, the task is accepted only if **the integrated vertical slice as a whole** meets the frozen oracle, not if components pass independently.

## 5. Synthetic example: a false-green that must not count

An AI developer changes the Collective Lab UI and records that `npm test` succeeded. Its task requires member access checks and a PostgreSQL migration. However, the test command returned zero because no test files matched, the migration never ran and a viewer can edit tasks in the API.

**Correct decision:** `VERIFIED_REJECTED` or `UNKNOWN_OR_AMBIGUOUS` depending on independently observed evidence, never `VERIFIED_ACCEPTED`.

Another developer submits patch `SHA_B` but the evaluator reuses a green cache from `SHA_A`. **Correct decision:** reject stale evidence, require a new version-bound verification; cache keys/manifest must include exact evaluated patch identity.

These are illustrative Foromni scenarios, not actual SWE-bench findings or executed attacks.

## 6. Econometric relevance

A superficial metric rewards number of finished tickets, green tests or passing patches. A scientifically useful metric uses the **entire trial denominator**, maintains difficult and incomplete tasks, records human interventions and total costs, and separates infra errors from true software failures.

A benchmark method can itself bias the observed "convergence effect" if:
- one treatment gets easier tasks or learns hidden answers from prior public benchmark exposure;
- failed attempts vanish from reports;
- evaluators differ between control and treatment;
- tests are generated/edited by the same agent whose solution is graded;
- suite/run identities are reused across different patch SHA values;
- cost of planners, reviewers, retries or developer setup is omitted;
- high-severity permission breaches are averaged away as ordinary task failures.

Proposed preregistered study: same frozen Collective Lab reference specification, independent acceptance suite and comparable model/provider/hosting; vary only convergence-first packet vs ordinary work instructions at first. Existing SWE-bench methodology is an inspiration, not a drop-in final AINO scoring oracle.

## 7. Security observation requiring caution

The inspected [harness module](https://github.com/SWE-bench/SWE-bench/blob/02e7a74ffd0b707aab73d203fe87bdc7c76afc8e/swebench/harness/run_evaluation.py) creates per-instance Docker containers and includes settings accommodating some browser testing. Containers and evaluator logs do **not automatically** imply strong isolation from a deliberately hostile patch, network egress, host credentials or the Docker daemon. The future Foromni security review must evaluate its own experimental threat model and sandbox choices. This source inspection did not identify an exploit.

## 8. Collaboration opportunities, ordered by usefulness

**First (low intrusion):** Publish a correct source-linked synthesis explaining how to prevent stale cache results and false-green test execution in AI coding benchmarks; credit SWE-bench maintainers.

**Second (after review):** Compare Foromni's full-stack acceptance-envelope approach with the current SWE-bench reporting schema and submit a small, reproducible documentation clarification or example if the maintainers welcome it. Check open issues and PRs to avoid duplicating planned work.

**Third (later and authorized):** Share fully documented AINO controlled experiments and proposed optional metadata for source revision, evaluator provenance, resource consumption, incomplete results, and multi-agent team counts. Preserve SWE-bench's benchmark scope: do not demand that their project adopt all Foromni objectives.

**Fourth (mutual interest only):** Explore interoperability or research cooperation around trustworthy measurement of agent work. No implied endorsement, formal partnership or contact has occurred.

The repository README welcomes contributions through issues/PRs and provides citation guidance. The license checked is MIT, with separate obligations and source attribution when reusing material.

## 9. Next Foromni action

Create a focused **E0 acceptance-evidence schema and grade decision table** that forces the independent reviewer to distinguish valid test execution from no-test / stale-run / infra-error / incomplete behavior, and to bind any successful verdict to the exact source SHA. Then return to the remaining full-stack readiness gates: Git permission audit, independent evaluator isolation, environment pinning and founder-approved trial.

Keep broader inter-agent communication work deferred. Do not add an unnecessary benchmark platform to E0 without clear evidence it is needed.

## Source references

- [Repository overview and dataset descriptions](https://github.com/SWE-bench/SWE-bench/blob/02e7a74ffd0b707aab73d203fe87bdc7c76afc8e/README.md)
- [Evaluation and cache behavior](https://github.com/SWE-bench/SWE-bench/blob/02e7a74ffd0b707aab73d203fe87bdc7c76afc8e/docs/guides/evaluation.md)
- [Grading logic](https://github.com/SWE-bench/SWE-bench/blob/02e7a74ffd0b707aab73d203fe87bdc7c76afc8e/swebench/harness/grading.py)
- [Run reporting](https://github.com/SWE-bench/SWE-bench/blob/02e7a74ffd0b707aab73d203fe87bdc7c76afc8e/swebench/harness/reporting.py)
- [Evaluation harness](https://github.com/SWE-bench/SWE-bench/blob/02e7a74ffd0b707aab73d203fe87bdc7c76afc8e/swebench/harness/run_evaluation.py)
- [MIT license](https://github.com/SWE-bench/SWE-bench/blob/02e7a74ffd0b707aab73d203fe87bdc7c76afc8e/LICENSE)
- [SWE-bench homepage](https://www.swebench.com/)

**What was not done:** no installed benchmark, runnable E0 app, tests, outcomes, external contribution, contact or deployment.

*Build today, so others can enjoy tomorrow.* ❤️🐂
