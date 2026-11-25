# EXP-32 — Concurrent Admission, Revocation Ordering, and CAS State Transitions (Executed AAR)

**Date:** 2026-11-25. **Scope:** Foromni research branch `research/global-agent-roadmap-execution`, disposable local Python experiment. **Executed result:** 24/24 unittest cases passed in one run (0.219 s), under `-W error::ResourceWarning`, with no warnings or failures. The frozen FOR-007, IE, protected branches, external services and production were not touched.

## Question and concrete findings

After EXP-31 fixed pre-authentication admission, can multiple workers racing on one effect ID produce one mock effect, while grant revocation and late response handlers do not corrupt the recorded outcome? Can a separate signed read-only grant recover a historical effect after original grant expiry/revocation?

**Implementation:** `engine.py` defines a demonstration Ed25519 grant verifier, SQLite transactional `BEGIN IMMEDIATE` admission/effect/revocation checks, a `version` field with status compare-and-set (CAS) transitions, and a distinct `receipt.read` recovery route. `test_experiment.py` runs 24 positive and intentionally insecure negative-control tests.

**Run:**
```sh
cd foromni_exp32_concurrency
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py
```

**Observed:** `Ran 24 tests in 0.219s; OK`.

## Key observations

- 24 simultaneous requests using 12 Python threads for the **same** signed effect ID returned exactly **one `APPLIED` and 23 `DUPLICATE` results** from the mock provider ledger.
- 24 parallel admission calls for the same ID created **one `PENDING` row**; two conflicting admission bindings yielded one `PENDING` and one `CONFLICT`.
- Invalid signature did **not** create an attempt row. Separate valid effect IDs could both commit.
- Explicitly ordered revocation before provider commit denied mutation; effect commit before subsequent revocation left a historical record but denied a new attempt.
- A terminal `CONFIRMED` row refused a delayed `UNKNOWN` overwrite; `UNKNOWN` could transition to `CONFIRMED`; `DENIED` remained terminal.
- A fresh signed read-only grant found a historical record after original mutation expiry/revocation. Wrong scope and expired receipt-read grants failed.
- Restarting the Store object preserved the SQLite state; unresolved `PENDING` and `UNKNOWN` were *not* taken as effect confirmation.
- **Negative control:** experimenter with the private fixture owner key can mint arbitrarily signed task claims. Test pass documents this weakness, not real owner authenticity.

## 24 test method groups

1–2 basic admission and invalid-grant fail-closed behavior; 3–6 24-way admission/effect concurrency and collisions; 7–10 forced revocation ordering; 11–14 legal state transitions and missing rows; 15–18 read-only recovery with revoked/expired grants and scope isolation; 19–20 persistence and unknown-outcome caveat; 21–22 key-custody/common DB negative controls; 23 expired recovery grant denial; 24 competing admission with one effect ID.

## Exact reproducible evidence

Download artifact: `foromni_exp32_concurrency_evidence.zip` (SHA-256 `e7c30ea432e7d11dec69b6e64f9b861154c8f5f8f885abe7fbc800acf4d4e15c`). Includes runnable code, README, exact test output and SHA256SUMS. **Only this AAR is committed to GitHub; source/testing lives in the conversation archive**.

| Artifact | SHA-256 |
|---|---|
| `engine.py` | `195fa3aef0759d3715647055a1225946906be8893b650a20a2c8843cd0db6fd4` |
| `test_experiment.py` | `bcfb2037438a7dddb5d0295a9b0a6476e578e9d938c917ebcfd17dc1fc75a8f8` |
| `README.md` | `7cf786a53f3000b430238740d7482f0d559cd8026d2ce994aaccd9f93d7589fe` |
| `test_output.txt` | `bf09f5e23c0e152e5fd18471828ffcf0dac81b27bdea1e16b96b447e0ba15442` |

## Crucial limitations

- **Single local SQLite trust domain:** the mock broker attempts and mock provider effects are in the *same SQLite database*. Unlike EXP-30, this experiment does **not** show distributed or external-provider idempotency, two-phase remote recovery, or separate-UID IPC. Local DB atomicity cannot establish remote side-effect exactly-once behavior.
- **Concurrent scheduling is limited:** 24 threads exercise SQLite serialization and real races but not separate machines or all possible interleavings. The explicit revoke-before/after tests fix event order; no generalized linearizability proof or revocation concurrent with a real remote call.
- **Fixture owner authority:** one test author generates both signing key and sample grants; the `revoke` method is called directly by tests without authenticated administrative identity. A signer with the key can authorize fabricated tasks.
- **No independent QA:** author of code also wrote tests; no external reviewer, GitHub CI, fuzzing, threat model review, cost budget, protected branch integration or real MCP/AI-agent interface.
- **Grant and historical record semantics:** repeated already-committed effects after revocation return `REVOKED`, not `DUPLICATE`; they remain discoverable only using separately authorized `receipt.read`. That is deliberate fail-closed behavior, but production requires explicit human-facing recovery contracts.
- **Not complete security:** no independent key custody, root compromise mitigation, immutable audit witness, network confinement, realistic provider failure or side-effect uncertainty.

## Next gate: EXP-33

Integrate the concurrent admission/CAS controller with EXP-30's **separate-UID and separate-database mock remote provider**, test concurrent crash-after-effect and revocation race using actual IPC, require an authenticated owner/control-plane revocation grant, and reconcile unknown outcomes using provider readback with a distinct read-only permission. Then have an independent QA author devise negative-case fixtures and source-bound test evidence before contemplating security services.

**Verdict:** `EXP32_LOCAL_CONCURRENT_SQLITE_24_OF_24_PASS`; `REVOCATION_AND_CAS_STATE_TRANSITIONS_REPRODUCED`; `REMOTE_CONCURRENT_EFFECT_TRUTH_AND_INDEPENDENT_OWNER_AUTH_UNPROVEN`; `FOR007_UNCHANGED`.
