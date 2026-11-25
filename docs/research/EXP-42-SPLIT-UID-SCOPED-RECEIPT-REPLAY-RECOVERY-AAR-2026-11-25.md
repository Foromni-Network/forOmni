# EXP-42 — Split-UID scoped receipt verification and durable replay response (Executed AAR)

**Date:** 2026-11-25. **Repo/branch:** `Foromni-Network/forOmni` / `research/global-agent-roadmap-execution`. **Executed evidence:** 20/20 Python unittest cases passed in one uninterrupted concluding run (`Ran 20 tests in 39.015s; OK`) with `-W error::ResourceWarning`. This is a disposable local research experiment, not production integration.

## Research objective

EXP-40 separated provider, witness, anchor and observer across Unix service identities but allowed broad receipt readback and effect-ID enumeration. EXP-41 narrowed provider reads to task-scoped signed grants, but a single-use read nonce made recovery after lost replies impossible. EXP-42 combines the **four-service EXP-40 IPC workflow** with **task-scoped signed provider receipt reads and durable same-grant replay recovery**.

## Concrete implemented change

Using byte-identical EXP-39 `protocol39.py`, modified EXP-40 `service.py` and authored a new 20-test executable suite:

- Authority UID **22140** issues Ed25519-signed `receipt.read` grant with exact `effect/task/project/action`, expiry, nonce and expected observer UID. Provider UID **22141** independently checks grant signature and scope, serving reads only to observer UID **22144** authenticated by Linux `SO_PEERCRED`. Witness UID **22142** and anchor UID **22143** retain separate processes/SQLite files and signing keys.
- Provider disables the `ids` enumeration endpoint. Observer may query **only effect IDs present in the signed witness checkpoint**, and must obtain a signed read grant for every such effect.
- Provider stores a canonical grant fingerprint and the first JSON read response in its own durable SQLite `read_receipts` journal keyed by nonce. Identical authorized repeats return the exact same response after simulated reply loss or service restart. A reused nonce with another valid grant returns `REPLAY_CONFLICT`. A mutation grant does not authorize a read and a read grant does not authorize mutation.
- Observer verifies anchored witness head and individual provider receipt signatures, returning `CORROBORATED_SCOPED` when all listed effects match. It does **not** make a global-completeness claim.
- Missing read grant yields `UNCONFIRMED_READ_GRANT`, unavailable provider yields an unconfirmed outcome, cross-task/project/effect requests and tampered signatures fail closed.

**Important negative control:** After witness/anchor v1 listed effect E1, a new provider effect E2 was committed but withheld from the witness list. Observer still returned `CORROBORATED_SCOPED` for E1 because enumeration was forbidden. **Global completeness is unproven**, and this explicitly labeled test is a *demonstrated weakness* rather than a victory.

## Tests and exact result

Command, requires root-capable **disposable** Linux container, Python `cryptography` and available synthetic UIDs 22140–22144:

```sh
cd foromni_exp42
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py
```

A first run was interrupted during a later real IPC check. The second **full run completed successfully**: `Ran 20 tests in 39.015s; OK`; no final errors or resource warnings.

The 20 checks cover process UIDs; enumeration denial; missing read grant; read before effect; authorized apply/read; exact same-nonce retry; conflicting nonce binding; cross-project/task/ID denial; expiration; anchored scoped corroboration; missing grant; observer lost-response retry; invalid grant rejection; deliberately undiscoverable extra provider effect; restart; mutation/read action separation; wrong peer UID; provider unavailable; tampered signature; and root trust-key custody negative control.

## Reproducible archive and hashes

Complete runnable source, README, exact final log, and SHA256SUMS are in conversation artifact **`foromni_exp42_scoped_recovery_evidence.zip`**, SHA-256 **`be4487cccc09b17f9113826d95332627c5b0b28c6a3013f50efaa95bac683121`**.

| File | SHA-256 |
|---|---|
| `protocol39.py` | `eb5b7404e4064198bb350a9bd5b614a9e8d7aa649fbf68d71d963c78c5d2c233` |
| `service.py` | `9cd44d0bfd02c6849c6181931d09bc7190637aef29b5b8f1f9413facf8686860` |
| `test_experiment.py` | `bb7b55d9b2402bee0ed1eaf214edd0cb3a28135f1e7532d2f3b56fd50fcd82e2` |
| `README.md` | `6dcad4ea6dc06b2018940bdf13ad8db14dcf441c0ab087c7a17307aabea50fc4` |
| `test_output.txt` | `67522639e9075708f5072b940adb95861f25c215783870fbd50ca150ca0cacce` |

GitHub stores **only this after-action report**. Runnable source/logs are in the attached archive, not checked into the application source or tested by an independent CI system.

## Critical qualifications

1. **Scoped corroboration ≠ complete audit:** disallowing list operations protects receipt confidentiality but makes a withheld-tail effect invisible unless an independently signed aggregate commitment, append-only external ledger or independently established expected count is available. Forensic completeness is not established.
2. **Response caching remains bounded:** identical-grant replay works only while the signed read grant remains unexpired. Cached `NOT_FOUND` never upgrades to `FOUND` under that nonce; issue a fresh authorized grant for a new read. The journal caches responses and protects nonce binding; no distributed exactly-once read guarantee.
3. **Fixture privileges:** socket modes are 0666 in an accessible test directory, relying on `SO_PEERCRED` for the attempted operation checks. Root coordinator controls all issuer/provider/witness/anchor private keys and SQLite databases. No independent provider custody, owner consent or external truth is proven.
4. **Not EXP-36 parallelism:** service socket loops are sequential; earlier parallel process/concurrency and revocation-race features have not been combined into this fixture. No tenant production policy, real API, threat-model review, external audit, sandbox network confinement or key rotation.
5. **Same-author synthetic test corpus:** no independent challenge set or external security assessor. Passing negative tests document reproduced flaws rather than readiness.

## Next discriminating experiment: EXP-43

Introduce **privacy-preserving, provider-signed aggregate effect commitments** that expose only a hash/count for a separately authorized checkpoint scope, not the raw inventory. The observer should compare anchored witness effect-ID digest against that authenticated provider commitment and reject hidden-tail omissions. Enforce exact tenant and grant scopes, simulate an issuer or provider lying about count, and use a separate verifier-authored corpus before claiming completeness; prevent accidental leak of effect inventory via count/hash side channels.

**Verdict:** `EXP42_SPLIT_UID_SIGNED_READ_20_OF_20_LOCAL_PASS`; `EXP42_SAME_GRANT_RESPONSE_RECOVERY_VERIFIED`; `EXP42_GLOBAL_EFFECT_COMPLETENESS_UNPROVEN`; `FOR007_AND_IE_UNCHANGED`.
