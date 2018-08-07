import pytest
import magma as m
from mantle.coreir.LUT import LUT
from magma.testing import check_files_equal


@pytest.mark.skip(reason='Abort 6')
def test_coreir_lut():
    class Test(m.Circuit):
        name = "test_coreir_lut3"
        IO = ["I", m.In(m.Bits(3)), "O", Out(Bit)]
        @classmethod
        def definition(cls):
            lut3 = LUT(0xDE, 3)
            for i in range(3):
                m.wire(cls.I[i], getattr(lut3, "I{}".format(i)))
                m.wire(lut3.O, cls.O)

    m.compile("build/test_lut3", Test, output="coreir")
    assert check_files_equal(__file__,
            "build/test_lut3.json", "gold/test_lut3.json")
