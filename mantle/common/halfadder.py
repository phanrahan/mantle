import magma as m
from mantle import XOr, And

__all__ = [ "HalfAdder" ]

class HalfAdder(m.Circuit):
    IO = ["I", m.In(m.Bit), "CIN", m.In(m.Bit),
          "O", m.Out(m.Bit), "COUT", m.Out(m.Bit)]

    @classmethod
    def definition(io):
        # Generate the sum
        m.wire( XOr(2)(io.I, io.CIN), io.O )
        # Generate the carry
        m.wire( And(2)(io.I, io.CIN), io.COUT )
