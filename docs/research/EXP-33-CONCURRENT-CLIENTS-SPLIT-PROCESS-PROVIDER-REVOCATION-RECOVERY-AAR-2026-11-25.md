# EXP-33 — Concurrent Clients, Separate-Process Provider, Atomic Mock Effects and Recovery (Executed AAR)

**Date:** 2026-11-25. **Scope:** Foromni only, research branch `research/global-agent-roadmap-execution`. **Result:** 15/15 unit/integration test cases PASSED in one uninterrupted local Python run, `Ran 15 tests in 19.623s; OK`, with ResourceWarnings promoted to errors. No FOR-007 or Internet Embassy modification, no protected merge, production deployment, real MCP/API operations or paid tests.

## Question

Can the EXP-31 pre-admission permission checks and outcome state behavior be combined with a **separately running mock remote provider and separate broker/provider SQLite databases** from EXP-30, while concurrent clients race to execute the same effect ID? Can provider-side revocation and local crash/retry preserve one mock effect?

## Implementation

- `base_exp31.py`: exact copied EXP-31 signed grant, AF_UNIX and SQLite helper module (SHA-256 `e37675a9d2a65bda6db2bf08de071582207b181206dca32d70d7a6da0a716db0`).
- `system33.py`: separate process broker and mock provider with separate SQLite ledgers, authorization before admission, durable versioned broker attempt status, `UNKNOWN` for uncertain transport, `CONFIRMED` only on provider `APPLIED`/`DUPLICATE`, guard against demoting confirmed state on later timeout, and provider-side `BEGIN IMMEDIATE` transaction encompassing revocation lookup and mock effect insertion.
- `test_exp33.py`: launches actual broker/provider subprocesses communicating over AF_UNIX. Twenty clients invoke the broker via concurrent Python threads, but **broker accept loop handles one request at a time**. Both services and test client use the **same Unix UID**; EXP-30's split-UID worker/broker/provider separation is **not repeated** in EXP-33. Keys, databases and subprocesses are under the one local experimenter.

## Actual execution

```sh
cd foromni_exp33_distributed
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_exp33.py
```

**Observed final:** `Ran 15 tests in 19.623s; OK`.

### Test cases

01. Valid task-scoped grant applies one mock effect.
02. Invalid signature fails broker-side admission with no pending row.
03. Twenty simultaneous clients for one effect ID result in one `APPLIED`, nineteen `DUPLICATE`, and one persisted mock effect.
04. Conflicting task binding with same effect ID denied.
05. Authorized provider revocation **before** effect prevents mutation.
06. Revocation **after** effect prevents new mutation, while separate signed receipt grant recovers historical effect.
07. Provider outage is recorded `UNKNOWN`.
08. Recovered provider allows an `UNKNOWN` attempt to become confirmed.
09. Broker deliberately exits code 79 after remote SQLite commit; restarted broker receives `DUPLICATE`, effect count stays one.
10. Mutation grant cannot be used for receipt read.
11. Scoped receipt read finds prior effect; task mismatch denied.
12. Expired signed grant denied without broker admission.
13. Restart of both broker and provider retains state and deduplication.
14. Provider rejects unsupported proxy operation.
15. A later provider outage does not demote an already `CONFIRMED` attempt to `UNKNOWN`.

An initial 15-case run had 14 successful cases and a test-helper argument error for expiry; the test helper was corrected and two placeholder checks replaced by real security assertions. The final **15/15 result is the run to cite**.

## Evidence and fingerprints

The local archive `foromni_exp33_distributed_evidence.zip` contains exact implementation, tests, README, final test log and SHA256SUMS. ZIP SHA-256 `953c545c90ccb5d39d89773f8e78fa92427b1a51342641d6445db05a8f0296b7`.

| Source artifact | SHA-256 |
|---|---|
| base_exp31.py | `e37675a9d2a65bda6db2bf08de071582207b181206dca32d70d7a6da0a716db0` |
| system33.py | `95da38889f7fa5b147fb98cf8e2402563d18152fb41c36e5b204f4d88bac965c` |
| test_exp33.py | `2b5cf06ed11c46af36fcc82170f556fff3a8ccce27cd3323e738c406843748bf` |
| README.md | `691195587478d1e355f47b2b1f8a2adcdab8cd6a3f9f0b55f376bd6eb8fa7abc` |
| test_output.txt | `c0714ef6747c877c954c8edd94d1d86a252ea538565f455ecb7b2b4999679c7f` |

**Distribution:** this GitHub commit stores the AAR only. Runnable code is in the conversation archive, not the Foromni source tree, CI or a deployable service.

## Critical negative evidence / limitations

- **Not true parallel provider mutation:** broker serially accepts requests and provider also serially serves IPC. The 20 concurrent client submissions exercise queuing/idempotent retries, not actual simultaneous provider transactions. A multi-threaded broker and multiple separately authenticated worker processes are still required for a distributed concurrency claim.
- **Not a simultaneous revocation race:** revocation is tested in predetermined before/after order; `BEGIN IMMEDIATE` serializes revocation lookup and effect insertion in the provider's one local SQLite DB, but no controlled race between separate revoke/apply processes is executed.
- **Not independent authority:** same-user test controls Ed25519 owner fixture key, signed admin revocation claims and both processes. Unix socket mode 0666 and same UID are unsuitable production controls; no independent policy issuer or separate credential custody.
- **Not real provider exactly-once:** mock provider's effect and idempotency ledger are a single local SQLite transaction; a third-party external side effect before provider receipt persistence is untested.
- **Not source-bound independent QA:** implementation and tests by one author; no GitHub CI, separate reviewer, hostile unseen fixtures, real distributed partitions or trusted witness services.

## Next discriminating experiment: EXP-34

Run **two separate worker UIDs and broker/provider UIDs**, add actual threaded/multiprocess provider concurrent request serving and force a reproducible revocation/apply race with a synchronization gate. Preserve scope and task grants but move owner/revocation authority to a distinct role and use fail-closed client permissions. Test ambiguous external-effect recovery and independent witness checkpoint corroboration separately; label `UNKNOWN` until authoritative readback.

**Verdict:** `EXP33_CONCURRENT_CLIENTS_15_OF_15_LOCAL_PASS`; `EXP33_SPLIT_PROCESS_PROVIDER_REPLAY_RECOVERS_WITH_ONE_EFFECT`; `EXP33_TRUE_PARALLEL_MUTATION_AND_INDEPENDENT_AUTHORITY_UNPROVEN`; `FOR007_UNCHANGED`.
