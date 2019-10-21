import pytest
import mantle
import magma as m
from magma.testing import check_files_equal


@pytest.mark.parametrize("has_ce", [True, False])
def test_reg(has_ce):

    def DefineReg():
        class testReg(m.Circuit):
            name = "test"
            IO = ["clk", m.In(m.Clock)]
            IO += ["ce", m.In(m.Enable)]
            IO += ["In0", m.In(m.Bits[1])]
            IO += ["Out0", m.Out(m.Bits[1])]

            @classmethod
            def definition(io):
                reg0 = mantle.Register(1, has_ce=has_ce)
                m.wire(reg0.CLK, io.clk)
                if has_ce:
                    m.wire(reg0.CE, io.ce)
                m.wire(reg0.I, io.In0)
                m.wire(reg0.O, io.Out0)
        return testReg

    test = DefineReg()
    m.compile(f"build/testReg-{has_ce}", test, output="coreir-verilog")

    assert check_files_equal(__file__,
            f"build/testReg-{has_ce}.json", f"gold/testReg-{has_ce}.json")
