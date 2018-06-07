from magma import *
from .RAM import RAM16D, RAM64Q

__all__ = ['RAM16DxN', 'RAM64Q']

def _RAMName(name, n):
    return name + '%d' % n

RAMCache = {}

def def_RAM16DxN(n, init=0):

    name = _RAMName('RAM16D_', n)
    if name in RAMCache:
         return RAMCache[name]

    ArrayN = Array(n, Bit)
    args =  ["input A0",  Array4,
             "input A1",  Array4,
             "output O0", ArrayN,
             "output O1", ArrayN,
             "input I",   ArrayN,
             "input WE",  Bit,
             "input CLK", Bit]

    define = DefineCircuit(name, *args)

    def ram16d(y):
        # fix init
        return RAM16D(0)

    ram = braid(col(ram16d, n), forkargs=['A0', 'A1', 'WE'])

    ram(define.A0, define.A1, define.I, define.WE)
    wire( ram.O0, define.O0 )
    wire( ram.O1, define.O1 )

    EndCircuit()

    RAMCache[name] = define
    return define

def RAM16DxN(n, init=0):
    return def_RAM16DxN(n, init=init)()

def def_RAM64QxN(n, init=0):
    name = _RAMName('RAM64Q_', n)
    if name in RAMCache:
        return RAMCache[name]

    ArrayN = Array(n, Bit)
    Array6 = Array(6, Bit)
    args = ["input A0", Array6,
            "input A1", Array6,
            "input A2", Array6,
            "input A3", Array6,
            "output O0", ArrayN,
            "output O1", ArrayN,
            "output O2", ArrayN,
            "output O3", ArrayN,
            "input I", ArrayN,
            "input WE", Bit,
            "input CLK", Bit]
    define = DefineCircuit(name, *args)

    def ram64q(y):
        # fix init
        return RAM64Q(0)

    ram = braid(col(ram64q, n), forkargs=['A0', 'A1', 'A2', 'A3', 'WE'])

    ram(define.A0, define.A1, define.A2, define.A3, define.I, define.WE)
    wire(ram.OA, define.O0)
    wire(ram.OB, define.O1)
    wire(ram.OC, define.O2)
    wire(ram.OD, define.O3)

    EndCircuit()
    RAMCache[name] = define
    return define

def RAM64QxN(n, init = 0):
    return def_RAM64QxN(n, init=init)()


