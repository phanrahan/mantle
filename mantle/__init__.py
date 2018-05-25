import os

mantle_target = os.getenv('MANTLE_TARGET', "coreir")

from mantle.primitives import *

if mantle_target == 'verilog':
    from mantle.verilog import *
elif mantle_target == 'coreir':
    from mantle.coreir import *
elif mantle_target == 'lattice':
    from mantle.lattice import *
else:
    raise RuntimeError(f"MANTLE_TARGET={mantle_target} not supported")


A0 = 0xAAAA
A1 = 0xCCCC
A2 = 0xF0F0
A3 = 0xFF00

from mantle.common import *
