from __future__ import division


from magma import *
import magma as m
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
        return DeclareCircuit("coreir_mux{}".format(N),
            *["in0", In(Bit), "in1", In(Bit), "sel", In(Bit),
             "out", Out(Bit)],
            verilog_name="coreir_bitmux",
            coreir_name="mux",
            coreir_lib="corebit",
            simulate=simulate
        )
    else:
        return DeclareCircuit("coreir_mux{}".format(N),
            *["in0", In(Bits(N)), "in1", In(Bits(N)), "sel", In(Bit),
             "out", Out(Bits(N))],
            verilog_name="coreir_mux",
            coreir_name="mux",
            coreir_lib="coreir",
            simulate=simulate,
            coreir_genargs={"width": N}
        )


is_power_of_two = lambda num: num != 0 and ((num & (num - 1)) == 0)


def _declare_muxn(height, width):
    def simulate(self, value_store, state_store):
        sel = BitVector(value_store.get_value(getattr(self, "in").sel))
        out = BitVector(value_store.get_value(getattr(self, "in").data[sel.as_int]))
        value_store.set_value(self.out, out)
    return DeclareCircuit(f"coreir_commonlib_mux{height}x{width}",
        *["in", In(Tuple(data=Array(height, Bits(width)),
                         sel=Bits(m.bitutils.clog2(height)))),
          "out", Out(Bits(width))],
        coreir_name="muxn",
        coreir_lib="commonlib",
        simulate=simulate,
        coreir_genargs={"width": width, "N": height}
    )


@cache_definition
def DefineMux(height=2, width=None):
    if width is None:
        T = Bit
    else:
        T = Bits(width)

    io = []
    for i in range(height):
        io += ["I{}".format(i), In(T)]
    if height == 2:
        select_type = Bit
    else:
        select_type = Bits(m.bitutils.clog2(height))
    io += ['S', In(select_type)]
    io += ['O', Out(T)]

    class _Mux(Circuit):
        name = "Mux{}x{}".format(height, width)
        IO = io
        @classmethod
        def definition(interface):
            if width is None:
                mux = _declare_muxn(height, 1)()
            else:
                mux = _declare_muxn(height, width)()
            for i in range(height):
                if width is None:
                    m.wire(getattr(interface, f"I{i}"), getattr(mux, "in").data[i][0])
                else:
                    m.wire(getattr(interface, f"I{i}"), getattr(mux, "in").data[i])
            if height == 2:
                m.wire(interface.S, getattr(mux, "in").sel[0])
            else:
                m.wire(interface.S, getattr(mux, "in").sel)
            if width is None:
                wire(mux.out[0], interface.O)
            else:
                wire(mux.out, interface.O)
    return _Mux


def Mux(height=2, width=None, **kwargs):
    return DefineMux(height, width)(**kwargs)

Mux2 = DefineMux(2)
Mux4 = DefineMux(4)
Mux8 = DefineMux(8)
Mux16 = DefineMux(16)

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
                                             name, ["mantle", "coreir", "global"],
                                             {"N": N, "width": width})

def CommonlibMuxN(cirb: CoreIRBackend, N: int, width: int):
    return DefineCommonlibMuxN(cirb, N, width)()
