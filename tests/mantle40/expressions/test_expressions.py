from magma import *
from mantle import *
from loam.boards.icestick import IceStick


def test():
    icestick = IceStick()
    icestick.Clock.on()
    icestick.D1.on()
    icestick.D2.on()
    icestick.D3.on()

    main = icestick.main()
    @circuit
    def func(a : In(Bit), b : In(Bit), c : Out(Bit)):
        c = a + b

    circ = func()
    reg = Register(1, ce=True)
    counter = Counter(24)
    wire(reg.O[0], main.D1)
    wire(reg.O[0], main.D2)
    wire(reg.O[0], main.D3)
    wire(reg.CE, counter.O[23])
    wire(reg.O[0], circ.a)
    wire(1, circ.b)
    wire(reg.I[0], circ.c)
    wireclock(main, reg)
    compile("build/test_expr", main)
    assert magma_check_files_equal(__file__, "build/test_expr.v", "gold/test_expr.v")

if __name__ == "__main__":
    test()
