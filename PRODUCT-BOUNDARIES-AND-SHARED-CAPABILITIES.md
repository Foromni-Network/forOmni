# Foromni and Internet Embassy: Product Boundaries and Shared Capabilities

**Status:** Founder-aligned strategic proposal; requires maintainer review before becoming a binding architecture decision.

## 1. The two products have different jobs

Foromni and Internet Embassy are complementary, independently governed products. They should reinforce one another without collapsing into a single product, sharing every internal system, or creating a dependency that prevents either from serving others.

### Foromni — horizontal ecosystem infrastructure

Foromni focuses on foundational utilities and common infrastructure that can benefit many independent people, businesses, communities, projects, and AI-native operations.

Examples of potential Foromni capabilities:

- Portable identity and organization/project references.
- Capability discovery and interoperable descriptions.
- Permissioned capability exchange and task handoffs.
- Contribution provenance, attribution, and portable records.
- Cross-project discovery and relationship coordination.
- Interoperability adapters, schemas, and reference implementations.
- Shared trust, authorization, audit, and policy primitives.
- Open developer utilities that make independent AI-native operations easier to connect.

These are ecosystem-level capabilities. They should be designed for reuse across multiple independent operators, not tailored to one membership business.

### Internet Embassy — member-facing ecosystem and vertical operations

Internet Embassy focuses on its own members, partners, customers, and commercial ecosystem.

Examples include:

- Member onboarding, Passport experiences, profiles, and membership journeys.
- IE-specific pillar navigation, services, marketplace, recruiting, learning, and venture workflows.
- Member engagement, growth, referrals, and business operations.
- IE-specific automation, agent workflows, dashboards, and internal operating utilities.
- Commercial packaging, billing, customer support, and service delivery.
- Proprietary workflows, business logic, and customer-specific integrations.

IE can build these utilities to solve its own real operating needs and serve its members. It should not be forced to wait for a generalized Foromni equivalent before improving its product.

## 2. The shared-capability flywheel

The intended relationship is reciprocal and selective:

1. **Foromni establishes common infrastructure** where a capability has broad ecosystem value.
2. **IE builds its member-facing product and operations** using its own architecture and the shared capabilities that make sense.
3. **IE discovers a useful general-purpose solution** while solving a real member or operating problem.
4. **The reusable portion is identified and separated** from IE-specific workflows, proprietary business logic, customer data, and secrets.
5. **Ownership, contributor permissions, license compatibility, security, and maintenance responsibility are established.**
6. **An appropriately generalized capability may be contributed to Foromni** as a reusable utility, reference implementation, specification, or adapter.
7. **Foromni documents and maintains the common capability** so other independent AI-native operations can adopt it.
8. **IE can continue using it**, while retaining its own differentiated member experience and product-specific implementation.

The flow works in both directions. Foromni capabilities can be adopted by IE; reusable lessons and components from IE can flow back to Foromni when permission and licensing allow.

## 3. The key boundary: generalize, do not indiscriminately copy

A capability developed inside IE is not automatically eligible for Foromni.

Before moving anything across the boundary, classify it:

| Class | Examples | Default treatment |
|---|---|---|
| General ecosystem utility | Portable schema, generic adapter, reusable authorization primitive | Candidate for Foromni contribution after review |
| IE-specific product capability | Member Passport experience, IE marketplace flow, pillar-specific UX | Remains in IE unless deliberately generalized |
| Proprietary business logic | Pricing strategy, internal growth logic, differentiated service delivery | Remains private to IE |
| Customer/member data | Profiles, private records, communications, usage data | Never copied into public Foromni repositories |
| Third-party asset | Upstream code, licensed datasets, external API client | Reuse only within license and permission terms |
| Shared specification | Neutral interface contract or interoperability standard | Can be co-developed with explicit ownership and governance |

A useful test is: **Could several unrelated organizations use this capability without adopting IE's membership model, brand, business rules, or customer data?** If yes, it may be a Foromni candidate. If not, it likely belongs in IE.

## 4. Ownership and contribution rules

- Neither project automatically owns the other's code, data, infrastructure, or roadmap.
- A shared capability needs a named maintainer and an explicit source-of-truth repository.
- Contributions require clear provenance, ownership, permission, and compatible licensing.
- Do not move code from a private IE repository into a public Foromni repository until its owner has approved publication and all embedded dependencies, assets, and data have been reviewed.
- Customer data, credentials, internal prompts, secrets, and private operational details must never be used as contribution material.
- When only the concept is reusable, implement a clean, independently authored general-purpose version rather than copying protected implementation details.
- Record upstream/downstream versions and compatibility expectations.
- Either project must be able to continue operating if the other is unavailable.

## 5. Architecture implications

Prefer a layered architecture:

- **Common contracts:** open, versioned schemas and protocols for identity references, capabilities, task exchange, provenance, and authorization.
- **Reusable utilities:** independently deployable components that implement common contracts.
- **Adapters:** small connectors that let different products adopt the utilities without surrendering their existing architecture.
- **Product applications:** Foromni's network experience and IE's member-facing experience, each with its own UX, policies, data model extensions, and commercial logic.
- **Governance boundary:** separate maintainers, repositories, credentials, data stores, release decisions, and production environments unless a specific shared service is explicitly agreed.

Avoid premature centralization. A shared contract can be adopted before a shared hosted service exists. Independent deployments should remain possible.

## 6. Prioritization rule

Prioritize a capability for Foromni when:

- Multiple independent operators could benefit.
- It solves an interoperability or ecosystem infrastructure problem.
- It can be described and maintained independently of IE.
- It has clear security, privacy, licensing, and operational boundaries.
- There is evidence of demand beyond one internal use case, or a strong foundational reason to standardize it.

Prioritize a capability for IE when:

- Its primary value is serving IE members or customers.
- It depends on IE-specific business processes or product experience.
- It is a competitive differentiator or proprietary operating method.
- Generalization would add complexity without clear ecosystem benefit.

A capability can begin in either place. Its eventual home is determined by its purpose, ownership, and reuse potential—not by which team implemented it first.

## 7. What this means for the roadmap

### Foromni
Build the common infrastructure, utility contracts, reusable components, and open interoperability layer. Prove that multiple independent operations can use them.

### Internet Embassy
Continue building the full member-facing ecosystem and the practical utilities needed to operate it. Adopt shared Foromni capabilities selectively and contribute generalized improvements back when appropriate.

### Together
Use IE as an early real-world proving ground, not as the definition of the whole Foromni network. Seek additional independent adopters early so Foromni's architecture is tested against different operating models.

## 8. Success measures

Measure the relationship by outcomes rather than code volume:

- Number of independently operated systems adopting a Foromni utility.
- Reusable capabilities contributed with clear provenance and maintainership.
- Reduction in duplicated integration effort.
- Successful cross-system task and capability exchanges.
- Independent deployments that remain operable without IE.
- IE member value delivered without forcing IE-specific assumptions into common infrastructure.
- External contributions and reciprocal collaborations that are mutually confirmed.

## 9. Open decisions

This proposal does not yet decide:

- Repository-by-repository licensing.
- Whether any common utility is hosted centrally or self-hosted by participants.
- The exact source-of-truth policy for each shared component.
- Whether Foromni and IE share any operational service.
- Long-term governance or funding arrangements.

Resolve these through separate, evidence-based decisions. Do not infer shared ownership or operational access from strategic alignment alone.
