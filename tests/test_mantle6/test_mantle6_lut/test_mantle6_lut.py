from mantle.xilinx.mantle6 import LUT1, LUT2, LUT3, LUT4

def test_lut1():
    test = LUT1([0,1])
    print(repr(test))
    assert ' = LUT1(INIT=0x2)' == (repr(test))

def test_lut2():
    test = LUT2([0,0,0,1])
    print(repr(test))
    assert ' = LUT2(INIT=0x8)' == (repr(test))

def test_lut3():
    test = LUT3([0, 0, 0, 0, 0,0,0,1])
    print(repr(test))
    assert ' = LUT3(INIT=0x80)' == (repr(test))

def test_lut4():
    test = LUT4(15*[0] + [1])
    print(repr(test))
    assert ' = LUT4(INIT=0x8000)' == (repr(test))




