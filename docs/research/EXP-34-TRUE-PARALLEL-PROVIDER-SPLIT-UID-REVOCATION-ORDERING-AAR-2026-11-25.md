# EXP-34 — True Parallel Execution and Revocation Ordering

Executed 2026-11-25 on a disposable Linux fixture: 17/17 local tests passed in one run (25.877s, warnings-as-errors). Two authorized worker UIDs accessed threaded Unix socket broker/provider services running under separate UIDs. Six provider handlers overlapped; 16 simultaneous same-effect requests resulted in one committed SQLite mock effect and 15 duplicates. A controlled revocation-before-commit schedule denied the queued effect; revocation after commit retained it.

**Limitations:** root coordinator controlled all keys; test-only diagnostic gate/stats APIs lacked authorization; broad socket modes; provider writes serialize under SQLite; synthetic—not external services or independent QA. No production, FOR-007 or Internet Embassy changes. Executable exact source/tests/log are in the EXP-34 evidence ZIP shared in conversation. SHA256 of archive: `e9b90260c3f254f587ad5c32eab459cf23b302416988de629d393995cfc34a0c`.

**Next:** EXP-35 restrict diagnostic routes; unify historical receipt read with concurrent provider and witness reconciliation. This research report is not a production source integration.