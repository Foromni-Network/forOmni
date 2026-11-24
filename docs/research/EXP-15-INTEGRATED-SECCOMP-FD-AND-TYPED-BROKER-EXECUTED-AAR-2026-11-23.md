# EXP-15 — Integrated Worker Confinement + Task-Scoped Unix Broker (Executed Local AAR)

**Date:** 2026-11-23 (America/Chicago) / 2026-11-24 UTC. **Project:** Foromni only. **Status:** `12/12 local Python unittest PASS`, ResourceWarnings promoted to errors; 0 final warnings. **Location:** disposable Linux test container. **Changes:** research report only on `research/global-agent-roadmap-execution`; no frozen FOR-007 mutation, protected merge, real API/MCP provider, paid operations or Internet Embassy changes. The exact runnable experiment is supplied as `foromni_exp15_integrated_evidence.zip` in the research conversation; **not uploaded as GitHub source files**.

## Scientific question and hypotheses

EXP-13 established file-descriptor launch hygiene with seccomp but found a generic AF_UNIX proxy bypass. EXP-14 established a typed broker and audited denies, but did not integrate seccomp or a separate unprivileged worker. Can the source controls be converged in **one single actual worker subprocess** that runs under an unprivileged Unix UID, blocks new TCP/UDP sockets, talks to the typed broker over AF_UNIX, and performs one allowed mock draft operation while rejecting unauthorized operations?

**Prediction:** the integrated path works for a tightly scoped operation; denied operations produce no provider effect, duplicate requests do not create new mock effects, and new AF_INET creation is blocked. Negative controls should still reveal bypasses through explicitly inherited TCP connections or independent public Unix proxies. No prediction of complete egress confinement.

## Implementation and local execution

- Reused `egress_guard.py` **exactly** from EXP-13 (Linux libseccomp deny AF_INET/AF_INET6 socket creation).
- Reused `typed_broker.py` **exactly** from EXP-14 (strict `draft.create` operation, signed test grant, typed arguments and resources, `SO_PEERCRED` UID, persisted SQLite operations/mock provider effects).
- Wrote `worker.py`: installs seccomp, then dispatches local AF_UNIX typed-broker request; also offers test-only network and inherited-FD probe modes.
- Wrote `test_experiment.py`: launches a real worker subprocess under **UID/GID 21103** using root-owned test coordinator `setgid/setuid`; launches with `stdin=DEVNULL` except typed request input, `close_fds=True`, `pass_fds=()` by default; creates broker in coordinator and deliberately makes only broker socket world-connectable in the disposable fixture, relying on broker's peer credential and signed test grant for effective authorization. This is **not** a recommended production socket-permission setup.
- Provider mock and broker share a single SQLite ledger in the coordinator, so this **does not** repeat EXP-10's three independently separated service UIDs or remote-effect recovery model.

**Final observed command:**

```sh
cd foromni_exp15_integrated
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py
```

**Actual result:** `Ran 12 tests in 12.913s / OK`. A first same-UID integration run also passed 12/12; then actual worker identity was changed to synthetic UID 21103 and entire suite rerun successfully. No CI or external QA performed.

## Twelve observed cases

| Case | Observation |
|---|---|
| Allowed `draft.create` through Unix broker | ACCEPT + one mock effect |
| New IPv4 TCP socket from seccomp worker | Blocked / PASS |
| Sanitized subprocess inherited connected TCP FD | Not accessible / PASS |
| Explicitly passed connected TCP FD | **BYPASS observed** / negative-control PASS |
| `proxy.connect` attempted via typed broker | Denied; 0 effects |
| Cross-project resource request | Denied; 0 effects |
| Extra MCP-like prompt instruction in tool arguments | Denied as schema mismatch; **not** an actual LLM prompt-injection study |
| Duplicate request via AF_UNIX | One provider effect |
| Revoked policy | Denied |
| Expired signed demonstration grant | Denied |
| Separate public Unix proxy | **Accessible** / negative-control PASS |
| Rebuilt broker on same SQLite DB | Original request returns; one mock effect |

**Crucial:** passing negative-control assertions means an unsafe condition was successfully reproduced. It does not mean egress protection is complete.

## Exact locally executed artifact SHA-256 values

| File | SHA-256 |
|---|---|
| `typed_broker.py` | `a64b5be057c9c07eed0320b868be8b113b7dc0dd16e0f115abf717e48925870d` |
| `egress_guard.py` | `7a5cecc9ba8551fd477974a2fed7658b19694c6d7ffb85fc653c52addaf16f02` |
| `worker.py` | `ddebffbaaa829de7ec9bf77b1ac308cb73def4587415d700c37a94d1aae6216c` |
| `test_experiment.py` | `aec6506fda8b78f88f4f0494a7a32a6f70c06da94dedf0f8ae36e8b56027341f` |
| `README.md` | `4b2aaae92dcc4dc01de381e68642c84c14b6f3bd13eaf217c84c032fe498e113` |
| `test_output.txt` | `f95653be889d4818a414cc2b135577b201106ddfbb7f6d37f350ee13b9595d1d` |

The downloadable archive includes exact source/test/output plus `SHA256SUMS`. Reproduce only on an authorized disposable root-capable Linux host with libseccomp and available UID 21103; do not run the root test coordinator on a production host.

## Limitations and next gating experiment

- **No complete network egress containment**: arbitrary public Unix proxies and passed connected TCP FDs still work; an authenticated broker alone cannot prohibit external brokers/proxies. Require explicit AF_UNIX reachable path allowlist, descriptor hygiene, validated broker protocol and host-level network/IPC boundary.
- **No full role separation**: test worker has distinct UID; broker and mock provider run in same coordinator. Root can access all files and keys. No external confidential token custody or independently authenticated reviewer.
- **No real provider-side distributed effect**: single SQLite database ensures model atomicity; no live OAuth/MCP, network provider or uncertainty after real remote effect. No measured cost/performance.
- **No complete prompt-injection assurance**: string rejected as extra argument; LLM was not exposed to malicious tools/results. No independent source-bound QA of the candidate.
- **No production license/contribution terms set**: Foromni ↔ AINO code import/export research is separately proposed; no code donation from IE was made.

**Recommendation:** Next EXP-16 should test mandatory mediation at the Unix socket/network boundary using a capability-focused broker service and OS-level per-worker IPC constraints in an environment that actually supports enforced network namespaces, proxy allowlists or equivalent. Explicitly test inherited/SCM_RIGHTS FDs, peer identity, distinct connector credentials and post-effect crash. Advance into source-bound independent QA and license-compliant reusable packages only after those controls are demonstrably enforced.

**Verdict:** `EXP15_INTEGRATED_UNPRIVILEGED_WORKER_12_OF_12_PASS`; `EXP15_TYPED_BROKER_REJECTS_UNAUTHORIZED_REQUESTS`; `EXP15_PUBLIC_UNIX_PROXY_AND_INHERITED_FD_BYPASSES_STILL_EXIST`; `FULL_RUNTIME_NETWORK_CONFINEMENT_NOT_PROVEN`; `FOR007_UNCHANGED`.

**Related:** [EXP-13](EXP-13-FD-SANITIZATION-UNIX-PROXY-AND-SECCOMP-AAR-2026-11-23.md), [EXP-14](EXP-14-TYPED-UNIX-BROKER-NO-ARBITRARY-PROXY-EXECUTED-AAR-2026-11-23.md), [AINO licensing/update research](FOROMNI-AINO-BIDIRECTIONAL-LICENSING-CONTRIBUTION-AND-UPDATE-EXCHANGE-RD-V0.1.md).
