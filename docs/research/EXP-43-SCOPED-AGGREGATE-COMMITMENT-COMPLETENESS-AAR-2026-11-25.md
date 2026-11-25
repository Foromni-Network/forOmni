# EXP-43 — Tenant-scoped signed aggregate commitments (Executed local AAR)

**Executed:** November 25, 2026, Foromni-only research branch `research/global-agent-roadmap-execution`. **Result:** 30/30 Python `unittest` tests passed in one uninterrupted final run (`Ran 30 tests in 0.937s; OK`) with `-W error::ResourceWarning`. One preliminary run failed due to a test helper keyword typo, which was fixed before the complete passing run. No FOR-007 or Internet Embassy modifications; no protected merges, external operations, or production deployment.

## Research question

EXP-42 showed that an observer with only scope-approved signed receipt reads can corroborate listed effects but cannot detect an extra effect withheld from its witness list. Can a tenant- and scope-bound, **provider-signed aggregate effect commitment** be compared with a witness-signed commitment and an authority-signed expected count **without disclosing raw effect IDs to the observer**?

## Implemented protocol and observations

`protocol.py` implements a 32-byte random-salted, domain-separated SHA-256 commitment of canonical sorted IDs, tenant and scope. The fixture authority creates Ed25519-signed exact mutation grants and expected checkpoint counts/sequences. The SQLite mock provider independently verifies mutation grants, deduplicates effect IDs, and signs a scope/sequence/count/digest head. The separate SQLite witness signs its own scope/sequence/count/digest checkpoint. The in-process observer checks all three signatures plus tenant/scope/sequence/count/digest equality and returns `CORROBORATED_SCOPED_COMMITMENT` only on agreement. The observer's protocol receives **no raw ID inventory**.

**Passing tests show:**
- Exactly scoped, signed mock mutation grant required; invalid, expired or mis-scoped action denied; idempotent effect duplicate vs task conflict differentiated.
- Provider extra effect withheld by witness causes `EXPECTED_COUNT_MISMATCH` when original expected count is independently signed. An equal-count substitution causes `EFFECT_SET_MISMATCH`.
- Tampered provider/witness signatures denied; missing provider/witness/expected checkpoint stays unconfirmed.
- Tenant/scope isolation, stale sequence, signed expected-count discrepancy, and immutable head checkpoint forks/gaps handled explicitly.
- Random salts produce different hashes; visible commitment need not contain effect IDs.

**Negative controls — not security wins:**
1. A dishonest provider and witness can sign a mutually consistent invented effect; with a matching signed expected count the observer returns `CORROBORATED_SCOPED_COMMITMENT`. It is not proof of physical execution.
2. A dishonest expected-count authority can sign zero and the signing services can corroborate an empty inventory.
3. A signed, internally consistent snapshot cannot detect a later extra provider effect unless a **newer externally trusted watermark** is available.
4. The mock provider accepts repeat uses of a valid grant nonce as an idempotent duplicate; no grant replay ledger is implemented.

## Reproduce

Requires Python and `cryptography`. Unzip conversation archive `foromni_exp43_scoped_commitments_evidence.zip`, then:

```sh
cd foromni_exp43
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py
```

Final recorded result `Ran 30 tests in 0.937s; OK`.

Archive SHA256: `9a2cc157e8e0aed89e7db87fdab02aa427434a0cf4385b4c59707954be20fac9`. Zip includes runnable source, README, exact test output and SHA256SUMS; zip integrity verified.

| Artifact | SHA256 |
|---|---|
| protocol.py | `5c4d0691e9fa00e4444cf21893aa7ba10e8dfe836035dacee80892bdd6d866df` |
| test_experiment.py | `be8b6d6bb50fb3698bd4757ca3b92e64b07adcaa4f421aa55bc58ed84fc99f35` |
| README.md | `9d3e9e58fb7a4183dcfdf9ab24893f28fe14428303879f2fd5f0cfabecf325d3` |
| test_output.txt | `0a7ece23c22d642e00fccdb88a3c62173c8f65883164e8d5202d2a02ae169555` |

## Limits of this claim

**Single-process local protocol regression**, not EXP-42's separate Linux UID/AF_UNIX integrated runtime. Multiple SQLite files and distinct keys are **all under the same author/operator**. Signing the same invented count and effect set is possible. There is no independent external source of execution truth, grant-revocation/epoch or authenticated aggregate-read boundary. Salt must be shared with provider and witness; commitment leaks scope, sequence, count and equality, and low-entropy IDs remain vulnerable to dictionary testing by an actor with the salt. It is **not zero knowledge or guaranteed privacy**. The mock `seal` method accepts direct fixture calls, and private `ids_for_fixture` enumerates effect IDs for tests only; neither is production authorized IPC. There are no real provider effects, independent assessor, reviewer-held negative corpus, GitHub CI or commercial security readiness.

## Recommended next experiment

**EXP-44:** restore multi-UID service boundary and require scoped, separately signed aggregate commitment-read authorization; add publisher-controlled expected watermarks from another independent trust domain, simulate concurrent effect creation and checkpoint sealing, test dishonest provider/witness/count issuer, revoked scopes and delayed tail effects, and obtain independent reviewer-authored challenge cases. Any `CORROBORATED` outcome must explicitly mean scope-limited agreement, never real-world execution or global completeness.

**Verdict:** `EXP43_SCOPED_AGGREGATE_30_OF_30_LOCAL_PASS`; `OMITTED_EFFECT_DETECTED_WITH_TRUSTED_EXPECTED_COUNT`; `INDEPENDENT_COMPLETE_EXECUTION_AND_PRIVACY_UNPROVEN`; `FOR007_AND_IE_UNCHANGED`.

**Artifact disposition:** This GitHub commit stores the **after-action report only**; runnable source, tests and output are in the conversation evidence ZIP and are not merged into application source or CI.