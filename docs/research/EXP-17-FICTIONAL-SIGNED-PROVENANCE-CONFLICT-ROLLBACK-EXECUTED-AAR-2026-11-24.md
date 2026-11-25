# EXP-17 — Fictional Signed Provenance, License Metadata, Conflicts and Rollback (Executed)

**Date:** 2026-11-24. **Project:** Foromni open-source research only. **Status:** locally executed **15/15 Python standard-library tests PASS**. **No actual Internet Embassy or Foromni code transferred, license applied, external Git integration, provider API, production release, protected merge or real owner consent.**

## Research question and fixture

Can a proposed exchange contract protect a fictional shared module's byte integrity and reject nonmatching ownership/maintainer claims, source revision mismatches, unsupported declared license metadata, locally divergent edits, unexpected module path, and failed post-import validation, while keeping an explicit rollback path?

**Source:** `exchange.py` defines a canonical JSON HMAC demonstration signature for an AINO owner fixture and a Foromni maintainer fixture. The fictional package carries a path, SHA-256 of previous and new module bytes, a 40-character placeholder upstream commit, an Apache-2.0 **metadata label**, and a nonempty attribution notice. `test_exchange.py` checks denial conditions and explicit commit-or-rollback state. This is an *inert synthetic interchange protocol*, not an approved legal license.

## Actual local execution

Command:

```sh
cd foromni_exp17
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest discover -v
```

Observed: `Ran 15 tests in 0.001s / OK`, 0 failures/errors. Test cases:

- accepted signed synthetic source/maintainer fixture; 
- mutated owner approval rejected by MAC;
- wrong signer rejected;
- tampered maintainer approval rejected;
- modified source bytes cannot satisfy owner-source hash;
- invalid commit identifier rejected;
- allowed update produces expected new content;
- divergent local changes return explicit `CONFLICT` with originals preserved;
- owner rejects proposed update, originals preserved;
- failed post-import check rolls back original bytes;
- incompatible declared license metadata denied;
- untrusted upstream commit value denied;
- missing attribution notice denied;
- modified payload hash denied;
- traversal path denied.

**Exact SHA-256 for locally executed artifacts:**

| Artifact | SHA-256 |
|---|---|
| `exchange.py` | `531189e66b5e45fc0471b6aa5de0db835c862961494b57b0a15765e0c67b06b1` |
| `test_exchange.py` | `1f547714a17339a1484f6bd808ec304e6d749eee428268271af209c5401f2d6e` |
| `README.md` | `994dcf9e186a363c363a0712ce1e99a35b69d4bc9f7a0a579e1248c1339fd477` |
| `test_output.txt` | `cd055cb39bc5ddf1e62f256d3c7d6ca2b3c7023d7317d9660630fbae1c0b43a0` |

Download `foromni_exp17_provenance_conflict_evidence.zip` with source/test/log/SHA256SUMS from the research response. **This GitHub commit is the research report; the source remains in the evidence ZIP.** The prior EXP-16 did execute a two-local-Git-repository round trip, but this EXP-17 focused on exchange-contract negative tests, not a new authenticated remote Git workflow.

## Scientific and legal limits

- The two HMAC keys are hardcoded demonstration test material; **not** protected issuer custody or independent owner consent. A malicious caller with the key can forge either claimed approval.
- The `upstream_commit` is a 40-hex-character dummy value and checked for string equality/shape, not retrieved through authenticated Git to bind exact source revision. A syntactically valid SHA string is not a signed release.
- `rights='fixture-verified'` is a claimed field, not a chain-of-title verification, contributor agreement, license grant, or determination that a patent/trademark/dependency is licensed.
- `Apache-2.0` represents a label in a mock allowlist, not legal compatibility verification. **Foromni has not selected or adopted a software license as a result of this experiment.**
- Conflict detection uses simple base-byte hash mismatch, **not** a three-way merge resolver, verified rollback of real side effects or safe dependency upgrade.
- This exercise did not execute a supply-chain scan, detect complex embedded secrets, support multiple-file changes, sign SBOM/provenance, or isolate independently authenticated reviewers.
- All tests and candidate implementation were authored by the same assistant; independent QA is not established.

## AAR and next research gate

**Supported locally:** fail-closed fixture approval, tamper detection against a test key, simple divergent-base conflict detection, explicit cancel and rollback, metadata/path checks.

**Not established:** legally enforceable AINO→Foromni rights, authentic owner authority, Git source-bound release, compatibility with project licenses or safe automated updates.

**Next discriminating step:** require actual accepted-owner permissions backed by trust service (or independently operated simulated issuer), verify exact Git commit/tree contents, import SPDX/NOTICE and dependency review, test three-way merge conflicts and package rollback on separate versioned repositories, and require human AINO update approval. Do not transfer real IE source until formal owner authorization and the licensing model are settled.

**Verdict:** `EXP17_SYNTHETIC_PROVENANCE_CONFLICT_15_OF_15_PASS`; `LEGAL_RIGHTS_AND_AUTHENTIC_GIT_PROVENANCE_UNVERIFIED`; `FOR007_UNCHANGED`.

**Research companion:** [PMI-CPMAI governance roadmap](PMI-CPMAI-AI-PROJECT-MANAGEMENT-AGENCY-EXECUTION-RD-V0.1.md) proposes a measured six-phase governance comparison, not credential purchase or an operational gate.
