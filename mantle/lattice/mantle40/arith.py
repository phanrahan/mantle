from magma import *
from .logic import Invert, Not
from .fulladder import FullAdder

__all__  = ['DefineAdd', 'Add'] 
__all__ += ['DefineSub', 'Sub']
__all__ += ['DefineNegate', 'Negate']
__all__ += ['DefineASR', 'ASR']

def _AdderName(basename, n, cin, cout):
    return "{}{}{}{}".format(
        basename, n,
        "Cin"  if cin  else "",
        "Cout" if cout else ""
    )

def _AdderArgs(n, cin, cout):
    T = Bits(n)

    args = ["I0", In(T), "I1", In(T)]
    if cin:
        args += ['CIN', In(Bit)]

    args += ["O", Out(T)]
    if cout:
        args += ['COUT', Out(Bit)]

    return args

def DefineAdders(name, n, cin, cout, forkargs=[]):

    def f(y):
        return FullAdder(loc=(0,y//8, y%8))

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
@cache_definition
def DefineAdd(n, cin=False, cout=False):
    class _Add(Circuit):
        name = _AdderName('Add', n, cin, cout)
        IO = _AdderArgs(n, cin, cout)
        @classmethod
        def definition(io):
            def f(y):
                return FullAdder(loc=(0,y//8, y%8))

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

def Add(n, cin=False, cout=False, **kwargs):
    return DefineAdd(n, cin, cout)(**kwargs)
    

@cache_definition
def DefineSub(n, cin=False, cout=False):
    class _Sub(Circuit):
        name = _AdderName('Sub', n, cin, cout)
        IO = _AdderArgs(n, cin, cout)
        @classmethod
        def definition(io):
            invert = Invert(n)
            add =  Add(n, True, cout)
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

def Sub(n, cin=False, cout=False, **kwargs):
    return DefineSub(n, cin, cout)(**kwargs)
    
    

@cache_definition
def DefineNegate(width):
    T = Bits(width)
    class _Negate(Circuit):
        name = 'Negate{}'.format(width)
        IO = ['I', In(T), 'O', Out(T)]
        @classmethod
        def definition(io):
            invert = Invert(width)
            add =  Add(width, False, False)
            wire( add( invert(io.I), (array(1,width))), io.O )
    return _Negate

def Negate(width, **kwargs):
    return DefineNegate(width)(**kwargs)
    

@cache_definition
def DefineFixedASR(width, shift):
    T = Bits(width)
    class _ASR(Circuit):
        name = 'FixedASR{}_{}'.format(width, shift)

        IO = ["I", In(T), "O", Out(T)]

        @classmethod
        def definition(io):
            for i in range(0, width - shift):
                wire(io.I[i + shift], io.O[i])
            for i in range(width - shift, width):
                wire(io.I[width-1], io.O[i])
    return _ASR

def FixedASR(width, shift, **kwargs):
    return DefineFixedASR(width, shift)(**kwargs)

DefineASR = DefineFixedASR
ASR = FixedASR
    
