# Foromni H0 Runner Case Studies — Source-Led Selection v0.1

**Status:** Public upstream documentation/source review plus a benign host inventory. **No runner installed, built, invoked or benchmarked in this pass.** External code was not copied, and no Git permissions or production resources changed.  
**Date:** 2026-11-21. **Scope:** Foromni only. IE separately owns its private future case study.
**Input experiments:** H0-M (18/18 selected classification matches), H0-S (24/24 synthetic DAC permission checks) and H0-R (3/3 nested user+network namespace observations); see their signed-off limits in Foromni research, not a claim of certified isolation.
**Comparison question:** What is the minimum defensible runner for the *future* H0-A one-worker / separate QA experiment, with exact source/evidence custody, denied egress, untrusted Python code, bounded costs and no production GitHub write credential?

## 1. Evidence standard

Evidence tags:
- **UPSTREAM-DOC:** an upstream statement about a tool, not a local capability or independent audit.
- **HOST-OBSERVED:** benign, read-only local inventory or previously recorded controlled Foromni probe; not proof of complete sandbox enforcement.
- **INFERRED/PROPOSAL:** our design recommendation or predicted integration burden.
- **NOT TESTED:** requires separately authorized proof on a disposable runtime.

Every tool must be pinned to an immutable release/source SHA, dependency inventory and license at actual installation. Today's referenced upstream pages are living sources, not an immutable compatible build.

## 2. Source-based case studies

### Case A — Native Linux namespaces + minimal launcher (baseline)

**Source / mechanism:** user, network, mount and PID namespace features from the Linux kernel; caller must supply root filesystem bind policy, mount propagation restrictions, capability reductions, seccomp filtering, resource quotas and teardown. A namespace on its own is NOT a sandbox security guarantee.

**HOST-OBSERVED:** H0-R found `unshare --net` directly returned EPERM, but `unshare --user --map-root-user --net --mount --pid --fork` succeeded 3/3, child only saw `lo` and had no IPv4 routes. A benign local TCP attempt failed. This is a narrowly scoped environment observation. H0-S's DAC file permissions separately denied selected reads/writes. The observations do **not** demonstrate safe evaluation of arbitrary source code, seccomp, executable mount visibility, IPv6/Unix sockets, cgroups or independent custody.

**Advantages:** no third-party runtime, fastest to understand the kernel controls one by one, minimal cold-start overhead expected (NOT MEASURED), best *control arm* for a simple runner comparison.

**Risks:** many security controls left for Foromni to implement, review and keep correct; inheriting the host root tree by mistake, Linux capability exposure, procfs/device leakage, inherited FDs and child-process cleanup are significant design hazards. A homemade launcher should not become the default production isolation boundary based only on H0-R.

**H0 verdict:** Keep as a **research control/reference**, not automatically production runner.

### Case B — Bubblewrap / bwrap (first practical H0-A candidate)

**Upstream:** https://github.com/containers/bubblewrap and https://github.com/containers/bubblewrap/blob/main/README.md  
**UPSTREAM-DOC:** bwrap starts with an empty mount namespace/root on tmpfs; the caller explicitly binds what it should see, may unshare network and PID namespaces, pass seccomp filters, clear environment variables and create a new session. The README specifically warns about using `--new-session` when `TIOCSTI` is not otherwise denied; host D-Bus sockets exposed into a sandbox can undermine the boundary. Source: https://github.com/containers/bubblewrap/blob/main/README.md and https://github.com/containers/bubblewrap/blob/main/bwrap.xml .

**Meaning for Foromni:** a small wrapper can mount a read-only pinned Python runtime and source snapshot, one writable scratch area, no host home, no environment credentials, no network and no privileged sockets. The evaluator must run independently and keep its suite/secret root out of worker mounts. bwrap is a mechanism, not a complete approval/budget/QA system. Require an outside supervisor for process/CPU/memory limits and command interruption.

**License caution:** upstream NEWS records a licensing update from LGPL-2.0-or-later to LGPL-2.1-or-later in newer releases. Do NOT quote one version-independent license or copy source without inspecting chosen release notices. https://github.com/containers/bubblewrap/blob/main/NEWS.md .

**Host:** `bwrap` was absent from PATH in the read-only host inventory. **NOT TESTED** here.

**H0 verdict:** **Top candidate to evaluate** *after* explicitly authorized installation, hardened configuration and independent denial tests.

### Case C — Docker Engine rootless

**Upstream:** https://docs.docker.com/engine/security/rootless/ ; https://docs.docker.com/engine/security/rootless/tips/ ; https://docs.docker.com/engine/security/rootless/troubleshoot/

**UPSTREAM-DOC:** rootless mode runs Docker daemon and containers as a non-root user to reduce daemon/runtime privilege exposure. Rootless resource-limit flags (`--cpus`, `--memory`, `--pids-limit`) are supported only with cgroup v2 and systemd configured appropriately; otherwise they can be ignored. Rootless networking is provided through RootlessKit and its user-mode network stack. **Rootless does not mean “no egress” or “limits definitely enforced.”**

**Meaning for Foromni:** container image/OCI packaging may become useful as the worker ecosystem grows, with reproducibility and established tooling. But requires a daemon, runtime, image provenance, actual cgroup/egress validation, base image hardening, socket/volume/secret controls, and evaluator isolation.

**Host:** docker executable not present; no Docker daemon or rootless cgroup driver verified. **NOT TESTED.**

**H0 verdict:** Backup option if bubblewrap is unavailable or prebuilt OCI images prove materially easier. Do not add it solely for a one-function baseline.

### Case D — gVisor / runsc (stronger syscall isolation candidate)

**Upstream:** https://gvisor.dev/docs/architecture_guide/intro/ ; https://gvisor.dev/docs/user_guide/rootless/ ; https://gvisor.dev/docs/user_guide/platforms/ ; https://github.com/google/gvisor .

**UPSTREAM-DOC:** gVisor's Sentry acts as an application kernel that intercepts Linux system calls, reducing direct host kernel exposure compared with namespaces-only containers. It has multiple platforms, including a systrap approach that does not require KVM; KVM is an optional platform and may be preferable on compatible bare-metal hosts. Rootless operation is documented. The documentation warns that `runsc do` is a quick convenience tool that grants read-only host filesystem access by default; **never use such defaults as the H0 confinement policy.** License: Apache-2.0 at upstream license.

**Meaning for Foromni:** candidate for executing less-trusted multi-provider worker code once a runnable container spec, image and source-custody path exist. Adds runtime compatibility, image/spec management and performance considerations. Candidate code still must be denied network/secret/output authority via explicit policy.

**Host:** `runsc` not installed; no KVM device, but systrap may avoid that dependency. No gVisor syscall compatibility or performance measured here.

**H0 verdict:** **Second-phase isolation challenger**, not needed before simpler H0 sandbox mechanics are proven.

### Case E — Firecracker microVMs (future hostile-workload isolation challenger)

**Upstream:** https://github.com/firecracker-microvm/firecracker/blob/main/docs/getting-started.md ; https://github.com/firecracker-microvm/firecracker/blob/main/docs/prod-host-setup.md ; https://github.com/firecracker-microvm/firecracker/blob/main/docs/jailer.md .

**UPSTREAM-DOC:** uses the KVM Linux kernel module and requires read/write `/dev/kvm`; provides guest kernel/hardware virtualization separation. Production guide calls for the `jailer` or equivalent restrictions, plus ongoing host hardening and patching. A Firecracker process by itself is not a complete secure multi-tenant hosting service. Upstream license Apache-2.0.

**Meaning for Foromni:** potential future boundary for hostile code, stronger tenant isolation and remotely provisioned evaluation; requires KVM-capable machine, microVM image/kernel management, jailer, networking, monitoring, patching, security and ops work. This would radically enlarge the H0 hypothesis.

**Host:** `/dev/kvm` absent, firecracker executable absent. **Not runnable on current observed host without a different authorized environment.**

**H0 verdict:** **Defer** until threat model, actual workload volume or evaluator results justify microVM hosting.

## 3. Comparative fit matrix — qualitative estimates, NOT benchmark scores

| Control / cost | Native namespace | Bubblewrap | Rootless Docker | gVisor runsc | Firecracker |
|---|---|---|---|---|---|
| Host availability NOW | Partial kernel features observed | Not installed | Not installed | Not installed | KVM unavailable |
| Explicit minimal rootfs visibility | Must implement | Strong documented primitive | OCI mounts/image policy | OCI rootfs plus Sentry | Guest image + jailer |
| Network restriction | Partial namespace observation | Built-in namespace option; verify | Explicit network configuration; verify | Explicit network policy; verify | Host/guest network policy; verify |
| Syscall isolation | Must add seccomp | Can add seccomp | Default seccomp/profiles configurable | Sentry application kernel | Separate guest kernel/KVM |
| CPU/memory/PID enforcement | External resource controller | External controller | cgroup driver/config dependent | Container/cgroup configuration | VM/vCPU/memory plus host/jailer limits |
| Trust-separated independent QA | External to runtime | External | External | External | External |
| Expected initial integration effort | Low code count, **high security-design burden** | Low/moderate | Moderate | Moderate/high | High/new host |
| Primary H0 role | Baseline/control | **Preferred trial runner** | Alternative packaging | Isolation challenger | Future escalation |

No cells claim an observed security PASS except expressly noted H0-R namespace capability. All alternatives need independent enforcement tests; the weakest exposed host mount, socket, privilege or credential determines actual security.

## 4. Additional lessons from real AI coding sandbox implementations

This is *comparative design evidence*, not a proposal to adopt the products:
- OpenAI Codex Linux sandbox source shows layering: bubblewrap for filesystem view and `seccomp` / `PR_SET_NO_NEW_PRIVS` for syscall/principal restrictions, rather than relying on a namespace alone: https://github.com/openai/codex/blob/main/codex-rs/linux-sandbox/src/bwrap.rs .
- Anthropic's open source sandbox-runtime docs describe Linux bwrap integration and version compatibility limits, reinforcing that wrappers and actual mount/session decisions are essential: https://github.com/anthropics/sandbox-runtime/blob/main/README.md .

**Takeaway:** a runner is only one component in the independently verified execution pipeline. Keep admission policy, authoritative identity, source custody, evaluator ownership, billing and release authority outside the runner.

## 5. Proposed staged evaluation, not yet authorized

### R0 — Readiness and build admission
Choose a pinned release and license, immutable artifacts, fixed OS/kernel, named operator, allowed mounts, path allowlist, OCI/bwrap profile, permitted syscall set, no root host credentials, no Docker/host socket and disposal rules. No “all green” if setup silently falls back to weaker security.

### R1 — Benign confinement assertions
For each candidate runtime, test *exact same* synthetic:
1. Read worker allowed input (must work).
2. Write dedicated scratch (must work).
3. Read hidden evaluator fixture (must fail).
4. Write evaluator result, including through symlink/hardlink (must fail).
5. List/access host home and parent source tree (must fail).
6. Network IPv4, IPv6, loopback/Unix sockets and DNS behavior (must match explicit policy).
7. Inherit host environment and file descriptors (must expose no token).
8. Process/UID/capability/mount/PID namespace inspection (must show intended restrictions).
9. Verify CPU/memory/PID ceiling with bounded benign resources, under supervisor.
10. Kill/reap/time out, clean scratch, restart with clean state and unchanged trusted digests.

### R2 — Controlled untrusted candidate evaluation
Only after R1 actually passes and is independently reviewed, allow disposable AI-generated Python candidate code in an evaluator sandbox without production tokens or network. Compare Bubblewrap against the native namespace baseline with identical source, judge and environment; record rejection of all dangerous effects, setup latency, startup overhead, successful candidate time and all costs. A side-effect denial check that cannot be safely staged must remain UNTESTED.

### R3 — gVisor challenger
Only if observed R2 risks justify: evaluate gVisor systrap with same cases and reproducibility guarantees. If bubblewrap meets a bounded risk model, do not automatically add gVisor complexity.

### R4 — VM escalation
Only after approved KVM-capable host is available and risk/cost justify a guest-kernel boundary. Do not move to Firecracker merely because it is more sophisticated.

## 6. Adoption decision rule

Prefer the **minimum runner that meets every mandatory safety gate** for the specific environment, with separately authenticated evaluator custody and no production credentials. Compute all costs, not just runtime startup latency. A “faster but unsafe” runner fails regardless of lower overhead. If Bubblewrap cannot enforce a required boundary under this host, stop; evaluate a stronger option rather than weaken gate criteria.

**Next Foromni research priority:** write a version-pinned Bubblewrap R0 admission profile and a cross-runner R1 checklist; obtain separate approval before installation or execution. **Do not resume H0-A until the runtime proves actual boundaries.**

## Sources and traceability

Upstream primary sources listed inline above; living URLs should be replaced by immutable commit/release references in the *accepted* R0 installation decision. Host inventory in this pass: Linux kernel 6.18.57, UID 0 for research process; `unshare`, `prlimit`, `setpriv` available; `bwrap`, `docker`, `podman`, `runsc`, `firecracker` absent; `/dev/kvm` absent. These are capability observations, **not a security audit**.

**Current decision:** Case studies complete as a research comparison. No runner passes R1, H0-A remains BLOCKED. No independent evaluator or source-host protection change is implied.

*Build today, so others can enjoy tomorrow.* ❤️🐂
