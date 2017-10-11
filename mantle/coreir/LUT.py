from magma import *
import coreir
from magma.bitutils import seq2int
from collections import Sequence


@circuit_generator
def DeclareCoreirLUT(N, init):
    return DeclareCircuit("coreir_lut{}".format(N),
            'in', In(Bits(N)), 'out', Out(Bit),
            coreir_name = "lutN",
            coreir_lib  = "commonlib",
            coreir_genargs = {"N": N},
            coreir_configargs = {"init": coreir.BitVector(1<<N, init)})


@circuit_generator
def LUT(init, N=None, **kwargs):
    """
    n-bit LUT

    I : In(Bits(n)), O : Out(Bit)
    """
    if isinstance(init, Sequence):
        if N is None:
            if 2 ** N < len(init):
                raise ValueError("init is too large for N={}".format(N))
        else:
            N = math.clog2(len(init))
        init = seq2int(init)
    else:
        if N is None:
            raise ValueError("N requires for not sequence init")

    io = []
    for i in range(N):
        io += ["I{}".format(i), In(Bit)]
    io += ["O", Out(Bit)]

    class LUT(Circuit):
        name = "LUT{}_{}".format(N, init)
        IO = io
        @classmethod
        def definition(cls):
            lutN = DeclareCoreirLUT(N, init)()
            for i in range(N):
                wire(getattr(lutN, "in")[i], getattr(cls, "I{}".format(i)))
                wire(lutN.out, cls.O)
    return LUT()
