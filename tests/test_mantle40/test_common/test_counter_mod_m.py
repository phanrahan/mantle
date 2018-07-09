import magma as m
import mantle


def test_counter_mod_m():
    CounterModM7 = mantle.DefineCounterModM(7, 3, has_ce=True, has_reset=True)
    m.compile("build/CounterModM7", CounterModM7)

