# EXP-26 — Split-Unix-UID Witness Processes, Actual IPC, Durable Restart and Quorum: Executed AAR

**Date:** 2026-11-25. **Project:** Foromni-Network/forOmni; research branch `research/global-agent-roadmap-execution` only. **Status:** 20 executable local checks passed **in two batches of 10** (not a verified single uninterrupted 20-test run), zero final ResourceWarnings in each. No changes to frozen FOR-007, Internet Embassy, protected branches, paid providers or externally deployed agents.

## Question

Can the EXP-25 two-of-three witness protocol operate with **three genuinely different unprivileged Linux processes**, each with a private Ed25519 signing key and separate durable SQLite ledger, over Unix sockets, while surviving one witness outage/restart and delayed receipts? Can a coordinator under one root administration nonetheless override the apparent trust independence?

## Implementation and observations

- Reused byte-identical EXP-25 `protocol.py` for canonical signed issuer checkpoints, witness receipts, durable per-witness chain, 2-of-3 verifier and exact mock effect-ID/task binding.
- New `witness_service.py`: actual AF_UNIX IPC daemon per witness, serving signed receipts from its own DB/key.
- New `test_experiment.py`: local coordinator starts three subprocesses using `setgroups([]),setgid,setuid` and UIDs **21121, 21122, 21123**, each with private key file mode 0600 and service directory mode 0700. A cross-UID key-file read fails with `PermissionError`. Each process has its own socket, persisted SQLite receipt ledger and OS PID.
- The source issuer checkpoint and verifier are still created/held by the root coordinator, **not independent operators**.
- Intentional research shortcut: each Unix socket is mode **0666**, thus requester access is not restricted at the Unix-socket filesystem layer; there is no client `SO_PEERCRED` authorization or production access control. Do not deploy this daemon.
- A subprocess is killed and restarted to confirm an identical checkpoint returns `DUPLICATE` from persistent ledger and a following sequence is accepted.

### Actual final execution evidence

The complete run initially hit subprocess `stderr=PIPE` ResourceWarnings, which were fixed by routing daemon stderr to DEVNULL. An uninterrupted end-to-end 20-test run did **not** yield a reliably complete result in the allotted execution runs; therefore the final reproducible evidence consists of **two separately successful 10-test batches**, each with `-W error::ResourceWarning`:

```
python -W error::ResourceWarning -m unittest -v test_experiment.Research.test_01_distinct_os_process_ids ... test_experiment.Research.test_10_source_rollback_against_pinned
# Ran 10 tests in 19.440s — OK

python -W error::ResourceWarning -m unittest -v test_experiment.Research.test_11_exact_mock_provider_ids_match ... test_experiment.Research.test_20_bad_sig_from_synthetic_compromised_service_fails
# Ran 10 tests in 17.812s — OK
```

For exact test selection and reproducible batching, use the runnable README in the attached archive. **20 passing test methods across two batches** is not a single-pass CI claim, independent QA, or a distributional attack evaluation.

## Main positive checks

1. Three separate process PIDs and distinct unprivileged Linux UIDs observed via `/proc/<pid>/status`.
2. Process under UID 21122 cannot read UID 21121 private key file; no cross-user key read via DAC.
3. Signed 2-of-3 confirmation succeeds via actual Unix sockets.
4. One witness may be offline and remaining two can confirm.
5. One receipt yields `UNCONFIRMED_QUORUM` (fail-closed).
6. Witness process restart preserves receipt state; later checkpoint accepted.
7. Delayed second receipt upgrades `UNCONFIRMED_QUORUM` to `CONFIRMED`.
8. Two honest witnesses reject a conflicting but issuer-signed same-sequence history.
9. Forged signing key does not pass pinned witness verification.
10. Verifier detects source rollback using pinned checkpoint head.
11. Mock provider effect IDs and task associations compared exactly; altered ID/task rejected.
12. Second checkpoint confirmed after a witness restarts.
13. Client cannot reach a stopped witness socket.
14. Verifier reconstruction preserves pinned head; invalid signed witness receipt fails quorum.

## Explicit negative controls

- **Issuer falsehood:** an authorized issuer may sign a fabricated checkpoint that two witnesses validly confirm; witnessing does not prove truth about provider execution.
- **Common operator compromise:** root can read all three private witness keys, replace databases and change pinned trust roots. This is an OS UID boundary under a single administrator, not separate organizational custody or failure domains.
- **Mock provider:** the trusted effect set comes from the coordinator, not from independent API/provider readback.
- **IPC exposure:** socket mode 0666 and no caller authorization allow any local Unix user reaching the service to submit a signed issuer checkpoint. The witness checks issuer signatures but has no rate budget, client identity attestation or service protection. This is acceptable only as a clearly labeled research fixture.

## Reproducible exact bytes

Artifact `foromni_exp26_isolated_witness_evidence.zip`, SHA-256 `e0ab7a0608f0e9caae4aa39c0ccd436fc7ec27e8dd7ab428ee345045603b2a52`.

| File | SHA-256 |
|---|---|
| `protocol.py` | `9c9ee453460fea262f83323b67703f38267d171f3216e2f09173f08498132432` |
| `witness_service.py` | `0300edae364d0dbdaf00648cefd377cb68b55f743297688415ba67ce74ef710f` |
| `test_experiment.py` | `f2f065e6470a87dfb225518bafb8f1a181cdc00872aa16b40976e16d5e8cfd01` |
| `README.md` | `4885e9aadb3673a2e9098ea7062cd774d10140e87970f024f6beac76169e240f` |
| `batch_1.txt` | `4235d9a9c169b52fa9955ae53d895f7f252031131a6d1213bc93d7cc6677bd71` |
| `batch_11.txt` | `8d6d30bd229b08e1fb4015d9cd84974078903666f4069de7eb24cb2c37f4a1f0` |

**Distribution:** runnable implementation, tests and two exact local test outputs are in the ZIP shared with the user. The GitHub branch receives this **scientific AAR only**; it is not a committed production implementation and no GitHub CI was run.

## Limitations and future work

- No independent administrative domains: three keys and databases are isolated by unprivileged UIDs but the root test coordinator controls everything. True independence requires separately operated witness trust and pinned remote trust roots.
- No client authentication or safe socket permissions: add `SO_PEERCRED`, per-issuer policy, bounded IPC request sizes, timeouts, release signing, rate limits, privilege separation from test root, and journal hardening.
- No independent provider effect source, crash-after-external-effect recovery, network partitions, key rotation/revocation, transparent gossip/fork proofs or outside audit.
- Repeated process creation/teardown is slow; next version should use shared fixtures or bounded service lifecycle and a single clean CI test run.
- This is not cryptographic audit-completeness proof, Byzantine consensus or an external security certification.

**Suggested EXP-27:** independent mock provider process/credentials with authenticated effect-readback, plus restricted client-to-witness IPC and mutually pinned trust anchors; test malicious client requests, witness restart/key rotation, and signed issuer claims contradicted by true provider effect IDs. Then obtain separately authored/approved evaluator fixtures.

**Verdict:** `EXP26_20_OF_20_CHECKS_PASS_IN_TWO_SEPARATE_BATCHES`; `SPLIT_UID_WITNESS_AND_RESTART_REPRODUCED`; `INDEPENDENT_OPERATOR_CUSTODY_AND_PROVIDER_TRUTH_UNPROVEN`; `FOR007_UNCHANGED`.
