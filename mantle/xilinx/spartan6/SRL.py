from magma import *
from magma.bitutils import int2seq, lutinit
from magma.compatibility import IntegerTypes

__all__  = ['SRL16E', 'SRLC16E', 'SRL32E']
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

SRL32E = DeclareCircuit('SRLC32E',
            "A", In(Bits[ 5 ]),
            "D", In(Bit),
            "Q", Out(Bit),
            "Q31", Out(Bit),
            "CE", In(Enable),
            "CLK", In(Clock) )


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

    srl32 = SRL32E(INIT=lutinit(init,64))

    args = ["A",   srl32.A,
            "O",  srl32.Q,
            "I",   srl32.D]
    if has_ce:
        args += ["CE", srl32.CE]
    else:
        wire(1,srl32.CE)

    if has_shiftout:
        args += ["SHIFTOUT", srl32.Q31]

    args += ["CLK", srl32.CLK]

    return AnonymousCircuit(args)

