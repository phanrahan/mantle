import os
os.environ['MANTLE'] = 'lattice'
from mantle import Mux2, Mux4, Mux8, Mux16, Mux

def test_muxn():
    mux = Mux2()
    assert str(mux.interface) == '"I", In(Bits(2)), "S", In(Bit), "O", Out(Bit)'

    mux = Mux4()
    print(mux.interface)
    assert str(mux.interface) == '"I", In(Bits(4)), "S", In(Bits(2)), "O", Out(Bit)'

    mux = Mux8()
    assert str(mux.interface) == '"I", In(Bits(8)), "S", In(Bits(3)), "O", Out(Bit)'

    mux = Mux16()
    assert str(mux.interface) == '"I", In(Bits(16)), "S", In(Bits(4)), "O", Out(Bit)'

def test_mux():
    mux = Mux(2,1)
    assert str(mux.interface) == '"I0", In(Bits(1)), "I1", In(Bits(1)), "S", In(Bit), "O", Out(Bits(1))'

