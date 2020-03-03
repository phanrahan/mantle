from __future__ import division


from magma import *
import magma as m
from magma.backend.coreir_ import CoreIRBackend
from magma.frontend.coreir_ import DefineCircuitFromGeneratorWrapper, GetCoreIRBackend
from .util import DeclareCoreirCircuit
from hwtypes import BitVector

import math


def DefineCoreirMux(width=None):
    N = width
    def simulate(self, value_store, state_store):
        I0 = BitVector[N](value_store.get_value(self.I0))
        I1 = BitVector[N](value_store.get_value(self.I1))
        S = BitVector[N](value_store.get_value(self.S))
        O = I1 if S.as_int() else in0
        value_store.set_value(self.O, O)
    if width is None:
        return DeclareCoreirCircuit("coreir_mux{}".format(N),
            *["I0", In(Bit), "I1", In(Bit), "S", In(Bit),
             "O", Out(Bit)],
            verilog_name="coreir_bitmux",
            coreir_name="mux",
            coreir_lib="corebit",
            simulate=simulate
        )
    else:
        return DeclareCoreirCircuit("coreir_mux{}".format(N),
            *["I0", In(Bits[N]), "I1", In(Bits[N]), "S", In(Bit),
             "O", Out(Bits[N])],
            verilog_name="coreir_mux",
            coreir_name="mux",
            coreir_lib="coreir",
            simulate=simulate,
            coreir_genargs={"width": N}
        )


is_power_of_two = lambda num: num != 0 and ((num & (num - 1)) == 0)


@m.cache_definition
def _declare_muxn(height, width):
    def simulate(self, value_store, state_store):
        sel = BitVector[m.bitutils.clog2(height)](value_store.get_value(self.I.sel))
        out = BitVector[width](value_store.get_value(self.I.data[int(sel)]))
        value_store.set_value(self.O, out)
    return DeclareCoreirCircuit(f"coreir_commonlib_mux{height}x{width}",
        *["I", In(Product.from_fields("anon",
                                      dict(data=Array[height, Bits[width]],
                                           sel=Bits[m.bitutils.clog2(height)]))),
          "O", Out(Bits[width])],
        coreir_name="muxn",
        coreir_lib="commonlib",
        simulate=simulate,
        coreir_genargs={"width": width, "N": height}
    )


@m.cache_definition
def DefineMux(height=2, width=None, T=None):
    if T is not None:
        assert width is None, "Can only specify width **or** T"
        # Sanitize names for verilog by removing parens
        # TODO: Make this a reuseable feature
        suffix = str(T).replace("(", "").replace(")", "").replace(",", "_").replace("=", "_").replace("[", "").replace("]", "").replace(" ", "")
        T = T
    else:
        suffix = f"{width}"
        if width is None:
            T = Bit
        else:
            T = Bits[width]

    decl = []
    for i in range(height):
        decl += ["I{}".format(i), In(T)]
    if height == 2:
        select_type = Bit
    else:
        select_type = Bits[m.bitutils.clog2(height)]
    decl += ['S', In(select_type)]
    decl += ['O', Out(T)]

    class _Mux(Circuit):
        name = "Mux{}x{}".format(height, suffix)
        io = m.IO(**dict(zip(decl[::2], decl[1::2])))

        # NOTE(rsetaluri): Because of scoping rules in the class definition, we
        # can not use 'io' in list comprehensions. Therfore we use simple
        # iteration-based list construction.
        if T is not None and not (issubclass(T, m.Digital) or issubclass(T, m.Array) and issubclass(T.T, m.Bit)):
            if issubclass(T, m.Tuple):
                for i in range(len(T.keys())):
                    Is = []
                    for j in range(height):
                        Is.append(getattr(io, f"I{j}")[list(T.keys())[i]])
                    io.O[i] <= DefineMux(height, T=list(T.types())[i])()(*Is, io.S)
            else:
                assert issubclass(T, m.Array), f"Expected array or type type, got {T}, type is {type(T)}"
                for i in range(len(T)):
                    Is = []
                    for j in range(height):
                        Is.append(getattr(io, f"I{j}")[i])
                    io.O[i] <= DefineMux(height, T=type(Is[0]))()(*Is, io.S)
        else:
            if T is None and width is None or issubclass(T, m.Digital):
                mux = _declare_muxn(height, 1)()
            else:
                mux = _declare_muxn(height, width if T is None else len(T))()
            for i in range(height):
                if T is None and width is None or issubclass(T, m.Digital):
                    m.wire(getattr(io, f"I{i}"), mux.I.data[i][0])
                else:
                    m.wire(getattr(io, f"I{i}"), mux.I.data[i])
            if height == 2:
                m.wire(io.S, mux.I.sel[0])
            else:
                m.wire(io.S, mux.I.sel)
            if T is None and width is None or issubclass(T, m.Digital):
                wire(mux.O[0], io.O)
            else:
                wire(mux.O, io.O)
    return _Mux


def Mux(height=2, width=None, T=None, **kwargs):
    return DefineMux(height, width, T=T)(**kwargs)

Mux2 = DefineMux(2)
Mux4 = DefineMux(4)
Mux8 = DefineMux(8)
Mux16 = DefineMux(16)

@cache_definition
def DefineCommonlibMuxN(N: int, width: int):
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
    return DefineCircuitFromGeneratorWrapper(GetCoreIRBackend(), "commonlib", "muxn",
                                             name, ["mantle", "coreir", "global"],
                                             {"N": N, "width": width})

def CommonlibMuxN(N: int, width: int):
    return DefineCommonlibMuxN(N, width)()
