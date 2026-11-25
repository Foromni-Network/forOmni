# EXP-28 — Provider-Side Task-Scoped Grants, Durable Revocation, and Crash-After-Effect Recovery

**Date:** 2026-11-25. **Repository:** Foromni-Network/forOmni, branch `research/global-agent-roadmap-execution`. **Result:** `22/22` local Python unittest checks passed in one run with `-W error::ResourceWarning`. No production FOR-007 change, Internet Embassy modification, paid testing, external service, real provider API, protected merge or deployment.

## Hypothesis

EXP-27 proved a separate mock provider could contradict witnessed claims, but an authenticated local client could still mutate provider state with no task-scoped authorization. This experiment tests **grant verification before any mock effect**, durable revocation/epoch changes, narrow typed action/resource/project/task matching, idempotent effect IDs, and a subprocess crash **after SQLite commit but before response**.

## Implementation and execution

- `provider.py`: a narrowly typed `draft.create` mock provider, Ed25519 owner-fixture signature verification, strict grant schema and expiry (max 1-hour grant horizon), exact task/project/resource/action matching, approval claim, durable grant revocation and authorization epoch, SQLite effect ledger with `BEGIN IMMEDIATE`, effect-ID idempotency and collision detection.
- The one real Unix-domain `provider.py` subprocess case deliberately invokes `os._exit(77)` after effect transaction commit but before replying. The test reopens the SQLite DB and verifies retry yields `DUPLICATE` and effect count remains 1.
- Most other tests call the class directly rather than over actual IPC; unlike EXP-27 this harness **does not** separate client and provider into different OS UIDs.
- `test_experiment.py` runs 22 cases, including correct grant, missing grant, wrong task/project/resource/action, expired grant, altered claims, wrong signer, unapproved grant, idempotent duplicate, changed request conflict, durable revocation, epoch rotation, unauthorized admin command, unrecognized URL/tool arguments, recreated provider, crash-after-effect, static-admin-secret negative control and forged authority by keyholder negative control.

```sh
cd foromni_exp28_provider_auth
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py
```

**Observed:** `Ran 22 tests in 0.898s; OK`, no final resource warnings, errors or failures.

## Main positive and negative findings

- Without a valid, task-matching signed fixture grant, a new effect is rejected before reaching SQLite.
- Once revoked, a grant remains denied when `Provider` is reconstructed from its DB.
- An old grant fails once the persisted epoch changes.
- Duplicate replay of a committed effect ID with the same binding returns `DUPLICATE`; changing the task under the same effect ID returns `CONFLICT`.
- A deliberate crash after durable SQLite commit but before response does not cause a second mock effect when the same valid request is replayed after restart.
- **Negative control:** a holder of the demonstration owner private key can authorize a fabricated task; a signature is not legal/human owner consent or reliable source custody.
- **Negative control:** an embedded administrative test secret permits privileged revocation/epoch operations; it is unsuitable for production, and no independent administrative identity service is implemented.
- **Missing distributed-effect recovery:** there is no external provider network call or independent provider-side effect idempotency. An external effect could happen without a local SQLite commit; this fixture cannot solve that ambiguity.
- **Missing expiry/revocation recovery:** effect replay requires a valid current grant. If a previous effect succeeded then its grant expires/revokes, a retry fails authorization rather than discovering a historical receipt. A separately authenticated readback is required to recover the confirmed prior outcome without allowing a new unauthorized mutation.

## Source evidence exact hashes

Exact tested runnable source, README, output and checksums reside in conversation artifact `foromni_exp28_provider_auth_evidence.zip`. Archive SHA-256: `ecf029bbeab359b04a0ac504d2a398a612d86ef4ee4ba9db2158f5adaf747750`.

| File | SHA-256 |
|---|---|
| `provider.py` | `4190386951a038a679c970e0f77c93f06cf39bd6bd57162c044bac7e2e869385` |
| `test_experiment.py` | `d6a19090a2089c4ad17aaf5d0e15dd9bd32675088739139a1986473c9fb25a11` |
| `README.md` | `291c85f5912e12a62c5f59a80d01be03b3d1ec2f8478e583ec78c23194b0f85a` |
| `test_output.txt` | `18eccb46aadcaf91f82800e12dd4cb3c12e010f3e8e7f87517e7d30a27bd1bb4` |

**GitHub disposition:** this research AAR is committed, while exact executable source/tests are in the downloadable conversation ZIP; no GitHub source-tree integration or CI performed.

## Key scientific boundaries

The provider signing key and fixture administrator identity are not independent of test author. Time is process wall-clock, not attested time. Provider accepts `readback` without authenticated access in the fixture and exposes a static admin secret in test code. Unix socket mode is set to 0600 but no `SO_PEERCRED` authentication is checked (in contrast to EXP-27). No live RPC credential escrow, explicit owner-task lease from trusted registry, capability budget, real service isolation, independent evaluation or multi-host trust. No claims of resistance to root compromise, real MCP behavior, or production security.

## Next experimental gate

**EXP-29:** combine EXP-27 separate UID authenticated provider IPC with EXP-28 authorization grants, plus *historical read-only receipt recovery* for expired/revoked grants, mock distributed provider idempotency and authoritative effect IDs; join back to EXP-25/26 witness reconciliation. Include false-grant negative cases, revocation races, crash-before/after durable effect and provider readback controls. Demand independent reviewer/evaluator and source-bound results before describing as security-assessment-ready.

**Verdict:** `EXP28_PROVIDER_GRANT_FIXTURE_22_OF_22_PASS`; `EXP28_UNAUTHORIZED_MOCK_MUTATION_DENIED`; `EXP28_CRASH_AFTER_SQLITE_EFFECT_RECOVERS_WITH_VALID_GRANT`; `OWNER_AUTHENTICITY_AND_EXTERNAL_EFFECT_GUARANTEES_UNPROVEN`; `FOR007_UNCHANGED`.
