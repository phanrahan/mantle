import math
from magma import *
import coreir
from magma.bitutils import clog2, seq2int, int2seq, fun2seq
from types import FunctionType
from collections.abc import Sequence
from hwtypes import BitVector


@cache_definition
def DeclareCoreirLUT(N, init):

    def _simulate(self, value_store, state_store):
        in_ = value_store.get_value(getattr(self, "in"))
        value_store.set_value(self.out, [bool(i) for i in int2seq(init, 2 ** N)][seq2int(in_)])

    args = {'in': In(Bits[N]), 'out': Out(Bit)}

    class _coreir_lut(Circuit):
        name = "coreir_lut{}".format(N)
        io = IO(**args)
        simulate = _simulate
        coreir_name = "lutN"
        coreir_lib  = "commonlib"
        coreir_genargs = {"N": N}
        coreir_configargs = {"init": BitVector[1 << N](init)}

    return _coreir_lut

def DefineLUT(init, N):
    ports = {f"I{i}": In(Bit) for i in range(N)}
    ports["O"] = Out(Bit)

    class LUT(Circuit):
        name = f"LUT{N}_{init}"
        io = IO(**ports)
        lutN = DeclareCoreirLUT(N, init)()
        for i in range(N):
            wire(getattr(lutN, "in")[i], getattr(io, "I{}".format(i)))
        wire(lutN.out, io.O)

    return LUT

def LUT(init, N=None, **kwargs):
    """
    n-bit LUT

    I0 : In(Bit), I1 : In(Bit), ..., In : In(Bit),  O : Out(Bit)
    """

    if isinstance(init, FunctionType):
        init = fun2seq(init, 1<<N)

    if isinstance(init, Sequence):
        if N is not None:
            if 2 ** N < len(init):
                raise ValueError("init is too large for N={}".format(N))
        else:
            N = clog2(len(init))
        init = seq2int(init)
    else:
        if N is None:
            raise ValueError("N requires for not sequence init")

    return DefineLUT(init, N)()
