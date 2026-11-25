# EXP-5 — Three-Stage Agency Communication Handoff and Evaluator Subprocess: Executed Local Report

**Date:** 2026-11-23 · **Scope:** Foromni research only, not Internet Embassy · **Execution:** local Python 3 standard library synthetic fixture. **Grade:** observed local software assertions, not independently secured evaluators, live MCP/webhook, or agency integration.

## Experiment and hypothesis

Research question: Can three simple/moderate communication tasks—(A) event normalization/schema screening, (B) event idempotency/deduplication, (C) project/task/revocation-scoped routing—converge into exactly one deterministic outcome, while a separate local evaluator process runs tests on an exact source revision and emits a source-and-suite-bound receipt?

Hypothesis: on a fixed benign + replay + cross-project + stale epoch fixture, pipeline dispatches precisely one authorized synthetic event, fails closed on conflicting event ID, ignores replay/cross-project/stale events and blocked protected actions; receipt verifier accepts correct result and rejects replay/tampering/stale source/suite. Same investigator authored tests and candidate so this is exploratory, not blinded, preregistered, or externally independently audited.

## Local construction

Four independently named Python files were created locally in `foromni_exp5/` (full exact bytes and hashes in downloadable evidence archive):

- `pipeline.py`: `normalize` validates required fields and types, `deduplicate` eliminates identical event replays but raises on same ID with conflicting payload, `dispatch` selects only matching project/task/current epoch/action while respecting revoked flag. These are **synthetic data predicates**, not production authorization.
- `test_pipeline.py`: nine `unittest` assertions covering normalization, missing fields, duplicate, collision, cross-project, revocation, stale epoch, protected action, end-to-end three-stage convergence.
- `evaluator.py`: invokes test suite in a Python child subprocess with signing-key environment variable **removed from test subprocess**, hashes source and suite bytes with SHA-256 and signs the verdict with HMAC-SHA256 from its own process environment.
- `verify.py`: checks HMAC, source SHA-256, suite SHA-256, PASS verdict, and in-memory attempt ID replay cache. **No durable attempt registry or trusted source checkout**.

## Actual observed results

**Command:** `EXP5_EVALUATOR_KEY=... PYTHONDONTWRITEBYTECODE=1 python evaluator.py pipeline.py test_pipeline.py`. Child Python run reports `Ran 9 tests ... OK`, evaluator exits 0. Receipt `attempt_id=EXP5-T1-001`, `suite_pass=true`, `verdict=ACCEPT`, and source/suite hashes. Five distinct verification observations were asserted with fresh/used replay sets:

| Check | Observed |
|---|---|
| Unchanged receipt, source and suite | `(True, 'accepted')` |
| Same accepted receipt replayed | `(False, 'replayed_attempt')` |
| Receipt verdict modified without resigning | `(False, 'bad_signature')` |
| Source file changed after signing | `(False, 'stale_source')` |
| Suite file changed after signing | `(False, 'stale_suite')` |

**Exact local SHA-256 files:**

| File | SHA-256 |
|---|---|
| `pipeline.py` | `647e3926f58ca39d0a81f07bd439fb9e435ef38f8c73f9bbadfea65ccd9b8257` |
| `test_pipeline.py` | `7878ea8a26c4a34858cc78b9541e595f36a052c7cba7e8eaf4cd2ba7d65413c0` |
| `evaluator.py` | `6c7b139a8deed99ee3d2908f2c073e9355e4d0b48cb99a878b086913cc867a33` |
| `verify.py` | `56171aefcda1d9427ba3e5235cb60dc740c2495383eef3008c17b9574beaa880` |

**Artifact:** `foromni_exp5_local_evidence.zip` is attached to this research conversation; it contains four source files and manifest. It was not pushed as source code to GitHub in this pass. This report is committed to the existing research branch, not protected main.

## AAR / scientific limits

- A separate *subprocess* evaluated Python tests and signed their result, but process separation on the same account is not trustworthy principal/secret isolation. In this prototype, controller knows/handles the demonstration key, so don't claim evaluator independence.
- `normalize` accepts synthetic caller-created events; no real webhook signature or provider OAuth verification. The producer could fabricate event fields.
- `deduplicate` uses an in-memory dictionary; replay after restart is not blocked. No transactional durable queue/inbox/outbox or multi-writer concurrency.
- `dispatch` filters by strings and boolean `revoked`; no effective credential/secret or real project access granted. It is not a security enforcement gateway.
- The evaluator reads exact local source bytes and suite bytes and checks executed tests; it does **not** independently fetch Git commit SHA or derive immutable trusted accepted task/attempt IDs.
- Source-level communications/handoff hypothesis got a positive deterministic *software test* but did not compare transport alternatives, throughput, latency distribution, failure under network partitions, cloud costs or real agent task execution.
- This experiment is explicitly not a test of APIs, MCP, webhook providers, cron scheduler, plugins or connectors in production.

**Verdict:** `EXP5_LOCAL_COMM_PIPELINE_9_OF_9_PASS`; `RECEIPT_CHECKS_5_OF_5_EXPECTED`; `ACTUAL_AGENT_ORCHESTRATION_NOT_PROVEN`; `INDEPENDENT_QA_NOT_PROVEN`; `DURABLE_REPLAY_NOT_PROVEN`.

## Convergence and next study

See [Agency Communication and Orchestration Transport Roadmap v0.1](AGENCY-COMMUNICATION-ORCHESTRATION-TRANSPORT-ROADMAP-V0.1.md), added from founder direction. The highest information-value next experiment is compare webhook callbacks vs a lease-fenced cron reconciler against a synthetic durable inbox, injecting missing, duplicate and out-of-order events and measuring accepted unique tasks, stale replays, attempts, compute, time and recovery. Then investigate MCP/connector capability narrowing, immediately adjacent to cyber security R&D.

Do not promote this local fixture into FOR-007 authority, protected main or production services without full independent gates.
