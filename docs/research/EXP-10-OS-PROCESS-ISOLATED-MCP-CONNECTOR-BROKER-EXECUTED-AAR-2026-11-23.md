# EXP-10 — OS-Level Worker/Broker/Provider Isolation and Restart Recovery (Executed)

**Date:** 2026-11-23 · **Scope:** Foromni research-only, disposable Linux local sandbox. **Status:** executed real operating-system identity separation, 18/18 local Python tests PASS with zero ResourceWarnings. No production service, live MCP server, OAuth provider, real connector, protected Git merge, deployment, spending, Internet Embassy change or frozen FOR-007 mutation.

## Scientific question and controlled hypothesis

Would placing a synthetic worker, capability broker and mock connector/provider under three **different Unix users and distinct processes**, combined with filesystem and Unix socket permissions, stop the worker from obtaining the broad provider credential or calling it directly? Could a provider-side idempotency ledger preserve a single external effect if the broker dies after the effect and then restarts?

EXP-9's negative control demonstrated that anyone holding the mock provider token could bypass the broker. EXP-10 changes the **actual OS permission boundary**, not just Python predicate checks. The working hypothesis predicted that a worker UID would be denied direct provider socket access and private key reads, while a broker UID with explicitly shared permission could perform one allowlisted draft operation, then recover from a crash by querying the independent provider-effect ledger.

## Experimental setup and ownership

The local coordinator, running as root only in the disposable test container, created separate private data directories and files and fork/exec-launched three real process identities:

| Role | Synthetic numeric UID | Access |
|---|---|---|
| Provider | 21102 | Owns provider SQLite effect ledger and protected Unix socket |
| Broker | 21101 | Owns HMAC test signing-key file and task SQLite ledger; receives permission to connect to provider socket via shared group 21110; can read mock provider credential |
| Worker | 21103 | No broker signing key, no provider credential, no provider-socket permission; may connect to broker's public Unix socket only |

The broker uses Linux `SO_PEERCRED` to bind a signed test grant's UID to the socket peer and checks project/task/action/resource/epoch plus a revoked flag. The provider uses SQLite to idempotently record synthetic effects by stable effect key; the broker independently persists operations in its own SQLite file. The provider protocol and worker request are line-delimited local JSON, **not MCP/A2A or an authenticated Internet API**.

The root coordinator issues test grants. Root can read all secrets and modify files; this is not a root-adversary containment experiment.

## Observations, failure and repair history

1. **First setup attempt failed before tests:** SQLite DB files were writable only to their designated unprivileged users, but their parent directory was root-owned and not writable; provider could not write SQLite's journal. This was a real setup blocker, not a security test pass. Resolved by per-service owner-writable data directories while retaining worker restrictions.
2. **Next test run:** all 16 initial assertions passed, but there were SQLite connection and process cleanup warnings. The tests were revised to close DBs and properly reap/reassign the restarted broker process in class-scoped fixtures.
3. **Final run:** `PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py` → **Ran 18 tests in 18.012s, OK; zero ResourceWarnings**.

### Exact final-run source hashes (SHA-256)

| Artifact in downloadable evidence ZIP | SHA-256 |
|---|---|
| `service.py` | `6ec27221cb950a1e6b8eeaf4bea0f7c1e3693bc6785177843111ba325507377e` |
| `test_experiment.py` | `6dc41e88a621fe295ba90d29c50ab0a937af122e601a64fa5dd1257b635018ab` |
| `README.md` | `01f984084ff599e010357590e8b6bd5f494db9ec3501d8b6505a6168cef7cbef` |
| `test_output.txt` | `deeee31803b3607136defc6a25a2d837946b581acaf67a152b9696517ac42639` |

The `foromni_exp10_process_isolation_evidence.zip` downloadable research artifact contains the exact tested source, full test output and SHA256SUMS. **This GitHub research commit is a documented report; the runnable code has not been pushed into GitHub's source tree.** This intentional distinction avoids claiming remote CI/integration that did not occur.

## Actual acceptance matrix

| Case | Observed |
|---|---|
| Distinct broker/provider OS identities | PASS |
| Worker cannot read test signing/provider credential files | PASS |
| Worker cannot connect to provider Unix socket | PASS |
| Broker executes one allowed synthetic draft | PASS |
| Signed admin tool request denied by broker | PASS |
| Signed cross-project request denied | PASS |
| OS peer UID mismatch denied even with a correctly signed grant | PASS |
| Tampered grant signature denied | PASS |
| Old lease epoch denied | PASS |
| Revoked project/task policy denied | PASS |
| Duplicate request returns existing mock provider effect | PASS |
| Same request ID with changed payload denied | PASS |
| Six concurrently submitted requests record one provider effect | PASS |
| Broker force-exits after provider effect; fresh broker process reconciles without duplicate effect | PASS |
| Privileged-looking tool metadata does not expand tool permissions in deterministic mock handler | PASS |
| Provider socket mode and owner verified as 0660/provider UID | PASS |
| Unauthorized same-request-ID variation rejected | PASS |
| Revocation following a successful operation prevents subsequent new effects | PASS |

**Interpretation:** local OS permissions and socket peer credentials materially improved on EXP-9's in-memory security boundary. Broker recovery after a genuine process crash returned the existing mock effect without duplicating the provider ledger entry. These results test a **single-host, test-coordinator-owned, deterministic fixture**, not a hostile multi-tenant production system.

## Important flaws and remaining gates — no false assurance

1. **Expiry check is a placeholder, not real time:** this experimental broker currently checks `expires < 1`, rather than authenticated wall-clock expiry. The experiment therefore **does not prove expiration enforcement**. Fix the clock and time-window verification in the next revision; do not use this broker for live grants.
2. **Root remains fully trusted:** root or compromised group member could read shared credentials. Separate process UIDs and mode 0660 protect only against the tested unprivileged worker, not privilege escalation, container escape, inherited descriptors or kernel bugs.
3. **Worker can connect to public broker socket:** signed grant restricts actions in this fixture, but there is no traffic quota, admission/rate limit, genuine issuer attestation, source-bound QA, separate end-user identity or denial-of-service resistance.
4. **Grant signing key and provider token are files on the same host**, not hardware/managed secret custody. Signing tests are generated by the root coordinator; no external issuer/revocation service.
5. **Provider still accepts the broad token if stolen**. Network segregation, private service identity, short-lived provider scopes, mTLS and provider-side restrictions are not implemented. The provider could be invoked with a privileged action by an entity that acquires both socket access and token.
6. **No authentic remote side effect:** provider and broker use distinct SQLite files, not different machines. Transaction and network failure models remain simplified. Provider idempotency and authoritative lookup are assumed.
7. **The crash injection flag is test-only and client-controlled in this fixture.** A production client must never be able to force broker exit; keep fault injection in an authenticated test harness outside the request surface.
8. **Tool description injection was inert JSON text** and no actual LLM processed it; prompt injection/SSRF, DNS egress, sandbox escape and real MCP OAuth were not tested.
9. **No independent QA principal:** the assistant created the candidate, tests and experiment; separate Unix roles are not an independently hired/authorized reviewer.
10. **Runtime permissions may vary by host/security policy** and the numeric UIDs are test data, not provisioned production accounts.

## Experiment disposition and engineering roadmap

**Locally established:** the workflow can enforce a concrete OS boundary against one unprivileged worker UID and maintain one simulated provider effect through concurrent retries and broker process restart. **Not established:** production connector isolation, cryptographic owner-grant issuance, genuine expiration, distributed exactly-once semantics, live MCP security or globally federated worker isolation.

**Next discriminating EXP-11:** move expiry to trusted current time; remove client-controllable crash injection; add per-UID rate/budget guard, validate structured tool arguments and provider resource normalization. Perform a separate source-bound evaluator on the actual tested code and run a local network-namespace/egress-denial fixture where the worker cannot reach even a known provider URL. Keep it safe, local and research-only. Then evaluate a real disposable MCP SDK under explicit authorization.

**Verdict:** `EXP10_LOCAL_OS_IDENTITY_ISOLATION_18_OF_18_PASS`; `EXP10_SINGLE_EFFECT_RECOVERY_PASS`; `EXP10_REAL_EXPIRY_AND_PRODUCTION_ISOLATION_UNPROVEN`.

References: [EXP-9 durable broker AAR](EXP-9-SQLITE-DURABLE-MCP-CONNECTOR-BROKER-EXECUTED-AAR-2026-11-23.md), [communication transport roadmap](AGENCY-COMMUNICATION-ORCHESTRATION-TRANSPORT-ROADMAP-V0.1.md), [cybersecurity 12-stage mapping](CYBERSECURITY-12-STAGE-LEARNING-ROADMAP-FOROMNI-RD-CROSSWALK-V0.1.md).
