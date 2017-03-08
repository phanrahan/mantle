from parts.xilinx.spartan3.primitives import FAMILY, \
    A0, A1, A2, A3, \
    I0, I1, I2, I3, \
    ALL, ANY, PARITY, ZERO, ONE, \
    LUTS_PER_LOGICBLOCK, BITS_PER_LUT, LOG_BITS_PER_LUT

from mantle.xilinx.port3.LUT import *
from mantle.xilinx.port3.ROM import *
from mantle.xilinx.port3.RAM import *

from mantle.xilinx.port3.MUX import *

from mantle.xilinx.port3.FF import *

from mantle.xilinx.port3.RAMB import *

from mantle.xilinx.port3.adder import *

from mantle.xilinx.port3.cascade import *
from mantle.xilinx.port3.flatcascade import *

from mantle.xilinx.port3.logic import *
from mantle.xilinx.port3.decode import *
from mantle.xilinx.port3.compare import *

print('import xilinx mantle port3')
