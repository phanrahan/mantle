from magma import compose
from .swap import swap, Swaps, swaps
from .permute import Riffle, UnRiffle, ReverseRiffle, UnReverseRiffle

__all__   = ['HalfCleaner', 'halfcleaner']
__all__  += ['ReverseHalfCleaner', 'reversehalfcleaner']

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
