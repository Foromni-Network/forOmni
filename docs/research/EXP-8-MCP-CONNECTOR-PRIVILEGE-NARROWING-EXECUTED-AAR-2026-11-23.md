# EXP-8 — MCP/Connector Capability Narrowing: Executed Synthetic Gateway Experiment (2026-11-23)

**Status:** locally executed, 15/15 Python standard-library tests passed. **Foromni only**, no Internet Embassy modifications. No real MCP protocol endpoint, OAuth, cloud API, plugin install, external connector, network request, live credentials, protected Git changes, or deployed security gateway. Companion roadmap: [12-stage cybersecurity R&D crosswalk](CYBERSECURITY-12-STAGE-LEARNING-ROADMAP-FOROMNI-RD-CROSSWALK-V0.1.md).

## Question and hypothesis

Can a restricted agent request execute an authorized narrow tool through a mock provider holding broad authority, while forbidden tools, cross-project resources, identity mismatch, revoked/expired leases, stale task epochs and conflicting retries are stopped at the gateway? What remains dangerous if a caller restarts the gateway or bypasses it?

**Experimental design:** deterministic local Python, 3 modules: `gateway.py`, `provider.py`, `test_gateway.py`. The provider is intentionally overprivileged and accepts all operations. The gateway receives a `Request` and `Lease` dataclass, checks project/task/capability-like tool/resource/epoch/expiry/revocation fields, issues one mock provider call if eligible, and maintains in-memory deduplication/audit. Tests are authored by the same assistant as code. No claims of independent reviewer, authentic issuer or real MCP compliance.

## Observed results

**Command:** `PYTHONDONTWRITEBYTECODE=1 python -m unittest -v` in the extracted `foromni_exp8_mcp_gateway` directory.

**Observed 15 tests, all PASS, no failures/errors**. Tests covered:
- expected allowed narrow task draft;
- mock provider's broad delete/admin tool not inherited by a narrower task;
- cross-project resource denial;
- forged agent ID denial **based on supplied dataclass**, not cryptographic authentication;
- revoked, expired and stale epoch denial;
- project-namespace assertion even if an incorrect grant lists foreign resource;
- exact same idempotency key/payload replay accepted without second in-process effect;
- same idempotency key with modified payload blocked;
- missing idempotency key blocked;
- privileged-sounding tool metadata not treated as authority;
- denial audit entry with zero mock-provider mutation;
- **negative control #1:** gateway restart loses in-memory idempotency map; same request causes another mock effect;
- **negative control #2:** direct mock-provider call bypasses gateway and executes broad operation.

**Important:** Negative controls passing are observations of deliberately vulnerable behavior. The results are *not* a claim that the gateway withstands restarts, direct credential bypass, untrusted tool descriptions interpreted by an LLM, or truly forged network principals.

## Exact test source hashes

| Locally executed file | SHA-256 |
|---|---|
| `gateway.py` | `a6478e458275d60298f46ea2bb5ffa852c88e33a40fe0603511e97bc3ee2f2d6` |
| `provider.py` | `298fe5d0684293acc7cabca9990d180f7b7e9c818f8e0ca0746964eae923be55` |
| `test_gateway.py` | `104837bf5faf9573569c504cfc98a446f48508dda9d84a02df7d8e40c5c9bf61` |
| `test_output.txt` | `e8a3028eec1155f9cc6cd12e9bab71b9eb349688003ff965ba93b6e62b23e7ef` |

**Reproduction:** use the downloadable `foromni_exp8_mcp_gateway_evidence.zip` from the research conversation. It contains the executed source, tests, test output and SHA256SUMS. The *report and roadmap* were pushed to GitHub; at this stage the zip is the exact source artifact; do not claim CI or GitHub source-tree integration.

## AAR / failed assumptions exposed

1. **No identity authentication:** `Principal` and `Lease` are caller-fed dataclasses. Even though the simulator rejects mismatching strings, it cannot tell an attacker who can forge *both* objects from the legitimate issuer. Proper runtime needs authenticated user/agent incarnation and trusted lease lookup or signature validation, never direct caller-provided authority.
2. **No real credential isolation:** provider instance is reachable to the test harness and can be called directly. The gateway is not a mandatory mediation boundary. Separate provider token process/account from agent sandbox; restrict network and file access; require all privileged actions through a hardened broker.
3. **No durable replay protection:** `seen` dictionary is process-local; restart causes duplicate external effects. Reuse EXP-7 SQLite durable inbox/claims/outbox and provider-side idempotency/reconciliation.
4. **Untrusted content not evaluated:** privileged-sounding tool name is rejected in one test. But the code does **not** test a language model reading tool descriptions, schema injection, prompt injection, tool shadowing, code injection or exploit payloads. Claiming prompt-injection resistance would be unwarranted.
5. **Opaque payload and coarse resources:** exact allowlist string matching is too narrow for full MCP tool arguments; need validated structured schemas, canonical resource identifiers, path/URL normalization, network egress controls, typed argument/resource digests and resource-level policy.
6. **No concurrency or genuine provider authorization:** no multiple processes, real credential expiry, OAuth issuer/audience, refresh/revoke, provider 429/rate budgeting, task owner authorization, review custody or actual external effects.

## External source references checked

- [MCP 2026-07-28 specification release](https://blog.modelcontextprotocol.io/posts/2026-07-28/) — authorization hardening and updated protocol semantics.
- [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html) — tool poisoning, action-specific approvals, spending ceilings and tool isolation.
- [OWASP MCP Top 10](https://owasp.org/projects/mcp-top-10) — tool poisoning, shadow MCP servers, context oversharing and supply-chain vulnerabilities.
- [OWASP Top 10:2025](https://top10.owasp.org/) — broken access control and related web risks.

The study makes no assertion that the tested simple Python classes implement MCP's OAuth or transport protocol.

## Next scientific gate

**EXP-9 recommended:** integrate durable SQLite idempotency from EXP-7 with a broker that actually owns the provider credential and accepts only authenticated/verified principals and issued task grants. Use an isolated mock provider interface and restart tests to check duplicate *effects*, plus fake MCP tool responses carrying inert injection text and structured argument validation. Fail closed on unknown provider effect status. Only after local reproducibility should a separately authorized disposable MCP SDK/OAuth integration be considered. No new scope in frozen FOR-007.

**Verdict:** `EXP8_SYNTHETIC_NARROWING_15_OF_15_PASS`, `EXTERNAL_CREDENTIAL_ISOLATION_NOT_PROVEN`, `AUTHENTIC_AGENT_AUTH_NOT_PROVEN`, `DURABLE_REPLAY_NOT_PROVEN`.
