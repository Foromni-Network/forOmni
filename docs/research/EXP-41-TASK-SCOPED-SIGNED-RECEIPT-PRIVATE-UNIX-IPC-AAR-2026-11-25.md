# EXP-41 — Task-scoped signed receipt grants and private Unix IPC: executed AAR

**Date:** 2026-11-25. **Project/branch:** Foromni-Network/forOmni / `research/global-agent-roadmap-execution`. **Execution:** 22/22 local Python unittest checks passed in one run (`Ran 22 tests in 22.867s; OK`), Python resource warnings treated as errors. No FOR-007 or Internet Embassy modifications, protected merge, customer testing or deployment.

## Research question

EXP-40 permitted observer-wide provider receipt readback based solely on an OS UID. Can exact task, project, resource and effect binding plus per-read signed Ed25519 grant narrow evidence access? Can Unix DAC protect the provider IPC path while `SO_PEERCRED` also checks caller UID?

## Executed implementation

- `engine.py` verifies signed `draft.create` mutation grants and signed `receipt.read` grants separately; grant scope checks cover exact task/project/resource/effect, operation, expiry (maximum one-hour horizon) and nonce. A `receipt.read` consumes nonce durably on first attempt, rejecting replay. Provider uses its own private signing key to produce exact receipt.
- `service.py` runs actual provider subprocess as UID 22201 with SQLite effect and nonce ledgers. Normal writer UID 22202 can only apply, reader UID 22203 can only read. UID 22205 cannot access IPC socket without group membership; if added to the socket group it still fails the peer-UID role check.
- Provider socket mode 0660 inside group-restricted directory 0770, separate provider private directory 0700 and key file 0600; tests confirm reader cannot inspect signing key. One root experiment operator creates all fixture keys and services.
- No broad `ids` / listing endpoint is exposed.

Command:
```sh
cd foromni_exp41
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py
```
**Actually observed:** `Ran 22 tests in 22.867s; OK`.

## Twenty-two verified test cases

1. Actual provider UID.
2. Private socket directory 0770 and socket 0660.
3. Reader denied private provider signing key.
4. Valid authorized effect applied.
5. Same effect deduplicated.
6. Missing mutation grant rejected.
7. Unauthorized UID denied by Unix DAC.
8. Group-member wrong UID denied by peer credentials.
9. Writer cannot read.
10. Reader cannot mutate.
11. Receipt read requires separate signed grant.
12. Exact authorized receipt obtained and Ed25519 verified.
13. Cross-project grant denied.
14. Cross-task grant denied.
15. No broad receipt enumeration endpoint.
16. Replayed read nonce rejected.
17. Expired read grant denied.
18. Cross-effect read denied.
19. Provider restart retains idempotent effect.
20. Authorized historical read succeeds after restart.
21. **Negative:** fixture owner-key holder can invent signed work.
22. **Negative:** common root coordinator can inspect provider signing key.

**Passing negative controls reproduce gaps, not guarantees.**

## Exact artifacts

The conversation archive `foromni_exp41_scoped_evidence.zip` (SHA-256 `ff80d9b513f67cc62b551cac76024792f9b9157fb3ea5f785dfe462f15343d9a`) includes runnable code, README, exact `test_output.txt`, and SHA256SUMS.

| File | SHA-256 |
|---|---|
| `engine.py` | e2b241319037f2b651695f12e9c64f0e84ae5838463f81650ade82ffd774a70a |
| `service.py` | db4396a41915b2549cd354325147bae1c24cb6dec77c31616e68f4333b5ff0f0 |
| `test_experiment.py` | 3650ef19bf5019bd5db81cade33671c811eaeb6a1246d4f15300cc337f150cc4 |
| `README.md` | a4ac899b292a55af732376e986f73b18c6a6256d16544c0a6bb1dd615953745c |
| `test_output.txt` | e8950a5dd05cade63eedc5ccda903c54f97cbbd14e9f035b492c5d77c0b305c0 |

**GitHub disposition:** this AAR is the sole committed research artifact. Executable source and tests are in the conversation ZIP, not integrated into Foromni source or CI.

## Scientific and security limitations

- The authority signing key and provider private key were minted and controlled by the same root operator. Unix DAC + peer credentials restrict tested unprivileged callers, not root or stolen service UIDs.
- One-use read grants improve replay handling but may reject harmless retries after a response was lost; a durable already-read receipt retrieval protocol would require its own idempotency design.
- Per-read tokens are ephemeral fixture grants, not actual independently administered legal owner approval. No key rotation, revocation, task registry, budget controls, tenant data/privacy rules, network confinement, remote audit or realistic external API.
- **Not a full EXP-40 rerun:** witness, anchor and observer are not included in this 22-test provider-focused fixture. No claim of globally reconciled audit truth or independent completeness.
- Single-process service request loop: no concurrent stress or controlled revocation race from earlier experiments.
- Developer also designed all tests: no independent source-bound security QA. Provider validates JSON/scopes in a toy contract, not actual MCP/OAuth semantics.

## Next experiment

**EXP-42:** integrate this exact receipt-access control with separate observer/witness/anchor service identities, split the provider signing authority, and test replay/response-loss idempotency of read grants, inaccessible historical records across tenants, and fail-closed missing evidence. Add an independently authored attack/evaluation corpus; only after external review consider a client-facing security readiness assessment.

**Verdict:** `EXP41_SPLIT_UID_SCOPED_READ_22_OF_22_LOCAL_PASS`, `EXP41_PROVIDER_ENUMERATION_DENIED`, `EXP41_ROOT_KEY_AND_AUTHORITY_TRUST_UNPROVEN`, `FOR007_UNCHANGED`.
