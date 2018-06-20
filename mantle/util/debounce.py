import magma as m
from mantle import FF, And

def debounce(a, slow):
    CLK = m.getCurrentDefinition().CLKIN

    ffa = FF(has_ce=True)
    m.wire(CLK, ffa.CLK)
    ffa(a, ce=slow)

    ffb = FF(has_ce=True)
    m.wire(CLK, ffb.CLK)
    ffb(ffa.O, ce=slow)

    return And(2)(ffa.O, ffb.O)
