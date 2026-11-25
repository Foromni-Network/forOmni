# Foromni H0-M — Executed Local Mechanical Experiment (2026-11-21)

**Status:** LOCAL EXPERIMENT EXECUTED AND INTERNALLY REPLICATED. **Not independently security attested, not an AI-worker trial, not E0a.**
**Scope:** Only synthetic local Python code and disposable Git repositories; no Foromni main commits, IE access, deployments, new services, model/API calls or CI.
**Protocol lineage:** H0-TINY-PATCH-EXPERIMENT-PACKET-V0.1.md; H0-PATCH-LAB-REPRODUCIBLE-HANDOFF-AND-FALSE-GREEN-CHALLENGES-V0.2.md; HYBRID-AINO-BOTTOM-UP-EXPERIMENTAL-LADDER-V0.1.md.

## Predeclared challenge

Can a minimal patch handoff, frozen local Git base and separate test-running Python process correctly classify six synthetic conditions: valid candidate; incorrect code; forged PASS text; stale base; out-of-scope file modification; missing expected tests?

The tested code is the synthetic ASCII-only `normalize_slug` function. Human/operator-authored variants—not an AI worker—were submitted as patches. A separate source observer directory cloned the initial local Git repository and applied allowed patches, checked the base SHA and changed paths, and committed candidate SHA. A separate evaluator directory executed a 14-test `unittest` suite via its own Python process. These are separate process/directories but **the same OS identity and operator**, so not independent security custody.

## Final observations: corrected protocol, three repetitions

| Condition | Expected classification | Run 1 | Run 2 | Run 3 |
|---|---|---|---|---|
| Good patch | VERIFIED_ACCEPTED_FOR_CANDIDATE | matched | matched | matched |
| Incorrect patch | VERIFIED_REJECTED | matched | matched | matched |
| Incorrect patch printing `ALL TESTS PASSED` | VERIFIED_REJECTED | matched | matched | matched |
| Changed base Git source | STALE_EVIDENCE | matched | matched | matched |
| Patch modifying evaluator/test scope | INVALID_PATCH | matched | matched | matched |
| Empty required test suite | NO_TEST_EXECUTION | matched | matched | matched |

**Result: 18/18 expected condition classifications in three local repetitions.** Each correct, incorrect and forged candidate ran 14 tests; the empty-suite challenge ran zero. Stale base and out-of-scope patch were refused before test execution. This is a selected challenge-set result, **not** an estimate of universal correctness or security.

**Wall time per complete 6-case repetition:** 3.004883, 2.769936 and 2.959014 seconds; median 2.959014 seconds. **Cloud/model/API spend:** $0, with human time and local compute not financially valued. Python 3.13.5, Git 2.47.3; source baselines were fresh per repetition and had distinct Git SHAs (normal due to commit metadata).

## Pre-final procedural correction

An earlier empty-suite fixture accidentally launched unittest discovery without the intended case path, producing one import-error test and a correct non-PASS classification. The experimenter corrected that procedural issue to a truly empty unittest suite (**Ran 0 tests**) and **repeated the entire six-case protocol three times**. Only those three corrected repetitions contribute to the 18/18 result. This design change is fully disclosed.

## Actual bottleneck discovered

**H0-B01 — Empty-suite fixture ambiguity:** A test runner invocation can execute the wrong suite and still generate a failure category that masks the underlying harness defect. Repair: predeclare a precise empty-suite fixture and verify observed test counts, not merely final process status. Severity: methodological validity; classification survived, but the injected condition initially did not represent the intended scenario.

**H0-B02 — Real independence unverified:** Separate directories and OS subprocesses do not establish genuine Q vs W security identities. Next experiment should isolate evaluator files, credentials, result storage and candidate code at the operating system/container level with independently observable access refusals. This is a known, **not tested** trust boundary, so do not call it a measured attack finding.

## Reproducibility package

Full local run script, corrected evaluator test source, public starter/contract, six patch variants, JSON evidence for all three repetitions, SHA-256 manifest and detailed scientific report are bundled as `foromni_H0M_experiment_bundle.zip` in the conversation artifact output, **not automatically checked into the Foromni repo**. Retain raw evidence before declaring independent verification.

## What this supports and excludes

**Supports:** In these chosen conditions, independently reconstructed local source and separate test process produced the expected acceptance/refusal categories; forged PASS and zero required tests did not count as verified success.

**Does NOT support:** AI agent competence, hidden reviewer independence, OS sandbox security, denial of network egress, causal multi-agent benefit, full-stack E0a, protected Git integration, production deployment, or full cost per accepted job.

## Next step

Subject to separate scoped approval, perform H0 security/custody isolation in a disposable environment with **different authenticated worker/evaluator principals** and independently checked negative access attempts. Only afterward add one actual coding model (H0-A) and preserve the same outcome inventory and full-cost accounting. Do not add LangGraph, Temporal, Rerun, OpenHands or OTel into H0 just to compensate for a source/grade problem.

*Build today, so others can enjoy tomorrow.* ❤️🐂
