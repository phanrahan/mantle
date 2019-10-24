import pytest
import mantle
import magma as m
from magma.testing import check_files_equal


@pytest.mark.parametrize("has_ce", [True, False])
@pytest.mark.parametrize("has_async_reset,has_async_resetn", [(True, False),
                                                            (False, True),
                                                            (False, False)])
def test_reg(has_ce, has_async_reset, has_async_resetn):

    def DefineReg():
        class testReg(m.Circuit):
            name = "test"
            IO = ["clk", m.In(m.Clock)]
            IO += ["In0", m.In(m.Bits[1])]
            IO += ["Out0", m.Out(m.Bits[1])]
            IO += m.ClockInterface(has_ce=has_ce,
                                   has_async_reset=has_async_reset,
                                   has_async_resetn=has_async_resetn)

            @classmethod
            def definition(io):
                reg0 = mantle.Register(1, has_ce=has_ce,
                                       has_async_reset=has_async_reset,
                                       has_async_resetn=has_async_resetn)
                m.wire(reg0.CLK, io.clk)
                m.wire(reg0.I, io.In0)
                m.wire(reg0.O, io.Out0)
        return testReg

    test = DefineReg()
    m.compile(f"build/testReg-{has_ce}-{has_async_reset}-{has_async_resetn}", test, output="coreir-verilog")

    assert check_files_equal(
        __file__,
        f"build/testReg-{has_ce}-{has_async_reset}-{has_async_resetn}.json",
        f"gold/testReg-{has_ce}-{has_async_reset}-{has_async_resetn}.json")

    assert check_files_equal(
        __file__,
        f"build/testReg-{has_ce}-{has_async_reset}-{has_async_resetn}.v",
        f"gold/testReg-{has_ce}-{has_async_reset}-{has_async_resetn}.v")
