import magma
from bit_vector import BitVector
from magma.bitutils import seq2int
from magma.testing.coroutine import check, coroutine
from magma.simulator import PythonSimulator
from mantle import DefineJohnson

magma.set_mantle_target('ice40')

def johnson_counter(n):
    @coroutine
    def johnson_counter_():
        O = BitVector(0, n)
        yield
        while True:
            yield O
            O = BitVector([not O[-1]] + O.as_bool_list()[:-1])
    return johnson_counter_

def test_lfsr():
    n = 8
    Johnson8 = DefineJohnson(n=n)
    check(Johnson8, johnson_counter(n)(), 3 * n)
