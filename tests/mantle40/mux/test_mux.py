import os
os.environ['MANTLE'] = 'lattice'
from mantle import Mux2, Mux4, Mux8, Mux16, MuxN, Mux

def test_mux():
    mux = Mux2()
    assert str(mux.interface) == 'I : Bits(2), S : In(Bit) -> O : Out(Bit)'

    mux = Mux4()
    assert str(mux.interface) == 'I : Bits(4), S : Bits(2) -> O : Out(Bit)'

    mux = Mux8()
    assert str(mux.interface) == 'I : Bits(8), S : Bits(3) -> O : Out(Bit)'

    mux = Mux16()
    assert str(mux.interface) == 'I : Bits(16), S : Bits(4) -> O : Out(Bit)'

    mux = MuxN(4)
    assert str(mux.interface) == 'I : Bits(4), S : Bits(2) -> O : Out(Bit)'

    mux = Mux(2,1)
    assert str(mux.interface) == 'I : Bits(2), S : In(Bit) -> O : Out(Bit)'

