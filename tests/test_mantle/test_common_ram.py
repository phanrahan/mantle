import magma as m
from magma.testing import check_files_equal

import mantle


def test_ram():
    main = m.DefineCircuit("main", "rdata", m.Out(m.Bit), "CLKIN",
                           m.In(m.Clock))

    ram = mantle.RAM(4, 1, name="ram")

    waddr = mantle.Counter(2, cout=False)
    wdata = mantle.Counter(1, cout=False)
    we = 1
    raddr = mantle.Counter(2, cout=False)

    ram(raddr.O, waddr.O, wdata.O, we, CLK=main.CLKIN)

    m.wire(ram.RDATA[0], main.rdata)
    m.EndDefine()
    if m.mantle_target == "coreir":
        output = "coreir"
        suffix = "json"
    else:
        output = "verilog"
        suffix = "v"
    m.compile(f"build/test_common_ram_{m.mantle_target}", main, output)
    assert check_files_equal(
        __file__, f"build/test_common_ram_{m.mantle_target}.{suffix}",
        f"gold/test_common_ram_{m.mantle_target}.{suffix}")
