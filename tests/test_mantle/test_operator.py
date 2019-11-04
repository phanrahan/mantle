import magma as m
from magma.testing import check_files_equal
import mantle


def test_mux():
    class Test(m.Circuit):
        IO = ["I0", m.In(m.Bits[10]),
              "I1", m.In(m.Bits[10]),
              "S", m.In(m.Bit),
              "O", m.Out(m.Bits[10])]
        @classmethod
        def definition(io):
            io.O <= mantle.mux([io.I0, io.I1], io.S, name="my_mux")

    if m.mantle_target == "coreir":
        output = "coreir"
        suffix = "json"
    else:
        output = "verilog"
        suffix = "v"
    m.compile(f"build/test_mantle_mux_{m.mantle_target}", Test, output)
    assert check_files_equal(
        __file__,
        f"build/test_mantle_mux_{m.mantle_target}.{suffix}",
        f"gold/test_mantle_mux_{m.mantle_target}.{suffix}")
