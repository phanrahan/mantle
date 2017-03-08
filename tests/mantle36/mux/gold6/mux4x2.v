module Mux4x2 (input [1:0] I0, input [1:0] I1, input [1:0] I2, input [1:0] I3, input [1:0] S, output [1:0] O);
wire  inst0_O;
wire  inst1_O;
LUT6 #(.INIT(64'hFF00F0F0CCCCAAAA)) inst0 (.I0(I0[0]), .I1(I1[0]), .I2(I2[0]), .I3(I3[0]), .I4(S[0]), .I5(S[1]), .O(inst0_O));
LUT6 #(.INIT(64'hFF00F0F0CCCCAAAA)) inst1 (.I0(I0[1]), .I1(I1[1]), .I2(I2[1]), .I3(I3[1]), .I4(S[0]), .I5(S[1]), .O(inst1_O));
assign O = {inst1_O,inst0_O};
endmodule

module main (output [1:0] LED, input [5:0] SWITCH);
wire [1:0] inst0_O;
Mux4x2 inst0 (.I0({SWITCH[0],SWITCH[0]}), .I1({SWITCH[1],SWITCH[1]}), .I2({SWITCH[2],SWITCH[2]}), .I3({SWITCH[3],SWITCH[3]}), .S({SWITCH[5],SWITCH[4]}), .O(inst0_O));
assign LED = inst0_O;
endmodule

