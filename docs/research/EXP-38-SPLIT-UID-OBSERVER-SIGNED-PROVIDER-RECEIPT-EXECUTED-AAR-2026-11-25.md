# EXP-38 — Split-UID Observer, Signed Provider Effects, and Durable Corroboration (Executed Local AAR)

**Date:** 2026-11-25. **Project:** Foromni-Network/forOmni. **Branch:** `research/global-agent-roadmap-execution`. **Executed outcome:** 19/19 Python unittest checks PASS in one clean uninterrupted run (`Ran 19 tests in 9.030s; OK`, `-W error::ResourceWarning`). No change to frozen FOR-007, Internet Embassy, production, protected branches or any real provider.

## Question

Can a separately running **observer with no access to the provider or witness private signing keys** verify witness checkpoint claims against **provider-signed exact effect records** using authenticated local Unix-socket IPC, persist its verdicts, and fail unconfirmed when required evidence is absent or the provider is unavailable? Can delayed witness evidence resolve an initially unconfirmed checkpoint?

## Executed system

- **Mock provider (UID 21802):** independent Unix subprocess; private Ed25519 key in UID-owned file, SQLite ledger of exact `effect_id/task/project/resource`; `read` returns a signed receipt only to observer UID 21803, authenticated using `SO_PEERCRED`. The fixture `apply` accepts only root test coordinator UID 0 but **does not require a real task grant**.
- **Witness (UID 21804):** reused byte-identical EXP-37 `witness.py`; stores signed checkpoint claims with its own Ed25519 key/SQLite ledger, accepts only the root coordinator; refuses conflicting payload for the same checkpoint.
- **Observer (UID 21803):** new `observation.py`; has **only provider and witness public keys**, signs nothing, queries the provider over AF_UNIX, checks both Ed25519 signatures and exact effect tuple, persists per-checkpoint verdict in its own SQLite DB. `UNCONFIRMED_WITNESS` and `UNCONFIRMED_PROVIDER` do not imply execution. A later valid witness receipt may replace an `UNCONFIRMED_WITNESS` placeholder. Differing claims for a checkpoint otherwise return `FORK`.
- **Test coordinator:** root creates all keys, services, DBs and fixtures. Thus processes and Unix users are distinct, but **administrative trust is not independent**; the test operator could rewrite every record.

## Local reproducibility

Requires a disposable root-capable Linux test container, Python `cryptography`, and unused synthetic UIDs 21802–21804. Archive `foromni_exp38_observer_evidence.zip` contains runnable code, README, exact logs and SHA256SUMS.

```sh
cd foromni_exp38
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py
```

**Final result:** `Ran 19 tests in 9.030s; OK`. Initial suite of 18 passed; manual review found the late-witness gap. Implemented its safe transition and added a nineteenth test, then reran the entire suite successfully.

## Actual acceptance cases

1. Three different Linux service UIDs/PIDs.
2. Observer UID cannot read private provider or witness signing-key files.
3. Observer UID cannot invoke mock provider mutation (only signed readback).
4. Valid mock effect + witness checkpoint → `CORROBORATED`.
5. Witness-signed nonexistent effect → `PROVIDER_MISMATCH`.
6. Witness-signed wrong task → `PROVIDER_MISMATCH`.
7. Witness-signed wrong project → `PROVIDER_MISMATCH`.
8. Tampered witness signature → `INVALID_WITNESS`.
9. No witness checkpoint → `UNCONFIRMED_WITNESS`.
10. Provider down when verified witness receipt arrives → `UNCONFIRMED_PROVIDER` (not false success).
11. Provider effect appears after first mismatch → later `CORROBORATED` upon recheck.
12. Observer process restart retains corroborated checkpoint state.
13. Changed checkpoint payload lacking valid signature rejected.
14. Witness rejects signed checkpoint fork.
15. Missing witness cannot overwrite prior `CORROBORATED` verdict.
16. Provider repeated identical effect has one persisted mock effect (`DUPLICATE`).
17. **Negative control:** root coordinator can get witness to sign a fabricated effect, which observer rejects against provider ledger.
18. Missing never-emitted tail event cannot be detected absent an independently anchored expected watermark.
19. Late witness receipt resolves initial `UNCONFIRMED_WITNESS` to `CORROBORATED`.

Passing negative controls document the reproduced weakness, not security assurance.

## Exact local artifact checksums

Evidence ZIP SHA-256 `0902d7a380fe696fb2fb48568cf0a313657ff6132828c213832088b7884c92f5`.

| File | SHA-256 |
|---|---|
| `base_exp31.py` | `e37675a9d2a65bda6db2bf08de071582207b181206dca32d70d7a6da0a716db0` |
| `witness.py` | `152d2813527aaf09b3b0ad208ef19bc29fdfec238a60393a1ab609b73583dfb2` |
| `observation.py` | `5cb6a3545ae49ac858201c7003ae9e6d55a7fb94e543ed50ec21a4708c25f52c` |
| `test_experiment.py` | `f56430121404bab82f4a69cce94590287761233891ba92fae21f41633e0ec273` |
| `README.md` | `98851fe35b2cb17c070c957560a0423e3578c66dd0ac8415e8e2e4841da110a0` |
| `test_output.txt` | `d9621c79bb7ad0780f421ac9dc9fdcdd69fd7de2ece6901f0d36d96de9ef7590` |

This GitHub commit is an AAR only. Runnable source is in the attached research archive; no application source integration or independent GitHub CI was run.

## Security and scientific limitations

- Test administrator controls signing keys, witness, observer and provider; no independent operator, external ledger custody or immutable transparency anchor. Test socket paths are mode 0666 and rely on `SO_PEERCRED`; production path permissions and least-privilege provisioning are absent.
- Mock provider effect creation lacks task-scoped owner-signed grant. This study isolates **readback evidence**, not full EXP-36 authorization enforcement; the experiments are not fully converged.
- Observer trusts provider **signed assertions**, not physical truth or external network provider semantics. A dishonest or compromised provider can sign a false effect, and a root operator can replace public keys. No third-party API, protected hardware or real owner consent is used.
- The observer retains its own SQLite verdict, which is writable by its process/administrator and not independently signed or witnessed. A malicious observer can lie about a verdict.
- No independently sourced expected-event watermark; an entirely withheld final event can remain invisible. No clock drift, operational timeouts, provider key rotation/revocation, compromise recovery, real tenant privacy controls or external security review.
- Researchers authored the code and synthetic tests. `19/19` is not real-world precision, security assurance, independent audit or commercial readiness.

## Next bounded experiment: EXP-39

Integrate task-scoped grants on the provider mutation path (EXP-36) with signed provider receipt verification (EXP-38), then add **durable external checkpoint/watermark anchoring** and simulated provider misinformation. Test that a forged but validly signed provider record is not treated as independently verified truth, and that a withheld terminal event is detected with an independently signed expected checkpoint. Freeze a separate reviewer-authored challenge set before claiming effectiveness. Do not deploy or import IE code until separate authorizations and licensing are resolved.

**Verdict:** `EXP38_SEPARATE_OBSERVER_PROVIDER_SIGNED_RECEIPT_19_OF_19_PASS`; `EXP38_ABSENT_EVIDENCE_REMAINS_UNCONFIRMED`; `EXP38_INDEPENDENT_TRUST_AND_TAIL_COMPLETENESS_UNPROVEN`; `FOR007_UNCHANGED`.
