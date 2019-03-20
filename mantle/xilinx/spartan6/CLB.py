from magma import *
from magma.bitutils import lutinit

__all__  = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']
__all__ += ['I0', 'I1', 'I2', 'I3', 'I4', 'I5']
__all__ += ['ALL', 'ANY', 'PARITY']
__all__ += ['ZERO', 'ONE']
__all__ += ['LUTS_PER_LOGICBLOCK', 'BITS_PER_LUT', 'LOG_BITS_PER_LUT']

__all__ += ['_LUT1', '_LUT2', '_LUT3', '_LUT4' , '_LUT5', '_LUT6', '_LUT6x2']

__all__ += ['MUXF7', 'MUXF8']

__all__ += ['MUXCY', 'XORCY', 'CARRY4', 'CARRY']

__all__ += ['FDRSE', 'FDCPE', 'FDCE']

LUTS_PER_LOGICBLOCK = 4
LOG_BITS_PER_LUT = 6
BITS_PER_LUT = 1 << LOG_BITS_PER_LUT

ZERO = 0
ONE = (1<<BITS_PER_LUT)-1

A0 = 0xAAAAAAAAAAAAAAAA
A1 = 0xCCCCCCCCCCCCCCCC
A2 = 0xF0F0F0F0F0F0F0F0
A3 = 0xFF00FF00FF00FF00
A4 = 0xFFFF0000FFFF0000
A5 = 0xFFFFFFFF00000000

I0 = A0
I1 = A1
I2 = A2
I3 = A3
I4 = A4
I5 = A5

ALL = A0 & A1 & A2 & A3 & A4 & A5
ANY = A0 | A1 | A2 | A3 | A4 | A5
PARITY = A0 ^ A1 ^ A2 ^ A3 ^ A4 ^ A5

_LUT1 = DeclareCircuit('LUT1',
               "I0", In(Bit),
               "O", Out(Bit))

_LUT2 = DeclareCircuit('LUT2',
               "I0", In(Bit),
               "I1", In(Bit),
               "O", Out(Bit))

_LUT3 = DeclareCircuit('LUT3',
               "I0", In(Bit),
               "I1", In(Bit),
               "I2", In(Bit),
               "O", Out(Bit))

_LUT4 = DeclareCircuit('LUT4',
               "I0", In(Bit),
               "I1", In(Bit),
               "I2", In(Bit),
               "I3", In(Bit),
               "O", Out(Bit)) 

_LUT5 = DeclareCircuit('LUT5',
               "I0", In(Bit),
               "I1", In(Bit),
               "I2", In(Bit),
               "I3", In(Bit),
               "I4", In(Bit),
               "O", Out(Bit)) 

_LUT6 = DeclareCircuit('LUT6',
               "I0", In(Bit),
               "I1", In(Bit),
               "I2", In(Bit),
               "I3", In(Bit),
               "I4", In(Bit),
               "I5", In(Bit),
               "O", Out(Bit)) 

_LUT6x2 = DeclareCircuit('LUT6_2',
               "I0", In(Bit),
               "I1", In(Bit),
               "I2", In(Bit),
               "I3", In(Bit),
               "I4", In(Bit),
               "I5", In(Bit),
               "O5", Out(Bit),
               "O6", Out(Bit)) 

# D-FF with Clock Enable and Aynchronous Clear
FDCE = DeclareCircuit('FDCE',
               "C",   In(Clock),
               "CE",  In(Enable),
               "CLR", In(Bit),
               "D",   In(Bit),
               "Q",   Out(Bit))
    
# D-FF with Clock Enable and Aynchronous Preset and Clear
FDCPE = DeclareCircuit('FDCPE',
               "C",   In(Clock),
               "CE",  In(Enable),
               "CLR", In(Bit),
               "PRE", In(Bit),
               "D",   In(Bit),
               "Q",   Out(Bit)) 

# D-FF with Synchronous Reset and Set and Clock Enable
FDRSE = DeclareCircuit('FDRSE',
               "C",   In(Clock),
               "CE",  In(Enable),
               "R",   In(Reset),
               "S",   In(Reset),
               "D",   In(Bit),
               "Q",   Out(Bit)) 

MUXF7 = DeclareCircuit('MUXF7',
               "I0", In(Bit),
               "I1", In(Bit),
               "S", In(Bit),
               "O", Out(Bit))

MUXF8 = DeclareCircuit('MUXF8',
               "I0", In(Bit),
               "I1", In(Bit),
               "S", In(Bit),
               "O", Out(Bit))


MUXCY = DeclareCircuit('MUXCY',
               "DI", In(Bit),
               "CI", In(Bit),
               "S", In(Bit),
               "O", Out(Bit))

XORCY = DeclareCircuit('XORCY',
               "LI", In(Bit),
               "CI", In(Bit),
               "O", Out(Bit))

def CARRY(I0, I1, CIN):
    mux = MUXCY()
    wire(I0,  mux.S)
    wire(I1,  mux.DI)
    wire(CIN, mux.CI)

    xor = XORCY()
    wire(I0,  xor.LI)
    wire(CIN, xor.CI)

    return xor.O, mux.O

#module CARRY4 (CO, O, CI, CYINIT, DI, S);
#
#    output [3:0] CO;
#    output [3:0] O;
#    input        CI;
#    input        CYINIT;
#    input  [3:0] DI;
#    input  [3:0] S;
#
#    wire ci_or_cyinit;
#
#//    initial
#//       ci_or_cyinit = 0;
#
#    assign O = S ^ {CO[2:0], ci_or_cyinit};
#    assign CO[0] = S[0] ? ci_or_cyinit : DI[0];
#    assign CO[1] = S[1] ? CO[0] : DI[1];
#    assign CO[2] = S[2] ? CO[1] : DI[2];
#    assign CO[3] = S[3] ? CO[2] : DI[3];
#    assign ci_or_cyinit = CYINIT | CI;
#
#//    always @(CYINIT or CI)
#//      if (CYINIT === 1'bz || CYINIT === 1'bx) begin
#//           $display("Error: CARRY4 instance, %m, detects CYINIT unconnected. Only one of CI and CYINIT inputs can be used and other one need be grounded.");
#//           $finish;
#//     end
#//      else if (CI=== 1'bz || CI=== 1'bx) begin
#//           $display("Error: CARRY4 instance, %m, detects CI unconnected. Only one of CI and CYINIT inputs can be used and other one need be grounded.");
#//           $finish;
#//     end
#//      else 
#//           ci_or_cyinit = CYINIT | CI;
#
#endmodule

CARRY4 = DeclareCircuit('CARRY4',
               "CYINIT", In(Bit),# 0
               "CI", In(Bit),    # CIN
               "S", In(Bits[ 4 ]), # I0
               "DI", In(Bits[ 4 ]), # I1
               "O", Out(Bits[ 4 ]),
               "outout CO", Out(Bits[ 4 ]))

if __name__ == '__main__':
     print("%016X" % (A0&~A0))
     print("%016X" % ((A0|~A0)&0XFFFFFFFFFFFFFFFF))
