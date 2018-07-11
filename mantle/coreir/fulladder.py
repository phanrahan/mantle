import magma as m
from .logic import XOr, And, Or

class FullAdder(m.Circuit):
    IO = ["I0", m.In(m.Bit), "I1", m.In(m.Bit), "CIN", m.In(m.Bit),
          "O", m.Out(m.Bit), "COUT", m.Out(m.Bit)]
    @classmethod
    def definition(io):
        # Generate the sum
        sum_ = XOr(3)(io.I0, io.I1, io.CIN)
        # Generate the carry
        cout = Or(3)(And(2)(io.I0, io.I1), And(2)(io.I1, io.CIN), And(2)(io.I0, io.CIN))
        m.wire(sum_, io.O)
        m.wire(cout, io.COUT)
