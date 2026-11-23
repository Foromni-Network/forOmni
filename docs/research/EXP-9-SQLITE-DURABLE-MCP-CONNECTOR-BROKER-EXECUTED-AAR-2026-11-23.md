# EXP-9 — Durable Synthetic Capability Broker for MCP/Connector Access (Executed)

**Date:** 2026-11-23 (UTC). **Repository:** Foromni-Network/forOmni; research branch `research/global-agent-roadmap-execution`. **Status:** executed local Python 3.13.5 / SQLite experiment, **18/18 unit and integration assertions PASS** with `ResourceWarning` treated as an error. **No live MCP, connector, provider API, production token, deployment, CI, protected Git merge, credential service or autonomous agents.**

## Experimental question and result

Can a broker enforce narrow signed *demonstration* task grants, maintain SQLite-backed durable request/effect records, and avoid duplicate mock provider effects after a crash and fresh-process retry—even though the simulated provider has broadly privileged tools?

**Result:** Within the model, **YES**, when all calls pass the broker and the mock provider enforces stable idempotency keys. A new Python process reconciled a deliberately crashed-after-effect request and left **one** recorded provider effect; twelve simultaneous duplicate requests likewise produced one effect. **Critical negative result:** an actor who has the provider credential can call the mock provider directly and execute an unrestricted admin operation. This is intentionally demonstrated in a passing negative-control test, and means **credential isolation is not solved** by the broker logic.

## Scientific procedure and recorded artifacts

The prior EXP-7 and EXP-8 studies established baseline problems: crash-after-side-effect ambiguity, in-memory replay loss, and gateway bypass. EXP-9 combined those concerns in two locally executed research modules:

- `broker.py`: HMAC-authenticated *test* grant envelopes bound to agent/project/task/action/resource/epoch/expiry/budget, SQLite `policy`, `operations`, `provider_effects` tables, atomic `BEGIN IMMEDIATE` reservation, simulated mock-provider credential check, stable effect idempotency key, mock provider lookup, and post-effect epoch/revocation recheck.
- `test_broker.py`: 18 tests covering grant tampering, wrong signer, cross-project and agent scope, unsupported admin actions even with valid signatures, missing policy, revocation, fencing, budget, expiration, tampered request ID, replay across a real subprocess, 12 concurrent duplicate submissions, needs-review when lookup unavailable, inert tool-instruction metadata, and deliberately compromised provider token.
- `README.md`, `SHA256SUMS`, `test_output.txt`: exact reproducibility commands, executed test output and file hashes.

**Command that passed after cleanup fix:**

```bash
cd foromni_exp9_broker
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v
```

**Observed:** `Ran 18 tests in 1.037s / OK`. An earlier 18/18 test run emitted SQLite connection ResourceWarnings; source was amended to explicitly close connections, then final rerun above passed without warnings. Do not conceal that repair sequence.

**SHA-256 of locally executed final artifacts:**

| File | SHA-256 |
|---|---|
| `broker.py` | `22b56e102526cb6b30e8148c7e693f397116b1cc2168bfcb9416df0f40eed5f6` |
| `test_broker.py` | `fde9befb0f30e7698d11e5ace04d49d706c0512bf5dfcbaec9c3bf6eaa1d67ef` |
| `README.md` | `2bd9ddb74e6803b004a3e60467397679da91f53800e1483a9ad4e4fac550ebee` |
| `test_output.txt` | `f2a74c2c50a69e5372dd5bab846a97d4a66ce5db480bda0af8c8bbd1faf38114` |

**Source distribution:** `foromni_exp9_broker_evidence.zip` in the research conversation is the exact tested code and logs. **Only this written report has been pushed to the research branch; the Python archive has not been uploaded as GitHub source files.** Do not misrepresent this as an integrated repository module.

## Meaning of the 18 passing tests

The following expected properties held *in this particular local harness*: test-key MAC validation rejects altered grants; independent project/action allowlist denies unsupported tools; policy epoch and revoked status are checked before task processing; SQLite operations survive a fresh subprocess; duplicate same-key requests settle to one mock provider effect; modified payload under reused request id is rejected; when provider lookup is unavailable, state is `NEEDS_REVIEW` rather than blind external retry.

Passing the deliberately unsafe test `test_broad_credential_still_dangerous_if_stolen` is **not a protection**. A token leak still lets the mock provider perform an unauthorized action. The test demonstrates the unacceptable bypass and guides the next design.

## Unresolved weaknesses (do not promote to production)

1. **The issuer and broker keys are demonstration strings** in the local harness and passed to a subprocess via environment variables. There is no truly isolated operator/agent principal, dedicated policy authority, hardware/secret store, OAuth issuer/audience, key rotation or credential escrow.
2. **Provider and task ledgers share a single SQLite database**, unlike a real networked external service. The modeled atomicity and provider lookup are stronger than typical external connector guarantees. There is no real distributed consistency, provider rate limit, loss of network, partial effects or true remote compromise.
3. **Grant/actor identity is not authenticated outside the signed test envelope.** An attacker obtaining a signing key can impersonate permitted principals.
4. **Post-effect policy revocation cannot undo an already executed external effect.** The code can return `NEEDS_REVIEW` after noticing a change; it does not enforce real atomic revoke across provider boundaries.
5. **Tool metadata is ignored as a string**, not processed by an LLM. It therefore does not demonstrate prompt-injection protection, malicious MCP server handling or agent behavior under tool poisoning.
6. **No actual MCP transport, plugin/connector adapter, OAuth scopes or runtime sandbox** was exercised. Running mock-provider Python functions is not equivalent to a mandatory mediation boundary.
7. Tests were authored by the same researcher as the candidate, and there was no independent evaluator credential or review. The code uses synthetic data only.
8. **Costs and successful work quality were not measured**. Passing a unit test is not a real-world security rate or productive-task result.

## After-action and next discriminating experiment

**Improvement over EXP-8:** in-memory replay was replaced by a persisted operations ledger, and fresh-process recovery and concurrent requests were actually tested; demo signatures prevent naive grant editing.

**Major remaining gate:** provider credential must become inaccessible from the worker's process, filesystem and network. A more discriminating EXP-10 would run a worker under a separate OS identity/container with no connector token or signer key, a separate broker service holding the token, a separate mock provider with audit logs, and a trusted receipt verifier. Adversarial tests must attempt to use direct provider URLs, read broker secrets, reuse expired/revoked grants and spoof MCP tool descriptions. If this runtime isolation is unavailable, stop at a design study rather than claiming enforced security.

**Roadmap relationship:** [communications architecture](AGENCY-COMMUNICATION-ORCHESTRATION-TRANSPORT-ROADMAP-V0.1.md); [12-stage cyber research crosswalk](CYBERSECURITY-12-STAGE-LEARNING-ROADMAP-FOROMNI-RD-CROSSWALK-V0.1.md); EXP-7 durable side-effect tests and EXP-8 MCP connector boundary tests. Scope is a research exercise **not** a new FOR-007 P0 gate.

**Verdict:** `EXP9_LOCAL_SQLITE_REPLAY_AND_NARROWING_PASS`; `EXP9_BROAD_TOKEN_BYPASS_DEMONSTRATED`; `EXP9_REAL_CREDENTIAL_ISOLATION_NOT_PROVEN`; `FOR007_UNCHANGED`.
