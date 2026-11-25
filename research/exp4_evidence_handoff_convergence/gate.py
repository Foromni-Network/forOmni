"""EXPERIMENT 4 / task B: synthetic invitation, consent and action-time gate."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ProposalGrant:
    agent_id: str
    project_id: str
    task_id: str
    capability: str
    action: str
    epoch: int
    valid_until_epoch: int
    owner_consented: bool
    revoked: bool = False
    suspended: bool = False


def eligible(grant:ProposalGrant, *, project_id:str,task_id:str,
             capability:str,current_epoch:int, action:str='draft_isolated') -> bool:
    return (grant.owner_consented and not grant.revoked and not grant.suspended and
            grant.agent_id != '' and grant.project_id == project_id and grant.task_id == task_id and
            grant.capability == capability and grant.action == action == 'draft_isolated' and
            grant.epoch == current_epoch and current_epoch <= grant.valid_until_epoch)
