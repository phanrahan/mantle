module Adders2_6_8_cinNone_coutNone (input [1:0] I0, input [1:0] I1, output [1:0] O);
wire  inst0_O;
wire  inst1_LO;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_LO;
wire  inst6_O;
wire  inst7_O;
LUT2 #(.INIT(4'h6)) inst0 (.I0(I0[0]), .I1(I1[0]), .O(inst0_O));
MULT_AND inst1 (.I0(I0[0]), .I1(I1[0]), .LO(inst1_LO));
MUXCY inst2 (.DI(inst1_LO), .CI(1'b0), .S(inst0_O), .O(inst2_O));
XORCY inst3 (.LI(inst0_O), .CI(1'b0), .O(inst3_O));
LUT2 #(.INIT(4'h6)) inst4 (.I0(I0[1]), .I1(I1[1]), .O(inst4_O));
MULT_AND inst5 (.I0(I0[1]), .I1(I1[1]), .LO(inst5_LO));
MUXCY inst6 (.DI(inst5_LO), .CI(inst2_O), .S(inst4_O), .O(inst6_O));
XORCY inst7 (.LI(inst4_O), .CI(inst2_O), .O(inst7_O));
assign O = {inst7_O,inst3_O};
endmodule

module main (output [1:0] LED, input [3:0] SWITCH);
wire [1:0] inst0_O;
Adders2_6_8_cinNone_coutNone inst0 (.I0({SWITCH[1],SWITCH[0]}), .I1({SWITCH[3],SWITCH[2]}), .O(inst0_O));
assign LED = inst0_O;
endmodule

