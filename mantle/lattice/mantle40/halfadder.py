from magma import *
from ..ice40.PLB import SB_CARRY, I0, I1, I2, I3
from .LUT import LUT4

__all__  = ["HalfAdder"]

#
# A : Bit, B : Bit -> S : Bit, COUT : BIT
#
def HalfAdder(**kwargs):
    A = In(Bit)()
    B = In(Bit)()

    sum = LUT4(I1^I2^I3, **kwargs)
    carry = SB_CARRY() # (I0&I1)|(I1&I2)|(I2&I0)

    sum(0,A,B,0)
    carry(A,B,0)

    return AnonymousCircuit("I0", A, "I1", B, "O", sum.O, "COUT", carry.CO)
