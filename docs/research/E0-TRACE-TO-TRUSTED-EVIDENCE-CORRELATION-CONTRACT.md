# E0 Trace-to-Trusted-Evidence Join Contract — Research v0.1

**Status:** Proposed correlation contract and anti-gaming protocol; **not coded, tested, deployed or authorized for data collection**.  
**Date:** 2026-11-21. **Foromni only.** No Internet Embassy modification.
**Inputs:** EXTERNAL-CASE-STUDY-OPENTELEMETRY-AGENT-OBSERVABILITY-AND-EVIDENCE.md, E0-INDEPENDENT-ACCEPTANCE-EVIDENCE-AND-GRADE-DECISION-TABLE.md, PERSISTENT-AGENT-REGISTRY-IDENTITY-AND-SHARED-CREDENTIALS.md, EXTERNAL-CASE-STUDY-SWE-BENCH-ACCEPTANCE-EVIDENCE-AND-BENCHMARK-INTEGRITY.md.

## Decision: observability is not a grant, receipt, grade or invoice

Agent-generated spans are context and performance *claims* from instrumentation. The authoritative E0 evidence ledger records independently observed state transitions under authenticated principals. A join between them can improve troubleshooting, but cannot elevate a self-authored span to an authorization check, GitHub write confirmation or QA PASS.

## Minimal model (conceptual)

- **Registry:** `agent_id` persists across runs; `incarnation_id` identifies a runtime/model/session; `attempt_id` belongs to a current accepted `task_id/task_revision`.
- **Runtime trace:** standard OTel `trace_id/span_id`, operation kind, model/provider name, token observations, duration and exception; correlation tags `foromni.task_id`, `foromni.attempt_id`, `foromni.operation_id` are **proposed internal extension fields**, not OTel standardized conventions.
- **Trusted action intent:** broker-issued `operation_id`, authenticated actor/session, effective grant and lease epoch, target repository/ref/base SHA, requested action, authenticated timestamp and attempt uniqueness.
- **Trusted action outcome:** authorized broker logs GitHub API response plus actual later read-back of target ref/commit; unknown remains `UNKNOWN`.
- **Independent evaluation:** evaluator principal, exact source SHA, test/fixture/env revision, number of tests actually run, positive/negative outcomes, noncompensable security gate, signed/authenticated evidence reference.
- **Cost:** provider usage receipts/invoices where available; resource/runtime/CI/human effort ledger. Missing amounts flagged; never infer all cost from tokens.
- **Business result:** merged source, released artifact and observed beneficiary outcome are separate records, no automatic progression.

## Join rules

| Claim or signal | Source-of-truth rule |
|---|---|
| Agent requested GitHub write | Span is supporting detail; broker intent under authenticated session is authoritative for *request* |
| Agent wrote Git commit | Query actual remote ref/commit and correlate broker receipt; trace alone insufficient |
| Agent QA passed | Independent evaluator under separate identity must attest exact source and suite |
| Agent finished task | Verified acceptance + actual Git ref state, not agent language or number of calls |
| Agent spent $X | Reconcile provider/model invoices and locally measured costs; record uncertainty |
| Agent was permitted to act | Current authenticated policy/grant decision at action time, never tracer labels |
| Agent failed/retried | Include ambiguous/no-ACK cases with reconciled outcome or honest UNKNOWN |
| Agent improved | Compare repeated verified outcomes in comparable task strata, with confidence/uncertainty |

## Missingness and contradiction categories

- `TRACE_PRESENT_MATCHED`: trace links to authenticated attempt/operation and consistent authoritative receipt.
- `TRACE_PRESENT_UNTRUSTED`: a trace exists but no authenticated binding can corroborate its actor claim.
- `AUTHORITATIVE_OPERATION_NO_TRACE`: broker/Git/evaluator evidence exists, telemetry was missing or sampled.
- `TRACE_NO_AUTHORITATIVE_OPERATION`: span states success but trusted side-effect receipt/ref is absent; do not credit contribution.
- `SOURCE_SHA_MISMATCH`: evaluator/trace references differ from actual candidate or prospective merge; invalidate reused verdict.
- `UNCERTAIN_EXTERNAL_SIDE_EFFECT`: ACK lost and ref cannot be read; no blind retry or implicit failure assumption.
- `COST_UNRECONCILED`: estimates available but billing full denominator missing.

Important distinction: missing telemetry does **not** invalidate independently accepted code if Git and QA proof are intact; it *does* reduce the reliability of detailed per-agent efficiency estimates. In contrast, missing QA or source proof blocks accepted-product claims.

## E0 acceptance and research measurements

Proposed secondary diagnostics:
1. **Attempt coverage:** authenticated attempts with at least one usable observed trace / all actual attempts.
2. **Operation reconciliation:** Git broker operations with independently corroborated final status / all attempted operations.
3. **Attribution precision:** trace claims matching broker-authenticated worker sessions / trace claims investigated.
4. **Missingness by failure class and task difficulty:** never assume failed attempts have the same telemetry availability as successful ones.
5. **Cost reconciliation share:** attributable actual provider+host+CI+review costs / all costs incurred (flag truly unknown values).
6. **Telemetry overhead:** incremental latency, storage and processing cost versus disabled telemetry in a separately controlled trial.

Do not compute 'agent productivity' by counting spans, token output or number of tool calls.

## Synthetic scenario for later evaluator (not executed)

Worker A uses a shared inference gateway and writes candidate `SHA_C`; its tool emits a `PASS` string. Independently authenticated evaluator tests `SHA_B` due to stale checkout. Expected: **SOURCE_SHA_MISMATCH**, no verified acceptance for `SHA_C`. A GitHub API ACK failure is later reconciled by reading the actual branch; the model's tool trace alone never determines write outcome. Subsequent task assignments must not treat this attempt as independently successful.

## Safe defaults

- No raw prompts, credentials, private file content or tool response bodies in ordinary telemetry.
- Opt in explicitly to sensitive captured content only under approved, bounded research protocol.
- High-cardinality task/commit identifiers belong to trace-level and ledger references, not aggregate metric dimensions.
- Receiver/exporter auth, tenant segregation, data retention and policy revision documented before collection.
- Make the causal-trial outcome oracle independent of the orchestrator/agent and the observability collector.

## Next open questions

Which identity-binding arrangement can a one-agent disposable E0 trial support with **no new elaborate telemetry infrastructure**? Can the worker write a small redacted local trace artifact and the independent evaluator verify exact Git/QA facts separately? How to preserve replay provenance after runner crashes? How do traces expose coordination cost rather than only model-call cost?

**Recommendation:** Record this minimal contract for E0, keep the first trial lightweight, and consider an OpenTelemetry collector only after observing a real scaling or standardization need.

*Build today, so others can enjoy tomorrow.* ❤️🐂
