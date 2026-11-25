# EXP-40 — Split-UID Signed-Grant Provider, Witness, Anchor and Observer IPC (Executed Research AAR)

**Date:** 2026-11-25. **Repository:** Foromni-Network/forOmni, branch `research/global-agent-roadmap-execution`. **Result:** 15/15 local Python unittest checks passed in **one uninterrupted run** (`Ran 15 tests in 32.008s; OK`), with ResourceWarnings treated as errors. No FOR-007 or Internet Embassy source changes, protected merge, real provider API, paid assessment, deployment or external probing.

## Hypothesis and design

EXP-39 combined signed grants, signed provider effects, witness checkpoints and anchored heads, but in one Python process. Can that protocol work through real AF_UNIX IPC and multiple Linux OS identities while preserving the same fail-closed outcomes?

**Implementation:** Exact EXP-39 `protocol.py` is copied to `protocol39.py` (byte-identical SHA-256). New `service.py` runs distinct real socket services with UIDs 22141 **provider**, 22142 **witness**, 22143 **anchor**, 22144 **observer**. Test authority uses UID 22140 as a separate subprocess caller. Each service owns its own SQLite DB and role-specific Ed25519 private key; public keys are available for verification. `SO_PEERCRED` restricts incoming operations by expected UID. The root test coordinator generates/retains all signing keys, starts processes and controls the files—**process separation is not independent administration**.

The provider verifies the signed task/project/effect/action/expiry grant prior to local SQLite effect insertion and signs the exact receipt. Witness signs an exact effect-ID-list checkpoint submitted by authority; anchor verifies witness signature and stores a signed expected head; observer independently queries the other services, validates signatures, and crosschecks provider effect IDs with the signed witness list and anchored digest. The observer does *not* have provider/witness/anchor signing keys.

## Reproducibility

Archive `foromni_exp40_split_uid_evidence.zip` contains exact executable source, test, README, final log and SHA256SUMS, SHA-256 `e57cc5f2bc20ca27ae2692606ca76f91b0a25af02efac0e6b25c6cd3946d7167`.

```sh
cd foromni_exp40
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py
```

Requires **disposable root-capable Linux**, Python `cryptography`, unused synthetic UIDs 22140–22144, and AF_UNIX. The test creates test-only sockets mode 0666 under a shared directory mode 1777, relying on `SO_PEERCRED` for tested operation authorization. **These filesystem permissions are intentionally unsuitable for deployment.**

**Observed final run:** `Ran 15 tests in 32.008s; OK`. The first run revealed a readiness-probe bug: a connect-and-close without request caused `BrokenPipeError` at response send and killed a service. Fixed the fixture server to handle disconnected clients, then reran 14/14 clean and added the final pair of more discriminating failure tests; final complete run 15/15 clean. Service startup path permissions also required a dedicated shared temporary socket directory.

## 15 observed cases

1. Four distinct service UIDs/PIDs.
2. Observer UID cannot read provider private signing key.
3. Authority UID valid signed grant produces one mock provider effect.
4. Invalid grant denied; observer UID cannot invoke provider mutation.
5. Authority UID cannot use observer-only provider receipt read; observer UID can.
6. Authority creates witness checkpoint and publishes anchor; observer returns `CORROBORATED`.
7. A newly committed provider effect omitted from anchored witness list produces `PROVIDER_MISMATCH`.
8. Witness rejects conflicting checkpoint revision; anchor refuses invalid witness signature.
9. Witness and anchor services restart with durable stored checkpoint/head intact.
10. Updated checkpoint and head restore successful `CORROBORATED`.
11. Provider unavailable: observer does not return `CORROBORATED`.
12. Unexpected UID cannot call observer reconciliation.
13. Deleted witness record while newer anchor retained: `MISSING_WITNESS`.
14. Witness restored but provider record deleted by privileged coordinator: `PROVIDER_MISMATCH`.
15. **Negative control:** shared root coordinator can read every role's 0600 signing-key file, and therefore can rewrite claimed authority/trust roots.

**Passing negative controls demonstrate open vulnerabilities, not guarantees.**

## Exact local source hashes

| File | SHA-256 |
|---|---|
| `protocol39.py` | `eb5b7404e4064198bb350a9bd5b614a9e8d7aa649fbf68d71d963c78c5d2c233` |
| `service.py` | `7576a0c2a90bd236d0ec29a49f9b4e71a26544d302699bc62da393be5dfbf6fb` |
| `test_experiment.py` | `6aee0f445e57042cc5f6d7e7919ec08e9393022f0a3038387b38dd717fd7f152` |
| `README.md` | `17012aca9f49ebfb58d5299e9f43227d8a43734e3e1c9fb46e470ee64f30b26e` |
| `test_output.txt` | `776e28c0ce8aac6753ff20af8acff179a4f09235ff3847f3cf7cc12699f89158` |

**Artifact disposition:** this GitHub commit is the executed AAR **only**. The executable code and actual logs are in the downloadable conversation archive, not merged into the main Foromni application or verified by GitHub CI.

## Security and operational limits

- All signing keys, owner identity and four SQLite ledgers administered by one root process. Independent administrative custody, immutable remote anchor and true third-party provider truth not demonstrated.
- The witness accepts the authority's claimed effect-ID list rather than observing provider operations. A malicious authorized authority may cause a signed-but-false checkpoint. Observer compares with provider, whose database is itself controlled by the same root user.
- Provider receipt readback is restricted only by observer UID, **not** per-task read-grants or privacy policy. No customer/tenant privacy controls, costs, revocation, admission budgets, key rotation or authenticated external source binding.
- Services use **sequential** socket accept loops; true threaded/multiprocess parallelism and revocation race behavior from EXP-36 were *not* carried forward. Sockets use insecure 0666 mode; a leaked authorized UID/FD or root defeats the local gate.
- Observer outcome may remain unconfirmed without correct and complete events/anchor history. Anchoring signed lists does not prove missing events before anchor publication.
- No independent QA, malicious service compromise, external networking, crash-after-remote-effect, protected release or verification against real production requirements.

## Next discriminating gate

**EXP-41 candidate:** allowlist the broker/provider caller through securely provisioned private socket directories and scope observer receipt readback to signed, owner-authorized task/project/effect; isolate issuer signing authority; add source-bound independent evaluator tests. Then test that an unauthorized observer cannot enumerate all provider effects and that a compromised authority cannot unilaterally manufacture corroborated outcome without independent provider truth. Reintroduce true parallelism only after a stable minimal security boundary is demonstrated.

**Verdict:** `EXP40_15_OF_15_SPLIT_UID_IPC_PASS`; `SIGNED_AUTH_PROVIDER_RECEIPT_WITNESS_ANCHOR_PROTOCOL_REPLAYED_ACROSS_PROCESSES`; `INDEPENDENT_TRUST_ROOT_AND_PRODUCTION_SECURITY_UNPROVEN`; `FOR007_UNCHANGED`.
