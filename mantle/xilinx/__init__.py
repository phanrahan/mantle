import os

print ('import xilinx')

target = os.getenv('MANTLE_TARGET', None)

assert target == 'spartan3' or target == 'spartan6' or target == 'kintex7'

if   target == 'spartan3':
    from .port3 import *
else:
    from .port6 import *

from .common import *

