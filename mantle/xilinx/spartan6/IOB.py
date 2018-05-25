from magma import *

__all__ = ["IOB", "ODDR2"]

_IOB = DeclareCircuit("IOBUF", 
                     "input T", Bit,
                     "input I", Bit,
                     "inout IO", Bit,
                     "output O", Bit)

_ODDR2 = DeclareCircuit("ODDR2", "input S", Bit, 
                                "input R", Bit,
                                "input CE", Bit,
                                "input D0", Bit,
                                "input D1", Bit,
                                "input C0", Bit,
                                "input C1", Bit,
                                "output Q", Bit)
def IOB(**params):
    iobuf = _IOBUF(**params)
    return AnonymousCircuit("input T", iobuf.T, "input I", iobuf.I, "inout IO", iobuf.IO, "output O", iobuf.O)


def ODDR2(**params):
    oddr2 = _ODDR2(**params)
    return AnonymousCircuit("input S", oddr2.S,
                   "input R", oddr2.R,
                   "input CE", oddr2.CE,
                   "input D0", oddr2.D0,
                   "input D1", oddr2.D1,
                   "input C0", oddr2.C0,
                   "input C1", oddr2.C1,
                   "output Q", oddr2.Q)
