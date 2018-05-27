import os
target = os.environ['MANTLE_TARGET']

assert target in [None, 'spartan3', 'spartan6', 'kintex7']

if   target == 'spartan3':
    print ('import xilinx mantle3')
    from .port3 import *
    from .common import *
elif target == 'spartan6':
    print ('import xilinx mantle6')
    from .port6 import *
    from .common import *


