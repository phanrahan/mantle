import operator
from magma import *
import gates

__all__  = ['And', 'And2', 'And3', 'And4']
__all__ += ['NAnd', 'NAnd2', 'NAnd3', 'NAnd4']
__all__ += ['Or', 'Or2', 'Or3', 'Or4']
__all__ += ['NOr', 'NOr2', 'NOr3', 'NOr4']
__all__ += ['Xor', 'Xor2', 'Xor3', 'Xor4']
__all__ += ['NXor', 'NXor2', 'NXor3', 'NXor4']

__all__ += ['AndN']
__all__ += ['NAndN']
__all__ += ['OrN']
__all__ += ['NOrN']
__all__ += ['XorN']
__all__ += ['NXorN']

__all__ += ['Not']
__all__ += ['Buf']

def flatten(l):
    return reduce(operator.add, l)

def Op1(op):
    op = op()
    I = In(Bit)()
    O = Out(Bit)()
    op(I)
    wire(op, O)
    return AnonymousCircuit("I", I, "O", O)

def Op(n, op):
    op = op(n)
    I = [In(Bit)() for i in range(n)]
    O = Out(Bit)()
    op(*I)
    wire(op, O)
    args = flatten([["I%d"%i, I[i]] for i in range(n)])
    args += ["O", O]
    return AnonymousCircuit(*args)

def OpN(n, op):
    op = op(n)
    I = In(Array(n, Bit))()
    O = Out(Bit)()
    op(*[I[i] for i in range(n)])
    wire(op, O)
    return AnonymousCircuit("I", I, "O", O)

def DefineOp(opname, op, height, width):
    """     
    Generate module
        
    I0 : Array(width, Bit), I1 : Array(n, Bit) -> O : Array(n, Bit)
    """
        
    T = Array(width, Bit)
    class _Op(Circuit):
        assert height > 1 and height <= 4

        name = '%s%dx%d' % (opname, height, width)

        if   height == 2:
            IO  = ['I0', In(T), 'I1', In(T)]
        elif height == 3:
            IO  = ['I0', In(T), 'I1', In(T), 'I2', In(T)]
        elif height == 4:
            IO  = ['I0', In(T), 'I1', In(T), 'I2', In(T), 'I3', In(T)]
        IO  += ['O', Out(T)]

        @classmethod
        def definition(def_):
            def opm(y):
                return op(height)
            opmxn = join(col(opm, width))
            wire(def_.I0, opmxn.I0)
            wire(def_.I1, opmxn.I1)
            wire(opmxn.O, def_.O)

    return _Op




def _And(n):
    return Op(n, gates.And)

def And2():
    return _And(2)

def And3():
    return _And(3)

def And4():
    return _And(4)

def AndN(n):
    return OpN(n, gates.And)

def And(height, width=2, **kwargs):
    return DefineOp('And', _And, height, width)(**kwargs)


def _NAnd(n):
    return Op(n, gates.NAnd)

def NAnd2():
    return _NAnd(2)

def NAnd3():
    return _NAnd(3)

def NAnd4():
    return _NAnd(4)

def NAndN(n):
    return OpN(n, gates.NAnd)

def NAnd(height, width=2, **kwargs):
    return DefineOp('NAnd', _NAnd, height, width)(**kwargs)


def _Or(n):
    return Op(n, gates.Or)

def Or2():
    return _Or(2)

def Or3():
    return _Or(3)

def Or4():
    return _Or(4)

def OrN(n):
    return OpN(n, gates.Or)

def Or(height, width=2, **kwargs):
    return DefineOp('Or', _Or, height, width)(**kwargs)


def _NOr(n):
    return Op(n, gates.NOr)

def NOr2():
    return _NOr(2)

def NOr3():
    return _NOr(3)

def NOr4():
    return _NOr(4)

def NOrN(n):
    return OpN(n, gates.NOr)

def NOr(height, width=2, **kwargs):
    return DefineOp('NOr', _NOr, height, width)(**kwargs)


def _Xor(n):
    return Op(n, gates.Xor)

def Xor2():
    return _Xor(2)

def Xor3():
    return _Xor(3)

def Xor4():
    return _Xor(4)

def XorN(n):
    return OpN(n, gates.Xor)

def Xor(height, width=2, **kwargs):
    return DefineOp('Xor', _Xor, height, width)(**kwargs)


def _NXor(n):
    return Op(n, gates.NXor)

def NXor2():
    return _NXor(2)

def NXor3():
    return _NXor(3)

def NXor4():
    return _NXor(4)

def NXorN(n):
    return OpN(n, gates.NXor)

def NXor(height, width=2, **kwargs):
    return DefineOp('NXor', _NXor, height, width)(**kwargs)


def Buf():
    return Op1(gates.Buf)

def Not():
    return Op1(gates.Not)


