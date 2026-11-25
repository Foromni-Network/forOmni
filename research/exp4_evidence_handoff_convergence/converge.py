"""EXPERIMENT 4: research-only integration; suggestion never creates runtime authority."""
from dataclasses import dataclass
from provenance import Receipt, verified_counts
from gate import ProposalGrant,eligible
from selection import select

@dataclass(frozen=True)
class Request:
    project_id:str
    task_id:str
    capability:str
    source_sha:str
    suite_id:str
    epoch:int

def propose(request:Request, historical_receipts:tuple[Receipt,...], grants:tuple[ProposalGrant,...], evaluator_keys:dict[str,bytes])->dict:
    counts,rejects,costs=verified_counts(historical_receipts,evaluator_keys,project_id=request.project_id,source_sha=request.source_sha,suite_id=request.suite_id)
    elig={g.agent_id for g in grants if eligible(g,project_id=request.project_id,task_id=request.task_id,capability=request.capability,current_epoch=request.epoch)}
    winner=select(counts,elig)
    return {'suggested_agent':winner,'eligible_agents':sorted(elig),
            'verified_counts':counts,'rejected_receipts':rejects,'verified_cost_cents':costs,
            'authority':'NONE','effective_grant':None,'execution':'NOT_RUN'}
