from magma import *
from .swap import swap, EvenOddSwaps
from .permute import Riffle, UnRiffle

__all__  = ['DefineEvenOddMerger', 'EvenOddMerger', 'evenoddmerger']
__all__  = ['DefineEvenOddSorter', 'EvenOddSorter', 'evenoddsorter']

#
# Convert an unsorted sequence into a sorted sequence
#
# EvenOdd(n) => 2 EvenOddMerger(n//2) => EvenOddSwaps(n)) 
#
def DefineEvenOddMerger(n):
    assert n in [2, 4, 8, 16]
    T = Bits(n)
    class _EvenOddMerger(Circuit):
        name = 'EvenOddMerger{}'.format(n)
        IO = ['I', In(T), "O", Out(T)]
        @classmethod
        def definition(io):
            if n == 2: # Sort 2 element sequences
                wire(swap(io.I), io.O)
            else:
                unriffle = UnRiffle(n)
                merger0 = EvenOddMerger(n//2) # bot merger 
                merger1 = EvenOddMerger(n//2) # top merger
                merger = flat( join(merger0, merger1) )
                riffle = Riffle(n)
                merger =  compose( riffle, compose( merger, unriffle ) )
                evenoddswap = EvenOddSwaps(n)
                merger = compose( evenoddswap, merger )
                wire( merger(io.I), io.O )
    return _EvenOddMerger

def EvenOddMerger(n):
    return DefineEvenOddMerger(n)()

def evenoddmerger(I):
    return EvenOddMerger(len(I))(I)

#
# Convert an unsorted sequence into a sorted sequence
#
# 2 EvenOddSorter(n//2) => EvenOddMerger(n)) 
#
def DefineEvenOddSorter(n):
    assert n in [2, 4, 8, 16]
    T = Bits(n)
    class _EvenOddSorter(Circuit):
        name = 'EvenOddSorter{}'.format(n)
        IO = ['I', In(T), "O", Out(T)]
        @classmethod
        def definition(io):
            if n == 2: # Sort 2 element sequences
                wire(swap(io.I), io.O)
            else:
                sorter0 = EvenOddSorter(n//2) # bot sorter 
                sorter1 = EvenOddSorter(n//2) # top sorter
                sorter = flat( join(sorter0, sorter1) )
                merger = EvenOddMerger(n)
                sorter = compose( merger, sorter )
                wire( sorter(io.I), io.O )
    return _EvenOddSorter

def EvenOddSorter(n):
    return DefineEvenOddSorter(n)()

def evenoddsorter(I):
    return EvenOddSorter(len(I))(I)

