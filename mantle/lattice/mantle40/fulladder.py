from magma import *
from ..ice40.PLB import SB_CARRY, I0, I1, I2, I3
from .LUT import LUT4

__all__  = ["FullAdder"]

#
# A : Bit, B : Bit, CIN : Bit -> S : Bit, COUT : Bit
#
def FullAdder(**kwargs):
    A = In(Bit)()
    B = In(Bit)()
    CIN = In(Bit)()

    sum = LUT4(I1^I2^I3, **kwargs)
    carry = SB_CARRY() # (I0&I1)|(I1&I2)|(I2&I0)

    sum(0,A,B,CIN)
    carry(A,B,CIN)

    return AnonymousCircuit("I0", A, "I1", B, "CIN", CIN, 
                            "O", sum.O, "COUT", carry.CO)
