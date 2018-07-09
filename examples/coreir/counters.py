import os
os.environ['MANTLE'] = 'coreir'
from magma import *
from mantle import *
import mantle.coreir


def DefineMantleReg(init):
    class MantleReg(Circuit):
        name = f"MantleReg{init}"
        IO = ["in", In(Bits(16)), "clk", In(Clock), "out", Out(Bits(16)), "clr", In(Bit)]
        @classmethod
        def definition(io):
            c0 = bits(0, 16)
            clrMux = mantle.coreir.DefineCoreirMux(width=16)()
            reg0 = mantle.coreir.DefineCoreirReg(16, init=init)()
            wire(c0, clrMux.in1)
            wire(getattr(io, "in"), clrMux.in0)
            wire(clrMux.out, getattr(reg0, "in"))
            wire(clrMux.sel, io.clr)
            wire(reg0.clk, io.clk)
            wire(reg0.out, io.out)
    return MantleReg


class Counter(Circuit):
    name = "Counter16"
    IO = ["clk", In(Clock), "clr", In(Bit), "out", Out(Bits(16))]

    @classmethod
    def definition(io):
        r = DefineMantleReg(init=55)()
        a = mantle.coreir.DefineCoreirAdd(16)()
        c1 = bits(1, 16)
        wire(c1, a.in0)
        wire(r.out, a.in1)
        wire(r.clk, io.clk)
        wire(a.out, getattr(r, "in"))  # r.in doesn't work because in is a keyword
        wire(r.out, io.out)
        wire(io.clr, r.clr)

class Counters(Circuit):
    name = "Counters"
    IO = ["clk", In(Clock)]
    @classmethod
    def definition(io):
        count0 = Counter(16)
        count1 = Counter(16)
        wire(io.clk, count0.clk)
        wire(io.clk, count1.clk)
        wire(count0.out[4], count1.clr)
        wire(count1.out[8], count0.clr)


if __name__ == "__main__":
    compile("counters", Counters, output="coreir")
