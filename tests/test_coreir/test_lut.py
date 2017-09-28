from magma import *
from mantle.coreir.LUT import LUT
from magma.testing import check_files_equal


def test_coreir_lut():
    class Test(Circuit):
        name = "test_coreir_lut3"
        IO = ["I", In(Bits(3)), "O", Out(Bit)]
        @classmethod
        def definition(cls):
            lut3 = LUT(0xDE, 3)
            for i in range(3):
                wire(cls.I[i], getattr(lut3, "I{}".format(i)))
                wire(lut3.O, cls.O)

    compile("build/test_lut3", Test, output="coreir")
    assert check_files_equal(__file__,
            "build/test_lut3.json", "gold/test_lut3.json")
