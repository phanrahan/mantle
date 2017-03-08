from magma import *
from .FF import FFs
from .register import _RegisterName
from .logic import Not, And2
from .shift import SISO

__all__  = ['DefineRing', 'Ring']
__all__ += ['DefineJohnson', 'Johnson']
__all__ += ['CascadedRing']

def DefineRing(n, init=1, ce=False, r=False, s=False):
    """
    Generate a n-bit ring counter.

    None -> O[n]
    """
    class Ring(Circuit):
        name = _RegisterName('Ring', n, init, ce, r, s)
        IO = ['O', Out(Array(n,Bit))] + ClockInterface(ce,r,s)
        @classmethod
        def definition(ring):
            ffs = FFs(n, init=init, ce=ce, r=r, s=s)
            reg = braid(ffs, scanargs={"I":"O"})
            reg(reg.O[n-1])
            wire(reg.O, ring.O)
            wireclock(ring, reg)
    return Ring

def Ring(n, init=1, ce=False, r=False, s=False, **kwargs):
    return DefineRing(n, init, ce, r, s)(**kwargs)


def DefineJohnson(n, ce=False, r=False, s=False):
    """
    Generate a n-bit johnson counter.

    Walking ring counter / Moebios counter

    None -> O[n]
    """
    class Johnson(Circuit):
        name = _RegisterName('Johnson', n, 0, ce, r, s)
        IO = ['O', Out(Array(n,Bit))] + ClockInterface(ce,r,s)
        @classmethod
        def definition(johnson):
            ffs = FFs(n, ce=ce, r=r, s=s)
            reg = braid(ffs, scanargs={"I":"O"})
            johnson.O(reg(Not()(reg.O[n-1])))
            wireclock(johnson, reg)
    return Johnson

def Johnson(n, ce=False, r=False, s=False, **kwargs):
    return DefineJohnson(n, ce, r, s)(**kwargs)


def CascadedRing(nlist, ce=False, **kwargs):
    """
    n cascaded shift registers in a ring
    """

    if ce:
        ce = In(Bit)()
        args = ['CE', ce]
    else:
        ce = 1
        args = []

    for i in range(len(nlist)):
        n = nlist[i] - 1
        assert(n < 32)
        ring = Ring(n, ce=True)
        ring(CE=ce)
        and2 = And2()
        and2(ce, ring.O[n-1])
        ce = and2.O

    args += ["O", ce]
    return AnonymousCircuit(args)

