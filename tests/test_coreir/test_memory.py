import pytest
coreir = pytest.importorskip("coreir")
from magma import *
from magma.testing import check_files_equal
from mantle.coreir.memory import DefineCoreirMem, DefineRAM
from magma.simulator.coreir_simulator import CoreIRSimulator
from magma.backend.coreir_ import CoreIRBackend


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


def test_coreir_rom_init():
    addr_width = 2
    width = 16
    class Mem(Circuit):
        name = "test_coreir_mem_init"
        IO = ["raddr", In(Bits(addr_width)),
              "rdata", Out(Bits(width)),
              "waddr", In(Bits(addr_width)),
              "wdata", In(Bits(width)),
              "clk", In(Clock),
              "wen", In(Bit) ]
        @classmethod
        def definition(io):
            mem = DefineCoreirMem(4, 16, init=(0xDEAD, 0xBEEF) * 2)()
            wire(io.raddr, mem.raddr)
            wire(io.rdata, mem.rdata)
            wire(io.waddr, mem.waddr)
            wire(io.wdata, mem.wdata)
            wire(io.clk, mem.clk)
            wire(io.wen, mem.wen)
    compile("build/test_coreir_mem_init", Mem, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_mem_init.json", "gold/test_coreir_mem_init.json")

def test_ram1x8():
    c = coreir.Context()
    cirb = CoreIRBackend(c)

    testcircuit = DefineRAM(1, 8)
    CoreIRSimulator(testcircuit, testcircuit.CLK, context=cirb.context)
