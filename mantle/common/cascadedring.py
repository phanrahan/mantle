from magma import *
from mantle import And
from .ring import Ring

__all__ = ['CascadedRing']

def CascadedRing(nlist, has_ce=False, **kwargs):
    """
    n cascaded shift registers in a ring
    """

    if has_ce:
        ce = In(Bit)()
        args = ['CE', ce]
    else:
        ce = 1
        args = []

    for i in range(len(nlist)):
        n = nlist[i] - 1
        assert(n < 32)
        ring = Ring(n, has_ce=True)
        ring(CE=ce)
        and2 = And(2)
        and2(ce, ring.O[n-1])
        ce = and2.O

    args += ["O", ce]
    return AnonymousCircuit(args)

