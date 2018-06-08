from magma import *

IOBUF = DeclareCircuit("IOBUF", "T", In(Bit),
                                "I", In(Bit),
                                "IO", InOut(Bit),
                                "O", Out(Bit))

def IOB(**params):
    iob = IOBUF(**params)
    args = ["T", iob.T, "I", iob.I, "IO", iob.IO, "O", iob.O]
    return AnonymousCircuit(args)





