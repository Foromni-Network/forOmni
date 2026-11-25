"""EXP-3 convergence: A evidence + B policy + C ranking -> one proposal.

No secrets, network, deployment, commits, credential issuance or effective grants.
"""
from dataclasses import dataclass
from slices.evidence import Receipt, accepted_receipts
from slices.policy import AgentGrant, eligible
from slices.ranking import choose

@dataclass(frozen=True)
class TaskRequest:
    id: str
    project_id: str
    capability: str
    source_sha: str
    suite_id: str
    epoch: int


def propose(task: TaskRequest, receipts: tuple[Receipt, ...],
            grants: tuple[AgentGrant, ...], evaluated: dict[str, int]) -> dict:
    accepted = accepted_receipts(receipts, source_sha=task.source_sha, suite_id=task.suite_id)
    matched: dict[str, tuple[int, int]] = {}
    for grant in grants:
        if not eligible(grant, project_id=task.project_id, task_id=task.id,
                        capability=task.capability, action='draft_isolated', epoch=task.epoch):
            continue
        a = accepted.get(grant.agent_id, 0)
        n = evaluated.get(grant.agent_id, 0)
        if a > n:  # no inconsistent source accounting
            continue
        matched[grant.agent_id] = (a,n)
    selection = choose(matched)
    return {'task_id': task.id, 'suggested_agent': selection,
            'eligible_agents': sorted(matched), 'authority': 'NONE',
            'integration_status': 'RESEARCH_ONLY'}
