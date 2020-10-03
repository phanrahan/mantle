from magma import *
from magma.compatibility import IntegerTypes
from magma.bitutils import int2seq, lutinit
from ..spartan6.CLB import *
from .LUT import *

__all__   = ['DFF', 'RSFF', 'SRFF', 'JKFF', 'TFF']
__all__  += ['FF', 'FFs']

def DFF(init=0, has_ce=False, has_reset=False, has_set=False):
 
    ff = FDRSE(INIT=lutinit(init,1))

    args = ['I', ff.D]
    if not has_reset:
        wire(reset(0), ff.R)
    else:
        args += ['RESET', ff.R]
    if not has_set:
        wire(reset(0), ff.S)
    else:
        args += ['SET', ff.S]
    if not has_ce:
        wire(enable(1), ff.CE)
    else:
        args += ['CE', ff.CE]
    args += ['CLK', ff.C]

    args += ['O', ff.Q]

    return AnonymousCircuit(args)



def SRFF( init=0, has_ce=False):

    """A S-R flip-flop."""

    dff = FF( init=init, has_ce=has_ce, has_set=True, has_reset=True)
    dff(dff)

    args = []
    if has_ce:
        args += ['CE', dff.CE]
    args += ["S", dff.SET, "R", dff.RESET, 'CLK', dff.CLK, "O", dff.O]

    return AnonymousCircuit(args)


def RSFF( init=0, has_ce=False):

    """A R-S flip-flop."""

    dff = FF( init=init, has_ce=has_ce, has_set=True, has_reset=True)
    dff(dff)

    args = []
    if has_ce:
        args += ['CE', dff.CE]
    args += ["S", dff.SET, "R", dff.RESET, 'CLK', dff.CLK, "O", dff.O]

    return AnonymousCircuit(args)


def JKFF( init=0, has_ce=False, has_set=False, has_reset=False):

    """A J-K flip-flop."""

    dff = FF( init=init, has_ce=has_ce, has_set=has_set, has_reset=has_reset)
    lut = LUT3( (~I0&I1)|(I0&~I2) )
    dff(lut)

    wire(dff.O, lut.I0)

    return AnonymousCircuit("J", lut.I1, "K", lut.I2, "O", dff.O)


def TFF( init=0, has_ce=False, has_set=False, has_reset=False):

    """A T flip-flop."""

    tff = FF( init=init, has_ce=has_ce, has_set=has_set, has_reset=has_reset)
    lut = LUT2( I0^I1 )
    tff(lut)

    wire(tff.O, lut.I0)

    return AnonymousCircuit("I", lut.I1, "O", tff.O)

#
# Create a column of n FFs initialized to init
#
# Each FF may have a ce, r, and s signal.
#   
def FFs(n, init=0, has_ce=False, has_reset=False, has_set=False):
    if isinstance(init, IntegerTypes):
        init = int2seq(init, n)
              
    def f(y):
        return FF(init[y], has_ce=has_ce, has_reset=has_reset, has_set=has_set)
    
    return col(f, n)

FF = DFF
