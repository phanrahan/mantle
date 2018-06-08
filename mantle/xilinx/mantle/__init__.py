import os
target = os.environ.get('MANTLE_TARGET', 'spartan3')

assert target == 'spartan3' or target == 'spartan6' or target == 'kintex7'

if   target == 'spartan3':
    from ..mantle3 import *
else:
    from ..mantle6 import *

