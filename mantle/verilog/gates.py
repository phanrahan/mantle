from magma import *

__all__  = ['And']
__all__ += ['NAnd']
__all__ += ['Or']
__all__ += ['NOr']
__all__ += ['Xor']
__all__ += ['NXor']

__all__ += ['Not']
__all__ += ['Buf']

def ins(n):
    l = []
    for i in range(n):
        #l.append('input in%d' % (i+1))
        l.append('input')
        l.append(In(Bit))
    return l

def DefineAnd(n):
    return DeclareCircuit(*(['and', 'output', Out(Bit)] + ins(n)))

def And(n):
    return DefineAnd(n)()


def DefineNAnd(n):
    return DeclareCircuit(*(['nand', 'output', Out(Bit)] + ins(n)))

def NAnd(n):
    return DefineNAnd(n)()


def DefineOr(n):
    return DeclareCircuit(*(['or', 'output', Out(Bit)] + ins(n)))

def Or(n):
    return DefineOr(n)()


def DefineNOr(n):
    return DeclareCircuit(*(['nor', 'output', Out(Bit)] + ins(n)))

def NOr(n):
    return DefineNOr(n)()


def DefineXor(n):
    return DeclareCircuit(*(['xor', 'output', Out(Bit)] + ins(n)))

def Xor(n):
    return DefineXor(n)()


def DefineNXor(n):
    return DeclareCircuit(*(['nxor', 'output', Out(Bit)] + ins(n)))

def NXor(n):
    return DefineNXor(n)()



DefineNot = DeclareCircuit('not', 'output', Out(Bit), 'input', In(Bit))

def Not():
    return DefineNot()


DefineBuf = DeclareCircuit('buf', 'output', Out(Bit), 'input', In(Bit))

def Buf():
    return DefineBuf()



