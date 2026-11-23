# EXP-11 — Hardening a Process-Isolated Agent Broker: Executed Research AAR

**Date:** 2026-11-23. **Project:** Foromni only. **Repository target:** existing `research/global-agent-roadmap-execution` branch. **Result:** 25/25 local Python unittest cases PASS, with ResourceWarnings treated as errors. **Experimental artifact:** `foromni_exp11_boundary_evidence.zip` supplied with the research conversation, containing tested source, test suite, test output and SHA256SUMS. **The runnable Python source is in the ZIP; this GitHub commit records the report, not live integration.** No FOR-007 change, CI, protected merge, production MCP, public port, or spending.

## Experiment objective

Follow EXP-10's verified local Unix-identity isolation and investigate four next security questions:

1. Are task grants denied when their expiry is past the actual broker OS clock or unreasonably far into the future?
2. Are malformed tool parameters, traversal/foreign resource names, overlong contents and unexpected request fields denied before calling a provider?
3. Can a worker still remotely trigger the broker's test crash injection?
4. Is worker network egress actually isolated, beyond denying access to the mock provider's protected Unix socket?

**Method:** Start from the exact EXP-10 local source archive and modify only the isolated `service.py` and `test_experiment.py`. Use distinct disposable Linux UIDs for worker/broker/provider, their existing protected Unix sockets, temporary distinct SQLite databases, in-process-generated test grants, and an owned local TCP socket for the egress *negative control*. Tests invoke unprivileged subprocesses and broker/provider OS processes. Tests are researcher-authored and no independent external QA principal inspected them.

## Observed development and test history

- Initial 24-case run had 23 passes and **one error**: the unbounded-future expiry test used a value too close to the one-hour cutoff, causing a test expectation mismatch around time. This was a test-design error; revised to an expiry 3,700 seconds ahead, clearly beyond the 3,600-second horizon. Full 24-case rerun passed.
- Added one **negative-control** test to check whether an unprivileged worker could create an ordinary TCP connection to a localhost listening socket operated by the trusted coordinator. It **could**. This is a deliberately demonstrated lack of network containment.
- Final invocation: `PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py`.
- **Final observed:** `Ran 25 tests in 25.357s / OK`, zero errors/failures or ResourceWarnings. These are software assertions on one local container—not an overall security grade.

## Specific results

| Tested boundary | Local observation | Interpretation |
|---|---|---|
| Worker/broker/provider have different Unix UIDs | PASS | Local OS identity separation |
| Worker denied broker signer key/provider token file reads | PASS | File permission protection against chosen unprivileged UID |
| Worker denied mock provider Unix socket | PASS | Unix socket DAC boundary holds |
| Allowed task-scoped draft | PASS | Known allowlisted action |
| Cross-project, admin, wrong peer UID, stale epoch, revocation | PASS | Broker-side synthetic policy denial |
| Expired OS-clock grant and grant > 1h future | PASS | Replacement of EXP-10's placeholder expiry check |
| Tool arguments with wrong operation, traversal, URL-shaped resource, oversized content | PASS (deny) | Typed fixture validation; not comprehensive URL/parser security |
| Unknown request fields | PASS (deny) | Unexpected control fields cannot enter action path |
| Client-supplied crash injection flag | PASS (ignored) | Old unauthenticated remote crash switch removed |
| Same request ID / concurrency / broker restart | PASS | One mock provider effect on stable ID under tested process/SQLite conditions |
| Local TCP egress from worker UID | **NEGATIVE CONTROL: CONNECTION SUCCEEDED** | **Network sandbox/egress denial not implemented** |

**Environment limitation:** `unshare -n` was attempted in the provided Linux environment and returned `Operation not permitted`; this prevents claiming a network namespace sandbox was tested. The remaining TCP test demonstrates accessible loopback, rather than an unauthorized external scan.

## Exact local-tested file hashes

| Artifact in accompanying ZIP | SHA-256 |
|---|---|
| `service.py` | `d0cd91dddb182b270303e0b673e88da1228dbbd11771a4d6d83a18a1f441f8ba` |
| `test_experiment.py` | `e8e9466cade9130f166e4457d8b853623e0e465667bb26ce5114b9a013346576` |
| `README.md` | `459c0b20a15fe4bb1d0d9b6d534482d8b8947da004d275bc1b3c90a58be532b6` |
| `test_output.txt` | `8a0d35f535ce06bd0343467f3e5a370bc6c6d2371f0e505784e173ae13803413` |
| Whole evidence archive | `3d0f83abdee47da8f1e45658d299ccfcff87819b1e268844baea5e0ad9e67cf3` |

Reproduce in a disposable/root-capable Linux sandbox with unallocated test UIDs 21101-21103 using the ZIP's README. Do not run in production hosts with conflicting UIDs or sensitive credentials.

## Honest AAR and go/no-go

**Meaningful improvement:** The grant expiry predicate now uses broker `int(time.time())` with a one-hour max horizon; structured arguments and unexpected request-field checks reject a set of undesirable input patterns; client-visible crash switch was removed; other process isolation and recovery tests remain passing.

**Not yet safe for production:**
- Ordinary loopback TCP egress is still available to the worker. Unix-socket access restriction does not imply network isolation. Do not allow untrusted workers to run with unrestricted network access.
- The test coordinator runs as root and knows signing material. No separate credible issuer, mTLS/client identity, secure time source, network namespace, container, eBPF/firewall egress policy, full resource path canonicalization or key vault.
- The checked `expires` value uses OS wall clock and a one-hour maximum, but no authenticated issuer timestamp, distributed clock skew policy, replay epoch ledger or expiry-driven active request cancellation.
- Content/metadata are still untrusted strings; no actual LLM or MCP server handled them, no prompt-injection resistance demonstrated.
- Mock provider is local, backed by SQLite, and supplies lookup/idempotency semantics. Real remote side effects, revocation races after effects and multi-host failure remain unknown.
- Worker can still submit many valid signed requests; lack of a durable cost/rate admission policy and quota is an unsolved denial-of-service/spend risk.
- No third-party independent source/evaluator review or signed exact-candidate source acceptance occurred.

**Next discriminating experiment:** Test an isolated worker with a real network egress boundary in a supported disposable VM/container environment (deny all except explicitly allowlisted broker path), rootless/unprivileged confinement where possible, and audit actual DNS/HTTP/metadata-service network denial. Independently verify source and provider effects using a distinct evaluator principal. Only after that consider disposable MCP SDK and real scoped OAuth adapter. If the runtime cannot enforce egress, record BLOCKED and do not claim the boundary.

**Verdict:** `EXP11_LOCAL_BROKER_HARDENING_25_OF_25_PASS`, `EXP11_EGRESS_ISOLATION_FAIL_NEGATIVE_CONTROL`, `EXP11_NETWORK_NAMESPACE_UNAVAILABLE`, `FOR007_UNCHANGED`.
