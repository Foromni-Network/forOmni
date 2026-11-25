# EXP-21 — Broker/provider separately keyed telemetry and causal effect correlation: executed local AAR

**Date:** 2026-11-25. **Scope:** Foromni research-only synthetic Python study; no Internet Embassy changes, live MCP, customer data, real webhook, paid service, deployment, protected Git integration or FOR-007 change.

## Goal

EXP-20 showed that event field forgery defeats even improved detection rules. This experiment asks whether **distinct demonstration signing keys for mock broker and provider records**, strict role-specific event types, monotonic per-issuer sequences and broker-grant/provider-effect correlation can expose simple tampering, replay and unauthorized effects.

**Hypothesis:** unchanged correctly keyed/granted sequences are accepted; mutations, wrong keys/roles, duplicate event IDs, gaps, rollbacks and provider effects lacking a matching broker grant are reported. This is an exploratory, researcher-authored deterministic suite; no independent evaluator.

## Implemented

`telemetry.py` (research prototype):
- `Event` immutable record binds `issuer`, `seq`, `event_id`, `task_id`, `attempt_id`, `action`, `project`, `effect_id`, `kind` and `signature`;
- canonical JSON payload with HMAC-SHA256 per issuer; broker may issue `grant`, `deny`, `complete`, provider may issue `effect`;
- `Monitor` rejects bad signatures, unknown issuers/kinds and event replay/gaps; it flags an `effect` with no prior matching `grant`, a repeated effect ID and a `complete` with no matching effect;
- no authorization grants issued or provider operations performed. These checks only interpret caller-supplied records whose signer keys are controlled by the experimenter.

`test_telemetry.py`: 17 executable unittest checks, including valid broker→provider→broker chain, modified signed payload, wrong signer key, role mismatch, unknown issuer, identical replay, sequence gap, rollback, effect without grant, completion without effect, duplicate signed effect, cross-project effect, inert suspicious text, invalid kind, denial and two negative controls.

## Observed execution

From evidence directory:
```bash
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v
```

**Observed:** `Ran 17 tests in 0.004s; OK` (zero failures, errors, or ResourceWarnings). Passing includes **two intentionally insecure negative-control cases**:
1. An experimenter holding the local demo signing key can fabricate records which the verifier accepts.
2. A missing last event cannot be detected without an externally anchored expected sequence watermark.

**No quantitative estimate of incident detection performance** is implied; these 17 assertions are a deterministic software test suite and the signer and verifier share one process/security principal.

## Reproducibility

The exact executed source, tests, README and output are in conversation artifact `foromni_exp21_telemetry_evidence.zip`. SHA-256:
- `telemetry.py`: `3b65c1c8f5415d3c19b8d674a1c0c868f4b41830027626cf8739cff5fb9b795d`
- `test_telemetry.py`: `d5c69aeadeb3189485585b7ead186aa4b6f59b980968ca169e9d559526aab421`
- `README.md`: `9876f00352995a7dae820ed8e6d3f2964fdc10a7c5a9f9985970245691d40e63`
- `test_output.txt`: `9926c796835b1ed79229b9f4961db780a4cc06b962ea318827815efa0b95155a`
- ZIP: `647243dedb7b92c8c35c06583dc8caffaf3d4e40ea185dd869b22a02dc24ef46`

**Distribution:** this GitHub commit records the report. The exact executable source exists in the linked local archive, not as an integrated repository module. No GitHub CI or independently signed source verification was performed.

## AAR — design and limitations

**Positive:** the test format can bind observations to specific task/attempt/action/project keys, distinguish asserted broker authorization from provider-side effect, and reject simple tampering, replay and ordering anomalies. This is a useful precursor to authenticated SIEM events and externally validated security assessments.

**Major outstanding gates:**
1. **Signing-key custody:** HMAC only proves possession of the key. Both keys are embedded in the same local test. A compromised issuer can sign a lie. Use independently administered identities and a protected producer/execution boundary.
2. **Event ordering & log durability:** one in-memory expected sequence is insufficient across crash/restart; signed checkpoints/high-water marks must be stored durably and independently anchored. Gaps may be mere out-of-order delivery; real ingestion needs buffer/timeout/reconciliation.
3. **Actual provider state:** the provider `effect` record is a signed assertion by the mock issuer, not verified from a real provider API or independent effect ledger. Compare with provider-authoritative readback and expense receipts before accepting completion.
4. **No policy authorization:** `grant` is a signed narrative, not a lease from the trusted task authority. Verify owner, revocation, scope and expiry when actually executing.
5. **Event integrity ≠ visibility completeness:** even perfect MAC checks do not reveal events that were never emitted; use authoritative task/effect reconciliation and independent observer.
6. **No signed release, source SHA or genuine independent QA:** no true separated signing service, source-bound test run, or customer data was involved.
7. **Detector remains advisory:** the EXP-20 detector and this monitor are separate experimental components; no validated integration with real SIEM or enforcement broker.

## Next experiment

**EXP-22:** persist immutable per-issuer event receipts and sequence watermarks in distinct SQLite ledgers; run producer/verifier in separately credentialed local processes; simulate missing, duplicated, reordered and forged callback events; independently reconcile provider actual-effect ledger and detect unsigned/signed-but-withheld tail. Compare verified-alert quality with EXP-20's caller-claimed events, tracking late delivery and false-positive tradeoffs. Retain all earlier restrictions and no production claims.

**Verdict:** `EXP21_SYNTHETIC_TELEMETRY_VALIDATION_17_OF_17_PASS`; `TRUE_SOURCE_AUTH_AND_EVENT_COMPLETENESS_UNPROVEN`; `FOR007_UNCHANGED`.
