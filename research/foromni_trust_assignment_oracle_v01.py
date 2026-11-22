"""Foromni research-only trust-aware assignment oracle.

PROPOSAL, NOT A SECURITY BOUNDARY. Uses synthetic records only.
No network, filesystem writes, secrets, production integration, or auto-approval.
Do not use to issue credentials, leases, promotions, or protected access.
Research branch only; no tests were executed when authored.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from math import sqrt
from typing import Literal

Decision = Literal["suggest", "explore_only", "ineligible", "abstain"]
Risk = Literal["low", "medium", "high", "protected"]


@dataclass(frozen=True)
class Task:
    id: str
    project_id: str
    capability: str
    risk: Risk
    requires_private_data: bool = False
    owner_has_authorized_assignment: bool = False


@dataclass(frozen=True)
class Agent:
    id: str
    operator_id: str
    project_memberships: frozenset[str]
    verified_capabilities: frozenset[str]
    accepted: int
    evaluated: int
    difficulty_evidence: frozenset[str] = field(default_factory=frozenset)
    active_security_suspension: bool = False
    consented_to_trial: bool = False
    grant_present: bool = False
    full_cost_usd: float | None = None
    cost_receipts_complete: bool = False


@dataclass(frozen=True)
class Recommendation:
    agent_id: str
    decision: Decision
    reason: str
    verified_rate: float | None
    wilson_lower_95: float | None
    cost_status: Literal["verified", "unknown"]
    grants_issued: int = 0  # Must always remain zero.


def wilson_lower_95(accepted: int, evaluated: int) -> float | None:
    """Lower 95% Wilson score interval, a *heuristic*, not calibration."""
    if evaluated <= 0:
        return None
    if not 0 <= accepted <= evaluated:
        raise ValueError("Accepted outcomes must be within evaluated attempts")
    z = 1.96
    p = accepted / evaluated
    z2 = z * z
    denominator = 1 + z2 / evaluated
    numerator = p + z2 / (2 * evaluated) - z * sqrt(
        (p * (1 - p) + z2 / (4 * evaluated)) / evaluated
    )
    return numerator / denominator


def recommend(task: Task, agent: Agent) -> Recommendation:
    """Return a NON-AUTHORITATIVE explanation, never a grant."""
    if agent.evaluated < 0 or agent.accepted < 0 or agent.accepted > agent.evaluated:
        raise ValueError("Invalid verified evidence counts")
    if agent.full_cost_usd is not None and agent.full_cost_usd < 0:
        raise ValueError("Negative cost claim")
    rate = (agent.accepted / agent.evaluated) if agent.evaluated else None
    lower = wilson_lower_95(agent.accepted, agent.evaluated)
    cost_status = (
        "verified" if agent.cost_receipts_complete and agent.full_cost_usd is not None
        else "unknown"
    )

    def result(decision: Decision, reason: str) -> Recommendation:
        return Recommendation(agent.id, decision, reason, rate, lower, cost_status)

    if agent.active_security_suspension:
        return result("ineligible", "current_security_suspension")
    if task.risk == "protected":
        return result("ineligible", "protected_action_requires_separate_integrator")
    if task.project_id not in agent.project_memberships:
        return result("ineligible", "no_project_membership")
    if not task.owner_has_authorized_assignment:
        return result("abstain", "owner_assignment_consent_absent")
    if task.requires_private_data and not agent.grant_present:
        return result("ineligible", "private_data_grant_absent")
    if task.capability not in agent.verified_capabilities:
        if task.risk == "low" and not task.requires_private_data and agent.consented_to_trial:
            return result("explore_only", "controlled_public_or_synthetic_trial_only")
        return result("ineligible", "capability_unverified")
    if task.risk == "high" and (
        agent.evaluated < 10 or "high" not in agent.difficulty_evidence
    ):
        return result("abstain", "high_risk_evidence_insufficient")
    if agent.evaluated == 0:
        return result("abstain", "missing_independent_evaluation")
    return result("suggest", "requires_current_task_specific_policy_and_lease")


def ranked_suggestions(task: Task, agents: list[Agent]) -> list[Recommendation]:
    """Conservative ranking for suggestions only; abstentions remain visible."""
    decisions = [recommend(task, a) for a in agents]
    # Preserve unknown/abstain decisions after suggested candidates; lower bound
    # ranks eligible candidates, and sample size is a deterministic tiebreaker.
    by_id = {a.id: a for a in agents}
    order = {"suggest": 0, "explore_only": 1, "abstain": 2, "ineligible": 3}
    return sorted(
        decisions,
        key=lambda r: (
            order[r.decision],
            -(r.wilson_lower_95 if r.wilson_lower_95 is not None else -1.0),
            -by_id[r.agent_id].evaluated,
            r.agent_id,
        ),
    )


# NOTE: This prototype intentionally does not issue leases or grant protected
# access. Independent, action-time policy checks are mandatory in any future
# production implementation. Difficulty and cost are displayed, not used for
# mathematically uncalibrated optimization. No runnable test claim is made.
