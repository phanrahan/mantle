module Mux4 (input [3:0] I, input [1:0] S, output  O);
wire  inst0_O;
LUT6 #(.INIT(64'hFF00F0F0CCCCAAAA)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .I4(S[0]), .I5(S[1]), .O(inst0_O));
assign O = inst0_O;
endmodule

module Mux4x2 (input [1:0] I0, input [1:0] I1, input [1:0] I2, input [1:0] I3, input [1:0] S, output [1:0] O);
wire  inst0_O;
wire  inst1_O;
Mux4 inst0 (.I({I3[0],I2[0],I1[0],I0[0]}), .S(S), .O(inst0_O));
Mux4 inst1 (.I({I3[1],I2[1],I1[1],I0[1]}), .S(S), .O(inst1_O));
assign O = {inst1_O,inst0_O};
endmodule

