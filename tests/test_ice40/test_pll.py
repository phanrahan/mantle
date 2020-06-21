import magma as m
from mantle.lattice.ice40 import SB_PLL
from magma.testing import check_files_equal

def test_pll():
    class TestPLL(m.Circuit):
        io = m.IO(CLKIN=m.In(m.Clock),
                  CLKOUT=m.Out(m.Clock))
        clk = SB_PLL(32000000, 16000000)(I=io.CLKIN)
        m.wire(clk, io.CLKOUT)

    m.compile("build/test_pll", TestPLL, output="coreir")
    assert check_files_equal(__file__, "build/test_pll.json", "gold/test_pll.json")
