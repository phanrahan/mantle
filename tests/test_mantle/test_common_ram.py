import magma as m
import mantle


def test_ram():
    main = m.DefineCircuit("main", "rdata", m.Out(m.Bit), "CLKIN",
                           m.In(m.Clock))

    ram = mantle.RAM(4, 1)

    waddr = mantle.Counter(4)
    wdata = mantle.Counter(1)
    we = 1
    raddr = mantle.FF()(mantle.Counter(4))

    ram(raddr, waddr, wdata, we, CLK=main.CLKIN)

    m.wire(ram.RDATA, main.rdata)
    m.EndDefine()
    m.compile("build/test_common_ram", main)
