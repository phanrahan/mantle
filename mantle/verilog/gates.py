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
        l.append('')
        l.append(In(Bit))
    return l

def DefineAnd(n=2):
    return DeclareCircuit(*(['and', '', Out(Bit)] + ins(n)))

def And(n=2):
    return DefineAnd(n)()


def DefineNAnd(n=2):
    return DeclareCircuit(*(['nand', '', Out(Bit)] + ins(n)))

def NAnd(n=2):
    return DefineNAnd(n)()


def DefineOr(n=2):
    return DeclareCircuit(*(['or', '', Out(Bit)] + ins(n)))

def Or(n=2):
    return DefineOr(n)()


def DefineNOr(n=2):
    return DeclareCircuit(*(['nor', '', Out(Bit)] + ins(n)))

def NOr(n=2):
    return DefineNOr(n)()


def DefineXOr(n=2):
    return DeclareCircuit(*(['xor', '', Out(Bit)] + ins(n)))

def XOr(n=2):
    return DefineXOr(n)()


def DefineNXOr(n=2):
    return DeclareCircuit(*(['nxor', '', Out(Bit)] + ins(n)))

def NXOr(n=2):
    return DefineNXOr(n)()


Not = DeclareCircuit('not', '', Out(Bit), '', In(Bit))
Buf = DeclareCircuit('buf', '', Out(Bit), '', In(Bit))



