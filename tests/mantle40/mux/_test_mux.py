import os
os.environ['MANTLE'] = 'lattice'
from mantle import Mux2, Mux4, Mux8, Mux16, MuxN, Mux

def test_mux():
    mux = Mux2()
    assert str(mux.interface) == 'I : Bits(2), S : In(Bit) -> O : Out(Bit)'

    mux = Mux4()
    assert str(mux.interface) == 'I : Array(4,In(Bit)), S : Array(2,In(Bit)) -> O : Out(Bit)'

    mux = Mux8()
    assert str(mux.interface) == 'I : Array(8,In(Bit)), S : Array(3,In(Bit)) -> O : Out(Bit)'

    mux = Mux16()
    assert str(mux.interface) == 'I : Array(16,In(Bit)), S : Array(4,In(Bit)) -> O : Out(Bit)'

    mux = MuxN(4)
    assert str(mux.interface) == 'I : Array(4,In(Bit)), S : Array(2,In(Bit)) -> O : Out(Bit)'

    mux = Mux(2,1)
    assert str(mux.interface) == 'I : Array(2,In(Bit)), S : In(Bit) -> O : Out(Bit)'

