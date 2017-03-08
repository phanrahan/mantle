import sys
from magma import *
from mantle import *
from boards.papilio import Papilio

N = 8

def Triangle(n):
    I = In(Array(n,Bit))()
    
    invert = Invert(n)
    mux = Mux(2, n)

    triangle = mux( I, invert(I), I[n-1] )

    return AnonymousCircuit("I", I, "O", triangle )

papilio = Papilio()
papilio.Clock.on()
for i in range(8):
    papilio.A[i].rename('SIG[%d]' % i).output().on()

main = papilio.main()

counter = Counter(32)
sawtooth = counter.O[8:8+N]

tri = Triangle(N)

wire( tri(sawtooth), main.SIG )

compile(sys.argv[1], main)

