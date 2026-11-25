# EXP-23 — Split-UID Ed25519 issuer checkpoints and monitor ledger rollback: executed local AAR

**Date:** 2026-11-25. **Project:** Foromni only; `research/global-agent-roadmap-execution`. **Status:** executed Python/Linux experiment, 18/18 unittest checks PASS, with ResourceWarnings elevated to errors; no warning or final failure. This report is research evidence, not an integrated production security component. Frozen FOR-007 and Internet Embassy unchanged; no client engagement, external API calls, paid testing or protected merge.

## Question and hypothesis

Following EXP-22's shared-parent fixture HMAC keys and unanchored event checkpoints, can a local **asymmetric Ed25519** checkpoint protocol validate an issuer's durable sequence chain from a distinct unprivileged monitor process that cannot read its private signing key? Will comparison with a separate issuer ledger detect monitor deletion/rollback? Does an attacker controlling the source ledger still evade detection?

**Prediction:** public-key verification works across distinct Linux UIDs, tampering and replay fail, monitor rollback is flagged against still-preserved source records; source-ledger truncation and valid-key falsification remain intentionally reproduced negative controls.

## Actual implementation and execution

- `checkpoint.py`: Python `cryptography` Ed25519 key generation, canonical JSON signing of `{seq, prior, value}`; `value` hashes count/previous checkpoint data; issuer SQLite `checkpoints` table and separate monitor SQLite `accepted` table. Monitor only needs public key. Exact monotonic sequence and previous-hash checks are applied on insert. `audit()` compares all records from the separate local SQLite files.
- `signer.py`: isolated subprocess signs checkpoint using issuer-owned private key/database.
- `verifier.py`: isolated subprocess verifies a record with the *public key* and appends to monitor database.
- `test_experiment.py`: 18 deterministic positive/negative tests. Distinct synthetic operating-system identities **UID 21114 for signer** and **UID 21115 for verifier**. Test coordinator is root and creates *all* artifacts, so this is not an independent administrative or root-compromise boundary. Files are in temporary directories.
- First run exposed unclosed SQLite connections and signer journal-directory permissions; fixed via explicit database closing and per-role writable paths. After adding the distinct-UID verifier test, **final reproducible run is clean**.

```bash
cd foromni_exp23_checkpoint
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py
```

Observed: `Ran 18 tests in 3.177s; OK`.

## Test observations

| Category | Result |
|---|---|
| Two valid signed linked checkpoints | accepted |
| Fresh DB connections across monitor reconstruction | sequence resumes |
| Replaying signed record | denied |
| Tampered signed digest | denied |
| Signature from different Ed25519 key | denied |
| Skipped checkpoint sequence | denied |
| Missed tail checkpoint detectable against issuer source ledger | detected |
| Delete one or all monitor records | detected against intact issuer |
| Modify monitor record | divergence detected |
| Signer private key read attempt from separate monitor UID | denied by OS DAC |
| Signer subprocess as distinct UID can issue | accepted |
| Verifier subprocess as distinct UID can accept using public key only | accepted |
| Repeated old checkpoint after restart | denied |
| **Negative: no source checkpoint consulted** | withheld tail unobservable |
| **Negative: issuer with valid private key signs fictitious event count** | false signed claim accepted |
| **Negative: source/issuer ledger itself truncated** | monitor/source can appear consistent despite hidden tail |

All 18 test methods pass. In negative cases a passing test **means the vulnerability was reproduced**, not security guarantee.

## Reproducible exact source and checksums

Local evidence file: `foromni_exp23_checkpoint_evidence.zip`; ZIP SHA-256 `2dee22e2e947559a0c89d1849db4cb5223d6b50e2ad5ebfaa4113fc414678059`. It contains exact source, README, `test_output.txt`, and `SHA256SUMS`.

| File | SHA-256 |
|---|---|
| `checkpoint.py` | `1180749e788e13796a78b72aa362a598c7c4721a21a300be1bdc32e05551856d` |
| `signer.py` | `de3f373a6ba91d0ca681dba29863272fdd8c57ee1c8996b0fc2cf0a923dda98a` |
| `verifier.py` | `615eb2ec2e9aa8d6af0d6766708c242f10655231eaf37175d880e987d52f1027` |
| `test_experiment.py` | `1adc46f67fde1e51132da8add4157e53086933125eb744969f370562f07ea332` |
| `README.md` | `83e1d98b9f996672d14adf5ae0e5f0e23e85d0decf6da5b5f4804a28193f7c08` |
| `test_output.txt` | `99454cced9cd1be40d1f4c703b6ebef0aff78ef8a4644f18cc6d0b21ca5ac05f` |

This GitHub commit includes **the research report only**; source remains in the downloadable evidence ZIP and has not been merged or CI-tested in the GitHub repository.

## Critical limitations and subsequent gate

1. An Ed25519 signature demonstrates possession of an issuer key, **not actual provider effects, task authorization, owner signoff or factual truth**. The fixture root coordinator may fabricate, delete or rewrite both ledgers.
2. A *separate local source ledger* is not a durable externally trusted anchor. If a privileged attacker truncates the issuer ledger, `audit()` can return `CONSISTENT` for a monitor missing that same tail. Need append-only externally witnessed checkpoints, receipts or remote verifier with independent administration.
3. `value` hashes fixture event counts and prior values. It is not Merkle proof over actual provider receipts. No real provider reconciliation from EXP-22 is integrated in this particular experiment.
4. No independent evaluator/source custody, automatic key rotation, pinning of trust roots, revocation, crash-safe atomic external publish, unique epoch/nonces, bounded out-of-order reconciliation or distributed split-brain handling.
5. Tests run on disposable root-capable Linux with `cryptography` library; actual package signature/audit semantics, secure key storage and OS privilege separation require independent expert review.
6. Failure modes beyond tested cases (host compromise, advanced Unix FD passing, network egress from EXP-15, actual MCP, real provider crash-after-effect) are not solved.

**EXP-24 suggestion:** prototype an **independently witnessed checkpoint receipt** with a separately owned trust store or mock external transparency witness. Check rollback/deletion of issuer and monitor simultaneously, forked checkpoint chains, key rotation, false claims vs separately reconciled mock provider effects, and verifier source binding. Keep all test assets synthetic and explicitly delineate which failures are still impossible to detect.

**Verdict:** `EXP23_ED25519_SPLIT_UID_18_OF_18_PASS`; `EXP23_MONITOR_ROLLBACK_DETECTABLE_WITH_INTACT_ISSUER`; `EXP23_SOURCE_TRUNCATION_AND_SIGNED_FALSE_CLAIMS_DEMONSTRATED`; `PRODUCTION_IMMUTABLE_AUDIT_UNPROVEN`; `FOR007_UNCHANGED`.
