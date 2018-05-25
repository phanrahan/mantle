from magma import *
from magma.compatibility import IntegerTypes
            
__all__  = ['SRL16E', 'SRLC16E', 'SRL32E']
__all__  += ['SRL16', 'SRL32']

SRL16E = DeclareCircuit('SRL16E',
            "input A0", Bit,
            "input A1", Bit,
            "input A2", Bit,
            "input A3", Bit,
            "input D", Bit,
            "output Q", Bit,
            "input CE", Bit,
            "input CLK", Bit )

SRLC16E = DeclareCircuit('SRLC16E',
            "input A0", Bit,
            "input A1", Bit,
            "input A2", Bit,
            "input A3", Bit,
            "input D", Bit,
            "output Q", Bit,
            "output Q15", Bit,
            "input CE", Bit,
            "input CLK", Bit )

SRL32E = DeclareCircuit('SRLC32E',
            "input A", Array5,
            "input D", Bit,
            "output Q", Bit,
            "output Q31", Bit,
            "input CE", Bit,
            "input CLK", Bit )

def SRL16(init=0, shiftout=False, ce=False):

    """
    Create a 16-bit shift register using a LUT

    [I, A[4]] -> O
    """

    if isinstance(init, IntegerTypes):
        init = int2seq(init, 16)

    if shiftout:
        srl16 = SRLC16E(INIT=lutinit(init,16))
    else:
        srl16 = SRL16E(INIT=lutinit(init,16))

    args = ["input A",   array(srl16.A0, srl16.A1, srl16.A2, srl16.A3),
            "output O",  srl16.Q,
            "input I",   srl16.D]
    if ce:
        args += ["input CE", srl16.CE]
    else:
        wire(1,srl16.CE)

    if shiftout:
        args += ["output SHIFTOUT", srl16.Q15]

    args += ["input CLK", srl16.CLK]

    return AnonymousCircuit(args)


def SRL32(init=0, shiftout=False, ce=False):
    """
    Configure a Slice as a 32-bit shift register

    [I, A[5]] -> O

    @note: SRL32's can be chained together using SHIFTOUT and SHIFTIN.
        In that case, an SRL32 does not generate any output.
    """

    if isinstance(init, IntegerTypes):
        init = int2seq(init, 32)

    srl32 = SRL32E(INIT=lutinit(init,64))

    args = ["input A",   srl32.A,
            "output O",  srl32.Q,
            "input I",   srl32.D]
    if ce:
        args += ["input CE", srl32.CE]
    else:
        wire(1,srl32.CE)

    if shiftout:
        args += ["output SHIFTOUT", srl32.Q31]

    args += ["input CLK", srl32.CLK]

    return AnonymousCircuit(args)

