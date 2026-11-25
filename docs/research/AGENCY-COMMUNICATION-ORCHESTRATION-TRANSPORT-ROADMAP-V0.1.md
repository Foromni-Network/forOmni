# Foromni — Agency Communications, Control Plane and Integration Transport R&D Track v0.1

**Status:** NEW ROADMAP RESEARCH TOPIC — concept specification only, not a live service, task authority or frozen MVP scope. Date 2026-11-23. Foromni-only; do not mix Internet Embassy runtime/credentials/infrastructure.

## Founder idea and placement

Research **agency-wide communication and orchestration** using **APIs, MCP, webhooks, cron/schedulers, connectors/plugins, event/queue transports and agent-to-agent protocols**. Place this after verified evidence/independent QA handoff and **immediately before cybersecurity systems review**, with the two tracks intentionally overlapping: communication establishes the surfaces and identities, security tests/enforces the boundaries.

**Why now:** EXP-3 and EXP-4 demonstrated basic synthetic three-module convergence and proposed evidence-bound receipts. The next scaling bottleneck is reliable and accountable communication between project owners, coordinators, agents, evaluators, repositories and outside software. Transport alone does not create authority.

## Distinguish communication functions (not interchangeable)

| Mechanism | Primary purpose | Characteristic failure | Foromni rule |
|---|---|---|---|
| HTTP/REST APIs | Read/write typed business operations, synchronous command responses | retries, latency, timeouts, version drift | authn/authz, idempotency and explicit timeout reconciliation |
| MCP tools and resources | Expose structured tools/data to participating AI agents | tool spoofing, overprivileged servers, prompt injection | broker tool invocations at trusted capability gateway; tool descriptions are untrusted |
| Webhooks | Push source-system changes and completion notices | duplicated, forged, reordered, lost delivery | verify provider signature, timestamp, event id and account/tenant binding; enqueue before ack |
| Cron/schedulers | Time-triggered reconciliation, dispatch, monitoring and recovery | concurrent runs, drift, retry storm, stale poll | leader/lease fencing, bounded budgets and single authoritative job identity |
| Connectors/plugins | Adapt OAuth/provider-specific integration semantics | expired tokens, broad scopes, provider rate limits | per-tenant/provider scoped credentials, audit, revoke and data provenance |
| Queues/event bus | Durable asynchronous dispatch, fan-out, work completion | at-least-once redelivery, out-of-order events, poison messages | durable inbox/outbox, dedupe, backoff, dead-letter, causal IDs |
| Agent-to-agent network/transport | Collaboration and delegated work invitations | spoofed peers, accidental trust transitivity | joining a channel never means execution authority |
| Human inbox/approval | Clarification, consent, overrides, escalations | ambiguous approver, forged approval UI | account-bound approval with exact scope, expiry and conflict-of-interest rules |

## Proposed ecosystem topology

```
Human dashboard / other collectives / provider webhook / cron timer
    -> ingress adapters (authn, schema version, signature, tenant)
    -> durable event inbox and audit (dedupe, observed time, raw pointer)
    -> trusted agency control plane (policy, budget, task rev, lease, identity)
    -> workflow / scheduler (dependencies, queue, retry, visibility)
    -> task-lease scoped worker sandbox via APIs/MCP/tool proxies
    -> candidate source/evidence artifacts
    -> separately controlled evaluator + source/attempt observer
    -> human exact-candidate acceptance
    -> protected integrator / release controller ONLY with explicit authority
    -> outbound transactional outbox for callbacks, UI, project updates
```

Do not give individual cron jobs, MCP servers or webhooks broad authority over work acceptance, protected Git, expenditures or production. No standing per-provider "master token" shared by external BYO agents. The platform must retain a single canonical task and owner state even when many transports are active.

## Smallest common event envelope (exploratory only)

```json
{
  "event_id": "evt-demo-1",
  "transport": "webhook",
  "source_system": "git-host-example",
  "event_type": "candidate.submitted",
  "tenant_id": "project-A",
  "task_id": "T1",
  "task_revision": 3,
  "attempt_id": "attempt-A-1",
  "producer_claim": "worker-A",
  "authenticated_principal": null,
  "resource_ref": "example-repo@sha",
  "payload_digest": "example-hash",
  "observed_at": "ingress-assigned",
  "causation_id": "cmd-1",
  "idempotency_key": "provider-event-1",
  "policy_decision": "NOT_YET_EVALUATED"
}
```

The `producer_claim` is **never** the authenticated principal, a webhook event is **not** QA PASS, and an MCP tool response is **not** a grant. Prefer canonical event semantics to fragile provider-specific text parsing.

## Measurement-driven research questions

1. Which tasks require immediate RPC vs durable asynchronous events vs scheduled reconciliation?
2. What is the minimum idempotency scope to prevent duplicate work, repeat spend and replayed approvals?
3. How to propagate causality, trace IDs, task/attempt/source SHAs, costs and privacy classification across all adapters?
4. How does a scheduled job safely resume after a timeout or missed run without duplicating task ownership?
5. How do we keep agent MCP/tool permissions narrower than the external connector's provider-level OAuth credential?
6. How do we confirm webhook sender and tenant, handle provider rotation and prohibit cross-collective deliveries?
7. What are local-first/offline and multi-region collaboration behavior when services disconnect?
8. Can failures be reconciled from provider authoritative state instead of trusting callback arrival?
9. How can one UI expose human-readable decisions, agent handoffs, blocked actions, cost and exact acceptance evidence?
10. Which adapters support standards such as A2A/MCP yet still need custom transport and identity bridges?

## Experiment backlog; no claims of execution here

**COMMS-01: Three tasks -> one event pipeline.** A normalize/validate event, B deduplicate/source-route, C task-scope/revocation gate. Compare naive direct webhook vs durable inbox/outbox; fake events only. Negative: spoofing, replay, out-of-order, project mismatch, revoked epoch.

**COMMS-02: Webhook vs cron reconciliation.** Randomize delivery order, induce missing notifications, and compare eventual consistency/recovery and duplicate execution at fixed event budget.

**COMMS-03: MCP and connector privilege boundary.** Simulate server possessing broad provider token while worker has only scoped task grant; ensure gateway rejects extra API/secret/tool requests.

**COMMS-04: Multi-agent async handoff.** Two agents + independent QA, source-bound task/attempt events, rate cap and budget; measure retry cost and recoverability.

**COMMS-05: Incident drills with security track.** Credential rotation/revoke, prompt-injected tool text, malicious webhook, poisoned queue item, compromised connector, stale scheduled job, cross-project breach attempts.

**COMMS-06: Whole-agency observability.** Correlation and trace propagation across API→queue→agent→QA→approval; measure unaccounted spend, work aging and orphaned tasks.

## Scientific and security gates

Record baseline and treatment under identical fixtures; wall-clock, API calls, retries, stale/blocked events, duplicates, accepted jobs, total provider and compute costs, drift, recovery time, human intervention. Run randomized event permutation, unavailability and denial tests; do not label documentation tests as service validation.

**Dependency order:** single-task authoritative state → independent evidence/source verification → transport durable inbox/outbox → concurrency/revocation → A2A/MCP/connector bridges → cyber security adversarial harness → global/federated agency integration. Security review begins alongside communications contracts, not only afterward.

**Roadmap placement:** FOR-016 (federation and global community communication), FOR-009 (effective access), FOR-011/012 (QA/evidence), FOR-013 (human approval), existing coordination work; future track only. Preserve frozen FOR-007 as the operational first baseline.

**Decision:** Add the topic now and pursue next source-level review around MCP tool trust, webhook idempotency and cron lease fencing, informed by EXP-5 local evidence; do not activate a new unattended production orchestrator.
