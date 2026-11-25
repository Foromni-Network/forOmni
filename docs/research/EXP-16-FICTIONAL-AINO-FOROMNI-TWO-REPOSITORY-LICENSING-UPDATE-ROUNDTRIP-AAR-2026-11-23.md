# EXP-16 — Fictional AINO ↔ Foromni Bidirectional Code and License-Metadata Round Trip (Executed)

**Date:** 2026-11-23 (America/Chicago) / 2026-11-24 UTC. **Scope:** Foromni research only. **Status:** LOCAL TWO-GIT-REPOSITORY EXPERIMENT, **16/16 final tests PASS**, zero ResourceWarnings. No Internet Embassy access or modification; no production Foromni source import, real license choice, signed legal agreement, remote Git push, protected merge, code deployment or paid API.

## Research question

Can an independently owned AINO upstream a **generic approved** module to Foromni, have an improvement committed there, and import the updated module back into the AINO **without transferring private files or Git history**, while a proposed manifest validator rejects missing approvals, incompatible license metadata, tampering, path traversal, version mismatch and obvious secret-shaped content?

**Hypothesis:** the permitted fictional round trip succeeds without modifying private AINO bytes; negative inputs are rejected before destination writes. This is a source/scope/provenance engineering exercise, **not** legal license compliance validation.

## Procedure and actual Git experiment

The Python standard-library fixture creates two separate **temporary local Git repositories**:

1. `fictional_aino_private`: contains `shared/task_envelope.py` and `private/proprietary_rules.py`; first commit `45a97a886d9a2bae2cef33ea40b1296dee213827`.
2. `fictional_foromni_upstream`: receives only the allowlisted shared module following mock owner/right approval fields and declared `Apache-2.0` metadata; first commit `e220d5066f4973cbdd9a902e29c6d6b7006d8618`.
3. Upstream adds `is_valid(task_id)` to the shared module and commits update `9845e031076a93eaf914aa948329cd1347bd8db8`.
4. Export creates a manifest with source ref, module path, SPDX-like declared expression, version `0.2.0`, origin label, byte SHA-256, notices and simulated owner approval. The fictional AINO importer verifies exact one-module allowlist, version, digest and mock approval before writing the updated module. The AINO update commit is `35754420eeb28b3a15d258d82c526669a45e3d0b`.
5. Verification confirms upstream tree contains only `shared/task_envelope.py`, the AINO private file remained unchanged, updated AINO module SHA-256 matches upstream, and each project maintained distinct commits and history. All Git operations were local; **those SHAs are from ephemeral Git repos and cannot be fetched from GitHub**.

## Actual local execution

```sh
cd foromni_exp16_license_exchange
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v
PYTHONDONTWRITEBYTECODE=1 python git_roundtrip.py
```

**Observed:** `Ran 16 tests in 0.116s / OK`. The extra Git script printed both local trees, four commit SHAs and all expected separation flags as true. **Test methods are deterministic assertions, not 16 statistically independent production replications.**

### Negative/positive cases executed

| Domain | Observed |
|---|---|
| One generic module upstream and imported back | PASS |
| Private AINO file unchanged, absent upstream | PASS |
| Separate real local Git histories | PASS |
| Missing inbound owner approval | Denied |
| Contributor rights unverified **mock flag** | Denied |
| Unknown license ID or declared mismatch | Denied |
| Upstream release or downstream import approval absent | Denied |
| Accidental private file in export package | Denied |
| Path traversal in module field | Denied |
| Modified package payload vs declared hash | Denied |
| Obvious `api_key` or `password` fixture | Denied |
| Version not in AINO compatible set | Denied |
| Missing notices or provenance | Denied |
| Unrecognized manifest schema | Denied |

## Exact executed source and evidence

The downloadable `foromni_exp16_aino_license_roundtrip_evidence.zip` contains `exchange.py`, `git_roundtrip.py`, `test_exchange.py`, `README.md`, `git_result.json`, `test_output.txt` and `SHA256SUMS`.

| Artifact | SHA-256 |
|---|---|
| `exchange.py` | `168d4709d1d53cd3389247e8199ab308d6b688e8f08e2c80b8c6400a70d3ba0b` |
| `git_roundtrip.py` | `f4a45bc651323404099ffb09b6a28a881c67cae1a153b03a8f7f364d2c2d8e55` |
| `test_exchange.py` | `ba1d8af6e72929db09fa255ae66319d74d319d19e1ca49068d086d2c589c9d06` |
| `test_output.txt` | `e0eeea0a52b19a98c605bd9897556132fd9d2368c288e5374057b0b179d5be64` |
| `git_result.json` | `e2a3d25e97607d6e3c1afe686801dd9f20ce48b8079cd876f1c133c3552d4c2e` |
| Evidence ZIP | `a6178e7c0674cb966509c3f6c040cf9d993771f368d94d268715e8a8ed26d584` |

**Distribution:** this GitHub commit stores the scientific report. Runnable source/test bytes are in the attached archive, not GitHub source files; the ephemeral Git repositories were deleted after tests.

## Scientific and legal limitations — important

1. **Not a grant of rights.** `owner_approved` and `rights_verified_mock` are boolean claims from caller-controlled input, not signed owner consent or chain-of-title proof. False claims could pass. No contributor agreement, DCO, copyright notice/license text, patent review or legal opinion was collected.
2. **No license has been applied to Foromni or IE.** `Apache-2.0` and `MPL-2.0` are hypothetical allowed metadata strings. The code does not implement SPDX's full license expression grammar or compute Apache/MPL/GPL compatibility. It cannot assert that an actual export is permitted.
3. **Hash is not authentication.** SHA-256 catches payload mismatch relative to declared manifest, but an adversary controlling the payload and manifest can replace both. Production needs trusted release signing, immutable upstream source checkout and independent verification.
4. **Secret scan is heuristic.** Simple patterns only reject tested secret-shaped strings, not arbitrary customer data, entire private histories, proprietary logic, embedded binary assets, tokens, archives or LFS objects. Require source allowlist, manual review and robust secrets/DLP before publishing.
5. **No external package publishing, release automation or real AINO/Foromni exchange.** Repositories are throwaway and local; remote protected-ref controls, maintainer approvals, source owner claims, vulnerability/SBOM checks, license text and trademark governance were not tested.
6. **File copy is not a Git merge.** This experiment proves two repository histories can be preserved and the one-module content exchanged, not automatic bidirectional patch convergence under nontrivial conflicts.
7. **No independent reviewer:** same assistant authored test code and candidate; no external authenticated QA or legal counsel reviewed actual rights.

## Decision

**Engineering hypothesis supported under toy conditions:** a narrow, versioned, provenance-manifest exchange can avoid importing AINO private files and preserve separate Git histories, when every upstream/export/import path is explicitly allowlisted and approver rights are assumed.

**Not established:** actual legal import/export permission, strong identity, cryptographically attested provenance or release, true conflict resolution, official SPDX compliance, or suitability for the live IE and Foromni repositories.

## Next gates and research backlog

- **LIC-07 provenance:** real signed owner attestations (test keys only), source-bound immutable Git SHA and accepted task/reviewer.
- **LIC-08 compatibility:** a counsel-reviewed Apache-2.0 vs MPL-2.0 distribution and SaaS AINO matrix with exact NOTICE/source disclosure and patent obligations.
- **LIC-09 conflict/rollback:** a two-repo patch conflict, three-way merge/rebase and safe human-controlled rollback, no auto-promote.
- **LIC-10 package boundary:** SPDX SBOM, dependency notices, secret and code-origin scan, trademark separation, fail-closed export.
- **LIC-11 exchange authorization:** AINO opt-in release/upgrade with human owner approval and no hidden tool/credential access.

**Founder licensing choice still pending.** Per GitHub documentation, a public repo without a chosen license does not grant default modify/redistribute rights. MPL-2.0 is file-level reciprocal for covered modifications; Apache-2.0 is permissive with patent terms. This report recommends neither automatically.

References:
- GitHub Docs: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
- Mozilla MPL FAQ: https://www.mozilla.org/en-US/MPL/2.0/FAQ/
- SPDX license expressions: https://spdx.github.io/spdx-spec/v3.0.1/annexes/spdx-license-expressions/

**Verdict:** `EXP16_LOCAL_BIDIRECTIONAL_EXCHANGE_16_OF_16_PASS`, `PRIVATE_HISTORY_EXCLUDED_FROM_UPSTREAM`, `LEGAL_RIGHTS_AND_SIGNED_PROVENANCE_UNVERIFIED`, `FOR007_UNCHANGED`.
