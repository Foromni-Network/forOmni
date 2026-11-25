# EXP-29 — Unified Task-Scoped Provider Authorization, Historical Receipt Recovery and Witness Corroboration (Executed AAR)

**Executed:** 2026-11-25. **Scope:** Foromni-Network/forOmni research branch `research/global-agent-roadmap-execution`; local synthetic fixture only. **Result:** 26/26 Python tests PASS in one uninterrupted run; ResourceWarnings elevated to errors. Frozen FOR-007 and Internet Embassy unchanged; no deployed service, real API, paid test, protected merge or external security audit.

## Research question

Can a task-scoped grant prevent new unauthorized mock provider effects while a separately authorized **read-only historical receipt recovery grant** confirms an earlier effect after the original mutation grant expires or is revoked? Can witness checkpoints be reconciled against the mock provider's exact effect IDs and task bindings? What happens when the provider crashes **after committing a local effect but before sending its response**?

## Architecture and actual implementation

This experiment reused byte-identical EXP-28 `provider.py` as `provider_base_exp28.py` and EXP-25 `protocol.py` as `protocol_exp25.py`. Added:
- `unified.py`: `UnifiedProvider` restricts newly created effects using the EXP-28 Ed25519 signed task/project/resource/action/approval/expiry/epoch grant, retaining durable SQLite revocation and effect-ID idempotency. Unrestricted `readback` is rejected; `receipt.read` requires a separate, signed short-lived **recovery purpose** and exact effect ID/task/project match. This historical read does not reactivate a revoked mutation grant. A revoked or stale recovery grant is denied. `audit.effects` is a **test-only** static-token verifier endpoint.
- `server.py`: Linux Unix socket IPC checks `SO_PEERCRED` connecting UID before reading a request. Tests use same Unix UID for client and server; they do **not** claim full separate-UID worker/provider isolation from EXP-27.
- `test_experiment.py`: 26 executable cases for authorization denial, replay collision, durable reinitialization, recovery under expired/revoked grants, post-epoch reauthorization, real IPC peer mismatch, signed witness effect matching/false claims, and *actual process exit code 77 after SQLite effect commit* with process restart/retry/historical receipt.

**Reproduce:**
```sh
cd foromni_exp29_unified
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py
```

**Actual result:** `Ran 26 tests in 2.310s; OK`. No warnings or failures.

## Observed results and crucial nuances

- Valid current owner-fixture grant permits exactly one mock `draft.create` effect. Missing, mismatched task/project, expired, revoked and stale-epoch mutation grants are denied **before new effect**.
- Exact same effect ID/authorized request gives `DUPLICATE`; conflicting request grants yield `CONFLICT`. SQLite effect ledger survives provider object reconstruction.
- When original mutation grant is **expired or revoked after success**, a separately signed valid receipt-read grant can recover the previous effect's bound task/project/grant ID/request hash without performing a new mutation. Denied stale/revoked recovery grant cannot read. Following authorization epoch rotation, a **new** recovery grant with current epoch may read the historical record.
- Authenticated Unix socket path tests allow the configured peer UID and reject a deliberately different peer UID; **same actual OS user** for service/client and world-access DAC is not characterized here.
- An EXP-25 local quorum verifies signed issuer/witness claims. A false-but-witness-confirmed claim is flagged when the provided mock effect list disagrees. **This test does not start independent witness services;** all signing keys and mock effect references are under one test coordinator.
- **End-to-end local crash simulation:** provider process commits effect, exits 77 before replying, then on restart identical valid request returns `DUPLICATE`, a newly authorized `receipt.read` returns `FOUND`, and local mock ledger contains one effect ID.
- **Negative controls:** test owner-key holder can forge apparently authorized tasks; hard-coded test administrator secret can change authorization epoch. Both are vulnerabilities by design and MUST NOT be taken as safe production authority.

## Exact reproducible evidence

Archive `foromni_exp29_unified_evidence.zip`, SHA-256 `0dd5079d7e5a4fec590876a16d9176129359a3aa34d7bc328c54eed7817a3433` contains exact test source, README, log and SHA256SUMS.

| File | SHA-256 |
|---|---|
| provider_base_exp28.py | `4190386951a038a679c970e0f77c93f06cf39bd6bd57162c044bac7e2e869385` |
| protocol_exp25.py | `9c9ee453460fea262f83323b67703f38267d171f3216e2f09173f08498132432` |
| unified.py | `3af521d10fee85cc0e0efd90d4d93b64c9833491b581c8719f65ace2230b141b` |
| server.py | `0c32ea42157e558dc4b25f1d9bfc146695c5b2c1138f08606526ca8e619c8e82` |
| test_experiment.py | `dc1518c393c2c7c14155023574ff58cbf3850a9a39f7cee1f1323f86d029081b` |
| README.md | `26cf574a015b450c710ddefab835182a4bb7c780691c975d651b10c7180b1665` |
| test_output.txt | `14c5f385a6878be5106528abee38ed9738b9ce4715c77d2b2945ac53a72a34ca` |

The runnable implementation is preserved in the conversation ZIP. **This GitHub commit is the research AAR only**, with no production source integration or GitHub CI.

## Limits and what is NOT proven

- Not an external API effect: crash idempotency is only demonstrated within the local SQLite transactional ledger, where commit and mock effect are the same action. A remote provider effect occurring before ledger commit remains an unresolved ambiguous outcome.
- Not independent owner approval: signing keys, test admin secret, audit token and mock provider records are under the same fixture author's control. No real task authority, legal consent or revocation races across independent administrators.
- Not full process separation: real socket peer check tested, but both service and client share one UID. Separate UID/credential execution from EXP-27 was not integrated here.
- Not independently verified witness custody: witness exercises run in the same test process with generated keys. Quorum does not prove truth.
- Not a secure audit API: fixture `audit.effects` uses a static token, and underlying EXP-28 `revoke`/`rotate_epoch` use a hard-coded administrator secret. No real client auth for the audit route or private receipts.
- No cost budgets, credential escrow, authorized operator training, real MCP SDK, signed source-bound independent QA or commercial assessment readiness.

## Next gate

**EXP-30 candidate:** consolidate actual separate Unix UID provider/broker/worker boundaries (EXP-27) and verified task-grant plus narrowly scoped historical recovery (EXP-29), remove hard-coded admin/audit credentials, and use distinct owner/policy issuer authorities. Include a mock remote-effect service in a separately persisted process to expose uncertainty between external effect and local ledger commit, with reconciliation by authoritative provider readback. Require a separately authored/independently reviewed negative-case suite and do not claim production trust from toy green tests.

**Verdict:** `EXP29_UNIFIED_LOCAL_26_OF_26_PASS`; `EXP29_REVOKED_OR_EXPIRED_MUTATION_CAN_RECOVER_PRIOR_RECEIPT_WITH_FRESH_READ_GRANT`; `EXP29_CRASH_AFTER_LOCAL_COMMIT_ONE_EFFECT`; `EXP29_EXTERNAL_TRUTH_AND_INDEPENDENT_AUTHORITY_UNPROVEN`; `FOR007_UNCHANGED`.
