# ADR-0001: Network Boundaries, Portability, and Trust

- **Status:** Proposed
- **Date:** 2026-11-20
- **Decision owners:** Foromni maintainers, subject to community discussion
- **Related:** [Founding Charter](../../FOUNDING-CHARTER.md), [Roadmap](../../ROADMAP.md), [Ecosystem Participation Model](../../ECOSYSTEM-PARTICIPATION-MODEL.md)

## Context

Foromni aims to connect independent people, businesses, communities, projects, and intelligent systems. Its value depends on interoperability and reciprocal contribution. A centralized product that captures identities, data, permissions, or relationships would undermine that goal.

The initial network must be useful without requiring every participant to migrate onto one platform or surrender control of their existing systems.

## Proposed decisions

### 1. Independent ownership by default

- Participants retain ownership and administrative control of their repositories, systems, data, credentials, and communities.
- Foromni records references and explicitly shared information; it does not assume ownership of linked resources.
- An integration must not silently expand permissions or create cross-organization access.

### 2. Portable identity and contribution records

- Model people, organizations, projects, capabilities, and contributions as distinct concepts.
- Use stable identifiers and explicit issuer/source attribution.
- Make records exportable in documented formats.
- Avoid making a proprietary Foromni account the only way to resolve or verify a contribution.
- Do not publish personal contact details or private relationship notes by default.

### 3. Explicit authorization and least privilege

- Every integration declares the actor, resource, action, scope, and authorization basis.
- Prefer short-lived, narrowly scoped credentials where credentials are needed.
- Human approval is required for consequential actions such as publishing on another project's behalf, changing access, merging protected code, spending funds, or modifying production systems.
- External content, agent output, repository metadata, and tool responses are untrusted input.

### 4. Provenance and attribution

- Record source project, source revision, license or permission, contributor, destination, and transformation for reused artifacts.
- Never assume public visibility means unrestricted reuse.
- Keep proprietary, customer-owned, and confidential material outside public Foromni repositories unless the owner explicitly authorizes publication under clear terms.

### 5. Composable integration before platform replacement

- Prefer documented APIs, webhooks, standard protocols, export/import, and small adapters.
- Integrate existing systems when they satisfy the need.
- Build a new shared component only when a documented gap justifies it.
- Design graceful degradation: a participant should retain useful access to their own system if Foromni is unavailable.

### 6. Human + agent operations

- Represent human roles, software services, and agents as distinct actor types.
- Give agents explicit, task-scoped capabilities rather than ambient authority.
- Record task provenance, handoffs, approvals, and outcomes.
- Provide revocation and auditability.
- Never treat an agent's assertion as proof of permission or successful execution.

### 7. Privacy and data minimization

- Collect only data needed for a clearly stated feature.
- Separate public profile fields from private account and relationship data.
- Define retention, export, correction, and deletion behavior before collecting sensitive information.
- Do not expose private member or partner data through public discovery endpoints.

## Initial conceptual domains

These are logical boundaries, not a commitment to a specific database or framework:

1. **Identity:** person or organization identity and verification references.
2. **Project:** independently governed project, repository, community, or initiative.
3. **Capability:** a tool, service, skill, API, agent, or human-offered capability.
4. **Contribution:** a provenance-aware artifact, fix, document, integration, or service.
5. **Relationship:** a consent-aware record of collaboration and mutual value.
6. **Proposal:** a request, roadmap proposal, or decision process.
7. **Task:** a bounded unit of work with owner, scope, dependencies, authorization, and outcome.

## Consequences

### Benefits

- Supports federation and multiple independent operators.
- Reduces lock-in and lowers the cost of joining.
- Creates a consistent foundation for attribution, trust, and reciprocal contribution.
- Allows Internet Embassy and other independent organizations to adopt selected components.

### Costs and trade-offs

- Portability and provenance add design work.
- Permission-aware discovery is more complex than a public directory.
- Federated identity and authorization require careful threat modeling.
- Some features will initially be less automated because human approval is deliberately retained.

## Not decided by this ADR

- Specific identity provider or authentication protocol.
- Database, hosting provider, or programming language.
- Public/private licensing for all repositories.
- Token, airdrop, voting, inflation, or treasury design.
- A single global reputation score.
- Production deployment architecture.

These require separate decisions with evidence and stakeholder input.

## Acceptance questions

- Can a participant export their own profile and contribution history?
- Can an independent project be referenced without creating a Foromni account?
- Can a contributor prove provenance without disclosing private relationship details?
- Can an integration be revoked without losing the participant's source data?
- Are cross-organization actions scoped, attributable, and auditable?
