from magma import *
from .LUT import A0, A1
from .logic import Not
from .cascade import FullCascade

__all__  = ['DefineAdd'] 
__all__ += ['DefineSub']
__all__ += ['DefineNegate']

def _Name(basename, n, cin, cout):
    name = basename + str(n)
    if cin is 0 or cin is 1:
        name += '_cin{}'.format(cin)
    elif cin:
        name += '_cin'.format(cin)
    if cout:
        name += '_cout'.format(cout)
    return name

def _Args(n, cin, cout):
    T = Bits[ n ]

    args = ["I0", In(T), "I1", In(T)]

    if cin is True:
        args += ['CIN', In(Bit)]

    args += ["O", Out(T)]

    if cout is True:
        args += ['COUT', Out(Bit)]

    return args

#
# Create an n-bit Add
#
# I0:In(Bits(n)), I1:In(Bits(n)), CIN:In(Bit), O:Out(Bits(n)), COUT:Out(Bit)
#
# if cin, CIN is added to the circuit
# if cout: COUT is added to the circuit
#
def DefineAdd(n, cin=False, cout=False):
    class _Add(Circuit):
        name = _Name('Add', n, cin, cout)
        IO = _Args(n, cin, cout)
        @classmethod
        def definition(io):
            add = FullCascade(n, 2, A0^A1, A0, cin, cout)
            wire(io.I0, add.I0)
            wire(io.I1, add.I1)
            wire(add.O, io.O)
            if cin is True:
                wire(io.CIN, add.CIN)
            if cout is True:
                wire(add.COUT, io.COUT)
    return _Add
    

def DefineSub(n, cin=1, cout=False):
    class _Sub(Circuit):
        name = _Name('Sub', n, cin, cout)
        IO = _Args(n, cin, cout)
        @classmethod
        def definition(io):
            sub = FullCascade(n, 2, A0^~A1, A0, cin, cout)
            wire(io.I0, sub.I0)
            wire(io.I1, sub.I1)
            wire(sub.O, io.O)
            if cin is True:
                wire( Not()(io.CIN), sub.CIN )
            if cout is True:
                wire(sub.COUT, io.COUT)
    return _Sub

def DefineNegate(n):
    T = Bits[ n ]
    class _Negate(Circuit):
        name = 'Negate{}'.format(n)
        IO = ['I', In(T), 'O', Out(T)]
        @classmethod
        def definition(io):
            sub =  DefineSub(n)()
            wire( sub( uint(0,n), io.I ), io.O )
    return _Negate
    

