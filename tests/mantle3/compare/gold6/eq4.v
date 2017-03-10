module Cascade4x2_9_0_1 (input [3:0] I0, input [3:0] I1, output  O);
wire  inst0_O5;
wire  inst0_O6;
wire  inst1_O;
wire  inst2_O5;
wire  inst2_O6;
wire  inst3_O;
wire  inst4_O5;
wire  inst4_O6;
wire  inst5_O;
wire  inst6_O5;
wire  inst6_O6;
wire  inst7_O;
LUT6_2 #(.INIT(64'h9999999900000000)) inst0 (.I0(I0[0]), .I1(I1[0]), .I2(1'b1), .I3(1'b1), .I4(1'b1), .I5(1'b1), .O5(inst0_O5), .O6(inst0_O6));
MUXCY inst1 (.DI(inst0_O5), .CI(1'b1), .S(inst0_O6), .O(inst1_O));
LUT6_2 #(.INIT(64'h9999999900000000)) inst2 (.I0(I0[1]), .I1(I1[1]), .I2(1'b1), .I3(1'b1), .I4(1'b1), .I5(1'b1), .O5(inst2_O5), .O6(inst2_O6));
MUXCY inst3 (.DI(inst2_O5), .CI(inst1_O), .S(inst2_O6), .O(inst3_O));
LUT6_2 #(.INIT(64'h9999999900000000)) inst4 (.I0(I0[2]), .I1(I1[2]), .I2(1'b1), .I3(1'b1), .I4(1'b1), .I5(1'b1), .O5(inst4_O5), .O6(inst4_O6));
MUXCY inst5 (.DI(inst4_O5), .CI(inst3_O), .S(inst4_O6), .O(inst5_O));
LUT6_2 #(.INIT(64'h9999999900000000)) inst6 (.I0(I0[3]), .I1(I1[3]), .I2(1'b1), .I3(1'b1), .I4(1'b1), .I5(1'b1), .O5(inst6_O5), .O6(inst6_O6));
MUXCY inst7 (.DI(inst6_O5), .CI(inst5_O), .S(inst6_O6), .O(inst7_O));
assign O = inst7_O;
endmodule

module main (output [0:0] LED, input [7:0] SWITCH);
wire  inst0_O;
Cascade4x2_9_0_1 inst0 (.I0({SWITCH[3],SWITCH[2],SWITCH[1],SWITCH[0]}), .I1({SWITCH[7],SWITCH[6],SWITCH[5],SWITCH[4]}), .O(inst0_O));
assign LED = {inst0_O};
endmodule

