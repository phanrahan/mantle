import magma
target = magma.mantle_target

if   target == 'spartan3':
    from ..mantle3 import *
elif target == 'spartan6':
    from ..mantle6 import *

