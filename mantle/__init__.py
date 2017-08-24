import os

mantletarget = os.getenv('MANTLE_TARGET', None)
if mantletarget == 'ice40':
    mantle = 'lattice'
else:
    mantle = os.getenv('MANTLE', 'verilog')

if mantle == 'verilog':
    from mantle.verilog import *
else:
    if mantle == 'lattice':
        from mantle.lattice import *
    from mantle.common import *


