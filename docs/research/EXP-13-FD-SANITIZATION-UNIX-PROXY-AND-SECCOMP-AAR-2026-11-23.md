# EXP-13 — Sanitized Worker FDs, Seccomp Broker Route and Unix Proxy Bypass (Executed Research AAR)

**Date:** 2026-11-23. **Project:** Foromni only. **Scope:** local Linux disposable synthetic research. **Status:** 14/14 final executable tests PASS with Python ResourceWarnings treated as errors; final rerun **Ran 14 tests in 14.537s, OK**. No Internet Embassy changes, live MCP server, external provider, privileged Git integration, new cron deployment, or FOR-007 modification.

## Research question and falsifiable prediction

After EXP-12 demonstrated that a preconnected TCP FD can bypass a seccomp policy denying new IPv4/IPv6 sockets, does launching the worker with `close_fds=True`, `pass_fds=()` eliminate that bypass while preserving a broker's AF_UNIX socket? A separate negative control checks whether a **publicly reachable AF_UNIX proxy** can still connect to TCP on the worker's behalf.

**Prediction:** sanitized launch closes an intentionally inheritable preconnected socket; deliberately passing that FD reintroduces bypass; controlled broker AF_UNIX works; a private Unix path denies the unprivileged user; a public Unix-to-TCP bridge defeats any claim of universal network egress prevention.

## Local implementation and actual test

- `egress_guard.py`: copied exact EXP-12 Linux libseccomp guard (`PR_SET_NO_NEW_PRIVS`; EPERM from `socket(AF_INET)` and `socket(AF_INET6)`). Unchanged source hash matches EXP-12.
- `worker.py`: launch-time filter installation, new-socket negative checks, inherited FD exercise, Unix broker/proxy connection and descriptor inventory under `/proc/self/fd`.
- `test_experiment.py`: creates exclusively owned local 127.0.0.1 TCP endpoints and temporary Unix socket paths. Worker subprocess uses explicit `stdin=DEVNULL`, `stdout/stderr=PIPE`, `close_fds=True`, and empty `pass_fds` by default; separate negative-control test explicitly opts into `pass_fds=(150,)`. Tests repeat under unprivileged synthetic UID/GID 21103.
- `README.md`, `test_output.txt`, `SHA256SUMS` in the downloadable evidence archive.

**Reproduce:**
```bash
cd foromni_exp13_fd_broker
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py
```
Requires Linux with libseccomp and a disposable root-capable test environment with no conflict at UID/GID 21103. Do not run unreviewed as a real sandbox.

## Exact observed acceptance matrix

| Local test | Observed |
|---|---|
| New AF_INET TCP, AF_INET UDP, AF_INET6 TCP sockets | denied / PASS (3) |
| Unprivileged child new TCP denied | PASS |
| Fresh worker's enumerated socket descriptors | zero / PASS |
| Fresh unprivileged worker's socket descriptors | zero / PASS |
| Coordinator passes an intentionally inheritable pre-opened connected TCP FD, but subprocess defaults to `close_fds=True, pass_fds=()` | child cannot use FD and peer receives no message / PASS |
| Same pre-opened FD explicitly put in subprocess `pass_fds` | **bypass reproduced**: child sends through inherited TCP / NEGATIVE CONTROL PASS |
| Normal AF_UNIX broker | reachable, returns ACK / PASS |
| Explicit public AF_UNIX broker from unprivileged UID | reachable, returns ACK / PASS |
| Private AF_UNIX socket mode `0600` with root owner | denied to worker UID with EACCES / PASS |
| Public AF_UNIX proxy, created by privileged test coordinator, forwards worker's PING to owned TCP loopback endpoint | **proxy bypass reproduced** / NEGATIVE CONTROL PASS |
| Unprivileged worker still denied direct TCP while allowed broker communication | PASS |
| Sanitized worker retains ordinary stdio/tests | PASS |

**Note:** the 14 count is unit/integration test methods, not independent security trials or 14 distinct threat actors. The bypass tests passing mean the deliberately unsafe condition occurred, **not that the system is secure from those conditions**.

## Reproducible bytes

| File in evidence ZIP | SHA-256 |
|---|---|
| `egress_guard.py` | `7a5cecc9ba8551fd477974a2fed7658b19694c6d7ffb85fc653c52addaf16f02` |
| `worker.py` | `b73b64f9f420b55affe2aae2aa80ed83fba017c32be4c7233b056fc0c9d463ca` |
| `test_experiment.py` | `afbd888682bec6a3d6cca8862bab5614e2149eb1d4442150dbb7ce62f8f74d44` |
| `README.md` | `2a28e8c7e11bb4837632fc79a40977533f2f88ecf0017d71946b194771ec5244` |
| `test_output.txt` | `f681ee8a4e5b6c6c082ae42d721bb81af99f30d59a8d05b4aa5a9d35a59ecc2d` |
| Full archive | `710e2f1d4c5fc9116a1d983e7ffc96cd1be4b0db417820c6d8d4420978b99013` |

**Source disposition:** Runnable exact code and test output are provided in `foromni_exp13_fd_broker_evidence.zip` in the research response. **This GitHub commit is the research report only**, not CI, source-tree integration or remotely pushed sandbox code.

## Interpretation and security limitations

**Supported locally:** process launch hygiene closes deliberately inheritable FDs and prevents EXP-12's inherited connected TCP leak in this particular Python child; AF_UNIX allows approved broker communications, while DAC on private Unix path blocks one unprivileged UID.

**Material remaining weakness:** a generic publicly reachable Unix-socket proxy can forward to TCP. Thus `socket(AF_INET/6)` syscall denial **does not constrain what other processes do on a worker's behalf**. Explicit broker admission, per-tool/project/resource authorization, peer UID attestation, strict protocol validation and provider-side scopes are necessary. An allowed broker must not expose arbitrary proxy or SSRF behavior.

**Unproven:** all FDs and file descriptor passing in a large production launcher, SCM_RIGHTS transfer, `connect` on inherited non-socket descriptors, AF_UNIX access by path only against malicious local services, network namespaces/firewalls, other socket families, DNS lookup/proxying, real MCP SDK tool semantics, signed evaluator source custody, real credential escrow and distributed partial failure. Root test harness can bypass isolation. The current tests do not prove complete containment, resistance to compromised host or production security.

## After-action and next gate

The *security condition* needs to be defined as **no unauthorized effects**, not merely "worker cannot open TCP." For EXP-14, use a **broker that handles only a strict typed, allowlisted protocol** (never a generic proxy) and an independent effect ledger. Test malicious URL-like MCP tool arguments and AF_UNIX socket abuse through the broker. Add a separately controlled evaluator source hash and a provider connector with restricted action/resource scopes in a disposable environment. If the host still lacks network namespace support, record `FULL_EGRESS_CONFINEMENT_BLOCKED` rather than promoting a partial syscall filter.

**Verdict:** `EXP13_FD_LAUNCH_SANITIZATION_PASS`, `EXP13_UNIX_PROXY_BYPASS_DEMONSTRATED`, `EXP13_FULL_NETWORK_EGRESS_CONFINEMENT_NOT_PROVEN`; frozen FOR-007 unchanged.

**Prior:** [EXP-12 inherited-FD AAR](EXP-12-SECCOMP-EGRESS-BROKER-SOCKET-AND-FD-BYPASS-AAR-2026-11-23.md); [agency communications](AGENCY-COMMUNICATION-ORCHESTRATION-TRANSPORT-ROADMAP-V0.1.md).
