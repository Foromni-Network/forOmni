# H0 Sandbox R1 — Paired Bubblewrap vs NsJail Admission and Evidence Matrix v0.1

**Status:** FUTURE TEST PROTOCOL ONLY; no software installed or executed, no PASS asserted. 2026-11-21, Foromni only.  
**Policy under test:** `H0-SBX-P0-MINIMUM-ENFORCEABLE-SANDBOX-POLICY-V0.1.md`.  
**Case-study provenance:** `EXPLORATORY-OPENAI-ANTHROPIC-AND-OSS-AGENT-SANDBOXES-V0.1.md`. Compare the **effective policy**, not merely the presence of feature flags.

## Preflight record — must be filled by an authorized reviewer

Record exact kernel/OS, host user namespace settings, cgroup controller delegation, chosen signed or hashed bwrap/nsjail binary and source/release SHA, dependency and license inventory, `no_new_privs`, seccomp availability, mount policy digest, evaluator identity, source/evidence store identities, resource ceiling, allowed network and teardown/retention plan. Record explicit founder approval reference and experiment cost cap. If any mandatory control is not actually available, mark that runner NOT ADMISSIBLE; do not silently loosen profile or fall back to shell.

**Matched comparison setup:** same synthetic Python runtime, read-only input, writable scratch, worker UID, fixture digests, Q test suite, execution time/memory/process limits, and no provider credentials for each candidate; randomized runner order if repeated experiments later justify; all attempts and incomplete runs included. Container image, full runtime path and start mode are actual treatment variables and must be disclosed.

## R1 check registry (specified only; execution requires approval)

| Case | Target / expected result | Required trusted observation | Bubblewrap | NsJail |
|---|---|---|---|---|
| R1-01 | Read allowed public source succeeds | Actual child read + SHA matches frozen source | NOT RUN | NOT RUN |
| R1-02 | Write candidate scratch succeeds; write anywhere else fails | External file digest + denial exit | NOT RUN | NOT RUN |
| R1-03 | Hidden evaluator fixture read/write denied | Separate principal-owned fixture unchanged | NOT RUN | NOT RUN |
| R1-04 | Hidden evaluator verdict overwrite including symlink/hardlink denied | External verdict digest unchanged | NOT RUN | NOT RUN |
| R1-05 | Host home, .git, package tokens and SSH agent invisible | Mount graph and child path/socket checks | NOT RUN | NOT RUN |
| R1-06 | IPv4 outbound / raw-IP and local loopback denied by H0 offline policy | Actual socket errors and host-visible network check | NOT RUN | NOT RUN |
| R1-07 | IPv6 and AF_VSOCK denied, no unexpected inherited network FDs | Child socket outcomes + supervisor FD inventory | NOT RUN | NOT RUN |
| R1-08 | Unix sockets / D-Bus / Docker socket not usable | Attempts confined to synthetic or known nonprivileged endpoints; no host effect | NOT RUN | NOT RUN |
| R1-09 | Mount, ptrace, keyring, io_uring, capability escalation denied | Reviewed effective syscall profile + benign probes | NOT RUN | NOT RUN |
| R1-10 | No host process visibility via procfs, PID/IPC separated | Process namespace and /proc inspection | NOT RUN | NOT RUN |
| R1-11 | CPU, memory, PID, FD and output limits enforced | Supervisor events plus bounded benign load; no uncontrolled DoS | NOT RUN | NOT RUN |
| R1-12 | Timeout/parent death kills descendants | Separate observer checks process tree and scratch cleanup | NOT RUN | NOT RUN |
| R1-13 | Unsupported sandbox flag / broken security setup fails closed | Deliberately invalid policy is refused; never executes unsandboxed | NOT RUN | NOT RUN |
| R1-14 | Worker cannot change policy or ledger | Separate owner credential and external digest check | NOT RUN | NOT RUN |
| R1-15 | Candidate's changed source SHA invalidates old green verdict | Trusted S/Q reproduction of wrong/stale source | NOT RUN | NOT RUN |
| R1-16 | True/false PASS only from actual positive and negative tests | Independent Q reports exit+inventory, fake PASS rejected | NOT RUN | NOT RUN |
| R1-17 | Cleanup and reset for next trial | No surviving child, mount, socket or stale workspace | NOT RUN | NOT RUN |
| R1-18 | Full costs and failures counted | Independent operator accounting; partial costs flagged | NOT RUN | NOT RUN |

**Classifications:** `PASS` (observation under matched accepted configuration), `FAIL`, `NOT_RUN`, `UNKNOWN`, `INFRA_BLOCKED`. `EXPECTED_DENIAL` is a PASS **only when a real attempted operation was denied under an independently observed guard**; distinguish from `TOOL_ABSENT`. Record every raw exit, process observation, evidence hash and researcher correction. Missing mandatory evidence is a NO_GO, not an inferred PASS.

## Review and selection criteria

**Safety admission** is binary: every mandatory security case from R1-01..R1-17 must pass against exact accepted profile (or be explicitly out of scope by pretrial founder/reviewer agreement without weakening H0's baseline). Failed/unrun/unknown mandatory cases block H0-A.

**Performance comparison** only after both runners satisfy safety admission:
- `T_start`: supervisor initiation to child-ready time (median, dispersion and cold/warm distinctions).
- `T_exec`: identical benign task wall time.
- `T_teardown`: stop command to observed descendant/mount cleanup.
- `M_peak`, `CPU_seconds`, `IO_bytes`: outside-observed, with capture completeness.
- `Q_false_green`: number of intentionally wrong candidates independently accepted (must be zero for selected suite; not proof of universal immunity).
- `C_total`: full model+worker+runtime+QA+human costs including failures and retries; no fabricated prices.

Predeclare number of repeated trials, task variants and comparative analysis **before** collecting performance data. No numerical superiority claims from isolated feature support or anecdotal startup time.

## Candidate-specific gaps to settle before execution

### Bubblewrap
- Pin executable/library provenance and `--unshare-user`/network/mount/PID behavior on actual host.
- Use minimal rootfs binds instead of exposing full host root read-only.
- Ensure `--new-session` or effective `TIOCSTI` protection, trusted seccomp, `PR_SET_NO_NEW_PRIVS`, capability drop.
- External resource supervisor must enforce cgroup/rlimit/timeout and descendants. Prove failed mount/namespace setup never launches child outside policy.

### NsJail
- Pin runtime plus Kafel/protobuf dependencies, cgroup v2 delegation and seccomp policy.
- Review exact protobuf config and CLI precedence; explicit mount read/write and no host `/` exposure.
- Verify `rlimit` vs actual cgroup effectiveness and partial failures. A CLI resource flag does not prove bounded host resources.
- Record any privileged setup requirement. No setuid/privileged fallback without separate risk approval.

### Additional architecture comparator, not immediate runner
Codex-style permission compiler and Anthropic-style external network decider are future adapters. H0 remains offline. NsJail and Bubblewrap should not be stacked; stack independent safeguards around one selected execution engine.

## Decision template (intentionally blank)

```text
reviewer_identity:
founder_authorization:
policy_sha:
runtime_bwrap_source_sha:
runtime_nsjail_source_sha:
host_kernel_and_config_digest:
suite_fixture_digest:
expected_cases: 18
observed_case_results_bwrap: NOT_RUN
observed_case_results_nsjail: NOT_RUN
unresolved_security_gates: 18
cost_reconciliation: NOT_STARTED
decision: NO_GO_FOR_UNTRUSTED_AI_CODE
reason: No authorized R1 execution or independent isolation attestation
```

**Next action after paper review:** obtain scoped founder approval before installing or running runners; independently execute benign R1 first, then decide whether H0-A can proceed. No Git main merges, CI, deployments or IE data flows are implied.

*Build today, so others can enjoy tomorrow.* ❤️🐂
