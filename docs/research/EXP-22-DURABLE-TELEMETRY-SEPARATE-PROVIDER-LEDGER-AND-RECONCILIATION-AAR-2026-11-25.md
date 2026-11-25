# EXP-22 — Durable signed telemetry, separate mock provider effect ledger, replay/reordering, and reconciliation: executed AAR

**Date:** 2026-11-25. **Repository:** Foromni-Network/forOmni, research branch `research/global-agent-roadmap-execution`. **Scope:** local synthetic research, not deployable security engineering. **Outcome:** `18/18 unittest checks PASS`, no ResourceWarnings under warnings-as-errors. Frozen FOR-007, production services and Internet Embassy unchanged.

## Research question

Can EXP-21's signed telemetry be made durable across monitor restart and correlated with a **separately stored mock provider effect ledger** to discover effect events missing from the log, impossible completion claims and unordered/duplicate deliveries? What remains invisible even when these controls pass?

**Prediction:** the persistent monitor will reject tampering/replays, buffer out-of-order but valid events, restore issuer watermarks, flag provider effects with no broker grant or signed event, and detect a withheld tail only if a separately asserted high-water checkpoint exists. The experiment deliberately tests negative boundaries.

## Test implementation

Exact Python sources/test outputs in accompanying `foromni_exp22_durable_evidence.zip`. The experiment combines:

- EXP-21 `telemetry_exp21.py` (byte-identical source) for HMAC-SHA256 demonstration event signing. Distinct broker and provider fixture keys, **both controlled by the test parent**.
- `durable.py`: two SQLite files. Monitor ledger stores signed event JSON, unique issuer sequence and event IDs, durable per-issuer next-sequence watermarks and alerts; provider ledger stores mock effect IDs and source-of-truth effect tuple, and optionally a claimed issuer high-water checkpoint. Out-of-order signed events are stored, with watermarks advanced once missing predecessors arrive.
- `producer.py`: broker/provider signing test subprocesses with different per-role injected environment keys. They are separate operating-system **processes**, not separately privileged principals with independently secured private keys.
- `test_experiment.py`: 18 positive/negative checks. Only fake project/task/action data and mock effects, no third-party API or network communication.

Reproduction:

```bash
cd foromni_exp22_durable
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py
```

**Actually observed:** `Ran 18 tests in 1.931s / OK`. This is a deterministic test run; 18 methods are not independent security replications or production attack coverage.

## Observed acceptance cases

1. Correct grant→effect→complete agrees with mock provider ledger.
2. Broker and provider event signing occurs in two distinct test subprocesses.
3. Monitor reconstruction from same DB preserves watermarks.
4. Signed event replay is rejected after monitor restart.
5. Payload tampering fails signature verification.
6. Signing a broker event with provider fixture key is rejected.
7. Event sequence 2 may arrive before 1; watermark waits then advances when 1 arrives.
8. Internal sequence gap detected using a separately claimed checkpoint.
9. Missing final (tail) event detected using claimed checkpoint.
10. **Negative control:** missing tail event remains invisible with no checkpoint.
11. Provider effect present in its ledger but missing from events is flagged.
12. Provider effect without accepted broker grant is flagged.
13. Signed provider effect claim with no real mock effect is flagged.
14. Provider ledger and signed effect disagree on project/resource tuple; flagged.
15. Broker completion without actual mock provider effect is flagged.
16. **Negative control:** someone with provider demo HMAC key can forge a valid-looking event.
17. Duplicate issuer sequence under a new event ID is rejected as rollback.
18. **Negative control:** local mock checkpoint does not prove an independent, authorized issuer supplied it.

All passing checks describe *test behavior*, not full containment. The three negative controls deliberately confirm open weaknesses.

## Evidence hashes

| File | SHA-256 |
|---|---|
| `telemetry_exp21.py` | `3b65c1c8f5415d3c19b8d674a1c0c868f4b41830027626cf8739cff5fb9b795d` |
| `durable.py` | `6ddd1256ebae1ace53a679946b728eeb8c29f219b70151fb8658aa31839bef7a` |
| `producer.py` | `94de1f6b6fc0d538eb6397bc17288ddd38144b19cf3fad36e5c4ae66e344e3dc` |
| `test_experiment.py` | `12d650bf2066017aa190fe08bb3acaa5422f553173db1a56650486a9a2d18b1c` |
| `README.md` | `5c392d9a5067f59e71b2eec563eb3219e18dc458ff85290a8f2aaa5047562462` |
| `test_output.txt` | `ba0b869456c38e31546facd0670547581d8cd0f60e3fc429e49b0f3650859be1` |
| `foromni_exp22_durable_evidence.zip` | `4d18606b1aa098490a06d9cd46e7c8659123ff334d2c590549e3accbe10d519f` |

**Artifact disposition:** the reproducible source/tests/README/test log/checksums are in the downloadable conversation ZIP. This GitHub change commits the scientific report, not integration of runnable source, and no GitHub CI was executed.

## Critical limitations

- The two ledgers are separate SQLite files but **both created and administered by the same test coordinator**. A privileged attacker could modify both. In a real service, trusted provider readback must not derive from the allegedly compromised monitor.
- The broker and provider are subprocesses but not isolated Linux UIDs or independent hosts, and the parent injects both demonstration HMAC keys. **True independent signer custody remains unproven**.
- The checkpoint is a local asserted integer, not an independently signed and anchored authoritative producer watermark. Without the checkpoint, a missing terminal event remains invisible. Out-of-order events are buffered, but no real bounded-time gap timeout or transport acknowledgement logic exists.
- The broker `grant` is only a correctly signed *synthetic assertion*, not proof of a task-scoped authorization lease checked at provider execution. Effect without grant can be flagged *after the fact* but is not prevented by the monitor.
- Provider effects use SQLite alone; no external provider crash-after-effect case, network partition, token escrow, or independent real provider inventory exists.
- Cryptographic integrity does not prove that an authorized event corresponds to the claimed truth; complicit signing keys can produce lies.
- Events are not chain-hashed or externally anchored; database deletion/rollback by privileged owner is outside the threat model. The fixture does not provide completeness guarantees, a SIEM, alert performance statistics or independent security review.

## Next bounded research gates

**EXP-23:** sign producer-side monotonically increasing durable checkpoints using a separate issuer service or independently controlled fixture, then append immutable reconciliation receipts; simulate deletion/rollback of monitor ledger, checkpoint replay, bounded delayed delivery, and producer restart. Experiment with distinct Linux UIDs and restricted key-file permissions, with explicit caveats about root compromise and owner authority. Treat signed checkpoints as evidence of *issuer claim*, not proof the issuer actually logged every effect.

Follow with a held-out incident-detection corpus and independently authored labeling to evaluate false positives. For a future Foromni security-assessment service, publish reproductions and negative controls without asserting complete event authenticity or detection accuracy.

**Verdict:** `EXP22_DURABLE_TELEMETRY_18_OF_18_PASS`, `EXP22_PROVIDER_RECONCILIATION_DETECTS_MISSING_EFFECT_EVENTS`, `EXP22_SIGNER_AND_WATERMARK_INDEPENDENCE_UNPROVEN`, `FOR007_UNCHANGED`.
