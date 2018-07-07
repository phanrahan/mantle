import magma as m

if m.mantle_target is None:
    m.set_mantle_target('coreir')

if m.mantle_target in [ 'coreir',
                        'ice40',
                        'spartan3', 'spartan6', 'kyntex7',
                        'cyclone4', 
                        'greenpak4', 
                        'verilog' ]:

    #from mantle.primitives import *

    if m.mantle_target == 'coreir':
        from mantle.coreir import *
    elif m.mantle_target in ['ice40']:
        from mantle.lattice import *
    elif m.mantle_target in ['spartan3', 'spartan6', 'kintex7']:
        from mantle.xilinx import *
    elif m.mantle_target in ['cyclone4']:
        from mantle.altera import *
    elif m.mantle_target in ['greenpak4']:
        from mantle.silego import *
    elif m.mantle_target == 'verilog':
        from mantle.verilog import *

    from mantle.common import *

else:
    raise RuntimeError(f"MANTLE_TARGET={m.mantle_target} not supported")


