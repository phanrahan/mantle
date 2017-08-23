import os
import sys
if sys.version_info > (3, 0):
    from .expressions import circuit
else:
    def circuit(fn):
        raise RuntimeError("@circuit decorator requires Python 3+")

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


