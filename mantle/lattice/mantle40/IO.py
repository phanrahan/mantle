from magma import *
from ..ice40.IOB import SB_IO

__all__ = ['IBuf', 'OBuf']

#
# SB_IO #(.PIN_TYPE(6'b00_0000)) in  ( .PACKAGE_PIN(PIO1_02), .D_IN_0(y) );
#
def IBuf(pin, **kwargs):
    io = SB_IO(**kwargs)
    wire(pin, io.PACKAGE_PIN)
    return AnonymousCircuit("O", io.D_IN_0);
    
#
# SB_IO #(.PIN_TYPE(6'b01_0110)) out ( .PACKAGE_PIN(D1), .D_OUT_0(y) );
#
def OBuf(pin, **kwargs):
    io = SB_IO(**kwargs)
    wire(pin, io.PACKAGE_PIN)
    return AnonymousCircuit("I", io.D_OUT_0);
    

