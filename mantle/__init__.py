import os

mantletarget = os.getenv('MANTLE_TARGET', None)
if mantletarget == 'ice40':
    mantle = 'lattice'
else:
    mantle = os.getenv('MANTLE', 'verilog')

from mantle.primitives import *

if mantle == 'verilog':
    from mantle.verilog import *
elif mantle == 'coreir':
    from mantle.coreir import *
else:
    if mantle == 'lattice':
        from mantle.lattice import *
    from mantle.common import *


A0 = 0xAAAA
A1 = 0xCCCC
A2 = 0xF0F0
A3 = 0xFF00
