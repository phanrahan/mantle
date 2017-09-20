from magma import *
from .swap import swap
from .halfcleaner import HalfCleaner, ReverseHalfCleaner

__all__  = ['DefineBitonicSorter', 'BitonicSorter', 'bitonicsorter']
__all__ += ['DefineMerger', 'Merger', 'merger']
__all__ += ['DefineSorter', 'Sorter', 'sorter']

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
