# EXP-24 — Witnessed signed checkpoint chains, rollback/fork detection and mock provider corroboration

**Date:** 2026-11-25. **Scope:** Foromni research branch `research/global-agent-roadmap-execution` only. **Result:** 19/19 local Python unittest checks passed with resource warnings treated as errors. No real AINO/IE data, production integration, protected merges, external witness, actual third-party API, paid assessment, or frozen FOR-007 changes.

## Research question

Can a separately retained, Ed25519-signed **witness ledger** detect a checkpoint deleted from BOTH source issuer and monitor, reject a fork that has a valid issuer signature, and distinguish issuer claims from an independently stored mock provider count? What does this demonstrate about real independently trusted transparency witnesses?

## Implementation and execution

This reuses byte-identical EXP-23 `checkpoint_exp23.py` and adds `witness.py`: a third SQLite witness ledger with Ed25519-signed acknowledgement receipts for *each accepted source checkpoint*. The witness verifies source signatures, strictly consecutive sequence numbers and previous source hash. It rejects gaps, duplicate or conflicting checkpoint revisions. The audit compares all witness-validated records against the two local source and monitor ledgers. An additional **third-party-style mock** provider SQLite ledger is queried to compare one checkpoint's **event count claim** against the mock effect count.

The witness/source/monitor keys, data and files are **all controlled by the same disposable local test runner**; the separation is *logical and durable*, not independent operator custody or physical/OS isolation. The mock provider is also local and trust-controlled by the same experimenter.

Reproduce from evidence ZIP:
```
cd foromni_exp24_witness
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py
```
**Observed:** `Ran 19 tests in 0.395s; OK`.

## Test observations

- Normal two-checkpoint signed witness chain accepted and independently compared to issuer and monitor.
- Repeated identical checkpoint returns `DUPLICATE`, conflicting signed revision returns `FORK_OR_REPLAY`.
- Incorrect source signature, skipped sequence and modified witness signature/hash are rejected.
- Missing/deleted/mutated issuer records detected **against intact witness ledger**.
- Missing/deleted/mutated monitor records detected **against intact witness ledger**.
- Issuer AND monitor truncated to the same prefix: `ISSUER_ROLLBACK` detected against intact witness.
- Witness head survives reopening SQLite database in the same test process.
- A valid signature over a deliberately false event count can be accepted absent provider corroboration (**negative control**).
- With a separate mock provider ledger, mismatched event count is flagged; matching count is corroborated, but no proof of individual event identities.
- **Negative control:** if no witness anchor exists, rollback is not detectable.
- **Negative control:** an actor with both signing keys and write access to all three ledgers can replace an old chain with a new, internally consistent and fully signed history.

**Passing negative-control tests reproduce unsafe conditions.** There is no assertion of production authenticity, immutability, general threat coverage or correctness of provider state.

## Evidence: local source plus checksums

Runnable code, tests, README, exact final test output and hashes: `foromni_exp24_witness_evidence.zip`. SHA-256 archive: `7404a7f2f94ee51dedf85ce5711534cad432bc65ece1bd2b6951cc621f16794d`.

| File | SHA-256 |
|---|---|
| `checkpoint_exp23.py` | `1180749e788e13796a78b72aa362a598c7c4721a21a300be1bdc32e05551856d` |
| `witness.py` | `a72cc7066ef210716e27b78e44cc7d0b20ce122a3034fd1186b367edcba41ff5` |
| `test_experiment.py` | `f45085c854fb1ac54eb2f8eca50f8bd4eab7a2be125c3b43f867d2fecb979a7a` |
| `README.md` | `f7ad42b01c8866e6a53151205c8b4f070e9755ecb97a09b60ddcf164ac171ba1` |
| `test_output.txt` | `f19ed4c115c250746b3d7a75606ed35a560f0ebec2470b22cb8d9557704828a8` |

**GitHub disposition:** this report is a research commit; exact executed code resides in the conversation ZIP, not integrated source or CI.

## Limitations and next experiment

Ed25519 signatures establish possession of a key, not event truth. The witness must live under a **separately administered, failure-independent** security principal and append-only or third-party transparency system, with pinned trust roots, external anchor availability and validation against authoritative provider receipts; none were supplied here. Single-count mock reconciliation is insufficient to validate unique effects, deleted effects, approvals or true event completeness. No remote network partitions, key rotation, durable independent signer process, fork gossip, malicious witness, outside auditor, source-bound independent QA or real provider readback.

**EXP-25 candidate:** simulate multiple mutually independent witness opinions and a separately controlled external anchor/checkpoint publication protocol, test equivocation/fork detection across witnesses, unavailable witnesses, delayed delivery and source rollbacks; bind exact provider effect IDs rather than event counts. Treat a failed witness quorum as **unconfirmed**, not evidence of safety. Consider hosted transparency systems only after explicit authorization, real security review and cost assessment.

**Verdict:** `EXP24_LOCAL_WITNESS_19_OF_19_PASS`, `EXP24_DUAL_LEDGER_ROLLBACK_WITH_INTACT_WITNESS_DETECTED`, `EXP24_SIGNED_FORK_REJECTED`, `EXP24_EXTERNAL_INDEPENDENCE_UNPROVEN`, `FOR007_UNCHANGED`.
