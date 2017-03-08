module Cascade2x2_9_C_1 (input [1:0] I0, input [1:0] I1, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
LUT2 #(.INIT(4'h9)) inst0 (.I0(I0[0]), .I1(I1[0]), .O(inst0_O));
MUXCY inst1 (.DI(I1[0]), .CI(1'b1), .S(inst0_O), .O(inst1_O));
LUT2 #(.INIT(4'h9)) inst2 (.I0(I0[1]), .I1(I1[1]), .O(inst2_O));
MUXCY inst3 (.DI(I1[1]), .CI(inst1_O), .S(inst2_O), .O(inst3_O));
assign O = inst3_O;
endmodule

module main (output [0:0] LED, input [3:0] SWITCH);
wire  inst0_O;
Cascade2x2_9_C_1 inst0 (.I0({SWITCH[1],SWITCH[0]}), .I1({SWITCH[3],SWITCH[2]}), .O(inst0_O));
assign LED = {inst0_O};
endmodule

