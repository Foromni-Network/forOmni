# EXP-12 — Linux seccomp socket-creation confinement vs broker communications: Executed AAR

**Date:** 2026-11-23. **Scope:** Foromni research only; disposable local Linux process test; no Internet Embassy changes, no real MCP/OAuth, no deployment, no privileged protected-main writes, no CI, no external traffic or production secrets. **Outcome:** 11/11 local Python unit/integration tests PASS, `ResourceWarning` treated as error.

## Question and controls

Following EXP-11's failed network-egress negative control, can a local worker process deny ordinary TCP/UDP socket creation while retaining approved AF_UNIX broker communication? What *specifically* escapes this restricted policy?

**Positive control:** unrestricted worker connects to an owned local TCP endpoint on 127.0.0.1.

**Treatment:** child sets `PR_SET_NO_NEW_PRIVS`, then uses `libseccomp.so.2` to install BPF rules returning EPERM from `socket(AF_INET, ...)` or `socket(AF_INET6, ...)`. The filter survives exec. All tests are local and standard-library Python aside from the Linux system libseccomp.

**Negative control:** coordinator intentionally passes a *pre-connected* local TCP file descriptor into the worker via subprocess `pass_fds`. The restricted worker writes through this inherited socket, proving new-socket filters **do not block all network I/O**.

**Environmental restriction:** `unshare -n true` returned `Operation not permitted`, and the container did not have CAP_NET_ADMIN. Thus **network namespace isolation was not run or verified**. The substitute is limited syscall mediation, not equivalent to a full network sandbox.

## Exact locally observed results

Command:
```bash
cd foromni_exp12_seccomp
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py
```

Observed `Ran 11 tests in 11.340s / OK`; 0 errors/failures and no resource warnings.

| Case | Local observation |
|---|---|
| Unrestricted TCP connection to owned loopback service | PASS (positive control) |
| Child new IPv4 TCP socket under seccomp | EPERM / PASS |
| Child new IPv4 UDP socket under seccomp | EPERM / PASS |
| Child new IPv6 TCP socket under seccomp | EPERM / PASS |
| Child approved AF_UNIX broker socket | Connected and received ack / PASS |
| Filter remains effective after `exec` | IPv4 socket still denied / PASS |
| Child's filter does not alter coordinator socket permissions | PASS |
| Child dropped to UID/GID 21103 still denied IPv4 TCP | EPERM / PASS |
| Child dropped to UID/GID 21103 still denied IPv4 UDP | EPERM / PASS |
| Unprivileged child still allowed configured AF_UNIX path | PASS |
| Pre-opened connected TCP descriptor deliberately inherited | **BYPASS OBSERVED / NEGATIVE CONTROL PASS** |

The last case is **not** an egress-security success. It is a demonstrated residual network path.

## Evidence and reproducibility

Exact tested bytes in `foromni_exp12_seccomp_evidence.zip`, attached to the experiment response:

| Artifact | SHA-256 |
|---|---|
| `egress_guard.py` | `7a5cecc9ba8551fd477974a2fed7658b19694c6d7ffb85fc653c52addaf16f02` |
| `worker.py` | `bd34cfcadf5343366c2bbab87ce018448c1b604d9e845ae59595beefc5265578` |
| `test_experiment.py` | `8177558970c0f6506483720054d0071d0105b07dc33ecd3019f4e4a6563722a4` |
| `test_output.txt` | `67439cc436a739f203e126fdb67c04c358454ccf7b7e574ff8aa960266e9abb4` |
| `README.md` | `f61024af3e17d43952ace4fb00e35a588cd631ba72c2bdfb56a783092cd2a4c7` |
| ZIP SHA-256 | `7657772d357d6df75868d60527cf86f66e07fb2d96799e77a94e6665c8f0a750` |

**Distribution:** The exact runnable source and logs are in the evidence ZIP; this GitHub commit contains the written study, not a source-tree import or executed GitHub CI proof.

## Limitations and security implications

- Denying `socket(AF_INET)` and `socket(AF_INET6)` is **not complete network egress policy**. A passed, inherited or SCM_RIGHTS-transferred connected descriptor can still perform I/O; Unix-domain proxies can also bridge to network. Other allowed address families and syscalls require policy review.
- `libseccomp` installed a narrow filter on child processes; this is no proof against compromised parent/root, ptrace, library abuse, inherited descriptors or sandbox escape. A production policy needs a closed descriptor table, independently controlled worker entrypoint, Unix broker request validation, mandatory mediation, network namespace/firewall or equivalent egress proxy, and security observability.
- UID 21103 is synthetic test data; do not reuse on a sensitive host without checking account conflicts. Tests used only owned loopback ports and Unix socket paths, not actual provider networks or DNS resolution.
- No true independent QA/agent providers or public services were involved. Experimenter authored source and checks.
- Test count is not a reliability, security coverage or statistical attack-resistance rate.

## AAR decision and next gate

**Practical progress:** EXP-11's unguarded TCP connection was stopped for *new sockets* under an installed OS policy while approved local broker communication continued. A real bypass was measured, preventing false promotion to "network isolated."

**Next discriminating research** should test sanitized descriptor inheritance and a mandatory egress proxy / supported network namespace in a disposable runner; audit whether worker can reach loopback, DNS, metadata, remote TCP and Unix proxy paths with a full egress allowlist. In parallel investigate live MCP tool schema/issuer verification and separately operated evaluator/source QA only in authorized test environments.

**Verdict:** `EXP12_PARTIAL_SOCKET_CREATION_CONFINEMENT_PASS`; `EXP12_PREOPENED_FD_BYPASS_DEMONSTRATED`; `EXP12_FULL_EGRESS_ISOLATION_NOT_PROVEN`; `FOR007_UNCHANGED`.
