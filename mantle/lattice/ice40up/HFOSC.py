from magma import *

# generate 48 Mhz clock
SB_HFOSC = DeclareCircuit("SB_HFOSC", 
                            'CLKHFPU', In(Bit), # power up
                            'CLKHFEN', In(Bit), # enable
                            'CLKHF', Out(Clock)
                         )

# parameters
#  CLKHF_DIV 0b00 48Mhz
#            0b01 24Mhz
#            0b10 12Mhz
#            0b11 6Mhz

#SB_HFOSC u_hfosc (
#                .CLKHFPU(1'b1),
#                .CLKHFEN(1'b1),
#                .CLKHF(clk)
#        );
