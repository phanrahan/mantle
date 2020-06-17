import os

import fault
import magma as m
from magma.testing import check_files_equal

from mantle import SIPO


def test_sipo_basic():
    class test_sipo_basic(m.Circuit):
        io = m.IO(
            I=m.In(m.Bit),
            O=m.Out(m.Bits[5])
        ) + m.ClockIO()
        io.O @= SIPO(5, m.Bit)()(io.I)

    m.compile("build/test_sipo_basic", test_sipo_basic)
    assert check_files_equal(__file__, f"build/test_sipo_basic.v",
                             f"gold/test_sipo_basic.v")

    tester = fault.SynchronousTester(test_sipo_basic, test_sipo_basic.CLK)
    tester.circuit.I = 1
    tester.advance_cycle()
    tester.circuit.O.expect(0b00001)
    tester.advance_cycle()
    tester.circuit.O.expect(0b00011)
    tester.circuit.I = 0
    tester.advance_cycle()
    tester.circuit.O.expect(0b00110)
    tester.circuit.I = 1
    tester.advance_cycle()
    tester.circuit.O.expect(0b01101)
    tester.circuit.I = 0
    tester.advance_cycle()
    tester.circuit.O.expect(0b11010)
    tester.compile_and_run("verilator", skip_compile=True,
                           directory=os.path.join(os.path.dirname(__file__),
                                                  "build"))


def test_sipo_product():
    class T(m.Product):
        X = m.Bit
        Y = m.Bits[5]

    class test_sipo_product(m.Circuit):
        io = m.IO(
            I=m.In(T),
            O=m.Out(m.Array[5, T])
        ) + m.ClockIO()
        io.O @= SIPO(5, T)()(io.I)

    m.compile("build/test_sipo_product", test_sipo_product)
    assert check_files_equal(__file__, f"build/test_sipo_product.v",
                             f"gold/test_sipo_product.v")

    tester = fault.SynchronousTester(test_sipo_product, test_sipo_product.CLK)
    sequence = [
        {"X": 1, "Y": 3},
        {"X": 0, "Y": 1},
        {"X": 0, "Y": 2},
        {"X": 1, "Y": 4},
        {"X": 0, "Y": 7},
    ]
    for i in range(len(sequence)):
        tester.circuit.I = sequence[i]
        tester.advance_cycle()
        for j in range(0, i + 1):
            tester.circuit.O[j].expect(sequence[i - j])
        for j in range(i + 1, len(sequence)):
            tester.circuit.O[j].expect(0)
    tester.circuit.I = 0
    for i in range(len(sequence)):
        tester.advance_cycle()
        for j in range(i + 1, len(sequence)):
            tester.circuit.O[j].expect(sequence[i - j])
        for j in range(0, i + 1):
            tester.circuit.O[j].expect(0)

    tester.compile_and_run("verilator", skip_compile=True,
                           directory=os.path.join(os.path.dirname(__file__),
                                                  "build"))


def test_sipo_arr():
    class T(m.Product):
        X = m.Bit
        Y = m.Bits[5]

    T = m.Array[2, T]

    class test_sipo_arr(m.Circuit):
        io = m.IO(
            I=m.In(T),
            O=m.Out(m.Array[5, T])
        ) + m.ClockIO()
        io.O @= SIPO(5, T)()(io.I)

    m.compile("build/test_sipo_arr", test_sipo_arr)
    assert check_files_equal(__file__, f"build/test_sipo_arr.v",
                             f"gold/test_sipo_arr.v")

    tester = fault.SynchronousTester(test_sipo_arr, test_sipo_arr.CLK)
    sequence = [
        [{"X": 1, "Y": 3}, {"X": 1, "Y": 6}],
        [{"X": 0, "Y": 1}, {"X": 0, "Y": 2}],
        [{"X": 0, "Y": 2}, {"X": 1, "Y": 3}],
        [{"X": 1, "Y": 4}, {"X": 0, "Y": 0}],
        [{"X": 0, "Y": 7}, {"X": 0, "Y": 1}],
    ]
    for i in range(len(sequence)):
        tester.circuit.I = sequence[i]
        tester.advance_cycle()
        for j in range(0, i + 1):
            tester.circuit.O[j].expect(sequence[i - j])
        for j in range(i + 1, len(sequence)):
            tester.circuit.O[j].expect(0)
    tester.circuit.I = 0
    for i in range(len(sequence)):
        tester.advance_cycle()
        for j in range(i + 1, len(sequence)):
            tester.circuit.O[j].expect(sequence[i - j])
        for j in range(0, i + 1):
            tester.circuit.O[j].expect(0)

    tester.compile_and_run("verilator", skip_compile=True,
                           directory=os.path.join(os.path.dirname(__file__),
                                                  "build"))
