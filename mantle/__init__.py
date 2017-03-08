import os

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
