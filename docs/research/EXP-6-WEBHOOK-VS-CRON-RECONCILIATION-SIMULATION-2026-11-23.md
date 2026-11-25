# EXP-6 — Webhook Delivery vs Cron Reconciliation: Executed Synthetic Comparison (2026-11-23)

**Scope:** Foromni open-source research only. No Internet Embassy changes. No real webhooks, cron scheduler, MCP, provider token, paid API, deployment, or protected Git operation. **Evidence:** Python standard library code, test suite and JSON summary in `foromni_exp6_evidence.zip` attached to the research conversation. **Local tests executed:** 9/9 PASS.

## Question and experimental design

Does periodic reconciliation against one authoritative task store complete more valid jobs than webhook-only dispatch when events are missing, duplicated, stale, reordered, and worker claims crash?

**Control:** webhook-only. **Treatment:** same webhook stream plus two idempotence-checking reconciliation passes that scan authoritative job records. Each of 100 paired deterministic seeded trials has 40 jobs, 22% simulated notice loss probability, 30% duplicate probability, 18% stale notice probability, and 13% crash-after-claim probability; order randomized with a seeded PRNG. Both arms use the same seed and job definition, so this is a paired **synthetic simulation**, not production reliability measurement. The reconciler uses a monotonically increasing fencing epoch in the single-process store.

## Observed local results

| Metric across 100 trials | Webhook only | Webhook + reconciler |
|---|---:|---:|
| Total synthetic job opportunities | 4,000 | 4,000 |
| Completed | 2,703 (67.575%) | 4,000 (100%) |
| Uncompleted | 1,297 | 0 |
| Duplicate notices seen | 972 | 972 |
| Stale notices rejected | 606 | 606 |
| Claims crashed before completion | 404 | 404 |
| Expired/abandoned claims recovered | 0 | 404 |
| Double completions | 0 | 0 |
| Active unfinished leases | 404 | 0 |
| Webhook delivery attempts | 4,685 | 4,685 |

**Test suite:** 9 unit/integration assertions pass, verifying missing-webhook behavior, reconciliation recovery, duplicate suppression, stale revision handling, fencing of old leases, crashed-claim recovery, repeated reconciliation idempotence, unknown-job rejection and 100-seed comparison.

**Hashes from actually executed files:** `experiment.py` SHA-256 `eb647c2686858c351f3c69c93b08f28ff470c634c96e2cd23db6574795c89f27`; `test_experiment.py` SHA-256 `c56c1a438d1f8f7ebb868165bb31099bf39f6acad0df369a72a048957b728bd6`; `summary.json` SHA-256 `8d6631518f28cf8e57d7316b899338d142a8cb86f62587ed9e384b64b4597ab0`.

**Reproduce:** unzip evidence archive; run `PYTHONDONTWRITEBYTECODE=1 python -m unittest -v` followed by `PYTHONDONTWRITEBYTECODE=1 python experiment.py` in the extracted directory.

## Scientific qualifications

- Model simulates **crash after claim but before completion**; does not simulate crash after actual irreversible external side effect but before receipt. Thus zero duplicate completion does NOT mean exactly-once external action.
- Store is an in-memory Python object, not durable SQL, queue, distributed lock, or multi-region system. There are no simultaneous writers, race tests, clock skew or process restart preservation.
- Reconciler is allowed to inspect all authoritative jobs and always eventually runs; with this constructed assumption full completion is expected. This is a comparative algorithm sanity check, not measured infrastructure uptime.
- PRNG trials are deterministic variants of one assumed data-generating model, not 100 independent real deployments, and no inference of production 100% recovery should be made.
- No practical runtime expense or scheduling latency measured; synthetic costs of repeated calls and full economic return still unknown.
- No independent QA reviewer principal: author and test writer are the same assistant.

## AAR / Decision

**Positive finding:** under this model, lost notices and crashed pre-completion leases create substantial backlog if webhook dispatch is the only trigger. Reconciliation from durable authoritative state can logically recover missing work, provided it is idempotent and fences old attempts.

**Rejected inference:** that one can safely combine an arbitrary webhook, cron and MCP tool to guarantee exactly-once external effects. Design must use transactional outbox/inbox, durable job records, idempotency keys, leases/fencing, provider-side request IDs when available, read-after-write reconciliation, credential-scoped tool boundaries, dead-letter strategy and trace/cost receipts.

**Next experiment:** implement a small SQLite-backed durable inbox/outbox with real process restart, concurrent claims and crash points **before and after** a simulated external side effect. Compare callback-only, cron-only and hybrid event schedules. Explicitly measure duplicate *effects*, not just duplicate completion records, and fail closed where the provider has no idempotency guarantee. Then test MCP/connector privilege narrowing, with cybersecurity collaboration in parallel.

**Research status:** `EXP6_SYNTHETIC_WEBHOOK_RECOVERY_PASS` and `EXP6_DURABLE_EXACTLY_ONCE_NOT_TESTED`. No change to frozen FOR-007.
