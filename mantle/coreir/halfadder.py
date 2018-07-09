import magma as m
from .logic import And, XOr

class HalfAdder(m.Circuit):
    IO = ["I0", m.In(m.Bit), "I1", m.In(m.Bit), "O", m.Out(m.Bit), "COUT", m.Out(m.Bit)]
    @classmethod
    def definition(io):
        # Generate the sum
        sum_ = XOr(2)(io.IO, io.I1)
        # Generate the carry
        cout = And(2)(io.I0, io.I1)
        m.wire(sum_, io.O)
        m.wire(cout, io.COUT)
