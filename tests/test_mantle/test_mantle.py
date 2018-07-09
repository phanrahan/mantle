from collections import namedtuple
import pytest
import magma
import mantle

HEIGHTS = [2, 4, 8]
WIDTHS = [2, 4, 8]

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


def test_lut1():
    target = magma.mantle_target
    if target == 'coreir':
        test = mantle.LUT([0,1], 1)
    else:
        test = mantle.LUT1([0,1])
    if target == 'spartan3' or target == 'spartan6':
        assert ' = LUT1(INIT=0x2)' == repr(test)
    elif target == 'ice40':
        assert 'AnonymousCircuitType("I0", .I0, "O", .O)' == repr(test)
    elif target == 'coreir':
        assert ' = LUT1_2()' == repr(test)


def test_lut2():
    target = magma.mantle_target
    if target == 'coreir':
        test = mantle.LUT([0,0,0,1], 2)
    else:
        test = mantle.LUT2([0,0,0,1])
    if target == 'spartan3' or target == 'spartan6':
        assert ' = LUT2(INIT=0x8)' == repr(test)
    elif target == 'ice40':
        assert 'AnonymousCircuitType("I0", .I0, "I1", .I1, "O", .O)' == repr(test)
    elif target == 'coreir':
        assert ' = LUT2_8()' == repr(test)

def test_lut3():
    target = magma.mantle_target
    if target == 'coreir':
        test = mantle.LUT([0, 0, 0, 0, 0,0,0,1], 3)
    else:
        test = mantle.LUT3([0, 0, 0, 0, 0,0,0,1])
    if target == 'spartan3' or target == 'spartan6':
        assert ' = LUT3(INIT=0x80)' == repr(test)
    elif target == 'ice40':
        assert 'AnonymousCircuitType("I0", .I0, "I1", .I1, "I2", .I2, "O", .O)' == repr(test)
    elif target == 'coreir':
        assert ' = LUT3_128()' == repr(test)

def test_lut4():
    target = magma.mantle_target
    if target == 'coreir':
        test = mantle.LUT(15*[0] + [1], 4)
    else:
        test = mantle.LUT4(15*[0] + [1])
    if target == 'spartan3' or target == 'spartan6':
        assert ' = LUT4(INIT=0x8000)' == repr(test)
    elif target == 'ice40':
        assert ' = SB_LUT4(LUT_INIT=0x8000)' == repr(test)
    elif target == 'coreir':
        assert ' = LUT4_32768()' == repr(test)

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
@pytest.mark.skipif(magma.mantle_target == 'coreir',   reason='NYI')
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

def test_not():
    Test = mantle.Not
    sim( Test, lambda x: not x )
    com( Test, 'not' )

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
    Test = mantle.HalfAdder
    #sim( Test, None)
    com( Test, 'ha' )

def test_fa():
    Test = mantle.FullAdder
    #sim( Test, None)
    com( Test, 'fa' )

@pytest.mark.parametrize("op", [
    op('DefineAdd', lambda x, y: x+y),
    op('DefineSub', lambda x, y: x-y),
])
@pytest.mark.parametrize("cin", [False, True])
@pytest.mark.parametrize("cout", [False, True])
@pytest.mark.parametrize("width", WIDTHS)
def test_arith(op, cin, cout, width):
    Define = getattr(mantle, op.name)
    Test = Define(width, cin=cin, cout=cout)
    sim( Test, op.func )
    com( Test, f'{op.name}{width}{"_cin" if cin else ""}{"_cout" if cout else ""}' )

@pytest.mark.parametrize("width", WIDTHS)
def test_negate(width):
    Define = mantle.Negate
    Test = Define(width)
    sim( Test, op.func )
    com( Test, f'Negate{width}' )

@pytest.mark.parametrize("op", [
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
def test_compare(op, width):
    Define = getattr(mantle, op.name)
    Test = Define(width)
    sim( Test, op.func )
    com( Test, f'{op.name}{width}' )

@pytest.mark.skipif(magma.mantle_target == 'coreir',   reason='NYI')
@pytest.mark.skipif(magma.mantle_target == 'ice40',    reason='NYI')
@pytest.mark.skipif(magma.mantle_target == 'spartan3', reason='NYI')
@pytest.mark.skipif(magma.mantle_target == 'spartan6', reason='NYI')
@pytest.mark.parametrize("op", [
    op('DefineASR', lambda x, y: x>>y),
    op('DefineLSR', lambda x, y: x>>y),
    op('DefineLSL', lambda x, y: x<<y)
])
@pytest.mark.parametrize("width", WIDTHS)
def test_shift(op, width):
    Define = getattr(mantle, op.name)
    for shift in range(width):
        Test = Define(width)
        sim( Test, lambda x, y: op.func(x,y) )
        com( Test, f'{op.name}{width}' )

@pytest.mark.skipif(magma.mantle_target == 'coreir',   reason='NYI')
def test_dff():
    DFF = mantle.DFF
    Test = DFF()
    #sim( Test, op.func)
    com( Test, 'DFF' )

@pytest.mark.skipif(magma.mantle_target == 'coreir',   reason='NYI')
@pytest.mark.parametrize("op", [
    op('SRFF', lambda x: x),
    op('RSFF', lambda x: x),
    op('JKFF', lambda x: x),
    op('TFF',  lambda x: x),
])
def test_ff(op):
    FF = getattr(mantle, op.name)
    Test = FF()
    #sim( Test, op.func)
    com( Test, f'{op.name}' )

@pytest.mark.parametrize("op", [
    op('DefineRegister', lambda x: x),
    op('DefineSISO',     lambda x: x),
    op('DefinePISO',     lambda x: x),
    op('DefineSISO',     lambda x: x),
    op('DefinePISO',     lambda x: x),
    op('DefineRing',     lambda x: x),
    op('DefineJohnson',  lambda x: x),
    op('DefineDecoder',  lambda x: x),
    op('DefineEncoder',  lambda x: x),
    op('DefineArbiter',  lambda x: x),
    op('DefineCounter',  lambda x: x),
    op('DefineCounterLoad',  lambda x: x)
])
@pytest.mark.parametrize("width", WIDTHS)
def test_decode(op, width):
    Define = getattr(mantle, op.name)
    Test = Define(width)
    #sim( Test, op.func)
    com( Test, f'{op.name}{width}' )

