from magma import *

SB_IO= DeclareCircuit("SB_IO", 
                        'input PACKAGE_PIN', In(Bit), # should be inout
                        'input CLOCK_ENABLE', In(Bit),
                        'input INPUT_CLOCK', In(Bit),
                        'input OUTPUT_CLOCK', In(Bit),
                        'input OUTPUT_ENABLE', In(Bit),
                        'input LATCH_INPUT_VALUE', In(Bit),
                        'input D_IN_0', In(Bit), # rising
                        'input D_IN_1', In(Bit), # falling
                        'output D_OUT_0', Out(Bit), # rising
                        'output D_OUT_1', Out(Bit), # falling
                        cells=1)

#module top (input PIO1_02, output D1);
#wire y;
#SB_IO #(.PIN_TYPE(6'b00_0000)) in  ( .PACKAGE_PIN(PIO1_02), .D_IN_0(y) );
#SB_IO #(.PIN_TYPE(6'b01_0110)) out ( .PACKAGE_PIN(D1), .D_OUT_0(y) );
#endmodule

