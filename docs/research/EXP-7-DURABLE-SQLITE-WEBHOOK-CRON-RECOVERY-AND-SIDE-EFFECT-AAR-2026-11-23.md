# EXP-7 — Durable SQLite Webhook/Cron Recovery and External-Effect Ambiguity (Executed)

**2026-11-23; Foromni only.** Research experiment performed in local Python 3.13.5 with SQLite standard library. **No actual cloud API, remote webhook, cron deployment, agent, credentials, paid operations, production writes, protected branch merge, or Internet Embassy change.** Reproducible source, 11 tests, results JSON and run instructions are in the research-session archive `foromni_exp7_durable_recovery.zip`; **the runnable source archive is not pushed to GitHub in this report commit**.

## Question and falsifiable hypothesis

When a worker crashes *after* a simulated external side effect but *before* recording completion, can a reopened durable task ledger plus authoritative provider lookup prevent blind retry and recover correctly? Compare webhook-only, cron-only and hybrid event triggers on identical synthetic jobs. **Prediction:** cron and hybrid will recover missing notifications while webhook-only leaves backlog; if provider lookup is unavailable, uncertain claims should be marked `needs_review`, not blindly replayed; blind replay to non-idempotent provider should cause duplicate effect.

## Architecture tested

- Two physically separate SQLite files: an authoritative `jobs` plus `inbox` ledger, and an independent simulated provider's `effects` ledger. This is not an atomic distributed transaction.
- `receive_webhook` uses a SQLite transaction and checks unique event ID + payload hash. Same event is idempotent; same ID with altered payload raises `event-id-collision`.
- `claim` uses `BEGIN IMMEDIATE` to atomically transition pending → running, increments per-job fencing epoch; simultaneous threads race the same claim.
- `external_effect` models either provider-enforced idempotency by stable key or a non-idempotent provider capable of duplicate effects.
- Inject `crash_after_effect` between provider effect and job completion. Reopen SQLite files and also perform one recovery in a **fresh operating-system subprocess**.
- `recover` uses provider lookup to confirm a completed effect before setting job `done`; if provider cannot be queried, mark `needs_review` (no blind external retry). Old epoch cannot finish a newer claim.

## Actual observed execution

**Final local command:** `PYTHONDONTWRITEBYTECODE=1 python -m unittest -v` followed by `PYTHONDONTWRITEBYTECODE=1 python experiment.py`. Final tests **11/11 PASS**, zero failures, ~1.012s; not a throughput measurement. An initial 10-case run had one failed assertion because the author mistakenly expected two claims to remain running in webhook-only after explicit restart reconciliation; observed outcome correctly recorded them as done. Corrected the assertion, closed database connections explicitly, and added a fresh-subprocess test before final run. Do not present that initial failed run as a pass.

### Fixed deterministic 20-job scenario

| Strategy | Done | Pending | Needs review | Recorded simulated provider effects | Jobs with duplicate effects |
|---|---:|---:|---:|---:|---:|
| Webhook only + final restart reconciliation | 15 | 5 | 0 | 15 | 0 |
| Cron-only scan | 20 | 0 | 0 | 20 | 0 |
| Webhook + cron | 20 | 0 | 0 | 20 | 0 |
| Hybrid with provider lookup unavailable | 18 | 0 | 2 | 20 | 0 |

The webhook-only arm includes a **final crash-claim reconciliation**; without it, 2 claims would remain uncertain. Five jobs received no event, so they remain pending. In hybrid-without-lookup, the external effects occurred but 2 claims are conservatively held for review; the task DB cannot conclude their success.

### 11 executable checks

1. Fixed paired webhook-only/cron-only/hybrid scenario.
2. Crash recovery after closing and reopening both SQLite connections.
3. A fresh OS subprocess confirms the simulated external effect and reconciles it.
4. Absent provider lookup sends uncertain work to needs_review.
5. Blind retry against a non-idempotent provider **creates one duplicated external effect** (negative control).
6. Retry against idempotent provider **does not** create duplicate effect.
7. Stale fencing epoch cannot finish newer claim.
8. Identical webhook ID is deduplicated; conflicting ID payload rejected.
9. Unknown webhook job rejected without persisting inbox event.
10. Eight simultaneous contender threads produce one successful atomic claim.
11. Repeat reconciliation has no duplicate provider effect.

## Reproducibility hashes (SHA-256 of final locally run bytes)

| File | SHA-256 |
|---|---|
| `experiment.py` | `84b41ab9f24df7cf1df313ab2ce32f38a270e7d88a07941262294771e12e7441` |
| `test_experiment.py` | `f3d0905469919d3926b14eb326772b3da9132e4db5fbb56892856e2a0e4691e8` |
| `results.json` | `13cd11d017b7570f0f6ad44a5cc3af311118780c9e94c1e0edae312a1f4dc99a` |

**Archive:** `foromni_exp7_durable_recovery.zip` linked in the research response, including source, tests, results, README. The report records checks but is not itself independent source/evaluator attestation.

## After-action findings and scope

**Supported:** unique webhook event deduplication, SQLite-atomic claims, fencing checks, file persistence, recovery in an actual new Python OS process, provider effect-query reconciliation, and concrete duplicate-effect risk from unsafe blind retry in a toy model. These were exercised by code, not just specified.

**Not supported:** an exactly-once guarantee across arbitrary external systems, durable queue/pubsub behavior, distributed worker security, multi-host concurrency, authentic signatures, MCP tool authorization, truly independent evaluator, long-duration timing/reliability, actual cloud provider billing, or a legally/accountably authorized production side effect. The provider was a second SQLite database controlled by the same test process; provider lookup reliability was assumed. With no trustworthy provider lookup or idempotency, abstention/review is necessary.

## Engineering decision

Recommend **webhook fast path + periodic durable reconciliation + single canonical task ledger + bounded claims/fencing + provider idempotency and authoritative lookup where available**, with explicit uncertain-effects state. Do not claim exactly-once external effects; implement dedupe and reconciliation with each connector's real semantics.

**Next discriminating experiment:** adapter-level capability narrowing for MCP/plugins/connectors, matching task scopes to provider token scopes; inject replay, overprivileged external MCP server, expired grants, and cross-project actions, then independently inspect effects. The broader cybersecurity workstream should include the same trust boundary.

**Verdict:** `EXP7_DURABLE_SIMULATION_11_OF_11_PASS`; `EXP7_RESTART_AND_SUBPROCESS_RECOVERY_PASS`; `REAL_EXTERNAL_EFFECT_EXACTLY_ONCE_UNPROVEN`. Frozen FOR-007 unchanged.
