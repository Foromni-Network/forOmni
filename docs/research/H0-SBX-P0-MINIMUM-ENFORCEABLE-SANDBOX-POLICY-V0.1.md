# Foromni Sandbox Admission Contract — H0-SBX-P0 v0.1

**Status: PROPOSED, UNAPPROVED, UNTESTED.** Foromni-only research, 2026-11-21.  
**Sources:** `EXPLORATORY-OPENAI-ANTHROPIC-AND-OSS-AGENT-SANDBOXES-V0.1.md`, `H0-RUNNER-CASE-STUDIES-AND-HYBRID-SELECTION-V0.1.md`, `ADR-E0A-002-INDEPENDENT-REVIEWER-CUSTODY-AND-PATCH-ONLY-TRIAL.md`. No installation, benchmarking, runner process or test executed by this document.

## 1. Contract: one governed task lease, one disposable sandbox

A sandbox is created only from a **trusted, frozen task lease**, never from natural-language worker instructions. Its durable identities are separate: `agent_id` (logical worker), `incarnation_id` (session), `task_id` and `attempt_id` (assignment), `sandbox_id` (ephemeral runtime), `grant_id` (effective permission), `base_sha` and `candidate_sha` (observed source). No one identifier authorizes another.

**H0 default:** offline single worker, synthetic source only, patch-out, no network, no GitHub API, no real user data, no model credentials or evaluator files in the worker namespace. The worker cannot change, sign or approve its own policy, source provenance, grader or verdict.

## 2. Proposed immutable profile `h0-offline-v1`

| Policy dimension | Required effective behavior | Failure condition |
|---|---|---|
| Start identity | Unprivileged effective UID/GID; fresh user namespace; `no_new_privs`; no inherited privileges or supplementary groups | Root-host capabilities, privileged helper access |
| Filesystem read | Empty-root by construction where available; explicit readonly runtime, public task file and minimal required shared libraries; no host home, checkout parents, `.git`, evaluator fixtures or provider configuration | Broad host root read or access to QA/secret paths |
| Filesystem write | Only single scratch/candidate directory; allowed patch paths checked again by trusted source observer | Write outside scratch, dangerous mounted socket/device |
| Filesystem symlink/hardlink | Resolve real paths and deny unexpected bind/alias paths; protect source/QA with separate ownership and mounts | Traversal or link escape to host/evaluator |
| Network | New network namespace with no external interface/routing, no proxy/socket exception, explicitly disallow IPv4/IPv6/AF_VSOCK escape; deny inherited connected FDs | Any unapproved host/Internet path or unknown outcome |
| IPC/process | New PID/IPC namespace when supported; minimal `/proc`; no host D-Bus, Docker socket, `/dev/kvm`, systemd or SSH agent; supervisor kills/reaps descendants | Host process visibility or lingering child |
| Syscalls | Explicit reviewed seccomp profile (incl. socket-family, `io_uring`, mount, ptrace, keyring and dangerous namespace operations); capability drop | Missing filter or silently downgraded profile |
| Resource ceilings | Independently enforced wall-clock, memory, CPU, file descriptor, process count, output size, disk use and retry limit; measure enforceability on actual host | Unsupported/ignored limit; not just setting CLI flags |
| Secrets | No shared GitHub token, service key, auth cookie, evaluator holdout or master model API key; controlled gateway only in later authorized networked stages | Any privileged credential visible to child |
| Source custody | Worker exports diff/patch; source observer reconstructs against frozen base and records exact clean candidate Git SHA | Worker-provided SHA accepted unverified |
| QA custody | Separate authenticated evaluator process/identity and protected suite/results; candidate executes inside evaluator-owned isolation | Worker can read or alter oracle/grade |
| Startup and teardown | Unknown/unsupported kernel features fail closed; verify mount/process/network state; terminate all descendants, clean scratch and revoke lease | Fallback to unsandboxed execution or abandoned process |
| Logs/economics | Externally observed resource usage, test runs, limits, denied operations, all trial/human/provider costs; privacy-safe retention | Worker self-report treated as authoritative |

**H0 is intentionally stricter than a general coding tool:** the agent cannot install packages, fetch dependencies or use an outbound inference endpoint from inside the sandbox. Any real AI worker should receive approved inference via a separately governed adapter, not a direct unrestricted child network connection.

## 3. Permission precedence and revocation

1. Effective policy is the **intersection** of organization maximum, founder-approved task scope, current lease/expiry, administrator runner constraints and independently enforceable host limits; agent requests can only **narrow**, never broaden.
2. Explicit deny wins over allow for restricted/secret paths, even when nested inside a writable directory. The policy compiler must canonicalize paths including symlinks, mount points and Git worktree gitdir references and reject ambiguous overlap.
3. A permission change creates a new version of the lease/policy digest. **H0 grants are immutable during execution**: stop and recreate sandbox instead of live relaxation. Later brokered network grants must be short-lived, scoped and independently checked at operation time.
4. Every external action requires the broker's effective grant, not one inferred from model messages, environment variables or generated source. Lost acknowledgment produces `UNKNOWN` until readback, never blind replay.
5. Missing policy, unsupported kernel control, unexpected inherited socket, unverifiable quota or failed cleanup means **NO_GO**. A technical workaround does not change required protections without a separately documented reviewer/founder decision.

## 4. Reference layering and selection

**From OpenAI Codex:** trusted permission profiles, layered bwrap + no-new-privs/seccomp, protected control files, explicit proxy boundary, documented launcher fallback; do not inherit Codex's broad read-root policy as H0 default.

**From Anthropic srt:** independent command wrapper, distinct static filesystem vs dynamic network policy, host proxy/decider; no network broker is necessary for offline H0.

**From Bubblewrap:** explicit minimal mount namespace and narrow binds; *caller must create security policy*. **From NsJail:** one-shot Linux isolation with seccomp, rlimits and cgroups as first-class controls. **From gVisor/Firecracker:** stronger isolation challengers if observed limitations justify additional runtime or KVM host costs.

Choose **one** runner for a given worker attempt. A second sandbox for evaluator is a distinct trust boundary; do not run both under a common writable credential. Each adapter must report actual effective limits and fail closed, not merely support flags.

## 5. Phase gates

- **P0 (this document):** freeze/approve minimum policy and test inventory; result is *paper-ready* only.
- **P1:** pinned Bubblewrap and NsJail releases/dep/license/security review; package admission authorized separately.
- **P2:** identical R1 benign confinement probes against each installed runner, independent evidence and effective resource quotas.
- **P3:** independent source + evaluator custody, incorrect candidate and fake PASS challenges within evaluator isolation.
- **P4:** first approved real AI coding worker using patch-only output; H0-A can then produce data on accepted behavior per full cost.
- **P5:** compare approved brokered-network architecture only when a task truly needs network; do not import srt/OpenShell/Temporal prematurely.

**No-Go until:** separate owner authorization, trusted reviewer and process identities, exact runtime/lease/host source versions, declared funding/time/retry limits, verified isolation and actual benchmark evidence. Current H0-S and H0-R results are capability observations and cannot be promoted into P2 PASS.

*Build today, so others can enjoy tomorrow.* ❤️🐂
