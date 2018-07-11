from __future__ import division


from magma import *
from magma.bit_vector import BitVector
from magma.backend.coreir_ import CoreIRBackend
from magma.frontend.coreir_ import DefineCircuitFromGeneratorWrapper

import math


@cache_definition
def DefineCoreirMux(width=None):
    N = width
    def simulate(self, value_store, state_store):
        in0 = BitVector(value_store.get_value(self.in0))
        in1 = BitVector(value_store.get_value(self.in1))
        sel = BitVector(value_store.get_value(self.sel))
        out = in1 if sel.as_int() else in0
        value_store.set_value(self.out, out)
    if width is None:
        return DeclareCircuit("coreir_mux".format(N),
            *["in0", In(Bit), "in1", In(Bit), "sel", In(Bit),
             "out", Out(Bit)],
            verilog_name="coreir_bitmux",
            coreir_name="mux",
            coreir_lib="corebit",
            simulate=simulate
        )
    else:
        return DeclareCircuit("coreir_mux".format(N),
            *["in0", In(Bits(N)), "in1", In(Bits(N)), "sel", In(Bit),
             "out", Out(Bits(N))],
            verilog_name="coreir_mux",
            coreir_name="mux",
            coreir_lib="coreir",
            simulate=simulate,
            coreir_genargs={"width": N}
        )


is_power_of_two = lambda num: num != 0 and ((num & (num - 1)) == 0)


@cache_definition
def _DefineMux(N):
    """Construct a Mux with N 1-bit inputs"""
    assert is_power_of_two(N)
    if N == 2:
        class _Mux(Circuit):
            name = "_Mux2"
            IO = ["I", In(Bits(2)), "S", In(Bit), "O", Out(Bit)]
            @classmethod
            def definition(mux):
                coreir_mux = DefineCoreirMux(None)()
                coreir_mux(mux.I[0], mux.I[1], mux.S)
                wire(coreir_mux.out, mux.O)
    else:
        class _Mux(Circuit):
            name = "_Mux{}".format(N)
            IO = ["I", In(Bits(N)), "S", In(Bits(int(math.log(N, 2)))), "O",
                    Out(Bit)]
            @classmethod
            def definition(interface):
                mux0, mux1 = DefineMux(N // 2)(), DefineMux(N // 2)()
                mux3 = DefineMux(2)()
                if math.log(N, 2) == 2:
                    assert isinstance(mux0.S, BitType)
                    select = interface.S[0]
                else:
                    select = interface.S[:-1]
                mux0(interface.I[:N//2], select)
                mux1(interface.I[N//2:], select)
                mux3(bits([mux0.O, mux1.O]), interface.S[-1])
                wire(mux3.O, interface.O)
    return _Mux


@cache_definition
def DefineMux(height=2, width=None):
    if width is None:
       return _DefineMux(height)

    T = Bits(width)

    io = []
    for i in range(height):
        io += ["I{}".format(i), In(T)]
    if not is_power_of_two(height):
        raise ValueError("DefineMux only supports heights that are powers of "
                "two")
    if height == 2:
        select_type = Bit
    else:
        select_type = Bits(int(math.log(height, 2)))
    io += ['S', In(select_type)]
    io += ['O', Out(T)]

    class _Mux(Circuit):
        name = "Mux{}x{}".format(height, width)
        IO = io
        @classmethod
        def definition(interface):
            mux = braid([curry(_DefineMux(height)()) for _ in range(width)],
                    forkargs=['S'])
            args = [getattr(interface, "I{}".format(i)) for i in range(height)]
            args += [interface.S]
            mux(*args)
            wire(mux.O, interface.O)
    return _Mux


def Mux(height=2, width=None, **kwargs):
    return DefineMux(height, width)(**kwargs)

Mux2 = Mux(2)
Mux4 = Mux(4)
Mux8 = Mux(8)
Mux16 = Mux(16)

def DefineCommonlibMuxN(cirb: CoreIRBackend, N: int, width: int):
    """
    Get a Mux that handles any number of inputs

    :param N: The number of inputs to select between
    :param width: The number of bits per input
    :return: A circuit with the following ports:
    I : {
        data: In(Array(N, Array(width, Bit)))
        sel: In(Array(getRAMAddrWidth(N), Bit))
    }
    out : Out(Array(width, Bit))
    Note: even though this isn't a RAM, the AddrWidth computation is the same.
    """
    name = "CommonlibMuxN_n{}_w{}".format(str(N), str(width))
    return DefineCircuitFromGeneratorWrapper(cirb, "commonlib", "muxn",
                                             ["mantle", "coreir", "global"], name,
                                             {"N": N, "width": width})

def CommonlibMuxN(cirb: CoreIRBackend, N: int, width: int):
    return DefineCommonlibMuxN(cirb, N, width)()