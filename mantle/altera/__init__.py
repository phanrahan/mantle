import magma
target = magma.mantle_target

if magma.mantle_target == 'cyclone4':
    from .mantle4 import *
