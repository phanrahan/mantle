import magma as m

import mantle


def test_ram():
    main = m.DefineCircuit("main", "rdata", m.Out(m.Bit), "CLKIN",
                           m.In(m.Clock))

    ram = mantle.RAM(4, 1)

    waddr = mantle.Counter(4, cout=False)
    wdata = mantle.Counter(1, cout=False)
    we = 1
    raddr = mantle.Counter(4, cout=False)

    ram(raddr, waddr, wdata, we, CLK=main.CLKIN)

    m.wire(ram.RDATA[0], main.rdata)
    m.EndDefine()
    if m.mantle_target == "coreir":
        output = "coreir"
    else:
        output = "verilog"
    m.compile("build/test_common_ram", main, output)
