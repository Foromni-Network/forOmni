# Convergence Work Packet v0.2 — Typed Contract and Authority Boundaries

**Status:** research schema PROPOSAL; not implemented, validated by a runtime, or an effective grant.  
**Date:** 2026-11-21. **Scope:** Foromni only. No IE repo/task/code transfer, merge, test or deployment.  
**Related:** CONVERGENCE-FIRST-CONTROLLER-ARCHITECTURE.md, CONVERGENCE-READINESS-RUBRIC-V0.1.md, CONVERGENCE-PACKET-FRESHNESS-AND-DECISION-RULES.md, AI-WORKFORCE-AUTHORITY-EVENT-CONTRACT-V0.1.md.

## Purpose

For an AINO to safely build from natural-language goals, its agents need machine-readable coordination *before* generating code. A work packet describes a specific attempt; it is NOT an authorization token or a statement that the current main branch accepted the work. An independent policy plane must check executable privileges at action time.

Proposed relations:
`objective → accepted task revision → work packet → isolated attempt → candidate + evidence → independent QA → protected integration → staging/release/outcome`.

The primary experiment will compare these packets against ordinary freeform task instructions, holding the actual work, test quality and budget constant.

## Work packet fields and provenance

| Field family | Required content | Who is authoritative? | Agent may do |
|---|---|---|---|
| Identity | objective/task UUID, revision, attempt UUID, packet revision | Accepted task registry/authorized coordinator | Suggest split, not forge accepted IDs |
| Source | repo, target ref, latest observed main SHA and observation provenance | Git host/trusted reader | Read permitted refs and request refresh |
| Ownership | isolated branch/worktree, claimed files and interface area, lease/epoch | Trusted task allocator + effective repo permissions | Propose ownership and handoff |
| Dependencies | prerequisite task revisions, schema/contract digests and migration compatibility | Versioned accepted dependencies / contract owners | Flag drift, draft repair plan |
| Acceptance | fixed observable criteria, independent reviewer, required check classes | Approved acceptance definition and QA policy | Generate tests but not self-certify |
| Tools | allowed operations, network/data boundary, model restrictions, budget, retry cap | Trusted policy/grants/billing source | Pick an allowed tool; request narrower/more authority |
| Delivery | candidate reference, handoff manifest, exact SHA, merge group verification protocol | Git/CI/policy controller | Submit candidate and evidence |
| Lifecycle | created_at, expires_at, supersedes, gate decisions | Trusted event ledger | Request renewal; never self-extend |

A field labeled `expected_main_sha` is a **snapshot assumption**, not a capability to update that ref. After any relevant source or policy change, reevaluate before privileged operations.

## JSON Schema 2020-12: structural **draft**, not executable policy

This schema can check types, required properties, identifier shapes and obvious omissions. It CANNOT attest Git state, confirm a grant, verify an actor, compute dependency conflicts, prove evidence independence or enforce a protected merge. These require trusted external systems.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.invalid/foromni/research/convergence-work-packet-v0.2",
  "title": "Foromni Convergence Work Packet (research draft)",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version", "packet_id", "packet_revision", "objective_id",
    "task_id", "task_revision", "attempt_id", "source",
    "ownership", "dependencies", "acceptance", "requested_actions",
    "resource_limits", "packet_state"
  ],
  "properties": {
    "schema_version": {"const": "0.2-research"},
    "packet_id": {"type": "string", "minLength": 1, "maxLength": 128},
    "packet_revision": {"type": "integer", "minimum": 1},
    "objective_id": {"type": "string", "minLength": 1},
    "task_id": {"type": "string", "minLength": 1},
    "task_revision": {"type": "integer", "minimum": 1},
    "attempt_id": {"type": "string", "minLength": 1},
    "source": {
      "type": "object", "additionalProperties": false,
      "required": ["repository", "target_ref", "observed_main_sha"],
      "properties": {
        "repository": {"type": "string", "minLength": 1},
        "target_ref": {"type": "string", "pattern": "^refs/heads/"},
        "observed_main_sha": {"type": "string", "pattern": "^[0-9a-f]{40}([0-9a-f]{24})?$"}
      }
    },
    "ownership": {
      "type": "object", "additionalProperties": false,
      "required": ["isolated_branch", "claimed_paths", "interface_areas", "lease_epoch"],
      "properties": {
        "isolated_branch": {"type": "string", "minLength": 1},
        "claimed_paths": {"type": "array", "uniqueItems": true, "items": {"type": "string"}},
        "interface_areas": {"type": "array", "uniqueItems": true, "items": {"type": "string"}},
        "lease_epoch": {"type": "integer", "minimum": 0}
      }
    },
    "dependencies": {
      "type": "array",
      "items": {
        "type": "object", "additionalProperties": false,
        "required": ["task_id", "task_revision", "required_state"],
        "properties": {
          "task_id": {"type": "string", "minLength": 1},
          "task_revision": {"type": "integer", "minimum": 1},
          "required_state": {"enum": ["contract_accepted", "integrated", "staging_verified"]},
          "interface_digest": {"type": "string", "minLength": 1}
        }
      }
    },
    "acceptance": {
      "type": "object", "additionalProperties": false,
      "required": ["criteria_revision", "criteria_refs", "independent_qa_required"],
      "properties": {
        "criteria_revision": {"type": "integer", "minimum": 1},
        "criteria_refs": {"type": "array", "minItems": 1, "uniqueItems": true, "items": {"type": "string"}},
        "independent_qa_required": {"const": true},
        "test_plan_revision": {"type": "integer", "minimum": 1}
      }
    },
    "requested_actions": {
      "type": "array", "uniqueItems": true,
      "items": {"enum": ["read_scoped_repo", "draft_in_isolation", "write_isolated_branch", "run_disposable_tests", "submit_candidate", "request_review"]}
    },
    "resource_limits": {
      "type": "object", "additionalProperties": false,
      "required": ["cost_cap_usd", "max_attempts", "data_classification"],
      "properties": {
        "cost_cap_usd": {"type": "number", "minimum": 0},
        "max_attempts": {"type": "integer", "minimum": 0},
        "data_classification": {"enum": ["synthetic", "public", "restricted"]},
        "network_egress": {"type": "array", "items": {"type": "string"}}
      }
    },
    "packet_state": {"enum": ["draft", "preflight_pending", "ready_scoped", "stale", "blocked", "retired"]},
    "effective_grant_ref": {"type": ["string", "null"]},
    "expires_at": {"type": ["string", "null"], "format": "date-time"}
  }
}
```

Design limitations: `format` is not necessarily assertion-enabled in every JSON Schema implementation. Matching a SHA regex is not verification that the Git object exists. `requested_actions` excludes protected merge and production release intentionally; such operations require separate trusted service credentials, policies, and direct approvals. Arrays of permitted path strings do not implement an enforced lease.

## Separate decision output (not a capability)

```json
{
  "schema_version": "0.2-research-decision",
  "packet_id": "PKT-DEMO",
  "packet_revision": 4,
  "evaluated_action": "write_isolated_branch",
  "readiness": "REPAIRABLE",
  "action_decision": "DENY_UNTIL_REMEDIATED",
  "reason_codes": ["API_CONTRACT_MISMATCH"],
  "observed_evidence": ["OBS-001"],
  "evaluator": "trusted-policy-service-placeholder",
  "effective_grant": "NONE_CONFIRMED",
  "last_known_valid_source": "UNKNOWN",
  "recommendation": "negotiate-versioned-consumer-provider-contract"
}
```

Each action is adjudicated independently. An agent can receive permission to read source while write or test remains denied. Do not emit a globally reassuring `READY` badge if any relevant hard gate is absent.

## Action-time decision logic (normative proposal)

1. Identify **actual** requested action, resource and authenticated principal.
2. Read trusted current policy/grant; deny if revoked, expired, wrong tenant/repo, over-budget or unsafe.
3. Verify task/attempt/lease revision and required ownership. Reject expired lease epoch.
4. Confirm relevant interface and task acceptance assumptions. Permit narrowly scoped diagnostic/read-only work when safe; otherwise require renewal.
5. For source-changing operations, validate branch/attempt scope and expected remote ref against trusted Git semantics.
6. For admission, require independently checked **exact current prospective merge result**, appropriate required statuses and real protected write authority, not merely packet consent.
7. Record decision/event with idempotency key, source evidence and reason. After commit, read back actual main ref; recover ambiguous network errors by reconciliation rather than retrying blindly.

No prompt instruction, JSON Schema validation or file lock can replace the effective authority of the Git host and credentials. Prefer native merge queue and branch protections when applicable.

## Adversarial contract cases to preregister

| Fixture | Candidate fault | Expected behavior |
|---|---|---|
| CWP-01 | SHA-looking string isn't a real Git object | Shape may pass; trusted Git observation fails |
| CWP-02 | Worker packet expires after creation | Subsequent privileged action denied |
| CWP-03 | Main changes in unrelated module | Local draft may continue; merge-group checks refreshed |
| CWP-04 | API contract digest changes | Dependent work packet goes stale; bounded repair |
| CWP-05 | Path ownership claims overlap in two packets | Trusted allocator resolves conflicts; neither gains authority by claim |
| CWP-06 | Agent requests new external network domain | Deny until appropriate policy grant |
| CWP-07 | Candidate source SHA differs from tested SHA | Independent check invalid for candidate |
| CWP-08 | Implementer writes fake reviewer event | Independent authority verification fails |
| CWP-09 | Old webhook arrives after revocation | Ignore as historical, do not restore grant |
| CWP-10 | Merge succeeds; ACK lost | Reconcile Git truth before any replay |
| CWP-11 | Human changes acceptance criterion mid-task | Re-scope and recheck; historical tests stay historical |
| CWP-12 | Planner says merge=done | Reject outcome promotion; stage/release/beneficiary separate |

## Portability across AINOs

The packet should describe provider-neutral facts, not model-provider IDs or vendor-specific workflow UI. Source adapters translate GitHub/GitLab/Forgejo refs, issue adapters translate task IDs, and permission adapters map to the actual enforcement system; **unknown adapter semantics must fail closed**. Independent collectives may exchange task descriptions without sharing write tokens, user identities or arbitrary tools. Cross-boundary tasks need explicit signed/authorized capability scopes and revocation.

## Open research decisions

- Whether to preserve a task ownership lease in a separate trusted state store versus use strictly ref-scoped Git permissions.
- Revision-based partial invalidation without brittle dependency inference.
- Reliable 'independent QA' authority across multiple service providers.
- Semantic version negotiation for APIs/schema/migrations.
- Which workflow features can be assembled from existing tooling rather than a bespoke controller.
- How to keep the contract simple enough for a 1-agent AINO and robust enough for 1000 agents.

**No schema validation, tests or experiments have been run.**

*Build today, so others can enjoy tomorrow.*
