"""EXP-3 Task A: verify immutable synthetic acceptance receipts (no cryptographic claims)."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Receipt:
    receipt_id: str
    agent_id: str
    task_id: str
    source_sha: str
    evaluator_id: str
    worker_id: str
    verdict: str
    suite_id: str


def accepted_receipts(receipts: tuple[Receipt, ...], *, source_sha: str, suite_id: str) -> dict[str, int]:
    """Fail closed on duplicate receipt IDs or forged/self-graded synthetic receipts."""
    seen: set[str] = set()
    counts: dict[str, int] = {}
    for r in receipts:
        if not r.receipt_id or r.receipt_id in seen:
            raise ValueError('duplicate_or_empty_receipt_id')
        seen.add(r.receipt_id)
        if not all((r.agent_id, r.task_id, r.evaluator_id, r.worker_id)):
            continue
        if (r.source_sha != source_sha or r.suite_id != suite_id or
            r.evaluator_id == r.worker_id or r.verdict != 'ACCEPT'):
            continue
        counts[r.agent_id] = counts.get(r.agent_id, 0) + 1
    return counts
