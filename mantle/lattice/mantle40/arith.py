from magma import *
from .logic import DefineInvert, Not
from .fulladder import FullAdder

__all__  = ['DefineAdd'] 
__all__ += ['DefineSub']
__all__ += ['DefineNegate']

def _AdderName(basename, n, cin, cout):
    name = f"{basename}{n}"
    if cin: name += '_CIN'
    if cout: name += '_COUT'
    return name

def _AdderArgs(n, cin, cout):
    T = Bits[ n ]

    args = ["I0", In(T), "I1", In(T)]
    if cin:
        args += ['CIN', In(Bit)]

    args += ["O", Out(T)]
    if cout:
        args += ['COUT', Out(Bit)]

    return args

def DefineAdders(name, n, cin, cout, forkargs=[]):

    def f(y):
        return FullAdder()

    c = braid( col(f, n), foldargs={"CIN":"COUT"}, forkargs=forkargs)

    wire(Adders.I0, c.I0)
    wire(Adders.I1, c.I1)

    wire(c.O, Adders.O)

    if cin:
        wire(Adders.CIN, c.CIN)
    else:
        wire(0, c.CIN)

    if cout:
        wire(c.COUT, Adders.COUT)

#
# create an n-bit Adder from n FullAdders
#
# I0:In(Bits(n)), I1:In(Bits(n)), CIN:In(Bit), O:Out(Bits(n)), COUT:Out(Bit)
#
# if cin, CIN is added to the circuit
# if cout: COUT is added to the circuit
#
def DefineAdd(n, cin=False, cout=False):
    class _Add(Circuit):
        name = _AdderName('Add', n, cin, cout)
        IO = _AdderArgs(n, cin, cout)
        @classmethod
        def definition(io):
            def f(y):
                return FullAdder()

            add = braid( col(f, n), foldargs={"CIN":"COUT"})

            wire(io.I0, add.I0)
            wire(io.I1, add.I1)
            if cin:
                wire(io.CIN, add.CIN)
            else:
                wire(0, add.CIN)
            if cout:
                wire(add.COUT, io.COUT)
            wire(add.O, io.O)
    return _Add
    

def DefineSub(n, cin=False, cout=False):
    class _Sub(Circuit):
        name = _AdderName('Sub', n, cin, cout)
        IO = _AdderArgs(n, cin, cout)
        @classmethod
        def definition(io):
            invert = DefineInvert(n)()
            add =  DefineAdd(n, True, cout)()
            wire(io.I0, add.I0)
            wire(io.I1, invert.I)
            wire(invert.O, add.I1)
            wire(add.O, io.O)
            if cin:
                wire( Not()(io.CIN), add.CIN )
            else:
                wire( 1, add.CIN )
            if cout:
                wire(add.COUT, io.COUT)
    return _Sub
    
    

def DefineNegate(width):
    T = Bits[width]
    class _Negate(Circuit):
        name = 'Negate{}'.format(width)
        IO = ['I', In(T), 'O', Out(T)]
        @classmethod
        def definition(io):
            invert = DefineInvert(width)()
            add =  DefineAdd(width, False, False)()
            wire( add( invert(io.I), (array(1,width))), io.O )
    return _Negate
    
