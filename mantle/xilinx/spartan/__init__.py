import os

target = os.getenv('MANTLE_TARGET', 'spartan3')
target = target.strip()

assert target == 'spartan3' or target == 'spartan6' or target == 'kintex7'

if   target == 'spartan3':
    from ..spartan3 import *
elif target == 'spartan6':
    from ..spartan6 import *
elif target == 'kintex7':
    from ..spartan6 import *
    from ..kintex7 import *

