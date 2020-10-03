from magma import *
import magma as m
from hwtypes import BitVector
from mantle.lattice.ice40.RAMB import ROMB, RAMB
from magma.simulator import PythonSimulator
from magma.testing import check_files_equal


def test_romb():
    main = DefineCircuit("test_romb",
                         "RDATAOUT", Out(Bits[ 8 ]),
                         "CLK", In(Clock)) # FIXME: hack
    romb = ROMB(512, 8, [0b00000001, 0b11111111] + [0] * 510)
    wire(romb.RADDR, uint(1, 9))
    wire(romb.RCLK, main.CLK)
    wire(romb.RE, enable(1))

    wire(romb.RDATA, main.RDATAOUT)
    EndCircuit()

    sim = PythonSimulator(main, clock=main.CLK)
    sim.evaluate()

    sim.advance(2)

    assert BitVector[8](sim.get_value(main.RDATAOUT)) == BitVector[8](0b11111111)


def test_ramb():
    main = DefineCircuit("test_ramb",
                         "RDATA", Out(Bits[ 8 ]),
                         "WDATA", In(Bits[ 8 ]),
                         "WE",   In(Enable),
                         "CLK", In(Clock))
    ramb = RAMB(512, 8, [0b00000001, 0b11111111] + [0] * 510)
    wire(ramb.RADDR, uint(1, 9))
    wire(ramb.RCLK, main.CLK)
    wire(ramb.RE, enable(1))
    wire(ramb.WADDR, uint(1, 9))
    wire(ramb.WCLK, main.CLK)
    wire(ramb.WE, main.WE)

    wire(ramb.RDATA, main.RDATA)
    wire(ramb.WDATA, main.WDATA)
    EndCircuit()

    sim = PythonSimulator(main, clock=main.CLK)
    sim.set_value(main.WE, False)
    sim.evaluate()

    sim.advance(2)

    assert BitVector[8](sim.get_value(main.RDATA)) == BitVector[8](0b11111111)

    # Write 0xBE to WADDR = 1
    sim.set_value(main.WE, True)
    sim.set_value(main.WDATA, BitVector[8](0xBE))

    sim.advance(2)

    # Read RADDR = 1 again
    sim.set_value(main.WE, False)
    sim.evaluate()

    sim.advance(2)

    assert BitVector[8](sim.get_value(main.RDATA)) == BitVector[8](0xBE)


def test_romb_coreir():
    main = DefineCircuit("test_romb_coreir",
                         "RDATAOUT", Out(Bits[16]),
                         "CLK", In(Clock))
    romb = ROMB(256, 16, [0b00000001, 0b11111111] + [0] * 254)
    wire(romb.RADDR, uint(1, 8))
    wire(romb.RCLK, main.CLK)
    wire(romb.RE, enable(1))
    wire(romb.RDATA, main.RDATAOUT)
    EndCircuit()

    compile("build/test_romb_coreir", main, output="coreir")
    assert check_files_equal(__file__,
            "build/test_romb_coreir.json", "gold/test_romb_coreir.json")

    compile("build/test_romb_coreir", main, output="coreir-verilog")
    assert check_files_equal(__file__,
            "build/test_romb_coreir.v", "gold/test_romb_coreir.v")
