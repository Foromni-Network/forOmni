# EXP-31 — Pre-admission grant validation and explicit UNKNOWN recovery (executed AAR)

**Date:** 2026-11-25. **Project:** Foromni-Network/forOmni; research-only branch `research/global-agent-roadmap-execution`. **Final execution:** **23/23 Python unittest checks PASSED in a single uninterrupted run**, 0 warnings with ResourceWarnings-as-errors, `Ran 23 tests in 1.657s; OK`. No protected merge, FOR-007 modification, IE change, production service, paid provider, or independent security audit.

## Research question

EXP-30 revealed that the broker wrote `PENDING` **before** verifying authorization, leaving false pending rows for denied requests. Can the broker reject invalid grants prior to admission, persist `DENIED` when the provider rejects an otherwise correctly signed grant (e.g. revocation), and mark lost-provider responses as `UNKNOWN` rather than `CONFIRMED`? Can retry after a committed-but-lost response recover without duplicate mock effects?

## Exact implementation

Starting from EXP-30 `system.py`, EXP-31 added **broker-side Ed25519 fixture-grant validation before inserting an attempt**, without removing the provider's independent grant check. The broker now receives its own copy of the issuer public key. For `apply` it inserts `PENDING` only after successful local grant validation; provider `APPLIED` or `DUPLICATE` transitions to `CONFIRMED`, provider `DENIED`/`REVOKED` transitions to `DENIED`, conflicting bindings to `CONFLICT`, and network timeout/connection drop or unrecognized provider statuses to `UNKNOWN`. Explicit `receipt.read` continues through a separate correctly signed grant and does not create a mutation attempt. **These labels are observations of the test broker/provider, not certified authority.**

`test_experiment.py` has 20 broker/provider logic checks with mocked transport and *separate SQLite broker/provider databases*; `test_ipc.py` runs **three real AF_UNIX process-level checks**, including denied unadmitted request with zero ledger row, legitimate effect with duplicate retry, and provider outage producing durable `UNKNOWN`. The IPC processes run under the **same Unix UID**, so EXP-30's actual split-UID setup was **not** carried over into this experiment. The test author also owns both signing and evaluation keys.

## Executed command and result

```sh
cd foromni_exp31_admission
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest discover -v
```

Actual final result: **`Ran 23 tests in 1.657s; OK`**. The first run of new source failed because the test transport mock had a callback arity mismatch; after correction, five cases still failed because exceptions were not forwarded correctly by the test mock. Those harness bugs were fixed and all 20 logic checks passed. Three actual socket/subprocess tests were then added and all **23 passed** in the final clean run.

### Key acceptance and negative cases

- Valid scoped grant permits one mock `draft.create` effect and records `CONFIRMED`.
- Missing/expired/bad-signer grant, wrong task or forbidden op returns `DENIED` **without an attempt row**.
- Provider-side durable revocation after broker's cryptographic pre-check becomes terminal `DENIED`, with **zero mock effects**.
- Unreachable provider returns `UNKNOWN` (durably), not an invented success.
- Lost response after provider commit returns `UNKNOWN`; repeating identical still-valid request yields `DUPLICATE` from provider and broker `CONFIRMED`; exactly one provider effect.
- Conflicting effect ID/request binding returns `CONFLICT`.
- A separately signed `receipt.read` grant obtains a prior receipt without a new effect; bad read grant does not create a mutation attempt.
- Broker reconstruction preserves an `UNKNOWN` record. Later invalid grant does not erase existing `UNKNOWN`.
- Actual Unix IPC process cases reject invalid request before admission, confirm same-effect dedupe, and correctly represent provider outage as `UNKNOWN`.
- **Negative controls:** anyone holding test issuer private key can produce valid-looking authorization; without authoritative provider readback, a pending/`UNKNOWN` row alone does not prove whether an external effect occurred.

## State semantics

`DENIED` is a terminal rejection from provider authorization **after** an authenticated incoming grant is checked; invalid broker-side claims are rejected without admission. `PENDING` is an admitted intent *before* provider resolution. `UNKNOWN` is an unresolved communication/outcome ambiguity, not success. `CONFIRMED` is assigned only after an `APPLIED` or `DUPLICATE` provider reply in the fixture. The workflow is **not** a linear DENIED→PENDING→CONFIRMED progression: denied is terminal, unknown may be reconciled, and an invalid claim never enters the state machine.

## Executed evidence fingerprints

The exact source, tests, README, output and SHA256SUMS are in downloadable `foromni_exp31_admission_evidence.zip`.

| File | SHA-256 |
|---|---|
| `system.py` | `e37675a9d2a65bda6db2bf08de071582207b181206dca32d70d7a6da0a716db0` |
| `test_experiment.py` | `e9b8fbff243785a338e29e0234d928455574645a9905c2d86db2f5b166751d48` |
| `test_ipc.py` | `a183923f6ac2f0b7811179ee02864d01f3c06425563c110f56472a7c67f03d4b` |
| `README.md` | `4df922be79e8e7706cdf137674f9e9e9ff7473a47730b9e5a59c072a403d339d` |
| `test_output.txt` | `b6ba4b75a5abdad0fa22e142cb367a6bb912a5731de950568c61a14a91dd87b2` |
| Evidence ZIP | `d81c53176c249bf788c4c85986835091dc10629d1b9a3abc5953655dee708c8a` |

**Source disposition:** the GitHub commit contains this AAR only; runnable sources/test logs are in the conversation artifact ZIP, not integrated Foromni application code or GitHub CI.

## Remaining limitations

No test of concurrent workers racing same `effect_id`, admission transactions and compare-and-set updates, revocation occurring between broker pre-check and provider acceptance, multiple principals/hosts, crash between broker DB write and provider send, provider idempotency after expiry, true remote API partial failure, signed witness quorum, independently administered task authority, provider-authenticated receipt readback, bounded retries/budgets, exact source-bound independent QA or legally authorized live security assessment.

The fixture uses a trusted local test signing key under one author, and real subprocess IPC cases share the same Unix UID; separate UID process isolation from EXP-30 is not proven within EXP-31. The implementation still uses permissive Unix socket mode and a demonstration administrator grant for revoke. A purported `UNKNOWN` entry requires trusted provider readback or human review before a positive assertion.

**Next discriminating experiment:** EXP-32 concurrent admission and revocation-race semantics with atomic state transitions, two separate worker UIDs, and a **historical receipt discovery route that survives expiry** without enabling unauthorized mutation. Use a separately authored test dataset and actual provider evidence contract.

**Verdict:** `EXP31_PREAUTH_PENDING_GAP_CLOSED_IN_LOCAL_FIXTURE`; `EXP31_UNKNOWN_NOT_CONFIRMED`; `EXP31_23_OF_23_EXECUTED_CHECKS_PASS`; `REAL_REMOTE_AND_INDEPENDENT_OWNER_AUTH_UNPROVEN`; `FOR007_UNCHANGED`.
