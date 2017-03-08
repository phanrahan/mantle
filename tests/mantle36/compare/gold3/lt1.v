module Cascade1x2_9_C_0 (input [0:0] I0, input [0:0] I1, output  O);
wire  inst0_O;
wire  inst1_O;
LUT2 #(.INIT(4'h9)) inst0 (.I0(I0[0]), .I1(I1[0]), .O(inst0_O));
MUXCY inst1 (.DI(I1[0]), .CI(1'b0), .S(inst0_O), .O(inst1_O));
assign O = inst1_O;
endmodule

module main (output [0:0] LED, input [1:0] SWITCH);
wire  inst0_O;
Cascade1x2_9_C_0 inst0 (.I0({SWITCH[0]}), .I1({SWITCH[1]}), .O(inst0_O));
assign LED = {inst0_O};
endmodule

