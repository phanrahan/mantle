import os
import sys
if sys.version_info > (3, 0):
    from .expressions import circuit
else:
    def circuit(fn):
        raise RuntimeError("@circuit decorator requires Python 3+")

mantle = os.getenv('MANTLE', 'lattice')
if mantle:
    mantle = mantle.strip()
    if   mantle == 'xilinx':
        from mantle.xilinx import *
    elif mantle == 'altera':
        from mantle.altera import *
    elif mantle == 'lattice':
        from mantle.lattice import *
    elif mantle == 'verilog':
        from mantle.verilog import *
