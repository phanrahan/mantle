from magma import Circuit, Bits, In, Out, wire, fork, join, flat, uncurry, map_, cache_definition
from mantle import And, Or

__all__  = ['Swap',  'swap']
__all__ += ['Swaps', 'swaps']
__all__ += ['DefineEvenOddSwaps', 'EvenOddSwaps', 'evenoddswaps']

#
# Binary swap circuit
#
class Swap(Circuit):
    IO = ['I', In(Bits(2)), "O", Out(Bits(2))]
    @classmethod
    def definition(io):
        swap = uncurry( fork( And(2), Or(2) ) , prefix="I")
        #swap = uncurry( fork( And(2), Or(2) ) , prefix="in")
        wire( swap( io.I ), io.O )

def swap(I):
    return Swap()(I)


def DefineSwaps(n):
    class Swaps(Circuit):
        name = 'Swap{}'.format(n)
        IO = ['I', In(Bits(n)), "O", Out(Bits(n))]
        @classmethod
        def definition(io):
            s = flat( join( map_(Swap, n//2) ), flatargs = ['I', 'O'] )
            wire(s(io.I), io.O)
    return Swaps

def Swaps(n):
    return DefineSwaps(n)()

def swaps(I):
    return Swaps(len(I))(I)


def DefineEvenOddSwaps(n):
    class EvenOddSwaps(Circuit):
        name = 'EvenOddSwap{}'.format(n)
        IO = ['I', In(Bits(n)), "O", Out(Bits(n))]
        @classmethod
        def definition(io):
            s = flat( join( map_(Swap, n//2-1) ), flatargs = ['I', 'O'] )
            wire(io.I[0], io.O[0])
            wire(s(io.I[1:-1]), io.O[1:-1])
            wire(io.I[-1], io.O[-1])
    return EvenOddSwaps

def EvenOddSwaps(n):
    return DefineEvenOddSwaps(n)()

def evenoddswaps(I):
    return EvenOddSwaps(len(I))(I)
