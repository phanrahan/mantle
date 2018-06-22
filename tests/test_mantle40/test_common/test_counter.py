import magma
from magma import *
from magma.testing.coroutine import check, coroutine
from mantle.common import DefineCounter, DefineDownCounter, DefineUpDownCounter

magma.set_mantle_target('ice40')

@coroutine
def counter4_sim():
    yield
    while True:
        for i in range(0, 1<<4):
            O = i
            yield O


def test_counter():
    Counter4 = DefineCounter(4, cout=False)

    check(Counter4, counter4_sim(), 1<<4 * 2)

@coroutine
def down_counter4_sim():
    yield
    # Counter starts at 0, then counts down
    while True:
        O = 0
        yield O
        for i in range((1<<4) - 1, 0, -1):
            O = i
            yield O


def test_downcounter():
    DownCounter4 = DefineDownCounter(4, cout=False)

    check(DownCounter4, down_counter4_sim(), 1<<4 * 2)
