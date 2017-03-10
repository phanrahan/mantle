from magma import *
from ..spartan import SRL32
from ..port import FFs, And2, Not
from .register import _RegisterName

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

def Ring(n, init=1, ce=False, r=False, s=False):
    return DefineRing(n, init, ce, r, s)()


def DefineJohnson(n, ce=False, r=False, s=False):
    """
    Generate a n-bit johnson counter.

    Walking ring counter / Moebios counter

    None -> O[n]
    """
    class Johnson(Circuit):
        name = _RegisterName('Johnson',n, 0, ce, r, s)
        IO = ['O', Out(Array(n,Bit))] + ClockInterface(ce,r,s)
        @classmethod
        def definition(johnson):
            ffs = FFs(n, ce=ce, r=r, s=s)
            reg = braid(ffs, scanargs={"I":"O"})
            johnson.O(reg(Not()(reg.O[n-1])))
            wireclock(johnson, reg)
    return Johnson

def Johnson(n, ce=False, r=False, s=False):
    return DefineJohnson(n, ce, r, s)()


def CascadedRing(nlist, ce=False):
    """
    n cascaded shift registers in a ring
    """

    if ce:
        ce = Bit()
        args = ['input CE', ce]
    else:
        ce = 1
        args = []

    for i in range(len(nlist)):
        n = nlist[i] - 1
        assert(n < 32)
        sh = SRL32(1,ce=True)

        A = int2seq(n, 5)
        sh(array(*A), sh, CE=ce)
        and2 = And2()
        and2(ce, sh)
        ce = and2.O

    args += ["output O", ce]
    return AnonymousCircuit(args)

