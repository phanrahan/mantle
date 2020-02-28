import os
from magma.backend.coreir_ import CoreIRBackend
from magma.simulator.coreir_simulator import CoreIRSimulator
from mantle import RAM
from mantle.coreir.memory import DefineCoreirMem, DefineRAM, DefineMemory
from magma.testing import check_files_equal
from magma import *
import pytest
coreir = pytest.importorskip("coreir")


def test_coreir_rom():
    addr_width = 2
    width = 16

    class Mem(Circuit):
        name = "test_coreir_mem"
        io = m.IO(raddr=In(Bits[addr_width]),
                  rdata=Out(Bits[width]),
                  waddr=In(Bits[addr_width]),
                  wdata=In(Bits[width]),
                  clk=In(Clock),
                  wen=In(Bit))

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


def test_ram1x8():
    c = coreir.Context()
    cirb = CoreIRBackend(c)

    testcircuit = DefineRAM(1, 8)
    CoreIRSimulator(testcircuit, testcircuit.CLK, context=cirb.context)


def test_ram_latency1():
    mem = DefineMemory(height=256, width=16, read_latency=1)
    compile("build/test_latency", mem, output='coreir-verilog')
    assert check_files_equal(
        __file__, "build/test_latency.v", "gold/test_latency.v")


def test_generic_memory_import():
    assert type(RAM(8, 8)) == DefineRAM(8, 8)
