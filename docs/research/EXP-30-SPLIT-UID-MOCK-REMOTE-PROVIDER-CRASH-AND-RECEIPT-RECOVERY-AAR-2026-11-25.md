# EXP-30 — Split-UID Mock Remote Effect, Provider-Authority Enforcement and Ambiguous Crash Recovery: Executed AAR

**Date:** 2026-11-25. **Repository:** Foromni-Network/forOmni. **Branch:** `research/global-agent-roadmap-execution`. **Outcome:** 22/22 tests PASS in **one uninterrupted final run**, 0 warnings with ResourceWarnings treated as errors. No protected merge, production deployment, paid calls, Internet Embassy access, or frozen FOR-007 modification.

## Research question

Can a Linux worker, broker and independently persisted mock remote provider retain strict task-scoped authorization and recover safely when the provider commits an effect but the broker crashes **before recording remote success**? Can a distinct signed read-only grant recover that effect after the original mutation grant expires/revokes?

## System tested

`system.py` runs two distinct AF_UNIX servers:
- **Broker**: UID 21301; its own SQLite attempts DB and `SO_PEERCRED` restricted to worker UID 21303; writes a pending attempt before forwarding.
- **Mock provider**: UID 21302; **separate SQLite effect ledger** and signer public key protected by file permissions; its `SO_PEERCRED` accepts only broker UID 21301; validates the Ed25519 fixture owner signed grant with action, task, project, resource, effect ID, one-hour maximum expiry, epoch=1 and approval. Owns authoritative idempotent effect ID and durable revocation records.
- **Worker**: actual subprocess under UID 21303; an additional UID 21304 is denied as a broker caller. Root test coordinator owns all key material, child processes and test data. It is **not independent administrative ownership**.
- The mock provider supports `draft.create` and signed `receipt.read`; a signed `grant.revoke` fixture administrative operation is issued by coordinator acting through broker UID, not a genuinely separate admin identity service. The protocol deliberately has no general arbitrary TCP/URL proxy.

## Decisive failure scenario

The broker writes a `PENDING` attempt in its own SQLite database, calls the mock provider over Unix IPC, and receives its `APPLIED` result **after the provider has durably committed**. For a special test-only effect ID `crash_13`, broker deliberately exits code 79 before writing local `CONFIRMED`. The test inspects the broker's pending record, restarts it, retries the same still-valid signed mutation grant, receives `DUPLICATE` from provider, and verifies the provider's SQLite ledger contains exactly **one** effect. This is more representative of remote state separation than EXP-29's single-process ledger; **it is still not a real third-party provider/API**.

An effect performed with a grant expiring two seconds later is denied on an attempted *new mutation* after the grant expires, while a separately signed `receipt.read` grant can recover the original effect. An effect whose grant is later revoked also remains readable under a fresh valid read-only grant.

## Execution evidence

```sh
cd foromni_exp30_remote
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py
```

**Observed final run:** `Ran 22 tests in 24.522s; OK`. First run passed 22 tests but emitted a subprocess stderr-stream cleanup warning; the harness was corrected and final run was clean. This is a **test suite**, not an independent audit or real-world efficacy metric.

### Test matrix

1. Broker/provider distinct Unix UIDs and PIDs.
2. Broker UID cannot read provider-owned signer public-key file (a fixture permission, not a secret-private-key custody study).
3. Valid grant permits exactly one effect.
4–8. Missing grant, task/project/resource mismatch and expired grant denied.
9. Worker UID cannot call provider directly.
10. Unrecognized UID cannot call broker.
11–12. Same-effect replay returns `DUPLICATE`, conflicting task returns `CONFLICT`.
13. **Actual split-DB, split-process crash-after-remote-effect** recovers without duplicate effect.
14. Truly expired original mutation grant denied; distinct fresh read grant retrieves historical receipt.
15. Read-only recovery grant does not create new effect.
16. Mutation grant cannot be used as receipt-read grant.
17. Provider restart retains committed effect and dedupe.
18. Signed owner fixture grant revocation prevents future effect.
19. Later revocation does not erase prior effect readback.
20. **Negative control:** root test coordinator controls all independent-looking services and signing keys.
21. **Negative control:** broker marks invalid-grant request `PENDING` before remote authorization.
22. **Negative control:** broker pending status alone does not prove an effect occurred; only provider readback can resolve outcome.

## Important limits / findings

- **New flaw:** broker creates a pending row before it validates authorization. Rejected requests can leave `PENDING`, potentially polluting reconciliation/analytics. In a real design either validate signed grant before admission, or record a distinct `DENIED` terminal status. No unverified pending record should be promoted to success.
- **Recovery after revocation:** this fixture allows direct new `receipt.read` under the current epoch, but does not verify actual project owner role/approval from an independent task registry; the issuer fixture can mint arbitrary claims.
- **No truly remote third-party effect:** the mock provider SQLite DB and broker SQLite DB run in different OS processes/UIDs but on the same test host controlled by root. No network partitions, third-party billing, uncertain idempotency support, external authorization revocation service or genuine isolated key owner.
- **Access:** Unix socket mode 0666 with peer UID checks and directory traversal allowances is synthetic; users who gain an allowed UID/FD or root remain in scope gaps. No network namespace, seccomp integration, mTLS or verified handler budgets.
- **Admin custody:** the same root test coordinator generates the Ed25519 signing key and signs admin commands. No independent human owner or independently witnessed signatures.
- **No independent witness integration:** this experiment tests authoritative remote mock provider effects only; multi-witness services and checkpoint attestation from EXP-25–27 were not included.
- **No independent QA:** test cases and implementation were authored by the same assistant and not run under GitHub CI. Running local checks is not product readiness.

## Exact artifacts

Download `foromni_exp30_remote_effect_evidence.zip` in the conversation, which includes exact runnable source, tests, README, `test_output.txt`, and SHA256SUMS. ZIP SHA-256: `20d37fdf8a50f32b50c8d16cf636f2e28939f13bcafd728a5ad64141ca48ae8d`.

- `system.py`: `9fdccb69122a0a0c13b75398960d8738a421e2fe063aae102fc06993b539d069`
- `test_experiment.py`: `009babea2ce26bdee5531c8785ced8959d2b86471afe125a4c667ab39f1c6f65`
- `README.md`: `c0b050c15e0b652945ef3db5770ced0cf313ef4d97c6b0c8e23e48ce3522e531`
- `test_output.txt`: `a42ccf4ac8dde416eb985ddcb6b6ee062741ccd13921338d59bc4a1e73b2d699`

**GitHub disposition:** this AAR is the commit; executable source/tests remain in evidence archive and are **not** merged into Foromni source or run by GitHub CI.

## Next discriminating experiment

**EXP-31:** move signed mutation admission validation into the broker *before* it creates a pending record, use a durable `DENIED` status for failed authorized requests, split provider/readback and witness ledgers under independent principals, and add an explicit state machine for outcome `UNKNOWN` when the provider is unavailable or a response is lost. Test races with grant revocation, replay after expiry, provider dedupe, multiple workers and bounded cost/attempt limits. Include a genuinely different reviewer or external fixture author before using security efficacy statistics in collaboration outreach.

**Verdict:** `EXP30_22_OF_22_LOCAL_TESTS_PASS`; `SPLIT_PROCESS_PROVIDER_EFFECT_RECOVERY_VALIDATED_IN_FIXTURE`; `PREAUTH_PENDING_RECORD_FLAW_DEMONSTRATED`; `PRODUCTION_EXTERNAL_TRUST_AND_INDEPENDENT_AUDIT_UNPROVEN`; `FOR007_UNCHANGED`.
