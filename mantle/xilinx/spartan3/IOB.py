from magma import *

IOBUF = DeclareCircuit("IOBUF", "input T", Bit,
                                "input I", Bit,
                                "inout IO", Bit,
                                "output O", Bit)

def IOB(**params):
    iob = IOBUF(**params)
    args = ["input T", iob.T, "input I", iob.I, "inout IO", iob.IO, "output O", iob.O]
    return AnonymousCircuit(args)





