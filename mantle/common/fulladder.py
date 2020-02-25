import magma as m
from mantle import XOr, And, Or

__all__ = [ "FullAdder" ]

class FullAdder(m.Circuit):
    io = m.IO(I0=m.In(m.Bit), I1=m.In(m.Bit), CIN=m.In(m.Bit),
              O=m.Out(m.Bit), COUT=m.Out(m.Bit))

    # Generate the sum
    io.O @= io.I0 ^ io.I1 ^ io.CIN
    # Generate the carry
    io.COUT @= io.I0 & io.I1 | io.I1 & io.CIN | io.I0 & io.CIN
