from magma import *

SB_IO= DeclareCircuit("SB_IO", 
                        'PACKAGE_PIN', In(Bit), # should be inout
                        'CLOCK_ENABLE', In(Bit),
                        'INPUT_CLOCK', In(Bit),
                        'OUTPUT_CLOCK', In(Bit),
                        'OUTPUT_ENABLE', In(Bit),
                        'LATCH_INPUT_VALUE', In(Bit),
                        'D_IN_0', In(Bit), # rising
                        'D_IN_1', In(Bit), # falling
                        'D_OUT_0', Out(Bit), # rising
                        'D_OUT_1', Out(Bit) # falling
                     )

#module top (input PIO1_02, output D1);
#wire y;
#SB_IO #(.PIN_TYPE(6'b00_0000)) in  ( .PACKAGE_PIN(PIO1_02), .D_IN_0(y) );
#SB_IO #(.PIN_TYPE(6'b01_0110)) out ( .PACKAGE_PIN(D1), .D_OUT_0(y) );
#endmodule

