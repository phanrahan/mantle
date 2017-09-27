import os
os.environ['MANTLE_TARGET'] = 'ice40'
from magma.simulator.python_simulator import PythonSimulator 
from mantle.lattice.mantle40.logic import DefineAnd
from mantle.lattice.mantle40.arith import DefineAdd

N = 2

#And = PythonSimulator(DefineAnd(2, N))
#for x in range(2**N):
#    for y in range(2**N):
#        print(x, y, And(x,y))

Add = PythonSimulator(DefineAdd(N))
for x in range(2**N):
    for y in range(2**N):
        print(x, y, Add(x,y))



