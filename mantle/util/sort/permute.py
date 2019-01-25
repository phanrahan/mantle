from magma import In, Out, Bits, Circuit, wire, cache_definition

__all__  = ['DefinePermute', 'Permute']
__all__ += ['Reverse']
__all__ += ['Riffle', 'UnRiffle']
__all__ += ['ReverseRiffle', 'UnReverseRiffle']
__all__ += ['EvenOdd']

def flatten(l):
    return sum(l, [])

def shuffle(l, r):
    return flatten([[l[i], r[i]] for i in range(n//2)])

def concat(l, r):
    return l+r

def inverse(l):
    return [l.index(i) for i in range(len(l))]


def _identity(n):
    return range(n)

def _reverse(n):
    return list(reversed(range(n)))

def _even(n):
    return [2*i for i in range(n//2)]

def _odd(n):
    return [2*i+1 for i in range(n//2)]

def _bottom(n):
    return [i for i in range(n//2)]

def _top(n):
    return [n//2+i for i in range(n//2)]

def _evenodd(n):
    return _even(n) + _odd(n)

def _riffle(n):
    return flatten([[i, i+n//2] for i in range(n//2)])

def _unriffle(n):
    return inverse(_riffle(n))

def _reverseriffle(n):
    return flatten([[i, n-1-i] for i in range(n//2)])

def _unreverseriffle(n):
    return inverse(_reverseriffle(n))

def DefinePermute(na,permutation):
    n = len(permutation)
    class Permute(Circuit):
        name = na
        IO = ["I", In(Bits(n)), "O", Out(Bits(n))]
        @classmethod
        def definition(io):
            [wire(io.I[permutation[i]], io.O[i]) for i in range(len(io.I))]
    return Permute

def Permute(name,permutation):
    return DefinePermute(name,tuple(permutation))()


def Reverse(n):
    return Permute('Reverse{}'.format(n),_reverse(n))

def Riffle(n):
    return Permute('Riffle{}'.format(n),_riffle(n))

def UnRiffle(n):
    return Permute('UnRiffle{}'.format(n),_unriffle(n))

def ReverseRiffle(n):
    return Permute('ReverseRiffle{}'.format(n),_reverseriffle(n))

def UnReverseRiffle(n):
    return Permute('UnReverseRiffle{}'.format(n),_unreverseriffle(n))

def EvenOdd(n):
    return Permute('EvenOdd{}'.format(n),_evenodd(n))

