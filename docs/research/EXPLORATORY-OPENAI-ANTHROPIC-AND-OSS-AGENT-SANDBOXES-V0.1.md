# Foromni AINO — Exploratory Study of AI Coding Sandboxes: Codex, Anthropic SRT and Open Alternatives

**Status:** Source-linked exploratory research; **no sandbox was installed, run, forked, copied, audited, benchmarked or independently verified in this pass.**  
**Date:** 2026-11-21. **Scope:** Foromni only, not Internet Embassy. **Parent studies:** H0-RUNNER-CASE-STUDIES-AND-HYBRID-SELECTION-V0.1.md, H0-R-LOCAL-RUNNER-NAMESPACE-CAPABILITY-AUDIT-2026-11-21.md, ADR-E0A-002-INDEPENDENT-REVIEWER-CUSTODY-AND-PATCH-ONLY-TRIAL.md.  
**Central question:** What should a Foromni agent's first trusted workspace be, and how should its policy, resources and source/evaluation handoff remain independently governed?

## 0. Terms: four different things called a “sandbox”

1. **Kernel execution boundary:** filesystem and process isolation, network path enforcement, credentials, IPC, syscall filtering, resource quotas. Failure can affect host/users.
2. **Agent permission model:** approval and escalation, files/domains allowed, temporary scoped grants, policy change authority. A prompt is not enforcement.
3. **Agent working environment:** writable project tree, shell, dependency cache, model tools, language runtime, test data and disposable lifetime. Usability and performance matter.
4. **Independent evidence boundary:** patch/source custody, evaluator-only oracle, genuine test execution, cost receipts, no self-approval. A sandbox that safely runs code does **not** automatically provide this.

The AINO sandbox should be an **instance of a governed task lease**, not an agent's permanent identity or a hidden organizational superuser. Its existence is necessary for work, but source acceptance and release are separate powers.

## 1. OpenAI Codex — source-linked case study

**Primary source:** OpenAI, “Inside the Codex sandbox” (2026-11-18), https://openai.com/index/inside-the-codex-sandbox/. **Pinned public source:** [openai/codex, commit 59edd0d512a9fc1660f2ecf6562c803051b90faa](https://github.com/openai/codex/tree/59edd0d512a9fc1660f2ecf6562c803051b90faa/codex-rs/linux-sandbox), especially `README.md`, `src/linux_run_main.rs`, `src/bwrap.rs`, `src/seccomp.rs`. License observed from GitHub repo metadata: Apache-2.0 (verify any vendored subcomponents before reuse).

### Observed source mechanism

- **Permission profiles** encode filesystem scopes and network domains; layered user/project/managed configuration constrains which permissions a task may request. The harness, not the model, resolves escalation and executes commands.
- **Linux layered launcher:** `bwrap` constructs the filesystem/namespace view; a re-executed `codex-linux-sandbox` launcher inside it applies `PR_SET_NO_NEW_PRIVS` and seccomp restrictions, then executes the actual command.
- The current pinned README describes bubblewrap as the default filesystem mechanism, with legacy Landlock available only for some older modes; it explicitly notes Landlock is inadequate for isolating certain Unix sockets.
- Read-only host filesystem view may be created with `--ro-bind / /`, then narrowed writable mounts; protected paths including `.git`/resolved gitdir and `.codex` are re-applied read-only. **This is not equivalent to exposing only a minimal empty-root filesystem:** allowed read scope and hidden home files still need review.
- For network restrictions, Codex can use a **host-side HTTP/SOCKS5 approval proxy**, with direct egress blocked inside the namespace. It employs a relay/listener via Unix descriptor handoff so the private namespace can reach only the proxy. Environment proxy variables are helpers, not the only confinement enforcement.
- Seccomp restrictions differ across direct-deny/proxy modes. The pinned source also documents blocking `io_uring` to prevent socket filter bypass, and blocking `AF_VSOCK` in relevant cases. These are important bypass classes for Foromni's threat model.
- The source README identifies **an inherited-PID-mode cleanup limitation**: certain background descendants may survive if supervisor/relay lifecycle fails. Treat process-tree/kill/reap as mandatory experiments, not an assumed property.

### Foromni interpretation

**Strong transferable ideas:** policy compiled by trusted harness; multiple independent Linux controls layered; tool-specific escalation remains outside worker; host-side network authorization; protected workspace metadata (`.git`, evaluator results) re-mounted read-only; explicit failure and fallback reporting.

**Do not copy uncritically:** whole-root read visibility may be too broad for a multi-project AI organization; system bwrap/bundled fallback changes binary provenance; proxy connectivity creates an intentionally privileged egress channel that needs separate audit and rate/spend caps. Nor does Codex's command sandbox automatically prove that hidden QA tests or GitHub merges cannot be self-approved.

**Foromni hypothesis:** adopt the *permission profile → compiled confinement → independently observed action → evidence* pattern, but prefer a minimal read-only runtime/root and disposable source mounts for H0.

## 2. Anthropic Sandbox Runtime (srt) — source-linked case study

**Pinned public source:** [anthropics/sandbox-runtime, commit 0bbebed0aa9a8e628dc4df8bc30293550a1988eb](https://github.com/anthropics/sandbox-runtime/tree/0bbebed0aa9a8e628dc4df8bc30293550a1988eb), `README.md`, `src/linux-sandbox-utils.ts`, `docs/srt-proxy.md`. GitHub repo metadata reports Apache-2.0. Upstream labels this **beta research preview**, so pin releases and check configuration compatibility before trying it.

### Observed source mechanism

- Reusable `srt` CLI and TypeScript API wraps arbitrary subprocesses, not only one coding model. The same approach applies to local MCP servers and tools.
- Linux runs through Bubblewrap with a separate network namespace and carefully bound Unix proxy sockets; macOS uses Seatbelt; current README also describes a separate Windows account/WFP/ACL implementation (not interchangeable security properties).
- **Distinct read/write rules:** current README describes reads as *allow broadly, deny sensitive paths and re-allow specific exceptions* while writes default to denied except explicitly allowed locations. This asymmetry is significant: for Foromni we should require a separately frozen **read** allowlist, not only a write allowlist.
- Network egress uses a host-side HTTP/SOCKS proxy with domain rules. Direct connections from sandboxed Linux processes lack a normal host network path; programs ignoring proxy environment variables generally fail to connect rather than automatically bypassing the namespace.
- Current source describes **live policy updates**: network allow/deny rules can change per request; startup filesystem mounts and selected credential masking cannot be loosened/tightened in a running process. On disconnect, update channels can retain the previously applied config; a Foromni trust system must explicitly choose whether revoked network grants must fail-closed.
- The standalone `srt proxy` mode delegates individual request decisions to an **external decider**, a useful reference pattern for action-time policy that stays outside untrusted code.
- Other documented escape-relevant boundaries include host Unix sockets, inherited descriptors, proxy startup/ownership, and Windows system-service-mediated traffic. No claim that a wrapper alone confers a sealed VM.

### Foromni interpretation

**Strong transferable ideas:** a reusable sandbox-tool adapter; external proxy/decider contract; explicit *static versus dynamic* permissions; command-agnostic wrapping; MCP server confinement separate from agent chat UI.

**Open questions:** what exact failure behavior is safe when policy update channel dies, how filesystem-read defaults are tightened for multi-tenant use, what per-operation network identity is recorded, how proxies prevent credential disclosure and how to enforce full resource quotas. Current srt behavior is source evidence, **not a deployed Foromni control**.

**Foromni hypothesis:** use external-decider semantics for network/tool actions in future H3–H5; keep H0 fully offline and use the wrapper only if verified requirements justify a dependency.

## 3. Additional open-source comparators

| Project | Pinned/read source | Mechanism worth studying | Potential Foromni role | Why not automatically import |
|---|---|---|---|---|
| [Bubblewrap](https://github.com/containers/bubblewrap/tree/1fb0aa26d3eb66254f7742e704add7f82f41a582) | `README.md` at `1fb0aa26d3eb66254f7742e704add7f82f41a582` | Create empty mount root, explicit binds, user/PID/network namespaces; no-new-privs | Minimal Linux confinement primitive | Upstream explicitly says **not** a complete security policy; exposed sockets, session, FDs and root mounts remain caller's problem |
| [Google NsJail](https://github.com/google/nsjail/tree/ec259a3edb34c3b138fbad859c09e0e70259ff8b) | `README.md` at `ec259a3edb34c3b138fbad859c09e0e70259ff8b` | Namespaces, `pivot_root`, seccomp Kafel rules, resource rlimits and cgroups, configurable one-shot/re-run modes | **Serious near-term alternative** to bwrap, because quotas and syscall policy are first-class | Config complexity, installed dependencies, host-specific cgroup privileges and effective deny behavior need testing |
| [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell) | Public official README, architecture/security docs (live; **commit not pinned in this pass**) | Separate supervisor/gateway, kernel-enforced filesystem/system-call policy, brokered egress and controlled attached providers | **Organizational policy architecture comparator** for H3+ | More infrastructure and lifecycle than the first tiny H0; maturity, performance and actual enforcement must be tested; no source/version compatibility claim |
| [Landlock Rust library](https://github.com/landlock-lsm/rust-landlock) | Official docs/library (not source-pinned here) | Unprivileged filesystem access restrictions under LSM | Layer/restriction research for narrowly scoped workloads | Landlock alone does not replace network namespace, token/IPC and evaluator separation |
| [gVisor](https://github.com/google/gvisor) | Official architecture docs (prior case study) | User-space application kernel isolates direct Linux syscall surface | Later challenger for hostile worker code | Runtime image integration and compatibility overhead; not installed/benchmarked |
| [Firecracker](https://github.com/firecracker-microvm/firecracker) | Official getting-started/jailer docs (prior case study) | Separate guest kernel via KVM microVM | Future high-risk/multi-tenant worker tier | H0 host lacks `/dev/kvm`; microVM provisioning, image and host cost unnecessary now |

**Potential hybrid is NOT** OpenAI Codex + srt + NsJail + OpenShell + gVisor installed simultaneously. Most overlap in execution enforcement. Design neutral interfaces, compare the smallest admissible alternatives, choose one primary boundary per risk tier, and keep supervisor/broker/QA duties independent.

## 4. Convergence result: sandbox-first organization, without a sandbox monoculture

```text
Founder/authorized objective and contract revision
         |
Trusted organization registry (logical agent != provider API key)
         |
Task lease + policy limits + cost ceiling + allowed paths/tools
         |
Trusted policy compiler / dispatcher  <--- authenticated decisions
         |
Disposable worker execution boundary  [one selected runner]
   | read: frozen minimal starter + runtime
   | write: isolated work tree only
   | network: denied (H0); brokered when specifically authorized
   | secrets: no organization/provider master keys in child
         |
Untrusted patch + logs + proposed events
         |
Source observer independently reconstructs exact Git SHA
         |
Independent evaluator in SEPARATE isolation + sealed oracle
         |
Trusted evidence / cost receipts / approval decision
         |
Potential future protected integration + independently authorized release
```

**Separation rule:** sandbox instance ID, persistent agent ID, task ID, source revision, policy grant and authenticated action principal are different objects. A sandbox cannot approve itself, edit hidden tests, make its own policy effective, or upgrade its tool scopes through prompts. On runtime restart, revive *work history* only after rechecking the current lease and permissions.

### Proposed neutral runner contract (research draft)

```text
create(lease, immutable_runtime_digest, read_mounts, write_mounts, quotas, network_mode)
  -> opaque sandbox_id + observed host policy digest
exec(sandbox_id, command, expiry, authenticated_operation_grant)
  -> observed exit, stdout/stderr refs, resource usage, side-effect records
export_patch(sandbox_id, allowed_paths)
  -> untrusted patch artifact + digest
terminate(sandbox_id, reason)
  -> observed descendants exit + cleanup evidence
```

Network modes should be **NONE, BROKERED or explicit unrestricted**; the latter excluded from H0 and subject to separate approval in later stages. A claimed runner capability is not a granted ability. Missing host feature, failed mount, policy-build error, optional missing binary or disconnected broker must not silently trigger unsandboxed execution.

## 5. Most important new research gaps

| ID | Question uncovered | Early validation that would actually answer it |
|---|---|---|
| SBX-01 | Does policy compilation have permission-precedence ambiguity, especially read vs write? | Conflicting allow/deny nested paths; inspect effective mounts and contents |
| SBX-02 | Can network proxy approval be bypassed via IP sockets, IPv6, AF_UNIX, AF_VSOCK, io_uring or leaked FDs? | Benign isolated denial tests, exact syscall/endpoint inventory; distinguish blocked from absent |
| SBX-03 | Are `.git`, workspace control files and hidden evaluator tests effectively immutable? | Attempt read/write/symlink/hardlink and verify outside-owned source digests |
| SBX-04 | What happens to a broker authorization when policy service dies/revokes mid-command? | Disconnect/revoke scenario, prove no new external action after grant expiry |
| SBX-05 | Can a child survive timeout/parent crash, or reach another process through procfs/IPC? | PID tree/cgroup/capability inspection, bounded safe process cleanup |
| SBX-06 | Does filesystem isolation leak host secrets via full-root reads or mounted user homes? | File visibility inventory from inside child under least-read policy |
| SBX-07 | How are direct provider API credentials kept outside the worker while allowing approved inference? | Authenticated model broker + no child access to master secret |
| SBX-08 | Can an already-accepted candidate SHA be substituted or cached across different patches? | Independent SHA check, QA suite digest, deliberately wrong patch and absent tests |
| SBX-09 | How expensive is each sandbox tier and where does it actually improve accepted outcomes? | Repeated cold start + teardown, memory/CPU, QA acceptance and human-minute measurements |
| SBX-10 | What upstream code can legally be reused? | Source-path license and dependencies at frozen release; explicit provenance and attribution |

These are **questions**, not observed Foromni vulnerabilities. Their inclusion does not imply probes were run.

## 6. Decision matrix for first actual follow-up

| Candidate | Value to test | Decision for H0 next |
|---|---|---|
| Native `unshare` prototype | Mechanism baseline; H0-R partially observed | **Control only; no arbitrary-worker admission** |
| **Bubblewrap policy adapter** | Minimum reviewed Linux process boundary, under a hand-written strict profile | **First controlled candidate** after R0 admission and authorization |
| **NsJail one-shot** | Comparable namespaces plus explicit resource/syscall controls | **Second candidate**, may surpass bwrap if quota evidence decisive |
| Anthropic `srt` wrapper | Reusable external network decider and MCP confinement | **Architecture comparator**; only trial when proxy/allowed-network tasks start |
| OpenAI Codex Linux helper | Integrated policy profiles, re-exec seccomp, bridge proxy | **Reference design**, not a plug-and-play generic runner |
| NVIDIA OpenShell | Network/tool permission supervisor for agent organization | **H3+ study**, not H0 bootstrap |
| gVisor/Firecracker | Additional isolation boundary for later malicious/multi-tenant workloads | **Defer pending actual risk results** |

### Suggested study ordering

**S0 — policy-model paper freeze:** choose minimal read/write mount visibility, no egress, process/resource ceilings, forbidden socket/proc/dev exposure and exact failure behavior.

**S1 — bounded benign admission:** compare Bubblewrap and NsJail on identical read/write/socket/capability/limits/cleanup fixtures, if founder separately authorizes packages/runtime and local tests. Require independent reviewer and exact image/package versions.

**S2 — small real worker:** only after S1 demonstrates effective boundaries, resume H0-A using one approved coding worker, patch-only output and source-bound evaluator.

**S3 — introduce brokered networking:** selectively test srt/OpenShell-style deciders once a task actually requires approved network access. Revocation and auditability are mandatory.

**S4 — larger teams:** candidate pool/scheduling/agent relationships only after H0 shows independently verified benefits.

## 7. Research conclusions / guardrails

- **Codex:** strongest lesson is explicit *permission profile → layered kernel enforcement → host proxy/escalation* with a tested command launcher.
- **srt:** strongest lesson is a portable *sandbox wrapper → distinct static filesystem and dynamic proxy policy → external decider*.
- **NsJail:** strong missed contender from the first runner comparison because built-in cgroup/rlimit and seccomp options may remove the need for a custom quota supervisor.
- **OpenShell:** strongest organizational lesson: policy **belongs to the trusted control plane**, not the agent's worktree or model memory.
- **Foromni-specific insight:** treat sandbox lifecycle, persistent agent identity, authorization, independent evidence and organizational learning as **separate layers** that can be improved/changed without rebuilding the whole network.

**Do not treat vendor publications as independent penetration test reports or general security proofs.** No copied source, new dependency, Linux probe, CI run, merge, deployment, credential grant, paid runtime or outreach occurred in this study. All local runner security claims remain limited to H0-S/H0-R observed scenarios.

*Build today, so others can enjoy tomorrow.* ❤️🐂
