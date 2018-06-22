import magma
target = magma.mantle_target

if   target == 'spartan3':
    from ..spartan3 import *
elif target == 'spartan6':
    from ..spartan6 import *
elif target == 'kintex7':
    from ..spartan6 import *
    from ..kintex7 import *

