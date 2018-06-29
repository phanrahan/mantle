from collections import namedtuple
import pytest
import magma
import mantle

HEIGHTS = [2]
WIDTHS = [2,4]

op = namedtuple("op", ["name", "func"])

def com(Test, name):
    import magma
    from magma import compile
    from magma.testing import check_files_equal
    name = f'test_{magma.mantle_target}_{name}'
    build = 'build/' + name
    gold = 'gold/' + name
    compile(build, Test)
    #assert check_files_equal(__file__, build+'.v', gold+'.v')

def sim(Test, TestFun):
    return
    from magma.testing.newfunction import testvectors as funtest
    from magma.simulator.python_simulator import testvectors as simtest
    tvsim = simtest(Test)
    tvfun = funtest(Test, TestFun)
    assert tvsim == tvfun


@pytest.mark.skipif(magma.mantle_target == 'coreir',   reason='NYI')
@pytest.mark.skipif(magma.mantle_target == 'spartan3', reason='NYI')
@pytest.mark.skipif(magma.mantle_target == 'spartan6', reason='NYI')
def test_lut1():
    test = mantle.LUT1([0,1])
    assert 'AnonymousCircuitType("I0", .I0, "O", .O)' == repr(test)

@pytest.mark.skipif(magma.mantle_target == 'coreir',   reason='NYI')
@pytest.mark.skipif(magma.mantle_target == 'spartan3', reason='NYI')
@pytest.mark.skipif(magma.mantle_target == 'spartan6', reason='NYI')
def test_lut2():
    test = mantle.LUT2([0,0,0,1])
    assert 'AnonymousCircuitType("I0", .I0, "I1", .I1, "O", .O)' == repr(test)

@pytest.mark.skipif(magma.mantle_target == 'coreir',   reason='NYI')
@pytest.mark.skipif(magma.mantle_target == 'spartan3', reason='NYI')
@pytest.mark.skipif(magma.mantle_target == 'spartan6', reason='NYI')
def test_lut3():
    test = mantle.LUT3([0, 0, 0, 0, 0,0,0,1])
    assert 'AnonymousCircuitType("I0", .I0, "I1", .I1, "I2", .I2, "O", .O)' == repr(test)

@pytest.mark.skipif(magma.mantle_target == 'coreir',   reason='NYI')
@pytest.mark.skipif(magma.mantle_target == 'spartan3', reason='NYI')
@pytest.mark.skipif(magma.mantle_target == 'spartan6', reason='NYI')
def test_lut4():
    test = mantle.LUT4(15*[0] + [1])
    # this is only correct for ice40
    assert ' = SB_LUT4(LUT_INIT=0x8000)' == repr(test)

@pytest.mark.skipif(magma.mantle_target == 'coreir',   reason='NYI')
def test_mux2():
    Test = mantle.Mux2
    sim( Test, lambda i, s: (i>>s)&1 )
    com( Test, 'mux2' )

@pytest.mark.skipif(magma.mantle_target == 'coreir',   reason='NYI')
def test_mux4():
    Test = mantle.Mux4
    sim( Test, lambda i, s: (i>>s)&1 )
    com( Test, 'mux4' )

@pytest.mark.skipif(magma.mantle_target == 'coreir',   reason='NYI')
def test_mux8():
    Test = mantle.Mux8
    sim( Test, lambda i, s: (i>>s)&1 )
    com( Test, 'mux8' )

# this test if very expensive becuase it tests all possible inputs
@pytest.mark.skip
def test_mux16():
    Test = mantle.Mux16
    sim( Test, lambda i, s: (i>>s)&1 )
    com( Test, 'mux16' )

@pytest.mark.parametrize("height", HEIGHTS)
@pytest.mark.parametrize("width", WIDTHS)
def test_mux(height, width):
    Test = mantle.DefineMux(height,width)
    sim( Test, lambda i0, i1, s: i1 if s else i0 )
    com( Test, f'mux{height}x{width}' )

@pytest.mark.skip
def test_not():
    Test = mantle.Not
    sim( Test, lambda x: not x )
    com( Test, 'not' )

@pytest.mark.skipif(magma.mantle_target == 'spartan3', reason='NYI')
@pytest.mark.skipif(magma.mantle_target == 'spartan6', reason='NYI')
@pytest.mark.parametrize("op", [
    op('DefineReduceAnd', lambda x: x),
    op('DefineReduceNAnd', lambda x: x),
    op('DefineReduceOr',  lambda x: x),
    op('DefineReduceNOr',  lambda x: x),
    op('DefineReduceXOr',  lambda x: x),
    op('DefineReduceNXOr',  lambda x: x),
    op('DefineInvert',  lambda x: ~x)
])
@pytest.mark.parametrize("height", HEIGHTS)
def test_logic(op, height):
    Define = getattr(mantle, op.name)
    Test = Define(height, height)
    sim( Test, op.func )
    com( Test, f'{op.name}{height}' )

@pytest.mark.skipif(magma.mantle_target == 'spartan3', reason='NYI')
@pytest.mark.skipif(magma.mantle_target == 'spartan6', reason='NYI')
@pytest.mark.parametrize("op", [
    op('DefineAnd', lambda x, y: x&y),
    op('DefineNAnd', lambda x, y: ~(x&y)),
    op('DefineOr',  lambda x, y: x|y),
    op('DefineNOr',  lambda x, y: ~(x|y)),
    op('DefineXOr',  lambda x, y: ~(x^y)),
    op('DefineNXOr',  lambda x, y: ~(x^y))
])
@pytest.mark.parametrize("height", HEIGHTS)
@pytest.mark.parametrize("width", WIDTHS)
def test_logic(op, height, width):
    Define = getattr(mantle, op.name)
    Test = Define(height, width)
    sim( Test, op.func )
    com( Test, f'{op.name}{height}x{width}' )

def test_ha():
    pass

def test_fa():
    pass

@pytest.mark.parametrize("op", [
    op('DefineAdd', lambda x, y: x+y),
    op('DefineSub', lambda x, y: x-y),
    op('DefineNegate', lambda x: -x),
    op('DefineEQ', lambda x, y: x==y),
    op('DefineNE', lambda x, y: x!=y),
    op('DefineUGT', lambda x, y: x>y),
    op('DefineUGE', lambda x, y: x>=y),
    op('DefineULT', lambda x, y: x<y),
    op('DefineULE', lambda x, y: x<=y),
    op('DefineSGT', lambda x, y: x>y),
    op('DefineSGE', lambda x, y: x>=y),
    op('DefineSLT', lambda x, y: x<y),
    op('DefineSLE', lambda x, y: x<=y)
])
@pytest.mark.parametrize("width", WIDTHS)
def test_arith(op, width):
    Define = getattr(mantle, op.name)
    Test = Define(width)
    sim( Test, op.func )
    com( Test, f'{op.name}{width}' )

@pytest.mark.skipif(magma.mantle_target == 'coreir',   reason='NYI')
@pytest.mark.parametrize("op", [
    op('DefineASR', lambda x, y: x>>y),
    op('DefineLSR', lambda x, y: x>>y),
    op('DefineLSL', lambda x, y: x<<y)
])
@pytest.mark.parametrize("width", WIDTHS)
def test_shift(op, width):
    Define = getattr(mantle, op.name)
    for shift in range(width):
        Test = Define(width, shift)
        sim( Test, lambda x: op.func(x,shift) )
        com( Test, f'{op.name}{width}x{shift}' )


