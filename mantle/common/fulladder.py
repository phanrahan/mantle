import magma as m
from mantle import XOr, And, Or

__all__ = [ "FullAdder" ]

class FullAdder(m.Circuit):
    IO = ["I0", m.In(m.Bit), "I1", m.In(m.Bit), "CIN", m.In(m.Bit),
          "O", m.Out(m.Bit), "COUT", m.Out(m.Bit)]

    @classmethod
    def definition(io):
        # Generate the sum
        m.wire( XOr(3)(io.I0, io.I1, io.CIN), io.O)
        # Generate the carry
        m.wire( Or(3)(And(2)(io.I0, io.I1),
                      And(2)(io.I1, io.CIN),
                      And(2)(io.I0, io.CIN)), io.COUT)
