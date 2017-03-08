from parts.xilinx.spartan6.primitives import FAMILY, \
    A0, A1, A2, A3, \
    I0, I1, I2, I3, \
    ALL, ANY, PARITY, ZERO, ONE, \
    LUTS_PER_LOGICBLOCK, BITS_PER_LUT, LOG_BITS_PER_LUT

from mantle.xilinx.port6.LUT import *
from mantle.xilinx.port6.ROM import *
from mantle.xilinx.port6.RAM import *

from mantle.xilinx.port6.MUX import *

from mantle.xilinx.port6.FF import *

from mantle.xilinx.port6.RAMB import *

from mantle.xilinx.port6.adder import *

from mantle.xilinx.port6.cascade import *
from mantle.xilinx.port6.flatcascade import *

from mantle.xilinx.port6.logic import *
from mantle.xilinx.port6.decode import *
from mantle.xilinx.port6.compare import *

print('import xilinx mantle port6')
