import sys
import math
from magma import *
from mantle import Counter, ROM6
from loam.boards.papilio import Papilio

N = 8

papilio = Papilio()
papilio.Clock.on()
for i in range(N):
    papilio.A[i].rename('SIG[%d]' % i).output().on()

main = papilio.main()

counter = Counter(32)
sawtooth = counter.O[8:8+6]

def int256(x):
    return int2seq(int(x), N)

sintab = [int256(128 + 127 * math.sin(2 * math.pi * i / 64.)) for i in range(64)]
sintab = zip(*sintab) # transpose

print(len(sintab))
print(len(sintab[0]))

def ROM(y):
    return ROM6(sintab[y])

rom = fork(col(ROM, N))

rom(sawtooth)

wire( rom, main.SIG )

compile(sys.argv[1], main)

