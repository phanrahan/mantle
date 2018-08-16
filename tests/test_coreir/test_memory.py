import pytest
coreir = pytest.importorskip("coreir")
from magma import *
from magma.testing import check_files_equal
from mantle.coreir.memory import DefineCoreirMem


def test_coreir_rom():
    addr_width = 2
    width = 16
    class Mem(Circuit):
        name = "test_coreir_mem"
        IO = ["raddr", In(Bits(addr_width)),
              "rdata", Out(Bits(width)),
              "waddr", In(Bits(addr_width)),
              "wdata", In(Bits(width)),
              "clk", In(Clock),
              "wen", In(Bit) ]
        @classmethod
        def definition(io):
            mem = DefineCoreirMem(4, 16)()
            wire(io.raddr, mem.raddr)
            wire(io.rdata, mem.rdata)
            wire(io.waddr, mem.waddr)
            wire(io.wdata, mem.wdata)
            wire(io.clk, mem.clk)
            wire(io.wen, mem.wen)
    compile("build/test_coreir_mem", Mem, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_mem.json", "gold/test_coreir_mem.json")
