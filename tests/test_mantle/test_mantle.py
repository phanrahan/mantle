import re
from collections import namedtuple
import operator
import pytest
import magma as m
import magma

if magma.mantle_target == "coreir":
    output = "coreir"
    suffix = ".json"
else:
    output = "verilog"
    suffix = ".v"
    

import mantle
from fault.test_vectors import generate_function_test_vectors, \
    generate_simulator_test_vectors
from ..test_coreir.util import wrap

HEIGHTS = [2, 4, 8]
WIDTHS = [2, 4, 8]

op = namedtuple("op", ["name", "func"])

def com(Test, name):
    import magma
    from magma import compile
    from magma.testing import check_files_equal
    name = f'{name}_{magma.mantle_target}'
    build = 'build/' + name
    gold = 'gold/' + name
    if magma.is_primitive.isprimitive(Test):
        Test = wrap(Test)
    compile(build, Test, output=output)
    assert check_files_equal(__file__, build+suffix, gold+suffix)
    if output == "coreir":
        # Check verilog compile through coreir
        compile(build + "-verilog", Test, output="coreir-verilog")
        assert check_files_equal(__file__, build + "-verilog.v", gold +
                                 "-verilog.v")
        # Test inline code path
        compile(build + "-verilog-inline", Test, output="coreir-verilog",
                inline=True)
        assert check_files_equal(__file__, build + "-verilog-inline.v", gold +
                                 "-verilog-inline.v")

def sim(Test, TestFun):
    if TestFun is None:
         return
    if magma.mantle_target in ['spartan3', 'spartan6']:
         return
    tvsim = generate_simulator_test_vectors(Test)
    tvfun = generate_function_test_vectors(Test, TestFun)
    assert tvsim == tvfun


def strip_anonymous_circuits(string):
    # These names are generated based on the object ID so they change between
    # test runs
    return re.sub(r'AnonymousCircuitType[0-9]+', '', string)


def test_lut1():
    target = magma.mantle_target
    class Main(m.Circuit):
        if target == 'coreir':
            test = mantle.LUT([0,1], 1)
        else:
            test = mantle.LUT1([0,1])
        if target == 'spartan3' or target == 'spartan6':
            assert 'LUT1(INIT=0x2)' == repr(test)
        elif target == 'ice40':
            assert 'AnonymousCircuitType("I0", .I0, "O", .O)' == strip_anonymous_circuits(repr(test))
        elif target == 'coreir':
            assert 'LUT1_2()' == repr(test)


def test_lut2():
    target = magma.mantle_target
    class Main(m.Circuit):
        if target == 'coreir':
            test = mantle.LUT([0,0,0,1], 2)
        else:
            test = mantle.LUT2([0,0,0,1])
        if target == 'spartan3' or target == 'spartan6':
            assert 'LUT2(INIT=0x8)' == repr(test)
        elif target == 'ice40':
            assert 'AnonymousCircuitType("I0", .I0, "I1", .I1, "O", .O)' == strip_anonymous_circuits(repr(test))
        elif target == 'coreir':
            assert 'LUT2_8()' == repr(test)

def test_lut3():
    target = magma.mantle_target
    class Main(m.Circuit):
        if target == 'coreir':
            test = mantle.LUT([0, 0, 0, 0, 0,0,0,1], 3)
        else:
            test = mantle.LUT3([0, 0, 0, 0, 0,0,0,1])
        if target == 'spartan3' or target == 'spartan6':
            assert 'LUT3(INIT=0x80)' == repr(test)
        elif target == 'ice40':
            assert 'AnonymousCircuitType("I0", .I0, "I1", .I1, "I2", .I2, "O", .O)' == strip_anonymous_circuits(repr(test))
        elif target == 'coreir':
            assert 'LUT3_128()' == repr(test)

def test_lut4():
    target = magma.mantle_target
    class Main(m.Circuit):
        if target == 'coreir':
            test = mantle.LUT(15*[0] + [1], 4)
        else:
            test = mantle.LUT4(15*[0] + [1])
        if target == 'spartan3' or target == 'spartan6':
            assert 'LUT4(INIT=0x8000)' == repr(test)
        elif target == 'ice40':
            assert 'SB_LUT4(LUT_INIT=0x8000)' == repr(test)
        elif target == 'coreir':
            assert 'LUT4_32768()' == repr(test)

def test_mux2():
    Test = mantle.Mux2
    #sim( Test, lambda i, s: i[s] )
    com( Test, 'mux2' )

def test_mux4():
    Test = mantle.Mux4
    #sim( Test, lambda i, s: i[s] )
    com( Test, 'mux4' )

def test_mux8():
    Test = mantle.Mux8
    #sim( Test, lambda i, s: i[s] )
    com( Test, 'mux8' )

# this test if very expensive becuase it tests all possible inputs
@pytest.mark.skip
def test_mux16():
    Test = mantle.Mux16
    #sim( Test, lambda i, s: i[s] )
    com( Test, 'mux16' )

@pytest.mark.parametrize("height", HEIGHTS)
@pytest.mark.parametrize("width", WIDTHS)
def test_mux(height, width):
    Test = mantle.DefineMux(height,width)
    #sim( Test, None )
    com( Test, f'mux{height}x{width}' )

def test_not():
    if magma.mantle_target == "coreir":
        pytest.skip("Not circuit is wrapper around coreir declaration, cannot compile")
    if magma.mantle_target in ["spartan3", "spartan6", "ice40"]:
        pytest.skip("Not circuit is function, cannot compile")
    Test = mantle.Not
    #sim( Test, operator.invert )
    com( Test, 'not' )

@pytest.mark.parametrize("op", [
    op('DefineReduceAnd',  None),
    op('DefineReduceNAnd', None),
    op('DefineReduceOr',   None),
    op('DefineReduceNOr',  None),
    op('DefineReduceXOr',  None),
    op('DefineReduceNXOr',  None),
    op('DefineInvert',  operator.invert)
])
@pytest.mark.parametrize("height", HEIGHTS)
def test_logic(op, height):
    Define = getattr(mantle, op.name)
    Test = Define(height, height)
    #sim( Test, op.func )
    com( Test, f'{op.name}{height}' )

@pytest.mark.parametrize("op", [
    op('DefineAnd',  lambda x, y: x&y),
    #op('DefineNAnd', lambda x, y: ~(x&y)),
    op('DefineOr',   lambda x, y: x|y),
    #op('DefineNOr',  lambda x, y: ~(x|y)),
    op('DefineXOr',  lambda x, y: x^y),
    #op('DefineNXOr',  lambda x, y: ~(x^y))
])
@pytest.mark.parametrize("height", HEIGHTS)
@pytest.mark.parametrize("width", WIDTHS)
def test_logic(op, height, width):
    Define = getattr(mantle, op.name)
    Test = Define(height, width)
    if height == 2 and width == 2:
        if magma.is_primitive.isprimitive(Test):
            Test = wrap(Test)
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
    op('DefineAdd', operator.add),
    op('DefineSub', operator.sub),
])
@pytest.mark.parametrize("cin", [False, True])
@pytest.mark.parametrize("cout", [False, True])
@pytest.mark.parametrize("width", WIDTHS)
def test_arith(op, cin, cout, width):
    Define = getattr(mantle, op.name)
    Test = Define(width, cin=cin, cout=cout)
    #sim( Test, op.func )
    com( Test, f'{op.name}{width}{"_cin" if cin else ""}{"_cout" if cout else ""}' )

@pytest.mark.parametrize("width", WIDTHS)
def test_negate(width):
    if magma.mantle_target in ["spartan6", "ice40", "coreir", "spartan3"]:
        pytest.skip("Negate circuits are wrappers around declarations, cannot compile")
    class Main(m.Circuit):
        Define = mantle.Negate
        Test = Define(width)
        #sim( Test, operator.neg)
        com( Test, f'Negate{width}' )

@pytest.mark.parametrize("op", [
    op('DefineEQ',  operator.eq),
    op('DefineNE',  operator.ne),
    op('DefineUGT', operator.gt),
    op('DefineUGE', operator.ge),
    op('DefineULT', operator.lt),
    op('DefineULE', operator.le),
    op('DefineSGT', operator.gt),
    op('DefineSGE', operator.ge),
    op('DefineSLT', operator.lt),
    op('DefineSLE', operator.le)
])
@pytest.mark.parametrize("width", WIDTHS)
def test_compare(op, width):
    Define = getattr(mantle, op.name)
    Test = Define(width)
    #sim( Test, op.func )
    com( Test, f'{op.name}{width}' )

@pytest.mark.parametrize("op", [
    op('DefineASR', operator.rshift),
    op('DefineLSR', operator.rshift),
    op('DefineLSL', operator.lshift),
    #op('DefineROL', None),
    #op('DefineROR', None)
])
@pytest.mark.parametrize("width", WIDTHS)
def test_shift(op, width):
    if magma.mantle_target == "coreir":
        pytest.skip("Shift operators are wrappers around coreir declarations, cannot compile")
    Define = getattr(mantle, op.name)
    Test = Define(width)
    #sim( Test, op.func )
    com( Test, f'{op.name}{width}' )

@pytest.mark.skipif(magma.mantle_target == 'coreir',   reason='NYI')
def test_dff():
    if magma.mantle_target in ["spartan6", "ice40", "spartan3"]:
        pytest.skip("DFF circuits are wrappers around declarations, cannot compile")
    class Main(m.Circuit):
        DFF = mantle.DFF
        Test = DFF()
        #sim( Test, None)
        com( Test, 'DFF' )

@pytest.mark.skipif(magma.mantle_target == 'coreir',   reason='NYI')
@pytest.mark.parametrize("op", [
    op('SRFF', None),
    op('RSFF', None),
    op('JKFF', None),
    op('TFF',  None),
])
def test_ff(op):
    if magma.mantle_target in ["spartan6", "ice40", "spartan3"]:
        pytest.skip("FF circuits are wrappers around declarations, cannot compile")
    class Main(m.Circuit):
        FF = getattr(mantle, op.name)
        Test = FF()
        ##sim( Test, op.func)
        com( Test, f'{op.name}' )

@pytest.mark.parametrize("op", [
    op('DefineRegister', None),
    op('DefineSISO',     None),
    op('DefinePISO',     None),
    op('DefineSISO',     None),
    op('DefinePISO',     None),
    op('DefineRing',     None),
    op('DefineJohnson',  None),
    op('DefineDecoder',  None),
    op('DefineEncoder',  None),
    op('DefineArbiter',  None),
    op('DefineCounter',  None),
    op('DefineCounterLoad',  None)
])
@pytest.mark.parametrize("width", WIDTHS)
def test_decode(op, width):
    Define = getattr(mantle, op.name)
    Test = Define(width)
    #sim( Test, op.func)
    com( Test, f'{op.name}{width}' )

