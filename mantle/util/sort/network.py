from magma import *
from magma.bitutils import log2
from mantle import *
from .swap import swap, Swaps, swaps, EvenOddSwaps, evenoddswaps
from .permute import Riffle, UnRiffle, ReverseRiffle, UnReverseRiffle, EvenOdd

__all__  = ['HalfCleaner', 'halfcleaner']
__all__ += ['ReverseHalfCleaner', 'reversehalfcleaner']
__all__ += ['ReverseHalfCleaner', 'reversehalfcleaner']

# HalfCleaner
#
# Convert bitonic input into two bitonic halves
#
# Either the top half or the bottom half will be clean, all 0's or 1's
#
def HalfCleaner(n):
    if n == 2:
        return Swap()
    u = UnRiffle(n)
    s = Swaps(n)
    r = Riffle(n)
    return compose( u, compose( s, r ) )

def halfcleaner(I):
    return HalfCleaner(len(I))(I)

#
# ReverseHalfCleaner
#
# Convert 2 sorted inputs into two bitonic halves
#
def ReverseHalfCleaner(n):
    if n == 2:
        return Swap()
    u = UnReverseRiffle(n)
    s = Swaps(n)
    r = ReverseRiffle(n)
    return compose( u, compose( s, r ) )

def reversehalfcleaner(I):
    return ReverseHalfCleaner(len(I))(I)

#
# Convert a bitonic sequence into a sorted sequences
#
# HalfCleaner(n) => 2 BitonicSorter(n//2)
#
def DefineBitonicSorter(n):
    assert n in [2, 4, 8, 16]
    T = Bits(n)
    class _BitonicSorter(Circuit):
        name = 'BitonicSorter{}'.format(n)
        IO = ['I', In(T), "O", Out(T)]
        @classmethod
        def definition(io):
            if n == 2:
                wire(swap(io.I), io.O)
            else:
                halfcleaner = HalfCleaner(n)
                bitonic0 = BitonicSorter(n//2)
                bitonic1 = BitonicSorter(n//2)
                bitonic = flat( join(bitonic0, bitonic1), flatargs=['I','O'] )
                s = compose( bitonic, halfcleaner )
                wire( s(io.I), io.O )
    return _BitonicSorter

def BitonicSorter(n):
    return DefineBitonicSorter(n)()

def bitonicsorter(I):
    return BitonicSorter(len(I))(I)


#
# Merge 2 sorted sequencers into a sorted sequence
#
# 2 BitonicSorter(n/2) => ReverseHalfCleaner
#
def DefineMerger(n):
    assert n in [2, 4, 8, 16]
    T = Bits(n)
    class _Merger(Circuit):
        name = 'Merger{}'.format(n)
        IO = ['I', In(T), "O", Out(T)]
        @classmethod
        def definition(io):
            if n == 2:
                wire(swap(io.I), io.O)
            else:
                revhalfcleaner = ReverseHalfCleaner(n)
                bitonic0 = BitonicSorter(n//2)
                bitonic1 = BitonicSorter(n//2)
                bitonic = flat( join(bitonic0, bitonic1), flatargs=['I','O'] )
                s = compose( bitonic, revhalfcleaner )
                wire( s(io.I), io.O )
    return _Merger

def Merger(n):
    return DefineMerger(n)()

def merger(I):
    return Merger(len(I))(I)

#
# Convert an unsorted sequence into a sorted sequence
#
# 2 Sorters(n/2) => Merger(n) 
#
def DefineSorter(n):
    assert n in [2, 4, 8, 16]
    T = Bits(n)
    class _Sorter(Circuit):
        name = 'Sorter{}'.format(n)
        IO = ['I', In(T), "O", Out(T)]
        @classmethod
        def definition(io):
            if n == 2: # Sort 2 element sequences
                wire(swap(io.I), io.O)
            else:
                merger = Merger(n)
                sorter0 = Sorter(n//2) # bot sorter 
                sorter1 = Sorter(n//2) # top sorter
                sorter = flat( join(sorter0, sorter1), flatargs=['I','O'] )
                s = compose( merger, sorter )
                wire( s(io.I), io.O )
    return _Sorter

def Sorter(n):
    return DefineSorter(n)()

def sorter(I):
    return Sorter(len(I))(I)

#
# Convert an unsorted sequence into a sorted sequence
#
# EvenOdd(n) => 2 EvenOddMerger(n//2) => EvenOddSwap(n)) 
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

#
# Brick Sorter
#
def DefineBrickSorter(n):
    assert n % 2 == 0
    T = Bits(n)
    class _BrickSorter(Circuit):
        name = 'BrickSorter{}'.format(n)
        IO = ['I', In(T), "O", Out(T)]
        @classmethod
        def definition(io):
            I = io.I
            for i in range(n//2):
                I = swaps(I)
                I = evenoddswaps(I)
            wire(I, io.O)
    return _BrickSorter

def BrickSorter(n):
    return DefineBrickSorter(n)()

def bricksorter(I):
    return BrickSorter(len(I))(I)
