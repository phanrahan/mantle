from magma import *

__all__  = ['And']
__all__ += ['NAnd']
__all__ += ['Or']
__all__ += ['NOr']
__all__ += ['XOr']
__all__ += ['NXOr']
__all__ += ['Not']
__all__ += ['Buf']

def ins(n=2):
    l = []
    for i in range(n):
        l.append('input')
        l.append(In(Bit))
    return l

def DefineAnd(n=2):
    return DeclareCircuit(*(['and', 'output', Out(Bit)] + ins(n)))

def And(n=2):
    return DefineAnd(n)()


def DefineNAnd(n=2):
    return DeclareCircuit(*(['nand', 'output', Out(Bit)] + ins(n)))

def NAnd(n=2):
    return DefineNAnd(n)()


def DefineOr(n=2):
    return DeclareCircuit(*(['or', 'output', Out(Bit)] + ins(n)))

def Or(n=2):
    return DefineOr(n)()


def DefineNOr(n=2):
    return DeclareCircuit(*(['nor', 'output', Out(Bit)] + ins(n)))

def NOr(n=2):
    return DefineNOr(n)()


def DefineXOr(n=2):
    return DeclareCircuit(*(['xor', 'output', Out(Bit)] + ins(n)))

def XOr(n=2):
    return DefineXOr(n)()


def DefineNXOr(n=2):
    return DeclareCircuit(*(['nxor', 'output', Out(Bit)] + ins(n)))

def NXOr(n=2):
    return DefineNXOr(n)()


Not = DeclareCircuit('not', 'output', Out(Bit), 'input', In(Bit))
Buf = DeclareCircuit('buf', 'output', Out(Bit), 'input', In(Bit))



