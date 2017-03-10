module Mux8 (input [7:0] I, input [2:0] S, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
LUT6 #(.INIT(64'hFF00F0F0CCCCAAAA)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .I4(S[0]), .I5(S[1]), .O(inst0_O));
LUT6 #(.INIT(64'hFF00F0F0CCCCAAAA)) inst1 (.I0(I[4]), .I1(I[5]), .I2(I[6]), .I3(I[7]), .I4(S[0]), .I5(S[1]), .O(inst1_O));
MUXF7 inst2 (.I0(inst0_O), .I1(inst1_O), .S(S[2]), .O(inst2_O));
assign O = inst2_O;
endmodule

module main (output [0:0] LED, input [6:0] SWITCH);
wire  inst0_O;
Mux8 inst0 (.I({SWITCH[3],SWITCH[2],SWITCH[1],SWITCH[0],SWITCH[3],SWITCH[2],SWITCH[1],SWITCH[0]}), .S({SWITCH[6],SWITCH[5],SWITCH[4]}), .O(inst0_O));
assign LED = {inst0_O};
endmodule

