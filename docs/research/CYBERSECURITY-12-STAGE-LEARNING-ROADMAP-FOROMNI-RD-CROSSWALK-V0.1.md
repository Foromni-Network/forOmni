# Foromni Cybersecurity R&D — 12-Stage Learning Roadmap Crosswalk v0.1

**Date:** 2026-11-23. **Status:** research backlog and educational laboratory design only. Foromni only. No Internet Embassy changes, live probing, external exploitation, production credential use, continuous scanning, CI or frozen FOR-007 mutation.

## Origin and intent

Founder supplied a 12-stage synthesis credited to Dhanush N (@Dhanush_Nehru): learn Linux/networking, web security, recon, Active Directory, cloud, detection/SIEM, IR/forensics, malware/reverse engineering, supply-chain/DevSecOps, crypto/PKI, threat intelligence/emulation, and responsible disclosure/portfolio. This document treats the supplied outline as a **learning framework**, not a verified statement of the author's exact wording, a complete industry curriculum, or permission to probe real targets.

**Foromni-specific approach:** map each stage to security controls for global multi-tenant agents, MCP/plugins/connectors, webhooks/cron, trust reputation, source/evaluator custody, and secure release. Do hands-on exercises only in owned/disposable labs and explicitly authorized scopes. Prefer safe synthetic fixtures to live exploitation.

## Priority placement

The existing [communication orchestration research roadmap](AGENCY-COMMUNICATION-ORCHESTRATION-TRANSPORT-ROADMAP-V0.1.md) stays immediately before and overlapping with cybersecurity. **Near-term execution order is risk-based, not the educational 1–12 order:** transport/identity security, web authorization, cloud/token scopes, supply chain, audit/detection and incident handling first; extend to deeper enterprise, malware and adversary research after ownership boundaries and lab capacity exist.

## Twelve-stage crosswalk

| Original stage | Foromni-specific question | Safe proof artifact | Scheduling |
|---|---|---|---|
| 1. Linux, networking and protocols | Which processes, ports, TLS peers, DNS routes and Unix credentials can each runner use? | Owned local packet trace; least-privilege process/container map | Early, with communications |
| 2. Web application security | Can task API/MCP tool endpoint bypass project/owner/lease enforcement? | Synthetic IDOR, injection and auth-negative tests; source-bound fixes | **Immediate** |
| 3. Recon / attack-surface mapping | What endpoint, callback, webhook, plugin, MCP server and agent identity is exposed? | Inventory of owned local/sandbox routes; no unauthorized public scanning | Early, alongside web |
| 4. AD and identity paths | How do operator, human, agent incarnation and reviewer credentials differ? Where is privilege transitive? | Small simulated identity directory, delegated-token denial tests | Later enterprise adapter |
| 5. Cloud IAM | Does a provider token grant a worker broader rights than its task lease? | Mock cloud policy and limited disposable sandbox IAM with budget safeguards | **Immediate** |
| 6. Detection engineering / SIEM | Can we correlate denied MCP action, webhook replay, spend anomaly and tool output tampering? | Synthetic agency audit event → rule → false-positive/negative evaluation | Next after policy baseline |
| 7. IR and forensics | Can we reconstruct agent action order, actual effects and revoked credentials without trusting self-report? | Synthetic timestamped incident timeline and evidence-custody record | After logging |
| 8. Malware and reverse engineering | Can an untrusted plugin/dependency run within a confined analysis environment? | Non-malicious surrogate sample and inert signature; no malware distribution | Deferred, isolated |
| 9. Supply-chain / DevSecOps | How do we validate MCP server, skill, extension, dependency, model tool and source provenance? | SBOM/dependency lock, secret detection and local signed-artifact verification | **Immediate**, before adding integrations |
| 10. Crypto and PKI | Which keys sign evaluator receipts, webhook events, token audiences and approvals, and how rotate/revoke? | Test CA or signing-key rotation fixture; no weak real credentials | Early, with identity |
| 11. Threat intelligence and emulation | Which agent-specific abuse paths matter most: confused deputy, tool poisoning, prompt injection, replay? | ATT&CK-like tactic mapping and wholly synthetic attack/defense matrix | After controls exist |
| 12. CVEs, writeups and portfolio | How do we publish responsible methodology, independent evidence and maintainers-first disclosures? | Reproducible case-study/experiment reports and coordinated disclosure template | Ongoing, no unsolicited disclosure |

## External security references checked in November 2026

- [OWASP Top 10:2025](https://top10.owasp.org/): broken access control, supply-chain, authentication and logging are directly relevant to Foromni.
- [OWASP MCP Top 10](https://owasp.org/projects/mcp-top-10): model/tool poisoning, context manipulation, shadow servers and software-supply-chain risk.
- [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html): untrusted tool metadata, least privilege, action-specific approvals, spending limits.
- [MCP 2026-07-28 specification announcement](https://blog.modelcontextprotocol.io/posts/2026-07-28/): stateless protocol core and authorization hardening; implementation must verify exact SDK/spec and not assume all servers enforce the same grant semantics.
These are research references, **not** a claim that our synthetic gateway implements an official MCP server.

## Most urgent attack paths for Foromni

1. **Confused deputy / broad connector credential:** MCP server has workspace-wide OAuth/provider token but agent is allowed one task/resource. Actual gateway must derive effective scope from authenticated principal+task+action+resource, not provider capabilities.
2. **Tool poisoning and prompt injection:** tool descriptions, schemas, search results or webhook body request privileges or reinterpret approval. Treat all third-party content as data, never policy.
3. **Replay / restart:** external side effect finishes and agent loses response; durable transaction ledger, provider idempotency and read-after-write reconciliation are required.
4. **Forged QA / provenance:** worker supplies claimed PASS or receipt with no separate evaluator execution. No accepted confidence or role promotion.
5. **Cross-tenant sharing and agent masquerade:** agent aliases, project IDs, task epochs, secrets and security classifications need independently bound scope at every handoff.
6. **Supply-chain:** extension/MCP/skill updates can change advertised tools. Freeze allowlisted tool IDs/versions and inspect plugin dependencies.

## Experimental roadmap integration (not new frozen P0 scope)

- **SEC-COMMS-01:** synthetic privilege-narrowing gateway against intentionally broad mock provider — performed as EXP-8, with known open issues (see companion report).
- **SEC-COMMS-02:** SQLite durable replay across restart, concurrent workers, provider lookup; re-use EXP-7 rather than duplicate infrastructure.
- **SEC-COMMS-03:** malicious tool description/prompt-injected payloads as inert strings, ensure policy rejects regardless of model text.
- **SEC-COMMS-04:** owned mock connector protocol with independent authentication and scoped tokens; verify no bypass route can reach broad token.
- **SEC-COMMS-05:** synthetic security events into basic SIEM detector; measure denial coverage, false positives and incident chain.
- **SEC-COMMS-06:** source/plugin/dependency provenance and secret/permission scans with local fixtures.

## Controls and experimental integrity

All labs are owned or explicitly authorized. No testing third-party websites, domains, or private accounts; no real malware. Preregister task definition, source SHA, negative conditions, independent reviewer, budget/stop condition, actual command and environment. Maintain distinct status **SOURCE_INSPECTED / SPECIFIED / LOCALLY_TESTED / INDEPENDENT_QA / INTEGRATED** rather than promoting desk research to runtime PASS. Separate single-operator mock harness from true agent/evaluator principal isolation.

**Roadmap disposition:** communication and cybersecurity now share a defined boundary-focused bridge. FOR-009 identity and grants, FOR-011/012 independent QA and evidence, FOR-013 human approval, FOR-016 federation use this as research input. Frozen FOR-007 scope remains unchanged.
