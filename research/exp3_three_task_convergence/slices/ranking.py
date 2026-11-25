"""EXP-3 Task C: conservative ranking of eligible, evidence-bearing candidates."""
from math import sqrt


def wilson_lower(accepted: int, evaluated: int) -> float:
    if evaluated <= 0 or accepted < 0 or accepted > evaluated:
        return 0.0
    z = 1.96
    p = accepted / evaluated
    z2 = z*z
    return (p + z2/(2*evaluated) - z*sqrt((p*(1-p)+z2/(4*evaluated))/evaluated))/(1+z2/evaluated)


def choose(candidates: dict[str, tuple[int, int]]) -> str | None:
    """Select only from trusted eligible candidates; never issue a grant."""
    usable = {agent: (a,n) for agent,(a,n) in candidates.items() if 0 <= a <= n and n > 0}
    if not usable:
        return None
    return sorted(usable, key=lambda agent:(-wilson_lower(*usable[agent]), -usable[agent][1], agent))[0]
