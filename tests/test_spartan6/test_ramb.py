import magma

import pytest
from fault.test_vectors import generate_function_test_vectors, \
    generate_simulator_test_vectors

def com(Test, name):
    import magma
    from magma import compile
    from magma.testing import check_files_equal
    name = f'{name}_{magma.mantle_target}'
    build = 'build/' + name
    gold = 'gold/' + name
    compile(build, Test, output="verilog")
    assert check_files_equal(__file__, build+'.v', gold+'.v')

import magma as m
from mantle.xilinx.spartan6 import ROMB16, RAMB16

def test_romb():
    main = m.DefineCircuit("test_romb",
                         "O", m.Out(m.Bits[8]),
                         "CLK", m.In(m.Clock)) 
    rom = [i % 256 for i in range(2048)]
    romb = ROMB16(rom, 8)
    m.wire(romb( m.bits(1,11), clk=main.CLK ), main.O)
    m.EndCircuit()

    com(main, 'romb2048x8')

@pytest.mark.skip(reason='NYI')
def test_ramb():
    main = m.DefineCircuit("test_ramb",
                         "RDATA", m.Out(m.Bits[8]),
                         "WDATA", m.In(m.Bits[8]),
                         "WE",   m.In(m.Bit),
                         "CLK", m.In(m.Clock))
    ram = [i % 256 for i in range(2048)]
    ramb = ROMB16(ram, 8)
    m.wire(ramb.A, uint(1, 11))
    m.wire(ramb.CLK, main.CLK)
    m.wire(ramb.RE, 1)
    m.wire(ramb.WADDR, uint(1, 11))
    m.wire(ramb.WCLK, main.CLK)
    m.wire(ramb.WE, main.WE)

    m.wire(ramb.RDATA, main.RDATA)
    m.wire(ramb.WDATA, main.WDATA)
    m.EndCircuit()

    com(main, 'romb2048x8')


