import os
mantle_target = os.environ.get('MANTLE_TARGET', 'coreir')

if mantle_target in ['coreir', 'verilog', 
                     'cyclone4', 
                     'spartan3', 'spartan6', 'kyntex7',
                     'ice40']:

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

    from mantle.common import *

else:
    raise RuntimeError(f"MANTLE_TARGET={mantle_target} not supported")


