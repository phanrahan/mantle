from magma import *

__all__  = ['A0', 'A1', 'A2', 'A3']
__all__ += ['I0', 'I1', 'I2', 'I3']
__all__ += ['ALL', 'ANY', 'PARITY']
__all__ += ['ZERO', 'ONE']
__all__ += ['LUTS_PER_LOGICBLOCK', 'BITS_PER_LUT', 'LOG_BITS_PER_LUT']

__all__ += ['LCELL']
__all__ += ['LUT_INPUT', 'LUT_OUTPUT', '_LUT4']
__all__ += ['CARRY_SUM']
__all__ += ['CASCADE']
__all__ += ['DFFE']

LUTS_PER_LOGICBLOCK = 2
LOG_BITS_PER_LUT = 4
BITS_PER_LUT = 1 << LOG_BITS_PER_LUT

ZERO = 0
ONE = (1<<BITS_PER_LUT)-1

A0 = 0xAAAA
A1 = 0xCCCC
A2 = 0xF0F0
A3 = 0xFF00

I0 = A0
I1 = A1
I2 = A2
I3 = A3

ALL = A0 & A1 & A2 & A3
ANY = A0 | A1 | A2 | A3 
PARITY = A0 ^ A1 ^ A2 ^ A3 

LCELL = DeclareCircuit('LCELL', "I", In(Bit), "O", Out(Bit))
LUT_INPUT = DeclareCircuit('LUT_INPUT', "I", In(Bit), "O", Out(Bit))
LUT_OUTPUT = DeclareCircuit('LUT_OUTPUT', "I", In(Bit), "O", Out(Bit))

CARRY_SUM = DeclareCircuit('CARRY_SUM', 
               "SIN", In(Bit),
               "CIN", In(Bit),
               "SOUT", Bit,
               "COUT", Bit)

CASCADE = DeclareCircuit('CASCADE', "I", In(Bit), "O", Bit)

_LUT4 = DefineCircuit("_LUT4",
            "I0", In(Bit),
            "I1", In(Bit),
            "I2", In(Bit),
            "I3", In(Bit),
            "O", Out(Bit))
_LUT4.verilog = """\
wire aw,bw,cw,dw;
lut_input lut_in1 (I0, aw) ;
lut_input lut_in2 (I1, bw) ;
lut_input lut_in3 (I2, cw) ;
lut_input lut_in4 (I3, dw) ;
lut_output lut_o (aw & bw & cw & dw, O) ;"""
EndCircuit()

# DFF with synchronous enable, asynchronous preset and clear
DFFE = DeclareCircuit('DFFE', 
                        "D", In(Bit),
                        "CLK", In(Bit),
                        "CLRN", In(Bit),
                        "PRN", In(Bit),
                        "ENA", In(Bit),
                        "Q", Out(Bit),
                        )

# DFF with synchronous enable, asynchronous preset, clear and load
DFFEA = DeclareCircuit('DFFEA', 
                        "D", In(Bit),
                        "CLK", In(Bit),
                        "CLRN", In(Bit),
                        "PRN", In(Bit),
                        "ENA", In(Bit),
                        "ASDATA", In(Bit),
                        "ALOAD", In(Bit),
                        "Q", Out(Bit),
                        )

# DFF with synchronous enable, asynchronous preset, and both synchronous and
# asynchronous load and clear
DFFEA = DeclareCircuit('DFFEAS', 
                        "D", In(Bit),
                        "CLK", In(Bit),
                        "CLRN", In(Bit),
                        "PRN", In(Bit),
                        "ENA", In(Bit),
                        "ASDATA", In(Bit),
                        "ALOAD", In(Bit),
                        "SCLR", In(Bit),
                        "SLOAD", In(Bit),
                        "Q", Bit,
                        )


#module lut_sub (din,out);
#   parameter LUT_SIZE = 4;
#   parameter NUM_BITS = 2**LUT_SIZE;
#   [LUT_SIZE-1:0] din;
#   parameter [NUM_BITS-1:0] mask = {NUM_BITS{1'b0}};
#   out;
#   wire out;
#   // buffer the LUT inputs
#   wire [LUT_SIZE-1:0] din_w;
#   genvar i;
#   generate
#       for (i=0; i<LUT_SIZE; i=i+1)
#       begin : liloop
#       lut_li_buf (din[i],din_w[i]);
#       end
#   endgenerate
#   // build up the pterms for the LUT
#   wire [NUM_BITS-1:0] pterms;
#   generate
#   for (i=0; i<NUM_BITS; i=i+1)
#       begin : ploop
#       assign pterms[i] = ((din_w == i) & mask[i]);
#       end
#    endgenerate
#   // assign the pterms to the LUT function
#   wire result;
#   assign result = | pterms;
#   lut_lo_buf (result,out);
#   endmodule
