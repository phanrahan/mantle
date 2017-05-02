import sys
from magma import *
from mantle import *
from loam.boards.icestick import IceStick

def test_circular_shift():
    icestick = IceStick()
    icestick.Clock.on()
    icestick.D1.on()
    icestick.D2.on()
    icestick.D3.on()
    icestick.D4.on()
    icestick.D5.on()

    main = icestick.main()

    counter = Counter(23, cout=True)

    reg5 = Register(5, ce=True)
    wire(reg5.CE, counter.COUT)
    shift5 = ShiftRightArithmetic(5, 1)()

    wire(shift5.I[4], Not()(reg5.O[0]))
    wire(reg5.O[:4], shift5.I[:4])

    wire(shift5.O, reg5.I)

    wire(reg5.O[0], main.D5)
    wire(reg5.O[1], main.D4)
    wire(reg5.O[2], main.D3)
    wire(reg5.O[3], main.D2)
    wire(reg5.O[4], main.D1)

    compile("build/test_arith_shift", main)
    assert magma_check_files_equal(__file__, "build/test_arith_shift.v", "gold/test_arith_shift.v")


def test_circular_shift_by_two():
    icestick = IceStick()
    icestick.Clock.on()
    icestick.D1.on()
    icestick.D2.on()
    icestick.D3.on()
    icestick.D4.on()
    icestick.D5.on()

    main = icestick.main()

    counter = Counter(23, cout=True)

    reg5 = Register(5, ce=True)
    wire(reg5.CE, counter.COUT)
    shift5 = ShiftRightArithmetic(5, 2)()

    wire(shift5.I[4], Not()(reg5.O[0]))
    wire(reg5.O[:4], shift5.I[:4])

    wire(shift5.O, reg5.I)

    wire(reg5.O[0], main.D5)
    wire(reg5.O[1], main.D4)
    wire(reg5.O[2], main.D3)
    wire(reg5.O[3], main.D2)
    wire(reg5.O[4], main.D1)

    compile("build/test_arith_shift_by_two", main)
    assert magma_check_files_equal(__file__, "build/test_arith_shift_by_two.v", "gold/test_arith_shift_by_two.v")
