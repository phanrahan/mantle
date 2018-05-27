from magma import *
from magma.compatibility import IntegerTypes
from magma.bitutils import int2seq
from ..spartan3.CLB import *
from .LUT import *

__all__   = ['DFF', 'RSFF', 'SRFF', 'JKFF', 'TFF']
__all__  += ['FF', 'FFs']

def DFF(init=0, has_ce=False, has_r=False, has_s=False):
 
    ff = FDRSE(INIT=lutinit(init,1))

    args = ['I', ff.D]
    if not has_r:
        wire(0, ff.R)
    else:
        args += ['RESET', ff.R]
    if not has_s:
        wire(0, ff.S)
    else:
        args += ['SET', ff.S]
    if not has_ce:
        wire(1, ff.CE)
    else:
        args += ['CE', ff.CE]
    args += ['CLK', ff.C]

    args += ['O', ff.Q]

    return AnonymousCircuit(args)



def SRFF( init=0, has_ce=False):

    """A S-R flip-flop."""

    dff = FF( init=init, has_ce=ce, has_s=True, has_r=True)
    dff(dff)

    args = []
    if ce:
        args += ['CE', dff.CE]
    args += ["S", dff.SET, "R", dff.RESET, 'CLK', dff.CLK, "O", dff.O]

    return AnonymousCircuit(args)


def RSFF( init=0, has_ce=False):

    """A R-S flip-flop."""

    dff = FF( init=init, has_ce=has_ce, has_s=True, has_r=True)
    dff(dff)

    args = []
    if ce:
        args += ['CE', dff.CE]
    args += ["S", dff.SET, "R", dff.RESET, 'CLK', dff.CLK, "O", dff.O]

    return AnonymousCircuit(args)


def JKFF( init=0, has_ce=False, has_s=False, has_r=False):

    """A J-K flip-flop."""

    dff = FF( init=init, has_ce=has_ce, has_s=has_s, has_r=has_r)
    lut = LUT3( (~I0&I1)|(I0&~I2) )
    dff(lut)

    wire(dff.O, lut.I0)

    return AnonymousCircuit("J", lut.I1, "K", lut.I2, "O", dff.O)


def TFF( init=0, has_ce=False, has_s=False, has_r=False):

    """A T flip-flop."""

    tff = FF( init=init, has_ce=has_ce, has_s=has_s, has_r=has_r)
    lut = LUT2( I0^I1 )
    tff(lut)

    wire(tff.O, lut.I0)

    return AnonymousCircuit("I", lut.I1, "O", tff.O)

#
# Create a column of n FFs initialized to init
#
# Each FF may have a ce, r, and s signal.
#   
def FFs(n, init=0, has_ce=False, has_r=False, has_s=False):
    if isinstance(init, IntegerTypes):
        init = int2seq(init, n)
              
    def f(y):
        return FF(init[y], has_ce=has_ce, has_r=has_r, has_s=has_s)
    
    return col(f, n)

FF = DFF
