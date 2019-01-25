import mantle
import magma as m
import importlib


def weak_import(module, scope):
    # Iterate over names defined in module, only define them here if
    # they haven't already been defined. This allows implementations to
    # specialize a common module. For example, mantle40 defines a FullAdder, so
    # it will not use the generic FullAdder in common.
    module = importlib.import_module(f"mantle.{module}")
    if hasattr(module, "__all__"):
        names = module.__all__
    else:
        names = dir(module)
    for name in names:
        try:
            getattr(mantle, name)
        except AttributeError:
            scope.update({name: getattr(module, name)})

if m.mantle_target is None:
    m.set_mantle_target('coreir')

if m.mantle_target in ['coreir',
                       'ice40',
                       'spartan3',
                       'spartan6',
                       'kintex7',
                       'cyclone4',
                       'verilog'
    ]:

    if m.mantle_target == 'coreir':
        from mantle.coreir import *
    elif m.mantle_target in ['ice40']:
        from mantle.lattice import *
    elif m.mantle_target in ['spartan3', 'spartan6', 'kintex7']:
        from mantle.xilinx import *
    elif m.mantle_target in ['cyclone4']:
        from mantle.altera import *
    #elif m.mantle_target in ['greenpak4']:
    #    from mantle.silego import *
    elif m.mantle_target == 'verilog':
        from mantle.verilog import *

    if m.mantle_target == 'verilog':
        print("Warning: verilog mantle target does not support common, will not be imported")
    else:
        import mantle.common
        for module in mantle.common.modules:
            weak_import(f"common.{module}", globals())

else:
    if m.mantle_target not in ['greenpak4']:
        raise RuntimeError(f"MANTLE_TARGET={m.mantle_target} not supported")
