# Foromni ↔ AINO Licensing, Contribution Provenance and Update Exchange R&D v0.1

**Status: RESEARCH IDEA / LEGAL-REVIEW GATE. NOT A LICENSE OR CONTRIBUTOR AGREEMENT.** Date: 2026-11-23. Foromni research branch only; no Internet Embassy repository modification, code imports, merges, releases, IP transfers or actual relicensing.

## Founder goal

A global open-source Foromni network in which independent AINOs, including Internet Embassy (IE), may **donate or upstream common infrastructure**, collaboratively develop and test it in Foromni, and **export upstream improvements back to their own separately owned repositories/operations**. Both Foromni and participating AINOs need legally sustainable rights, provenance and control of secrets, customer data, brands and proprietary extensions.

### Verified immediate blocker

On the `research/global-agent-roadmap-execution` branch, direct GitHub file checks for root `LICENSE`, `LICENSE.md`, and `CONTRIBUTING.md` returned not found; root `README.md` only described the mission. The absence of those named files is **not an exhaustive audit of all repository licensing metadata or every file header**. Treat both **code contribution intake** and **export** as hold-until-proven-rights. GitHub explains that without a license default copyright rules remain in effect; publicly viewable/forkable does not automatically give derivative/distribution rights.

## Separate rights layers — critical to the model

1. **Shared Foromni core** — independently selected OSI-approved license, copyright notices, patent grant/termination considerations, contribution rights, dependency and provenance scans.
2. **Inbound AINO contribution** — authorized legal owner, employment/contractor rights, third-party dependencies and submodules, existing license compatibility, consent to outbound distribution and scope, explicit non-confidentiality. **A PR does not cure missing upstream rights.**
3. **AINO-specific proprietary layer** — private configs, secrets, customer records, prompts, workflows, custom UI, internal policies and project assets stay in the AINO repo. Default: never import them into public Foromni.
4. **Outbound improvements** — versioned shared core updates with signed source commit/tree, SPDX licenses, attribution/NOTICE, change log, SBOM, compatibility/contract tests, and explicit AINO maintainer approval to integrate.
5. **Brand/identity** — separate trademark/name/logo permission policy; copyright license is not a trademark grant.
6. **Contributors and patent rights** — DCO vs CLA vs copyright assignment should be evaluated with counsel, not adopted by assumption. Ensure patent and future relicense goals align with inbound terms.
7. **Governance and safety** — project/maintainer authority, CODEOWNERS, review requirements, security disclosures, release signing, branch gates and export provenance, separate from software licenses.

## Candidate licensing patterns (research comparison)

| Candidate | Strength | Trade-off for AINO return flow | Question for legal review |
|---|---|---|---|
| Apache-2.0 (permissive, includes patent grant) | Broad commercial and closed-source AINO consumption; relatively straightforward import/export of core code | AINO modifications may remain private; core improvements may not flow back | Is voluntary upstream contribution sufficient for Foromni mission? How protect trademarks and shared governance? |
| MPL-2.0 (file-level copyleft) | Modifications to MPL-covered files distributed to others generally stay under MPL, while separate proprietary files can coexist | Requires file-level/source compliance on distribution; licensing combinations/secondary-license conditions need careful mapping | Is file-level reciprocal sharing the desired balance? What happens for network services not distributed? |
| AGPL-3.0 (network copyleft) | More reciprocal network-service obligations in covered combined/modified works | Harder compatibility and proprietary integration for independent AINOs; may inhibit collaboration | Would this undermine intended plug-in/private AINO ecosystem? |
| Dual licensing / commercial exceptions | Flexible outbound deals if every relevant rightsholder grants needed rights | Needs appropriate contributor rights/CLAs and sophisticated governance, not automatic | Who owns patents and has authority to sublicense/relicense? |
| Project-specific source-available license | May restrict defined uses | May not qualify as OSI open source; can make return flow and ecosystem trust harder | If restrictions are core goals, is calling project open source inaccurate? |

**No winner selected.** Initial technical hypothesis: an Apache-2.0 or MPL-2.0 **shared core plus separately licensed private AINO extensions** may support import/export with fewer conflicting aims. Which is optimal depends on contribution reciprocity, network use, future relicensing, commercial/managed service model, trademark policy and contributor patent rights. These are legal/governance decisions, not engineering defaults.

Open Source Initiative's definition requires rights to redistribute and modify, and forbids discriminating against classes of users or fields of endeavor. A clause forbidding competitors, certain AINOs or commercial reuse is incompatible with ordinary OSI open source. The software license **cannot guarantee that all downstream improvements are contributed back**, especially under permissive licensing.

## Source and ownership boundary matrix

| Source type | Default inbound disposition | Outbound to an AINO |
|---|---|---|
| Foromni original shared core with approved license | Eligible after provenance/rights verification | Yes, per actual license + notices |
| AINO-owned generic module explicitly released under compatible terms | Candidate upstream with attributable commit and contribution check | Yes, preserve attribution and same obligations |
| AINO proprietary feature or customer logic | **No public import**; replace with neutral interface, adapter or fresh implementation | Stays solely in that AINO repo |
| Third-party dependency, copied tutorial, AI-generated code | Verify origin, terms and patent/notice obligations first; no blanket assumption of ownership | Only if compatible, notices/SBOM preserved |
| Secrets, environment keys, employee/client data | **Never** put in public source or exported templates | Use local secret injection and placeholder configuration |
| Security exploit/unsafe sample | Private responsible-disclosure intake or inert fixture only | No automatic dissemination |
| Trademarks / names / logos | Separate permissions and brand policy | No implied use rights |

## Proposed reproducible update round trip (NOT IMPLEMENTED)

```
AINO private repo
  → identify generic shareable module + owner signoff
  → clean-room boundary/secrets scan + upstream source/license evidence
  → explicit outbound contribution authorization
  → isolated Foromni contribution branch and source-bound work packet
  → independently verified tests + review + maintainer accept
  → versioned shared-core release with license + provenance / SBOM / NOTICE
  → AINO import PR pinned to immutable upstream SHA/version
  → AINO-owned integration tests, security + licensing review
  → explicit owner merge/deploy approval (no auto-promote)
```

**Crucial:** do not simply `git push` private IE history, trade secrets or customer config into a public Foromni fork. Prefer a narrow original module or independently implemented interface; record code origin with file-level ownership and source revision. Separate *sharing* from *running, testing, merging and deploying*.

## Research questions / experiments backlog

- **LIC-01 Legal/technical inventory:** identify repository license declarations at root and nested modules, all copyright notices, dependency SPDX list, contributors, grants and any provenance restrictions. Validate default vs research branches before choosing license.
- **LIC-02 Compatibility matrix:** simulate Apache→MPL→GPL/AGPL and commercial AINO adoption on two example modules, including third-party dependency and patent cases; counsel-approved written conclusion.
- **LIC-03 DCO vs CLA:** who must sign, contractor/employee chain of title, patent rights, ability to dual-license, project stewardship and revocation; no contributor agreement without explicit informed founder authorization.
- **LIC-04 Export/update contract:** a signed update manifest with upstream commit, path, SPDX expression, notices, SBOM, checksums, compatibility tests, migration and rollback plan; AINO acceptance gate.
- **LIC-05 Two-repo synthetic tabletop:** Foromni generic module + **fictional** private AINO adapter; upstream, improve, package, export, pass source license and provenance checks; no actual IE repo import.
- **LIC-06 Risk and dispute drill:** license conflict, secret leak, brand misuse, attempted change of terms and contributor ownership challenge; require stop/escalation.

## Founder decisions needed before legal change

Clarify: desired code reciprocity on distributed core changes, proprietary plugin rights, network/SaaS use, whether competing AINOs can use shared core, commercial model, ability to relicense, who holds copyrights and trademarks, contributor patent treatment and formal AINO update approval. Seek qualified counsel for actual license selection/contributor terms if material business stakes.

## Reference authorities

- GitHub Docs — Licensing a repository: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
- Open Source Initiative — Open Source Definition: https://opensource.org/osd
- Apache Software Foundation — Apache License 2.0 text: https://www.apache.org/licenses/LICENSE-2.0.html
- Mozilla — MPL 2.0 and FAQ: https://www.mozilla.org/en-US/MPL/2.0/ and https://www.mozilla.org/en-US/MPL/2.0/FAQ/
- Software Freedom Conservancy — DCO and contribution rights discussion: https://sfconservancy.org/contractpatch/

**Next execution:** record this as a future idea, not an approved license. Continue EXP-15 security convergence separately; do not use Foromni as an IE staging server until licensing and data boundary gates are verified.
