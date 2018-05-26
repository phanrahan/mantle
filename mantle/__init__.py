import os

mantle_target = os.getenv('MANTLE_TARGET', "coreir")

from mantle.primitives import *

if mantle_target == 'verilog':
    from mantle.verilog import *
elif mantle_target == 'coreir':
    from mantle.coreir import *
elif mantle_target in ['cyclone4']:
    from mantle.altera import *
elif mantle_target in ['spartan3', 'spartan6', 'kintex7']:
    from mantle.xilinx import *
elif mantle_target in ['ice40']:
    from mantle.lattice import *
else:
    raise RuntimeError(f"MANTLE_TARGET={mantle_target} not supported")


from mantle.common import *
