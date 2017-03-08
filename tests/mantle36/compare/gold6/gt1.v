module Cascade1x2_9_A_0 (input [0:0] I0, input [0:0] I1, output  O);
wire  inst0_O5;
wire  inst0_O6;
wire  inst1_O;
LUT6_2 #(.INIT(64'h99999999AAAAAAAA)) inst0 (.I0(I0[0]), .I1(I1[0]), .I2(1'b1), .I3(1'b1), .I4(1'b1), .I5(1'b1), .O5(inst0_O5), .O6(inst0_O6));
MUXCY inst1 (.DI(inst0_O5), .CI(1'b0), .S(inst0_O6), .O(inst1_O));
assign O = inst1_O;
endmodule

module main (output [0:0] LED, input [1:0] SWITCH);
wire  inst0_O;
Cascade1x2_9_A_0 inst0 (.I0({SWITCH[0]}), .I1({SWITCH[1]}), .O(inst0_O));
assign LED = {inst0_O};
endmodule

