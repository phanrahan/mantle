import os
target = os.environ.get('MANTLE_TARGET', 'spartan3')

assert target in ['spartan3', 'spartan6', 'kintex7']

if   target == 'spartan3':
    print ('import xilinx mantle3')
    from .mantle3 import *
elif target == 'spartan6':
    print ('import xilinx mantle6')
    from .mantle6 import *


