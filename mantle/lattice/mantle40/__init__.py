from ..ice40 import FAMILY, \
    A0, A1, A2, A3, \
    I0, I1, I2, I3, \
    ALL, ANY, PARITY, ZERO, ONE, \
    LUTS_PER_LOGICBLOCK, BITS_PER_LUT, LOG_BITS_PER_LUT

from .LUT import *

from .MUX import *

from .FF import *

from .logic import *
from .decode import *

from .halfadder import *
from .fulladder import *
from .arith import *
from .compare import *

from .memory import Memory

print('import lattice mantle40')
