import magma
magma.set_mantle_target('ice40')

from mantle.lattice.mantle40 import Mux2, Mux4, Mux8, Mux16, DefineMux

def sim(Test, TestFun):
    from magma.simulator.python_simulator import testvectors as simtest
    from magma.testing.newfunction import testvectors as funtest
    tvsim = simtest(Test)
    print(tvsim)
    tvfun = funtest(Test, TestFun)
    print(tvfun)
    assert tvsim == tvfun

def com(Test, name):
    from magma import compile
    from magma.testing import check_files_equal
    name = 'test_{}'.format(name)
    build = 'build/' + name
    gold = 'gold/' + name
    compile(build, Test)
    assert check_files_equal(__file__, build+'.v', gold+'.v')

def test_mux2():
    Test = Mux2
    sim( Test, lambda i, s: (i>>s)&1 )
    com( Test, 'mux2' )

def test_mux4():
    Test = Mux4
    sim( Test, lambda i, s: (i>>s)&1 )
    com( Test, 'mux4' )

def test_mux8():
    Test = Mux8
    sim( Test, lambda i, s: (i>>s)&1 )
    com( Test, 'mux8' )

#takes too long!
#
#def test_mux16():
#    Test = Mux16
#    sim( Test, lambda i, s: (i>>s)&1 )
#    com( Test, 'mux16' )

def test_mux():
    Test = DefineMux(2,2)
    sim( Test, lambda i0, i1, s: i1 if s else i0 )
    com( Test, 'mux2x2' )

