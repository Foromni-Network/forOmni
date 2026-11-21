# Foromni MVP Domain Model

**Status:** Proposed conceptual model; validate through user research before implementation.  
**Related:** [ADR-0001](ADR-0001-network-boundaries-and-portability.md)

This document defines the smallest useful concepts for a network discovery and contribution MVP. It is not yet a database schema or API contract.

## Design rules

- Keep people, organizations, projects, capabilities, contributions, and relationships distinct.
- Separate public discovery data from private account and relationship data.
- Make ownership, source, attribution, visibility, and permission explicit.
- Prefer references to external resources over copying their content.
- Do not introduce a global reputation score in the MVP.
- Do not make Foromni identity mandatory to view public external projects.
- Every record has a stable identifier, creation/update metadata, and an accountable owner or source.

## Core concepts

### Person

A human participant.

Potential fields:
- Stable internal identifier.
- Display name or pseudonym.
- Optional public biography and declared capabilities.
- Optional links the person chooses to publish.
- Visibility and contact preferences.
- Account and authentication references stored separately from public profile data.

Never expose private email, phone, legal identity, or authentication metadata by default.

### Organization

A business, nonprofit, open-source collective, community, or other group.

Potential fields:
- Stable identifier.
- Display name and description.
- Canonical website and public links.
- Declared ownership/administrators.
- Public contact route, if explicitly supplied.
- Visibility and verification references.

Foromni membership does not imply endorsement or legal affiliation.

### Project

An independently governed initiative, product, repository, or community.

Potential fields:
- Stable identifier.
- Name and description.
- Canonical public URLs and repository references.
- Owner organization/person reference where publicly established.
- License/terms and source evidence.
- Governance and contribution guide references.
- Activity review timestamp.
- Relationship status, if any.

A project can exist in discovery without its maintainers joining Foromni.

### Capability

A discoverable ability offered by a person, organization, project, service, or agent.

Potential fields:
- Stable identifier and issuer.
- Human-readable name and description.
- Actor type: human, organization, software service, or agent.
- Input/output expectations or supported interface references.
- Scope, limitations, availability, and version.
- Authorization requirements.
- Evidence/source and last-reviewed timestamp.

A capability listing is descriptive, not a grant of execution authority.

### Contribution

A specific, attributable piece of work or resource shared with a project or community.

Potential fields:
- Stable identifier.
- Contributor identity or attribution label.
- Recipient project.
- Type: code, issue, documentation, design, research, service, integration, or other.
- Source and destination references.
- Commit/PR/release or artifact identifiers where applicable.
- License/permission and provenance evidence.
- Status and outcome.
- Optional recipient confirmation.

Do not infer that an opened PR was accepted or that an accepted contribution is maintained indefinitely.

### Relationship

A consent-aware record of collaboration between independent participants.

Potential fields:
- Stable identifier.
- Participating identities/projects.
- Relationship type: introduction, contribution, integration, collaboration, sponsorship, or other.
- Status and agreed scope.
- Public/private visibility.
- Evidence of mutual confirmation.
- Agreed next step and review date.

Private relationship notes must never be exposed through public search.

### Proposal

A request or suggested change to the network.

Potential fields:
- Stable identifier.
- Author.
- Problem statement and intended beneficiaries.
- Proposed change and alternatives.
- Dependencies, risks, and acceptance criteria.
- Discussion and decision record references.
- Status.

### Task

A bounded unit of work assigned to a human or authorized agent.

Potential fields:
- Stable identifier.
- Owner and authorized actor.
- Scope and acceptance criteria.
- Dependencies.
- Status and timestamps.
- Required approvals.
- Provenance and execution evidence.
- Result and follow-up.

A task record is not itself permission to execute. Authorization must be checked independently at action time.

## Visibility model

Initial visibility classes:

- **Public:** intentionally published for global discovery.
- **Unlisted/shared:** accessible only through an explicit sharing mechanism; not indexed by default.
- **Private:** visible only to the owner and explicitly authorized collaborators.
- **Restricted operational:** credentials, security events, private messages, and sensitive personal data; never part of public profiles or public discovery.

Visibility is enforced server-side. Hiding a field in the UI is not access control.

## Relationships and provenance

- Records identify their source and accountable owner.
- Imported public metadata retains the canonical source URL and review date.
- User-submitted claims are labeled as self-declared until verified.
- External projects are not treated as Foromni members unless they explicitly opt in.
- Contribution attribution links to upstream evidence where available.
- Edits to important claims should retain an audit trail.

## MVP workflows this model should support

1. A visitor discovers a public project without creating an account.
2. A participant creates or claims a profile with clear ownership.
3. A participant lists a project or capability with explicit visibility.
4. A contributor records an upstream contribution with source and recipient references.
5. Two participants mutually confirm a collaboration relationship.
6. A visitor submits a proposal without receiving privileged access.
7. An owner exports their profile and contribution records.
8. An owner revokes a connection without losing the source project or its own data.

## Deliberately excluded from the first model

- Financial balances, tokens, airdrops, inflation, or voting weight.
- Unverified reputation scores or automated trust rankings.
- Public contact scraping or unsolicited bulk outreach.
- Autonomous cross-organization actions without explicit scoped authorization.
- Central ownership of external project identities or content.

## Open questions before schema implementation

- Which profile fields are genuinely necessary for first-user value?
- Should project ownership be claimed, verified, or simply attributed to a public source?
- Which data needs to be portable across platforms from day one?
- What is the minimum viable moderation and abuse-reporting workflow?
- What public contribution evidence can be imported reliably without scraping or violating terms?
- What is the simplest safe authorization model for integrations?

Implementation should not begin until these questions are resolved sufficiently to define testable acceptance criteria and a privacy threat model.
