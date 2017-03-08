module Adders4_6_8_cinNone_coutNone (input [3:0] I0, input [3:0] I1, output [3:0] O);
wire  inst0_O;
wire  inst1_LO;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_LO;
wire  inst6_O;
wire  inst7_O;
wire  inst8_O;
wire  inst9_LO;
wire  inst10_O;
wire  inst11_O;
wire  inst12_O;
wire  inst13_LO;
wire  inst14_O;
wire  inst15_O;
LUT2 #(.INIT(4'h6)) inst0 (.I0(I0[0]), .I1(I1[0]), .O(inst0_O));
MULT_AND inst1 (.I0(I0[0]), .I1(I1[0]), .LO(inst1_LO));
MUXCY inst2 (.DI(inst1_LO), .CI(1'b0), .S(inst0_O), .O(inst2_O));
XORCY inst3 (.LI(inst0_O), .CI(1'b0), .O(inst3_O));
LUT2 #(.INIT(4'h6)) inst4 (.I0(I0[1]), .I1(I1[1]), .O(inst4_O));
MULT_AND inst5 (.I0(I0[1]), .I1(I1[1]), .LO(inst5_LO));
MUXCY inst6 (.DI(inst5_LO), .CI(inst2_O), .S(inst4_O), .O(inst6_O));
XORCY inst7 (.LI(inst4_O), .CI(inst2_O), .O(inst7_O));
LUT2 #(.INIT(4'h6)) inst8 (.I0(I0[2]), .I1(I1[2]), .O(inst8_O));
MULT_AND inst9 (.I0(I0[2]), .I1(I1[2]), .LO(inst9_LO));
MUXCY inst10 (.DI(inst9_LO), .CI(inst6_O), .S(inst8_O), .O(inst10_O));
XORCY inst11 (.LI(inst8_O), .CI(inst6_O), .O(inst11_O));
LUT2 #(.INIT(4'h6)) inst12 (.I0(I0[3]), .I1(I1[3]), .O(inst12_O));
MULT_AND inst13 (.I0(I0[3]), .I1(I1[3]), .LO(inst13_LO));
MUXCY inst14 (.DI(inst13_LO), .CI(inst10_O), .S(inst12_O), .O(inst14_O));
XORCY inst15 (.LI(inst12_O), .CI(inst10_O), .O(inst15_O));
assign O = {inst15_O,inst11_O,inst7_O,inst3_O};
endmodule

module main (output [3:0] LED, input [7:0] SWITCH);
wire [3:0] inst0_O;
Adders4_6_8_cinNone_coutNone inst0 (.I0({SWITCH[3],SWITCH[2],SWITCH[1],SWITCH[0]}), .I1({SWITCH[7],SWITCH[6],SWITCH[5],SWITCH[4]}), .O(inst0_O));
assign LED = inst0_O;
endmodule

