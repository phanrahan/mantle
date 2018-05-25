from collections import Sequence
from magma import *
from ..spartan6.CLB import *
from .ROM import ROMN

__all__ = ['FlatCascade', 'DefineFlatCascade']

def _Name(n, k, expr, input, din, cin):
    if isinstance(expr, Sequence):
        expr = "_".join(["%X" % uint(e, 1<<k) for e in expr])
    else:
        expr = "%016X" % uint(expr, 1<<k) 
    return 'FlatCascade%dx%d_%s_%d_%d_%d' % (n, k, expr, input, din, cin)

#
# create an And/NAnd gate using the carry chain 
#
#  cout = MUXCY( din, cin, ROM4() )
#
def FullCarry(k, expr, din):

    rom = ROMN(expr, k)

    CIN = Bit()

    mux = MUXCY()
    wire(rom.O, mux.S)
    wire(din,   mux.DI)
    wire(CIN,   mux.CI)

    return AnonymousCircuit( 'input I', rom.I, "output O", mux.O, "input CIN", CIN )



#
# Build a column of Ander
#
#  And = DefineFlatCascade(n,   A0&A1&A2&A3,  1, 0, 1)
# Nand = DefineFlatCascade(n,   A0&A1&A2&A3,  1, 1, 0)
#   Or = DefineFlatCascade(n, ~(A0|A1|A2|A3), 0, 1, 0)
#  Nor = DefineFlatCascade(n, ~(A0|A1|A2|A3), 0, 0, 1)
#
# expr is the expression that goes into the LUT
# i is the value that is wired into extra LUT inputs
#
# The S of MUXCY is controlled by the output of the LUT
#   din is the value going into the 0 slot of MUXCY
#   cin is the value going into the 1 slot of MUXCY

def DefineFlatCascade(n, k, expr, input, din, cin):
    class _FlatCascade(Circuit):
        name = _Name(n, k, expr, input, din, cin)
        IO = ["input I", Array(n, Bit), "output O", Bit]
        @classmethod
        def definition(carry):
            def f(y):
                e = expr[y] if isinstance(expr, Sequence) else expr
                return FullCarry(k, e, din)

            m = (n+LOG_BITS_PER_LUT-1)//LOG_BITS_PER_LUT
            c = braid( col(f, m), flatargs=['I'], foldargs={"CIN":"O"})

            for i in range(LOG_BITS_PER_LUT*m):
                if i < n:
                    wire(carry.I[i], c.I[i])
                else:
                    wire(input, c.I[i])

            wire(c.O, carry.O)
            wire(cin, c.CIN)

    return _FlatCascade

def FlatCascade(n, k, expr, input, din, cin):
    return DefineFlatCascade(n, k, expr, input, din, cin)()

