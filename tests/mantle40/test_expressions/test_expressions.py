from magma import *
from mantle import *
from loam.boards.icestick import IceStick


def test_bit():
    icestick = IceStick()
    icestick.Clock.on()
    icestick.D1.on()

    main = icestick.main()
    @circuit
    def add1(a : In(Bit), b : In(Bit), c : Out(Bit)):
        c = a + b

    circ = add1()
    reg = Register(1, ce=True)
    counter = Counter(22)
    wire(reg.O[0], main.D1)
    wire(reg.CE, counter.COUT)
    wire(reg.O[0], circ.a)
    wire(1, circ.b)
    wire(reg.I[0], circ.c)
    wireclock(main, reg)
    compile("build/test_bit", main)
    if __name__ != "__main__":
        assert magma_check_files_equal(__file__, "build/test_bit.v", "gold/test_bit.v")

def test_array():
    icestick = IceStick()
    icestick.Clock.on()
    icestick.D1.on()
    icestick.D2.on()
    icestick.D3.on()
    icestick.D4.on()
    icestick.D5.on()

    main = icestick.main()
    @circuit
    def add5(a : In(Array(5, Bit)), b : In(Array(5, Bit)), c : Out(Array(5, Bit))):
        c = a + b

    circ = add5()
    reg = Register(5, ce=True)
    counter = Counter(22)
    wire(reg.O[0], main.D1)
    wire(reg.O[1], main.D2)
    wire(reg.O[2], main.D3)
    wire(reg.O[3], main.D4)
    wire(reg.O[4], main.D5)
    wire(reg.CE, counter.COUT)
    wire(reg.O, circ.a)
    wire(array(*int2seq(1, 5)), circ.b)
    wire(reg.I, circ.c)
    wireclock(main, reg)
    compile("build/test_array", main)
    if __name__ != "__main__":
        assert magma_check_files_equal(__file__, "build/test_array.v", "gold/test_array.v")

def test_sub():
    icestick = IceStick()
    icestick.Clock.on()
    icestick.D1.on()
    icestick.D2.on()
    icestick.D3.on()
    icestick.D4.on()
    icestick.D5.on()

    main = icestick.main()
    @circuit
    def sub5(a : In(Array(5, Bit)), b : In(Array(5, Bit)), c : Out(Array(5, Bit))):
        c = a - b

    circ = sub5()
    reg = Register(5, ce=True)
    counter = Counter(23)
    wire(reg.O[0], main.D1)
    wire(reg.O[1], main.D2)
    wire(reg.O[2], main.D3)
    wire(reg.O[3], main.D4)
    wire(reg.O[4], main.D5)
    wire(reg.CE, counter.COUT)
    wire(reg.O, circ.a)
    wire(array(*int2seq(1, 5)), circ.b)
    wire(reg.I, circ.c)
    wireclock(main, reg)
    compile("build/test_sub", main)
    if __name__ != "__main__":
        assert magma_check_files_equal(__file__, "build/test_sub.v", "gold/test_sub.v")

if __name__ == "__main__":
    # test_bit()
    # test_array()
    test_sub()
