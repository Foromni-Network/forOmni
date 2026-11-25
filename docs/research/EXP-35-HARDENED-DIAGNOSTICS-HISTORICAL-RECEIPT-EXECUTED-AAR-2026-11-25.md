# EXP-35 — Hardened Diagnostic Surface and Historical Read Receipts (Executed Local AAR)

**Date:** 2026-11-25. **Scope:** Foromni-Network/forOmni, `research/global-agent-roadmap-execution` only. **Result:** 18/18 Python local tests passed in one clean run (`Ran 18 tests in 2.445s; OK`), ResourceWarnings treated as errors. No main/protected merge, FOR-007 or Internet Embassy modification, deployment, real provider API, paid tests or independent QA.

## Question and result

Can an EXP-34-style synthetic threaded broker/provider reject the unauthenticated diagnostic controls (`gate`, `stats`), provide a separately authorized, narrowly scoped historical `receipt.read` method, and make Unix socket files less broadly accessible?

**Implemented:** `service35.py` based on EXP-34 `service.py`, paired with byte-identical EXP-31 grant verification `base_exp31.py`. Explicitly rejects diagnostic and generic proxy operations. Signed grants must have matching task/project/resource/effect ID and a valid action. `receipt.read` is read-only, may retrieve a committed mock effect following expiry/revocation of the mutation grant, and cannot be invoked using a mutation grant. Unix socket mode changed from 0666 to 0660 (the fixture does **not** establish a secure production group/ownership provisioning model). Existing provider effect table and concurrency-oriented threading retained in code.

## Exact executable evidence

In attached conversation artifact `foromni_exp35_hardened_receipts_evidence.zip`, SHA-256 `05138ddba4a302b565aac9ff51f932398e628d2e182310fb87305ea83135ad49`, including source, README, exact log, and SHA256SUMS.

```sh
cd foromni_exp35
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_exp35 test_ipc35
```

Observed 18 tests PASS, 0 failures/warnings. Fifteen check deterministic state behavior (allowed apply, duplicate, invalid grant, removed diagnostic operations, fresh historical read after revoked/expired mutation, permission split, scope mismatch, absent record, no mutation attempt for read, restart, conflict, hypothetical ledger mismatch and **negative-control signing-key forgery**). Three checks launch a real AF_UNIX service subprocess and test diagnostic rejection, valid apply→read recovery, and mutation-grant rejection on read. These three IPC cases run **under the same UID**.

| Artifact | SHA-256 |
|---|---|
| base_exp31.py | e37675a9d2a65bda6db2bf08de071582207b181206dca32d70d7a6da0a716db0 |
| service35.py | 52bcd6636b17f052cb7278f8d934c5e5572e38f11078371d956b0da9bf0334e8 |
| test_exp35.py | 7bcf3581bbbdae1c46492157a22f5af87d81ba89d4c57a79eb46ec1de914e002 |
| test_ipc35.py | e121bc81240dd7f22daa82d7719c9ce63faec6f21150473216736cb8fb4a1560 |
| README.md | 251854d23c0eaa6b2a4481fe7f1ae9ef89435b6827bbe5d524a26eff620754c3 |
| test_output.txt | a7497157d4bc50cba1e20f08ae2a566c4c3d47e2a8714097717be218e22f57cd |

## Scope caveats and gaps

**Not a complete EXP-34 integration rerun.** Its 17 multi-UID parallelism and forced gate/revocation tests depend on test-only `stats` and `gate` endpoints removed by EXP-35; they were not rerun against the modified service. The test-only comparison of a claimed effect and SQLite row is **not** an independently running, signed witness ledger or real audit evidence. No separate mock provider readback under different trust custody, controlled concurrent grant revocation, expensive external effects, CI or third-party evaluator is established.

The root/test author holds the demonstration Ed25519 owner key and can sign fabricated work. The `grant.revoke` action is still a demonstration issuer claim, not an independently authenticated administrative service. The socket is mode 0660 but ownership/group rollout and full separate client/service identity isolation have not been demonstrated. A historical receipt returned by the same provider is not third-party certified truth.

## Next discriminating experiment

**EXP-36:** implement a separate *test-control channel* authenticated by a test-only controller credential, with its diagnostic controls omitted entirely from the normal worker socket; retain multi-UID concurrent workers and force a controlled revoke/commit race on the hardened service. Introduce an independently running mock witness with exact effect-ID readback and fail-closed mismatch, plus a separate reviewer-authored negative corpus before making security/service readiness claims.

**Verdict:** `EXP35_HARDENED_ENDPOINTS_AND_HISTORICAL_READ_18_OF_18_PASS`; `TRUE_CONCURRENT_HARDENED_RUNTIME_NOT_RETESTED`; `INDEPENDENT_OWNER_AND_WITNESS_TRUST_NOT_PROVEN`; `FOR007_UNCHANGED`.

**Previous:** [EXP-34](EXP-34-TRUE-PARALLEL-PROVIDER-SPLIT-UID-REVOCATION-ORDERING-AAR-2026-11-25.md).
