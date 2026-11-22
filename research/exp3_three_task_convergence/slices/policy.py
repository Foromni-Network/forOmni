"""EXP-3 Task B: synthetic project/action gate, not an effective credential service."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AgentGrant:
    agent_id: str
    project_id: str
    task_id: str
    capability: str
    action: str
    epoch: int
    revoked: bool = False
    suspended: bool = False


def eligible(grant: AgentGrant, *, project_id: str, task_id: str,
             capability: str, action: str, epoch: int) -> bool:
    return (not grant.revoked and not grant.suspended and
            grant.agent_id != '' and grant.project_id == project_id and
            grant.task_id == task_id and grant.capability == capability and
            grant.action == action and grant.epoch == epoch and
            action == 'draft_isolated')
