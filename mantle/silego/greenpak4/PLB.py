from magma import *

__all__  = ['A0', 'A1', 'A2', 'A3']
__all__ += ['I0', 'I1', 'I2', 'I3']
__all__ += ['ALL', 'ANY', 'PARITY']
__all__ += ['ZERO', 'ONE']

__all__ += ['GP_LUT2']
__all__ += ['GP_LUT3']
__all__ += ['GP_LUT4']
__all__ += ['GP_INV']
__all__ += ['GP_DFF']
__all__ += ['GP_DFFI']

ZERO = 0x0000
ONE  = 0xFFFF

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

GP_LUT2 = DeclareCircuit('GP_2LUT',
               "IN0", In(Bit),
               "IN1", In(Bit),
               "OUT", Out(Bit)) 

GP_LUT3 = DeclareCircuit('GP_3LUT',
               "IN0", In(Bit),
               "IN1", In(Bit),
               "IN2", In(Bit),
               "OUT", Out(Bit)) 

GP_LUT4 = DeclareCircuit('GP_4LUT',
               "IN0", In(Bit),
               "IN1", In(Bit),
               "IN2", In(Bit),
               "IN3", In(Bit),
               "OUT", Out(Bit)) 

GP_INV = DeclareCircuit('GP_INV',
               "IN",  In(Bit),
               "OUT", Out(Bit)) 

GP_DFF = DeclareCircuit('GP_DFF',
               "D",   In(Bit),
               "CLK", In(Clock),
               "Q",   Out(Bit)) 

GP_DFFI = DeclareCircuit('GP_DFFI',
               "D",   In(Bit),
               "CLK", In(Clock),
               "nQ",  Out(Bit)) 

GP_DFFR = DeclareCircuit('GP_DFFR',
               "D",   In(Bit),
               "CLK", In(Clock),
               "nRST", In(Reset),
               "Q",   Out(Bit)) 

GP_DFFRI = DeclareCircuit('GP_DFFSI',
               "D",   In(Bit),
               "CLK", In(Clock),
               "nRST", In(Reset),
               "nQ",  Out(Bit)) 

GP_DFFS = DeclareCircuit('GP_DFFS',
               "D",   In(Bit),
               "CLK", In(Clock),
               "nSET", In(Bit),
               "Q",   Out(Bit)) 

GP_DFFSI = DeclareCircuit('GP_DFFSI',
               "D",   In(Bit),
               "CLK", In(Clock),
               "nSET", In(Bit),
               "nQ",  Out(Bit)) 

GP_DFFSR = DeclareCircuit('GP_DFFSR',
               "D",   In(Bit),
               "CLK", In(Clock),
               "nRS", In(Reset),
               "Q",   Out(Bit)) 

GP_DFFSRI = DeclareCircuit('GP_DFFSI',
               "D",   In(Bit),
               "CLK", In(Clock),
               "nRS", In(Reset),
               "nQ",  Out(Bit)) 

# module GP_DLATCH(input D, input nCLK, output reg Q);

# module GP_DLATCHI(input D, input nCLK, output reg nQ);

# module GP_DLATCHR(input D, input nCLK, input nRST, output reg Q);

# module GP_DLATCHRI(input D, input nCLK, input nRST, output reg nQ);

# module GP_DLATCHS(input D, input nCLK, input nSET, output reg Q);

# module GP_DLATCHSI(input D, input nCLK, input nSET, output reg nQ);

# module GP_DLATCHSR(input D, input nCLK, input nSR, output reg Q);

# module GP_DLATCHSRI(input D, input nCLK, input nSR, output reg nQ);


# module GP_IBUF(input IN, output OUT);

# module GP_IOBUF(input IN, input OE, output OUT, inout IO);

# module GP_OBUF(input IN, output OUT);

# module GP_OBUFT(input IN, input OE, output OUT);


# module GP_PGEN(input wire nRST, input wire CLK, output reg OUT);

# module GP_SHREG(input nRST, input CLK, input IN, output OUTA, output OUTB);

# module GP_VDD(output OUT);

# module GP_VSS(output OUT);

# module GP_CLKBUF(input wire IN, output wire OUT);


# module GP_COUNT14(input CLK, input wire RST, output reg OUT);

# module GP_COUNT14_ADV(input CLK, input RST, output reg OUT,

# module GP_COUNT8_ADV(input CLK, input RST, output reg OUT,

# module GP_COUNT8(


# module GP_DCMPREF(output reg[7:0]OUT);

# module GP_DCMPMUX(input[1:0] SEL, input[7:0] IN0, input[7:0] IN1, input[7:0] IN2, input[7:0] IN3, output reg[7:0] OUTA, output reg[7:0] OUTB);


# module GP_DELAY(input IN, output reg OUT);

