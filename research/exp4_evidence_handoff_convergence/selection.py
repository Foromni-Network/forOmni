"""EXPERIMENT 4 / task C: evidence-filtered conservative selection."""
from math import sqrt

def lower_bound(accepted:int,total:int)->float:
    if total<=0 or not 0<=accepted<=total:return 0.0
    z=1.96;p=accepted/total;z2=z*z
    return (p+z2/(2*total)-z*sqrt((p*(1-p)+z2/(4*total))/total))/(1+z2/total)

def select(counts:dict[str,tuple[int,int]], eligible_ids:set[str])->str|None:
    available={k:v for k,v in counts.items() if k in eligible_ids and v[1]>0}
    if not available:return None
    return sorted(available,key=lambda k:(-lower_bound(*available[k]),-available[k][1],k))[0]
