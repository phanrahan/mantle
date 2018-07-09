import magma
target = magma.mantle_target

if target == 'ice40':
    from .mantle40 import *

