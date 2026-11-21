# Foromni Capability Exchange Contract

**Status:** Proposed design contract; not a finalized API, protocol, or implementation.  
**Purpose:** Define the minimum information independent systems need to describe, discover, request, and exchange capabilities without granting ambient authority.

## 1. Core rule

A capability description advertises what an actor or system can do. It does not authorize anyone to invoke it.

Discovery, authorization, execution, and outcome recording are separate operations. A consumer must obtain explicit authorization from the capability owner at invocation time.

## 2. Capability descriptor

A future machine-readable descriptor should include:

| Field | Required | Meaning |
|---|---:|---|
| `id` | Yes | Stable identifier scoped to the issuer |
| `issuer` | Yes | Person, organization, project, service, or agent publishing it |
| `name` | Yes | Short human-readable name |
| `description` | Yes | Intended purpose and boundaries |
| `actor_type` | Yes | `human`, `organization`, `service`, or `agent` |
| `version` | Yes | Descriptor version |
| `interface` | Yes | Documentation or protocol reference |
| `inputs` | Yes | Expected input schema or human task description |
| `outputs` | Yes | Expected result schema or deliverable |
| `permissions` | Yes | Requested scopes, never implicit grants |
| `constraints` | Yes | Rate, cost, environment, and operational limitations |
| `data_handling` | Yes | Data categories, retention, processing, and sharing |
| `availability` | No | Availability statement or service status reference |
| `provenance` | Yes | Source, publisher, publication time, and descriptor digest |
| `support` | No | Public support or issue-tracker URL |

Descriptors must be versioned and validated against a published schema before broad interoperability claims are made.

## 3. Discovery

A discovery response may expose only fields the issuer has made public.

- Public discovery must not reveal private endpoints, credentials, internal prompts, customer data, or private operational metadata.
- Search results must identify the issuer and source.
- Imported descriptors must retain canonical source references and retrieval timestamps.
- A stale descriptor must be labeled stale rather than silently treated as current.
- Discovery does not create a relationship or imply endorsement.

## 4. Invocation handshake

A future invocation should follow this sequence:

1. **Discover:** Consumer retrieves a public descriptor.
2. **Inspect:** Consumer reviews issuer, version, inputs, outputs, permissions, constraints, and data handling.
3. **Request:** Consumer submits a bounded request with a unique request ID and proposed scope.
4. **Authorize:** Issuer evaluates identity, purpose, scope, policy, and any required human approval.
5. **Grant:** Issuer returns a narrowly scoped, time-bounded authorization or rejects the request.
6. **Execute:** Provider executes only the authorized operation and validates inputs.
7. **Record:** Both sides retain appropriate audit evidence and provenance.
8. **Revoke/expire:** Authorization ends at expiry, completion, revocation, or policy-defined termination.

A consumer must not reuse an authorization for a different task, actor, resource, or scope.

## 5. Request envelope

A future request envelope should include:

- Protocol and schema version.
- Unique request identifier.
- Requesting actor and issuer.
- Capability identifier and descriptor version.
- Declared purpose and bounded task.
- Input payload or secure reference.
- Requested permissions and duration.
- Data classification and handling requirements.
- Correlation identifier for audit and support.

Secrets should not be embedded in public descriptors, repository examples, issue reports, or logs. Sensitive payloads require an explicitly agreed secure transport and retention policy.

## 6. Response envelope

A response should identify:

- Request and capability identifiers.
- Provider and execution identity.
- Status: accepted, rejected, awaiting approval, running, completed, failed, cancelled, or expired.
- Result or secure result reference.
- Error category and safe diagnostic detail, if applicable.
- Start/completion timestamps.
- Usage and cost metadata where available.
- Provenance and audit-event references.

A response status is a claim from the provider, not independent proof that the requested outcome is correct. Consumers may require separate verification.

## 7. Human approval and sensitive actions

Human approval should be required by default for actions involving:

- Publishing or communicating externally on behalf of another participant.
- Changing identity, access, permissions, or ownership.
- Merging protected code or changing release state.
- Spending money, creating paid resources, or changing billing.
- Accessing, exporting, or modifying sensitive personal or customer data.
- Production deployments or production data changes.

The issuer may impose stricter rules. A consumer cannot override them.

## 8. Trust and threat considerations

Treat descriptors, inputs, outputs, tool responses, and agent-generated content as untrusted.

Threats to address before implementation include:

- Impersonated issuers and descriptor substitution.
- Replay of old requests or authorization grants.
- Scope escalation and confused-deputy behavior.
- Prompt injection and malicious instructions embedded in project metadata.
- Secret leakage through logs, error messages, or result references.
- Denial of service, cost amplification, and unbounded retries.
- Incorrect or misleading capability claims.
- Compromised provider or consumer systems.

Mitigations must include issuer verification appropriate to the deployment, request binding, replay protection, strict scope checks, quotas, auditability, revocation, and safe failure behavior.

## 9. Compatibility and evolution

- Descriptors and envelopes are explicitly versioned.
- Breaking changes require a new major version and migration guidance.
- Unknown required fields or unsupported permission scopes must fail closed.
- Implementations publish supported versions and conformance evidence.
- Extensions use namespaced fields and must not redefine core semantics.
- No implementation may claim conformance solely because it can parse a descriptor.

## 10. Non-goals

This contract does not define:

- A specific transport (HTTP, MCP, message bus, or otherwise).
- A universal identity provider or credential format.
- A global trust or reputation score.
- A token or financial incentive mechanism.
- Permissionless execution of third-party agents.
- A guarantee that a listed capability is safe, available, or endorsed.

These require separate decisions and implementation-specific threat models.

## 11. Acceptance scenarios for a future prototype

1. A visitor can inspect a public descriptor without logging in.
2. A consumer can request a harmless, bounded capability.
3. The issuer can reject the request without disclosing private policy.
4. A sensitive request remains blocked until explicit human approval.
5. An expired or revoked grant cannot be reused.
6. An invalid or out-of-scope request fails closed.
7. Both sides can correlate the request and outcome without exposing secrets.
8. A participant can remove a capability listing without losing its source system.
