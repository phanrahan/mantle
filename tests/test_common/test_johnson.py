from magma.bitutils import seq2int
from magma.testing.coroutine import check, coroutine
from magma.simulator import PythonSimulator
import os
os.environ["MANTLE"] = "lattice"
from mantle.common import DefineJohnson

def johnson_counter(n):
    @coroutine
    def johnson_counter_():
        O = [False for _ in range(n)]
        while True:
            yield O
            O = [not O[-1]] + O[:-1]
    return johnson_counter_

def test_lfsr():
    n = 8
    Johnson8 = DefineJohnson(n=n)
    check(Johnson8, johnson_counter(n)(), 3 * n)
