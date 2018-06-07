from magma import *
from magma.bitutils import int2seq, lutinit
from magma.compatibility import IntegerTypes
from .CLB import MUXF5
            
__all__   = ['SRL16E', 'SRLC16E']
__all__  += ['SRL16', 'SRL32']

SRL16E = DeclareCircuit('SRL16E',
            "A0", In(Bit),
            "A1", In(Bit),
            "A2", In(Bit),
            "A3", In(Bit),
            "D",  In(Bit),
            "Q",  Out(Bit),
            "CE", In(Enable),
            "CLK", In(Clock) )

SRLC16E = DeclareCircuit('SRLC16E',
            "A0", In(Bit),
            "A1", In(Bit),
            "A2", In(Bit),
            "A3", In(Bit),
            "D",  In(Bit),
            "Q",  Out(Bit),
            "Q15", Out(Bit),
            "CE", In(Enable),
            "CLK", In(Clock))

def SRL16(init=0, has_shiftout=False, has_ce=False):

    """
    Create a 16-bit shift register using a LUT

    [I, A[4]] -> O
    """

    if isinstance(init, IntegerTypes):
        init = int2seq(init, 16)

    if has_shiftout:
        srl16 = SRLC16E(INIT=lutinit(init,16))
    else:
        srl16 = SRL16E(INIT=lutinit(init,16))

    args = ["A",   bits([srl16.A0, srl16.A1, srl16.A2, srl16.A3]),
            "I",   srl16.D,
            "O",   srl16.Q]
    if has_ce:
        args += ["CE", srl16.CE]
    else:
        wire(1,srl16.CE)

    if has_shiftout:
        args += ["SHIFTOUT", srl16.Q15]

    args += ["CLK", srl16.CLK]

    return AnonymousCircuit(args)


def SRL32(init=0, has_shiftout=False, has_ce=False):
    """
    Configure a Slice as a 32-bit shift register

    [I, A[5]] -> O

    @note: SRL32's can be chained together using SHIFTOUT and SHIFTIN.
        In that case, an SRL32 does not generate any output.
    """

    if isinstance(init, IntegerTypes):
        init = int2seq(init, 32)

    A = In(Bits(5))()
    srl0 = SRL16(init[ 0:16], has_shiftout=True, has_ce=has_ce)
    srl1 = SRL16(init[16:32], has_shiftout=True, has_ce=has_ce)
    srls = [srl0, srl1]
    srl = braid( srls, forkargs=['A', 'CE', 'CLK'], foldargs={"I":"SHIFTOUT"} ) 
    wire( A[0:4], srl.A )
    mux = MUXF5()
    mux(srl.O[0], srl.O[1], A[4])
    args = ["A", A, "I", srl.I, "O", mux.O]
    if has_ce:
        args += ['CE', srl.CE]
    args += ['CLK', srl.CLK]

    return AnonymousCircuit(args)
