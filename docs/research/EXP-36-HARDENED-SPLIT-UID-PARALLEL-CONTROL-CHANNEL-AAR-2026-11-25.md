# EXP-36 — Hardened Parallel Provider With Separate Test-Control Channel: Executed Research AAR

**Date:** 2026-11-25. **Project:** Foromni-Network/forOmni; branch `research/global-agent-roadmap-execution`. **Status:** 17/17 unittest tests passed in **one uninterrupted local run** (`Ran 17 tests in 29.405s; OK`, ResourceWarnings treated as errors). No FOR-007 modification, Internet Embassy access, protected merge, real remote provider, production deployment or paid external testing.

## Research question

Can EXP-34's concurrent separate-UID worker/broker/provider testing be combined with EXP-35's restricted worker-facing service and historical read-only receipt recovery, while keeping test-only concurrency controls off the worker socket?

## Implementation and actual evidence

Exact Python source and tests are included in `foromni_exp36_hardened_parallel_evidence.zip` distributed in the research conversation; **this GitHub commit is an AAR only, not executable source integration**. Uses EXP-31 `base_exp31.py` byte-identically and extends EXP-35 `service35.py` into `service36.py`.

- Provider UID **21632** and broker UID **21631** run actual threaded AF_UNIX socket services with separate SQLite ledgers. Two authorized workers use UID **21633** and **21634**, with unauthorized UID **21635** denied.
- Worker-facing service rejects `stats`, `gate`, `admin`, `proxy.connect`, and `revoke` operations.
- A **separate test-only controller AF_UNIX socket**, verified by `SO_PEERCRED` against root coordinator UID **0**, permits `stats`, `gate` and a grant-signed fixture `revoke`. Workers cannot invoke it.
- Provider SQLite `BEGIN IMMEDIATE` makes revocation lookup and mock effect insertion one local transaction. Gate can hold a request **before entering the transaction**, establishing a reproducible revoke-before-commit schedule. Service request handlers overlap; SQLite write transactions serialize.
- A separately signed `receipt.read` grant can retrieve a prior mock effect after its mutation grant is revoked; the read route is not authorized to mutate.

Final reproducible command (root-capable disposable Linux + Python cryptography + unused fixture UIDs required):
```sh
cd foromni_exp36
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py
```

**Actual result:** `Ran 17 tests in 29.405s; OK`. First integrated attempt had a failed overlap assertion due to worker subprocess startup latency and later timed out; the test polling window was corrected. Isolated 2-test and 3-test reruns passed, then **all 17 ran together** successfully.

## Observed checks

1. Distinct real provider/broker UIDs and PIDs.
2. Worker UID 21633 permitted scoped mock mutation.
3. Worker UID 21634 permitted scoped mock mutation.
4. Unauthorized UID 21635 denied at broker.
5. Worker cannot contact provider directly.
6. Ordinary worker requests for diagnostic/proxy ops rejected.
7. Unauthorized client of test-control channel rejected by peer UID.
8. Local root coordinator can inspect test-only stats.
9. Tampered grant rejected before effect.
10. **12 parallel same-effect requests** via both worker UIDs produced exactly one `APPLIED`, eleven `DUPLICATE`, one committed mock effect.
11. At least two provider request handlers simultaneously active while a test gate was held; four distinct effects committed after release.
12. Revoke sent through signed test-controller route before transaction admission caused queued effect to return `REVOKED`, zero committed effects.
13. Previously applied effect remained recoverable via a distinct `receipt.read` grant after revocation.
14. Missing receipt lookup returned `NOT_FOUND`, zero effects.
15. Mock provider direct ledger readback showed no fabricated effect ID; **not an independently witnessed/audited result**.
16. **Negative control:** test owner private-key holder minted a valid-looking fictional task; action applied, so signer custody/owner authenticity is unproven.
17. Ordinary worker cannot revoke through its broker.

## Exact artifacts

`foromni_exp36_hardened_parallel_evidence.zip` SHA-256 `b712d2a58728e6d9a5b73a829fca89a4372fcf25b328e5c3e6afcaae56f2a3e7`.

| Artifact | SHA-256 |
|---|---|
| `base_exp31.py` | `e37675a9d2a65bda6db2bf08de071582207b181206dca32d70d7a6da0a716db0` |
| `service36.py` | `d890bc76abafda8dd617c9f0c18ad3a00b24caf071e3c4807942dbdbd535e0bb` |
| `test_experiment.py` | `dbddc624b86878e0b93e9ccdc0df97b0d127e89e454926a6da9f815afdd23773` |
| `README.md` | `6c7872ae7b5fddaf08be8e675fe1e745e5ce185a9aa78b26c8bad20002156a45` |
| `test_output.txt` | `c4813ede9036e589782963c76f285ab0bf922e2713b62949733fab8b8ea68f47` |

## Safety and scientific limitations

- The controller socket **file mode is 0666** for this disposable fixture, with authorization at `SO_PEERCRED`. This is insufficient for defence-in-depth; path permissions, a separately allocated controller UID and secure initialization would be needed.
- Root test coordinator owns all keys, services, databases and permissions. Genuine independent owner authority, legal signing consent, root compromise resistance, key vault custody and secure grant revocation remain unproven. An actual unauthorized-but-allowed UID or leaked FD could bypass the intended client gate.
- The separate test controller includes a signed `revoke` fixture method; this is not a production administrative role.
- Concurrency is real at request-handler level, but provider SQLite writes are serialized by a local transaction. A controlled gate establishes only selected race orderings, not linearizability for arbitrary schedules or external providers.
- **No independent witness integrated:** the evidence check directly queries the mock provider SQLite ledger; EXP-25–27 witnesses are separate experiments, not in this run. There is no signed independent checkpoint or protected external trust root.
- No actual external APIs, cost controls, independent red-team reviewers, GitHub CI, source-bound QA, network namespace protection, malicious supply chain examination, or production readiness.

## Next bounded research milestone

**EXP-37:** integrate a separate mock witness service with distinct OS UID and private key, restrict its IPC and receive provider-authoritative exact effect IDs through separately authenticated readback. Require the signed witness checkpoint to correlate with actual effects, and test false claims, lost witness receipts, witness restarts and mismatched task IDs under approved test scopes. Then obtain a truly independently authored challenge set before public assessment-performance claims.

**Verdict:** `EXP36_SPLIT_UID_HARDENED_PARALLEL_17_OF_17_PASS`, `EXP36_CONTROL_PLANE_SEPARATED_FROM_WORKER_SOCKET`, `EXP36_REVOCATION_ORDERING_AND_HISTORICAL_READ_LOCAL_PASS`, `INDEPENDENT_WITNESS_AND_OWNER_CUSTODY_UNPROVEN`, `FOR007_UNCHANGED`.
