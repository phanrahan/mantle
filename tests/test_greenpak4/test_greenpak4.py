import magma

import pytest

import magma as m
from fault.test_vectors import generate_function_test_vectors, \
    generate_simulator_test_vectors

import mantle.silego.greenpak4 as greenpak4

#def sim(Test, TestFun):
#    tvsim = simtest(Test)
#    print(tvsim)
#    tvfun = funtest(Test, TestFun)
#    print(tvfun)
#    assert tvsim == tvfun

def com(Test, name):
    from magma.testing import check_files_equal
    name = f'test_{name}'
    build = f'build/{name}'
    gold = f'gold/{name}'
    m.compile(build, Test, output="verilog")
    assert check_files_equal(__file__, build+'.v', gold+'.v')

def test_inv():
    Test = m.DefineCircuit("INV",
              "I", m.In(m.Bit),
              "O", m.Out(m.Bit))
    inv = greenpak4.GP_INV()
    m.wire(Test.I, inv.IN)
    m.wire(inv.OUT, Test.O)

    com( Test, 'inv' )

def test_lut2():
    Test = m.DefineCircuit("LUT2",
              "I0", m.In(m.Bit), "I1", m.In(m.Bit), 
              "O",  m.Out(m.Bit))
    lut = greenpak4.GP_LUT2(INIT="4'h8")
    m.wire(Test.I0, lut.IN0)
    m.wire(Test.I1, lut.IN1)
    m.wire(lut.OUT, Test.O)

    com( Test, 'lut2' )

def test_lut3():
    Test = m.DefineCircuit("LUT3",
              "I0", m.In(m.Bit),
              "I1", m.In(m.Bit), 
              "I2", m.In(m.Bit), 
              "O",  m.Out(m.Bit))
    lut = greenpak4.GP_LUT3(INIT="8'h80")
    m.wire(Test.I0, lut.IN0)
    m.wire(Test.I1, lut.IN1)
    m.wire(Test.I2, lut.IN2)
    m.wire(lut.OUT, Test.O)

    com( Test, 'lut3' )
  
def test_lut4():
    Test = m.DefineCircuit("LUT4",
              "I0", m.In(m.Bit),
              "I1", m.In(m.Bit), 
              "I2", m.In(m.Bit), 
              "I3", m.In(m.Bit), 
              "O",  m.Out(m.Bit))
    lut = greenpak4.GP_LUT4(INIT="16'h8000")
    m.wire(Test.I0, lut.IN0)
    m.wire(Test.I1, lut.IN1)
    m.wire(Test.I2, lut.IN2)
    m.wire(Test.I3, lut.IN3)
    m.wire(lut.OUT, Test.O)

    com( Test, 'lut4' )

@pytest.mark.parametrize('ff',['DFF', 'DFFI'])
def test_ff(ff):
    Test = m.DefineCircuit(ff,
              "I",   m.In(m.Bit),
              "CLK", m.In(m.Clock),
              "O",   m.Out(m.Bit))
    DFF = getattr(greenpak4,'GP_'+ff)
    dff = DFF()
    m.wire(Test.I, dff.D)
    m.wire(Test.CLK, dff.CLK)
    m.wire(dff.Q if ff == 'DFF' else dff.nQ, Test.O)

    com( Test, ff )

