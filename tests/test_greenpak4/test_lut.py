import magma as m
from magma import compile
from magma.simulator.python_simulator import testvectors as simtest
from magma.testing.newfunction import testvectors as funtest
from magma.testing import check_files_equal

from mantle.silego import greenpak4

def sim(Test, TestFun):
    tvsim = simtest(Test)
    print(tvsim)
    tvfun = funtest(Test, TestFun)
    print(tvfun)
    assert tvsim == tvfun

def com(Test, name):
    name = f'test_{name}'
    build = f'build/{name}'
    gold = f'gold/{name}'
    compile(build, Test)
    assert check_files_equal(__file__, build+'.v', gold+'.v')

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
