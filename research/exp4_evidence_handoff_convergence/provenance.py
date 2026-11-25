"""EXPERIMENT 4 / task A: synthetic evaluator-issued authenticated receipts.

HMAC is valid only while the verification key remains private to a trusted service.
In this experiment the same Python process owns the issuer and verifier, so this
is a tamper-detection prototype, not deployed independent evaluator custody.
"""
from dataclasses import dataclass
import hashlib
import hmac
import json

@dataclass(frozen=True)
class Receipt:
    project_id: str
    task_id: str
    attempt_id: str
    agent_id: str
    evaluator_id: str
    worker_id: str
    source_sha: str
    suite_id: str
    verdict: str
    complexity: str
    cost_cents: int
    signature: str = ''

    def payload(self) -> bytes:
        return json.dumps({k:v for k,v in vars(self).items() if k != 'signature'},
                          sort_keys=True, separators=(',',':')).encode()


def issue_receipt(receipt: Receipt, evaluator_key: bytes) -> Receipt:
    """Simulates a trusted evaluator issuing its own provenance envelope."""
    from dataclasses import replace
    return replace(receipt, signature=hmac.new(evaluator_key, receipt.payload(), hashlib.sha256).hexdigest())


def verify_receipt(receipt: Receipt, evaluator_keys: dict[str,bytes],
                   *, project_id: str, source_sha: str, suite_id: str) -> tuple[bool,str]:
    key = evaluator_keys.get(receipt.evaluator_id)
    if key is None: return False, 'unknown_evaluator'
    if receipt.evaluator_id == receipt.worker_id: return False, 'self_review'
    if receipt.project_id != project_id: return False, 'wrong_project'
    if receipt.source_sha != source_sha or receipt.suite_id != suite_id: return False, 'stale_source_or_suite'
    if not isinstance(receipt.cost_cents,int) or receipt.cost_cents < 0: return False, 'invalid_cost'
    if receipt.verdict not in ('ACCEPT','REJECT'): return False, 'unknown_verdict'
    expected = hmac.new(key,receipt.payload(),hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected,receipt.signature): return False, 'invalid_signature'
    return True,'valid'


def verified_counts(receipts: tuple[Receipt,...], evaluator_keys: dict[str,bytes],
                    *, project_id: str, source_sha: str, suite_id: str) -> tuple[dict[str,tuple[int,int]],dict[str,int],dict[str,int]]:
    """Verified historical opportunities, all verdicts counted; fail closed on duplicate attempts.

    Non-accepting/invalid receipts do not increase accepted counts. Unknown invalid
    receipts are surfaced separately; missing verified denominators cannot be
    inferred from arbitrary untrusted caller-provided totals.
    """
    seen=set(); counts={}; rejected={}; costs={}
    for receipt in receipts:
        valid,why=verify_receipt(receipt,evaluator_keys,project_id=project_id,source_sha=source_sha,suite_id=suite_id)
        if not valid:
            rejected[why]=rejected.get(why,0)+1
            continue
        attempt_key=(receipt.project_id,receipt.task_id,receipt.attempt_id)
        if attempt_key in seen: raise ValueError('duplicate_valid_attempt')
        seen.add(attempt_key)
        acc,total=counts.get(receipt.agent_id,(0,0))
        counts[receipt.agent_id]=(acc+(receipt.verdict=='ACCEPT'),total+1)
        costs[receipt.agent_id]=costs.get(receipt.agent_id,0)+receipt.cost_cents
    return counts,rejected,costs
