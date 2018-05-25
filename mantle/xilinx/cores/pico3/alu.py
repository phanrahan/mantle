from magma import *
from mantle import *

__all__ = ['DefineLogic', 'DefineArith']

#
# Logic:: A:Array(n,Bit), B:Array(n,Bit), S0:Bit, S1:Bit B[n] -> O:Array(n,Bit)
#
def DefineLogic(n):

    T = Array(n, Bit)

    class _Logic(Circuit):
        name = 'Logic'+str(n)
        IO = ['A', In(T), 'B', In(T), 'S0', In(Bit), 'S1', In(Bit), 'O', Out(T)]

        @classmethod
        def definition(logic):

            def alu(y):

                # alu::  A:Bit, B:Bit, S0:Bit, S1:Bit -> O:Bit
                def f(A, B, S0, S1):
                    # switch(S)
                    #  case 00: B     -> 0xA
                    #  case 01: A | B -> 0xE
                    #  case 10: A & B -> 0x8
                    #  case 11: A ^ B -> 0x6
                    if S1:
                        if S0: return A^B
                        else:  return A&B
                    else:
                        if S0: return A|B
                        else:  return B
                # expr = 0x68EC
                return LUT4(f)

            print('logic')
            unit =  braid(col(alu, n), forkargs=['I2', 'I3'])

            unit(logic.A, logic.B, logic.S0, logic.S1)
            wire(unit.O, logic.O)

    return _Logic


#
#
# switch(SUB#SEL)
#  case 00: A+B
#  case 01: A+B+Cin
#  case 10: A-B
#  case 11: A-B+Cin
#
def DefineArith(n):

    T = Array(n, Bit)

    class _Arith(Circuit):
        name = 'Arith'+str(n)
        IO = ['A', In(T), 'B', In(T), 
              'SEL', In(Bit), 'SUB', In(Bit), 'CIN', In(Bit),
              'O', Out(T), 'COUT', Out(Bit)]

        @classmethod
        def definition(arith):
            print('arith')
            # I0 A
            # I1 B
            # I2 SUB
            # out = A ^ ((~SUB & B) | (SUB & ~B))
            e1 = A0 ^ ((~A2 & A1) | (A2 & ~A1))
            e2 = A0
            unit = Adders( n, 3, e1, e2, None, True, forkargs=['I2'] )

            # I0 SEL
            # I1 SUB
            # I2 CIN
            #        SEL SUB CIN
            #  ADD    0   0  0
            #  ADDC   1   0  CIN
            #  SUB    0   1  1
            #  SUBC   1   1 ~CIN
            expr = (~A0 & A1) | (A0 & ((A1 & ~A2) | (~A1 & A2)))
            carry = LUT3(expr)
            wire(arith.SEL, carry.I0)
            wire(arith.SUB, carry.I1)
            wire(arith.CIN, carry.I2)
            wire(carry, unit.CIN)

            print('arith.A')
            wire(arith.A, unit.I0)
            print('arith.B')
            wire(arith.B, unit.I1)
            print('arith.SUB')
            wire(array(*(n*[arith.SUB])), unit.I2)

            print('arith.O')
            wire(unit.O, arith.O)
            print('arith.COUT')
            wire(unit.COUT, arith.COUT)
            print('end arith')

    return _Arith
