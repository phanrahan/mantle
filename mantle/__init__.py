import magma as m

if m.mantle_target is None:
    m.set_mantle_target('coreir')

if m.mantle_target in ['coreir', 'verilog', 
                     'cyclone4', 
                     'spartan3', 'spartan6', 'kyntex7',
                     'ice40']:

    #from mantle.primitives import *

    if m.mantle_target == 'verilog':
        from mantle.verilog import *
    elif m.mantle_target == 'coreir':
        from mantle.coreir import *
    elif m.mantle_target in ['cyclone4']:
        from mantle.altera import *
    elif m.mantle_target in ['spartan3', 'spartan6', 'kintex7']:
        from mantle.xilinx import *
    elif m.mantle_target in ['ice40']:
        from mantle.lattice import *

    from mantle.common import *

else:
    raise RuntimeError(f"MANTLE_TARGET={m.mantle_target} not supported")


