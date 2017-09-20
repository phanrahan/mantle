import os
os.environ['MANTLE_TARGET'] = 'ice40'
from mantle import DefineCounter, DefineAdd
from mantle.lattice.ice40 import SB_LUT4, SB_CARRY, SB_DFF
from magma.passes import InstancePass, DefinitionPass, InstanceGraphPass
from magma.transforms import flatten, setup_clocks

class PrimitivesPass(InstancePass):
    def __init__(self, main):
        super(PrimitivesPass, self).__init__(main)
        self.nluts = 0
        self.ncarrys = 0
        self.ndffs = 0

    def __call__(self, instpath):
        instance = instpath[-1]
        if isinstance(instance, SB_LUT4):
            self.nluts += 1
        elif isinstance(instance, SB_CARRY):
            self.ncarrys += 1
        elif isinstance(instance, SB_DFF):
            self.ndffs += 1

def test_adder():
    add = DefineAdd(8, False, False)
    print(repr(add))
    c = flatten(add).circuit
    print(repr(c))
    p = PrimitivesPass(c).run()
    assert p.nluts == 8

def test_counter():
    Counter8 = DefineCounter(8)
    #print(repr(Counter8))
    p = PrimitivesPass(Counter8).run()
    print('nluts =',p.nluts)
    print('ncarrys =',p.ncarrys)
    print('ndffs =',p.ndffs)

    setup_clocks(Counter8)
    c = flatten(Counter8).circuit
    #print(repr(c))

    q = PrimitivesPass(c).run()
    print('nluts =',q.nluts)
    print('ncarrys =',q.ncarrys)
    print('ndffs =',q.ndffs)
    assert p.nluts == q.nluts
    assert p.ncarrys == q.ncarrys
    assert p.ndffs == q.ndffs

def test_print_instance():
    class PrintInstancePass(InstancePass):
        def __call__(self, path):
            print( ['{} {}.{}'.format(p.defn, type(p), p) for p in path] )
    Counter8 = DefineCounter(8)
    p = PrintInstancePass(Counter8).run()
    print(len(p.instances))
    assert len(p.instances) == 34

def test_print_instance_graph():
    class PrintInstanceGraphPass(InstanceGraphPass):
        def __call__(self, definition, dependencies):
            print(definition, list(map(str, dependencies)))
    Counter8 = DefineCounter(8)
    p = PrintInstanceGraphPass(Counter8).run()
    print(len(p.tsortedgraph))
    assert len(p.tsortedgraph) == 7

#test_print_instance()
#test_print_instance_graph()

