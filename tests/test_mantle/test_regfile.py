import os

import pytest

import fault
import magma as m
from magma.testing import check_files_equal
import mantle


@pytest.mark.parametrize("backend", ["magma", "verilog"])
def test_basic(backend):
    height = 4
    data_width = 4
    addr_width = m.bitutils.clog2(height)

    class _Main(m.Circuit):
        name = f"test_regfile_basic_{backend}"
        io = m.IO(
            write_addr=m.In(m.Bits[addr_width]),
            write_data=m.In(m.Bits[data_width]),
            read_addr=m.In(m.Bits[addr_width]),
            read_data=m.Out(m.Bits[data_width])
        ) + m.ClockIO(has_async_reset=True)
        reg_file = mantle.RegFileBuilder("my_regfile",  height, data_width,
                                         backend=backend)
        reg_file[io.write_addr] = io.write_data
        io.read_data @= reg_file[io.read_addr]

    m.compile(f"build/test_regfile_basic_{backend}", _Main)
    assert check_files_equal(__file__,
                             f"build/test_regfile_basic_{backend}.v",
                             f"gold/test_regfile_basic_{backend}.v")

    tester = fault.Tester(_Main, _Main.CLK)
    tester.circuit.CLK = 0
    for i in range(4):
        tester.circuit.write_addr = i
        tester.circuit.write_data = i
        tester.step(2)
    for i in range(4):
        tester.circuit.read_addr = i
        tester.eval()
        tester.circuit.read_data.expect(i)
    build_dir = os.path.join(os.path.dirname(__file__), "build")
    tester.compile_and_run(target="verilator", directory=build_dir,
                           flags=["-Wno-unused", "-Wno-undriven"])


@pytest.mark.parametrize("backend", ["magma", "verilog"])
def test_two_ports(backend):
    height = 4
    data_width = 4
    addr_width = m.bitutils.clog2(height)

    class _Main(m.Circuit):
        name = f"test_regfile_two_ports_{backend}"
        io = m.IO(
            write_addr0=m.In(m.Bits[addr_width]),
            write_data0=m.In(m.Bits[data_width]),
            write_addr1=m.In(m.Bits[addr_width]),
            write_data1=m.In(m.Bits[data_width]),
            read_addr0=m.In(m.Bits[addr_width]),
            read_data0=m.Out(m.Bits[data_width]),
            read_addr1=m.In(m.Bits[addr_width]),
            read_data1=m.Out(m.Bits[data_width])
        ) + m.ClockIO(has_async_reset=True)
        reg_file = mantle.RegFileBuilder("my_regfile",  height, data_width,
                                         backend=backend)
        reg_file[io.write_addr0] = io.write_data0
        io.read_data0 @= reg_file[io.read_addr0]
        reg_file[io.write_addr1] = io.write_data1
        io.read_data1 @= reg_file[io.read_addr1]

    m.compile(f"build/test_regfile_two_ports_{backend}", _Main)
    assert check_files_equal(__file__,
                             f"build/test_regfile_two_ports_{backend}.v",
                             f"gold/test_regfile_two_ports_{backend}.v")

    tester = fault.Tester(_Main, _Main.CLK)
    tester.circuit.CLK = 0
    for i in range(4):
        tester.circuit.write_addr0 = i
        tester.circuit.write_data0 = 3 - i
        tester.circuit.write_addr1 = 3 - i
        tester.circuit.write_data1 = i
        tester.step(2)
    for i in range(4):
        tester.circuit.read_addr0 = i
        tester.circuit.read_addr1 = 3 - i
        tester.eval()
        tester.circuit.read_data0.expect(3 - i)
        tester.circuit.read_data1.expect(i)

    # Test priority.
    tester.circuit.write_addr0 = 3
    tester.circuit.write_data0 = 3
    tester.circuit.write_addr1 = 3
    tester.circuit.write_data1 = 4
    tester.step(2)
    tester.circuit.read_addr0 = 3
    tester.eval()
    tester.circuit.read_data0.expect(4)
    build_dir = os.path.join(os.path.dirname(__file__), "build")
    tester.compile_and_run(target="verilator", directory=build_dir,
                           flags=["-Wno-unused", "-Wno-undriven"])


@pytest.mark.parametrize("backend", ["magma", "verilog"])
def test_write_enable(backend):
    height = 4
    data_width = 4
    addr_width = m.bitutils.clog2(height)

    class _Main(m.Circuit):
        name = f"test_regfile_enable_{backend}"
        io = m.IO(
            write_addr=m.In(m.Bits[addr_width]),
            write_data=m.In(m.Bits[data_width]),
            write_enable=m.In(m.Enable),
            read_addr=m.In(m.Bits[addr_width]),
            read_data=m.Out(m.Bits[data_width])
        ) + m.ClockIO(has_async_reset=True)
        reg_file = mantle.RegFileBuilder("my_regfile",  height, data_width,
                                         backend=backend)
        reg_file.write(io.write_addr, io.write_data, enable=io.write_enable)
        io.read_data @= reg_file[io.read_addr]

    m.compile(f"build/test_regfile_enable_{backend}", _Main)
    assert check_files_equal(__file__,
                             f"build/test_regfile_enable_{backend}.v",
                             f"gold/test_regfile_enable_{backend}.v")

    tester = fault.Tester(_Main, _Main.CLK)
    tester.circuit.CLK = 0
    for i in range(4):
        tester.circuit.write_enable = 1
        tester.circuit.write_addr = i
        tester.circuit.write_data = i
        tester.step(2)
        # Write enable low should not change the value
        tester.circuit.write_enable = 0
        tester.circuit.write_data = 0
        tester.step(2)
    for i in range(4):
        tester.circuit.read_addr = i
        tester.eval()
        tester.circuit.read_data.expect(i)
    build_dir = os.path.join(os.path.dirname(__file__), "build")
    tester.compile_and_run(target="verilator", directory=build_dir,
                           flags=["-Wno-unused", "-Wno-undriven"])
