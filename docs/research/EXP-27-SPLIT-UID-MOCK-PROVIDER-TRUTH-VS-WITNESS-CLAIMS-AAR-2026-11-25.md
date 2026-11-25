# EXP-27 — Split-UID Mock Provider Truth vs Signed Witness Claims: Executed AAR

**Date:** 2026-11-25. **Foromni research branch:** `research/global-agent-roadmap-execution`. **Result:** 16/16 checks PASS **in two verified separate batches of 8** using warnings-as-errors. An earlier uninterrupted full-suite run stalled; do **not** represent this as a clean single-run 16-test CI pass. Research only: no FOR-007 change, Internet Embassy modification, third-party API, protected merge, paid customer security assessment or production installation.

## Research question and decisive evidence

Can a distinct Linux UID mock provider with its own durable SQLite effect ledger, reached over a restricted Unix socket, refute false-but-validly-signed and two-witness-confirmed issuer checkpoint claims? Does the witness/provider IPC reject unauthorized local callers through DAC and `SO_PEERCRED`?

**Outcome:** yes within the disposable test fixture. Two witnesses can each accept a cryptographically valid but factually false issuer checkpoint; the verifier returns `CONFIRMED`, **but comparing exact effect IDs/task IDs against a separate provider service readback returns `PROVIDER_MISMATCH`**. The same comparison corroborates a valid claim. Signing/witnessing alone does not prove actual execution.

## Implementation

- `protocol.py`: byte-identical to EXP-25/26 fixture (Ed25519 issuer signatures, witness receipts, SQLite-ledger 2-of-3 verifier, exact provider effect-ID/task bindings).
- `provider_service.py`: independently running mock provider **UID 21135**, separate SQLite ledger, durable idempotent `apply` and `readback`; 0660 group-owned Unix socket, `SO_PEERCRED` rejects callers other than configured client UID 21134, typed JSON operations; no external API.
- `witness_service.py`: three independently running mock witnesses under **UID 21131, 21132, 21133**, individually protected Ed25519 private-key files and durable SQLite ledgers, Unix sockets restricted to group 21140 and authenticated against client UID 21134.
- `test_experiment.py`: root-only disposable test coordinator creates all keys, manages 4 child daemons, pins signer/verifier public keys and starts subprocess clients under UID 21134. The shared coordinator **can** read/rewrite all keys, DBs and policy; this is *OS-level local separation*, **not independent administrative trust**.
- Run only in an authorized disposable root-capable Linux environment with unoccupied synthetic UIDs and `cryptography` installed; do not deploy these services.

## Actual executed test batches

The uninterrupted `unittest -v test_experiment.py` run stalled around test 09 and did not produce a final OK; test 09 passed in isolated rerun. Then two separately logged commands ran tests 01–08 and 09–16 with `-W error::ResourceWarning`:

| Batch | Observed |
|---|---|
| Tests 01–08 | `Ran 8 tests in 29.715s; OK` |
| Tests 09–16 | `Ran 8 tests in 31.754s; OK` |

No ResourceWarnings or failures in these two completed runs. No independently administered CI or third-party QA.

### Verified test cases

01. Four separate OS process PIDs and UIDs verified from `/proc`.
02. One witness UID cannot read another witness UID's 0600 private signing-key file.
03. Typed mock provider apply and actual IPC readback returns effect ID and task ID.
04. Repeated apply is idempotent; same effect ID with different task is a conflict.
05. Provider denies unknown `proxy.connect` operation.
06. Unauthorized caller without configured group cannot connect to witness/provider Unix socket.
07. Caller with matching group but different UID is denied by `SO_PEERCRED`.
08. Valid witness-confirmed source checkpoint corroborated by provider readback.
09. **Negative control:** two witnesses confirm issuer-signed *false* effect; provider readback flags mismatch.
10. Provider has effect not claimed by issuer; reconciliation flags mismatch.
11. Mock provider process restart retains durable SQLite effects.
12. Mock witness process restart retains signed receipt.
13. 2-of-3 quorum works with third witness stopped.
14. One witness receipt is unconfirmed.
15. Valid-signed conflicting same-sequence checkpoint rejected by honest witness.
16. **Negative control:** authorized client can insert an unauthorized-looking mock effect, because provider performs caller UID authentication only and has **no actual task-scoped authorization lease check**.

## Evidence hashes

The conversation archive `foromni_exp27_provider_truth_evidence.zip` contains exact source, README, both completed test logs and SHA256SUMS. ZIP SHA-256: `d26b5b76731ff0c25de40d2e8f05c5af78f8a7706ce18e3ac1a7e1bfd47a0e89`.

| Artifact | SHA-256 |
|---|---|
| `protocol.py` | `9c9ee453460fea262f83323b67703f38267d171f3216e2f09173f08498132432` |
| `provider_service.py` | `73f1af8a84c3529114c0ce11374f5680f55be52eb9f9299c2ddabeab056d3613` |
| `witness_service.py` | `a820fab12ce89d389cc200b612aedd1a62faad9796078f07fc48c70a4e4f6b8e` |
| `test_experiment.py` | `ef57c70fda1508e6ba12bc6032fbfb1bd5251145fce87040de56b309520853ae` |
| `README.md` | `0e97f6d92da7086c67702267b8c4f9f017b55760adb5a825176471bea7d5e588` |
| `batch_1.txt` | `de8ae6bb277001a2f1b7d1fcd05da2f1d26a81ff5f3e636dc31221a96997269e` |
| `batch_9.txt` | `2193cbc45690e69fa1c81e72e80167f384c21d5b3b3e5fd393cc94632ab455e5` |

This GitHub commit stores the AAR. Runnable source/tests are in the conversation archive; **not** integrated with main, hosted in a service, independently reviewed, or exercised by GitHub CI.

## Critical boundaries

**Actual effect source vs narrative:** this experiment proves a separately stored mock provider ledger can disagree with witnessed claims. The provider is still part of a fixture created by the same trusted root process; no third-party source, independent organization, or external fact witness. An authorized client can create arbitrary mock effects; provider authorization remains **missing**. Provider readback is a separate process, not the same ledger as issuer/witness.

**Network/IPС:** Unix socket group permissions and peer UID defend against the two tested local unauthorized clients. They are not complete isolation of a root adversary, leaked access, inherited file descriptors, another Unix service, or network forwarding. The test client UID 21134 is hardcoded for the fixture; no worker task lease or runtime cost policy is implemented.

**Cryptographic truth:** an Ed25519 witness signing a checkpoint only attests to the checkpoint presented. The root operator can replace keys; a client can fabricate mock provider effects. The implementation does not provide authenticated immutable external provider truth, signed owner permissions, key rotation/revocation, independent source-bound QA or complete audit assurances.

## Next useful experiment

**EXP-28:** add a task-scoped owner-issued grant to the mock provider *execution boundary*, with authorized project, action, task, resource, expiry, replay/idempotency and approval scope; ensure the provider rejects unauthorized effects **before** they appear in its authoritative ledger. Keep external checkpoint/witness comparison as independent after-the-fact evidence; test grant revocation and task mismatch across restart, including one crash-after-effect scenario. Require reviewer-independent validation before any commercial readiness claim.

**Verdict:** `EXP27_16_OF_16_CHECKS_PASS_IN_TWO_BATCHES`; `FALSE_WITNESSED_CLAIMS_REFUTED_BY_MOCK_PROVIDER_READBACK`; `OS_UID_AND_PEER_IPC_CONTROLS_VERIFIED_LOCALLY`; `TASK_SCOPED_PROVIDER_AUTH_AND_TRUSTED_EXTERNAL_TRUTH_UNPROVEN`; `FOR007_UNCHANGED`.
