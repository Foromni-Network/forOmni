# H0-R — Runner Isolation Capability Audit (2026-11-21)

**Status:** BENIGN LOCAL PROBES EXECUTED, with raw evidence in conversation bundle. **NOT** a complete secure sandbox, independent security review or AI-worker trial. Foromni only; no IE access, Git main writes, deployment, new services or cloud spend.

## Scientific question

H0-S previously reported `unshare --net` -> `Operation not permitted`. Is the limitation a hard prohibition on creating an isolated network namespace, or can a user namespace be created first and used to create a separate network namespace?

This local audit tested both methods, captured process exit and namespace/interface/route state, and repeated the nested probe three times. A local TCP socket to `127.0.0.1:9` was attempted **inside** the new namespace; no external request or untrusted code was used.

## Observations

| Probe | Result | Scope of evidence |
|---|---|---|
| Direct `unshare --net /bin/true` | Exit 1, Operation not permitted | Direct namespace setup fails |
| Nested `unshare --user --map-root-user --net --mount --pid --fork` | Exit 0 in **3/3** corrected repetitions | Namespace construction works under this environment |
| Network namespace identity | Distinct from host in 3/3 | Actual separate Linux net namespace |
| Interfaces visible in child | `lo` only (host has `lo` and `eth0`) | No external host NIC visible |
| IPv4 route table | Zero route entries in 3/3 | No configured IPv4 route |
| Connection to `127.0.0.1:9` | `ENETUNREACH` errno 101 in 3/3 | Local socket did not connect; loopback not brought up |
| Docker, Podman, Bubblewrap, runsc, Firecracker executables | Not found | No existing runner installation observed |
| `/dev/kvm` | Not found | Cannot assume Firecracker available on this host |

**Protocol correction:** Initial script computed route count as `len(lines)-1` and classified -1 routes when `/proc/net/route` was wholly empty, leading to an incorrect 0/3 match count. Corrected to `max(0,len(lines)-1)` and reran all three repetitions: **3/3 expected observations matched**. The initial result is an experimenter measurement bug, not a failed nested namespace creation.

## Result and interpretation

**H0-S-B01 has been narrowed:** Network namespaces are not categorically unavailable on this host. Direct `unshare --net` remains unavailable, but *user namespace first* permits nested network+mount+PID namespace creation in a benign test. This is a specific, reproducible environment capability observation, **not** proof of a trustworthy arbitrary-code runner.

**Still unverified and blocking untrusted AI-generated code:** Seccomp policies, capability drop, mount whitelist, cgroup CPU/memory/process quotas, evaluator and worker authenticating as separate trust principals, restrictions on network reconfiguration/IPv6/DNS, candidate runner isolation, external side effects and guaranteed absence of host credentials. Tests here were started by one root-controlled operator.

**No external binaries were installed.** Do not treat Docker rootless, Bubblewrap, gVisor or Firecracker as deployed options. Official project references identify future candidates, not observed capabilities in this environment.

## Evidence and provenance

The local conversation artifact `foromni_H0R_runner_audit_bundle.zip` includes:
- `probe.py` (benign exact local probe);
- `results.json` (three corrected repetitions, host observations);
- `EXPERIMENT_REPORT.md` (method, correction, limitations, next gate).

Bundle SHA-256: `e00c4cfaaf8c7e49b2759b47fcd804913689fec9d7a28ca36e48bb268082881f`. The raw bundle **is not part of this GitHub commit**, so the research doc is a summary rather than self-contained independently duplicated evidence.

## Runner choice for next experiment

Prefer a **disposable local namespace runner only after** separately demonstrating required mount/capability/syscall/resource/network/security boundaries and independent evaluator custody. If a requisite kernel control cannot be enforced locally, use a separately authorized isolated runner such as an appropriately configured OCI runtime or microVM, rather than installing multiple orchestration frameworks.

**H0-A remains BLOCKED.** More isolation gates, not more agent agents, are the limiting work.

*Build today, so others can enjoy tomorrow.* ❤️🐂
