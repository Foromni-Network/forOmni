# EXP-37 — Separate-UID Witness Receipts and Provider Effect Corroboration (Executed Local AAR)

**Executed:** November 25, 2026. **Repo/branch:** `Foromni-Network/forOmni`, `research/global-agent-roadmap-execution`. **Result:** **12/12 Python unittest tests PASSED in one uninterrupted run**, 18.063 seconds, under `-W error::ResourceWarning`; zero final warnings or errors. No real provider or customer, Internet Embassy changes, production deployment, protected merge or FOR-007 modification.

## Research question

Can a **separately running Unix-UID witness** keep a private signing key and durable SQLite receipts while a verifier compares signed witness claims against the hardened EXP-36 broker/provider's exact mock effect IDs, tasks, projects, and resources? Does the verifier catch a plausible signed-but-false completion claim?

## Implementation

EXP-36's `base_exp31.py` and `service36.py` were copied **byte-for-byte**. The broker (UID **21631**) and mock provider (UID **21632**) operate distinct Unix socket services and separate SQLite databases; two test-authorized workers use UIDs 21633/21634.

New `witness.py` creates another actual AF_UNIX service under UID **21636**, with its own SQLite receipt database and owner-only 0600 Ed25519 private key. It authenticates the submitting **root test coordinator UID 0** using `SO_PEERCRED`. Receipts sign the canonical JSON tuple (checkpoint, effect_id, task, project, resource), are durable over witness restart, reject a conflicting second payload with the same checkpoint ID, and recognize identical repeats.

The *coordinator/verifier* validates the witness signature with only its public key, then obtains separate provider-authoritative **mock** state via a freshly signed `receipt.read` grant through the EXP-36 broker/provider path. It reports `CORROBORATED` when that provider finds the exact tuple, otherwise `PROVIDER_MISMATCH`.

**Crucial distinction:** The witness signs **a claim delivered by the coordinator**; it does not independently query or observe the provider. The verifier's readback is conducted by the same coordinator that controls issuer and witness keys. Thus, this is source separation and controlled reconciliation, **not independent eyewitness evidence or trust custody**.

## Actual test outcomes

Command:
```bash
cd foromni_exp37
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_exp37.py
```
Output: `Ran 12 tests in 18.063s; OK`.

1. Broker, provider and witness have three distinct actual Unix UIDs/PIDs.
2. Ordinary worker UID cannot read witness private-key file.
3. Worker UID denied direct witness IPC.
4. Authorized mock effect is attested and independently matched against provider receipt.
5. **Signed false effect claim** is detected as `PROVIDER_MISMATCH`.
6. Existing effect with **wrong task claim** is detected as `PROVIDER_MISMATCH`.
7. Modified signed receipt fails Ed25519 verification.
8. Conflicting payload at same checkpoint ID is rejected as `FORK`.
9. Identical repeated checkpoint returns `DUPLICATE`.
10. Witness process kill/restart preserves checkpoint receipt.
11. Missing provider effect remains uncorroborated.
12. **Negative control:** Coordinator can get a fully valid witness signature over a fabricated claim; only provider comparison exposes the falsehood.

A passing negative-control test means a weakness was reproduced, not that full security assurance is achieved.

## Reproducible source and checksums

Exact runnable source, test, README, final log and SHA256SUMS are in the conversation evidence artifact **`foromni_exp37_witness_evidence.zip`**, with ZIP SHA-256 `eeae692719d235334dde7d78e09275c427441c66faea52aeebf5ff5463656e5e`.

| File | SHA-256 |
|---|---|
| `base_exp31.py` | `e37675a9d2a65bda6db2bf08de071582207b181206dca32d70d7a6da0a716db0` |
| `service36.py` | `d890bc76abafda8dd617c9f0c18ad3a00b24caf071e3c4807942dbdbd535e0bb` |
| `witness.py` | `152d2813527aaf09b3b0ad208ef19bc29fdfec238a60393a1ab609b73583dfb2` |
| `test_exp37.py` | `464c7a6bac1144fdbb7f2fb4ffd3e46902cdeda138d9d72f7a6cda9c5a4a98da` |
| `README.md` | `407d88ca70d5d47e9c249b4afec5298f13f9ae6cbf0561a4d29d9759fa9a34db` |
| `test_output.txt` | `c97d72293c586bbe4be3c518bfe030e971dd3eceabdae1e4b290694c794f3b49` |

**GitHub disposition:** AAR/report only is committed, not executable source or independent CI.

## Explicit security gaps

- Root fixture operator owns both signing keys and all ledgers; keys are process-isolated but not independently administered.
- Witness has no direct provider observation and makes **no independent truth claim** about execution. A fabricated signed claim passes witness checks.
- The coordinator obtains all signed read grants itself; the grant issuer is not a separate independently administered task owner, so this is not real authorization.
- Witness Unix socket is fixture mode **0666**, protected by peer UID only, without suitable production socket path/DAC hardening, replay budgets, quotas or robust policy controls.
- One witness, **not** EXP-25/26's 2-of-3 quorum; no authenticated distributed consistency, missing-tail anchors, actual remote effects, external provider custody, root compromise defense, real MCP SDK, source-bound independent QA or real-world SIEM accuracy.
- No tested failure of provider returning a misleading but valid `FOUND` record; exact mock effect DB still under the same root coordinator.

## Next research gate

**EXP-38:** move corroboration into a *separately administered* observation service or at least another isolated UID with its own verified client-side access. Introduce durable signed provider effect receipts, independently anchored witness checkpoint heads, and explicit `UNCONFIRMED` for unavailable provider or absent witness. Simulate withheld provider entries, witness lag, signed fake completion, and coordinator tampering with its own local status. Retain strict consent and no external scanning. Separate reviewer-authored cases are required before claiming independent security assurance.

**Verdict:** `EXP37_SPLIT_UID_WITNESS_12_OF_12_PASS`; `WITNESS_FALSE_CLAIMS_CAUGHT_BY_MOCK_PROVIDER_READBACK`; `FULL_INDEPENDENT_WITNESS_CUSTODY_AND_REAL_PROVIDER_TRUTH_UNPROVEN`; `FOR007_UNCHANGED`.
