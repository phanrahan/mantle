from magma import *

__all__ = ["IOB", "ODDR2"]

_IOB = DeclareCircuit("IOBUF", 
                     "T", In(Bit),
                     "I", In(Bit),
                     "IO", InOut(Bit),
                     "O", Out(Bit))

_ODDR2 = DeclareCircuit("ODDR2", "S", In(Bit), 
                                 "R", In(Bit),
                                 "CE", In(Bit),
                                 "D0", In(Bit),
                                 "D1", In(Bit),
                                 "C0", In(Bit),
                                 "C1", In(Bit),
                                 "Q", Out(Bit))
def IOB(**params):
    iobuf = _IOBUF(**params)
    return AnonymousCircuit("T", iobuf.T, "I", iobuf.I, "IO", iobuf.IO, "O", iobuf.O)


def ODDR2(**params):
    oddr2 = _ODDR2(**params)
    return AnonymousCircuit("S", oddr2.S,
                            "R", oddr2.R,
                            "CE", oddr2.CE,
                            "D0", oddr2.D0,
                            "D1", oddr2.D1,
                            "C0", oddr2.C0,
                            "C1", oddr2.C1,
                            "Q", oddr2.Q)
