module Mux4 (input [3:0] I, input [1:0] S, output  O);
wire  inst0_O;
LUT6 #(.INIT(64'hFF00F0F0CCCCAAAA)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .I4(S[0]), .I5(S[1]), .O(inst0_O));
assign O = inst0_O;
endmodule

module Mux4x4 (input [3:0] I0, input [3:0] I1, input [3:0] I2, input [3:0] I3, input [1:0] S, output [3:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
Mux4 inst0 (.I({I3[0],I2[0],I1[0],I0[0]}), .S(S), .O(inst0_O));
Mux4 inst1 (.I({I3[1],I2[1],I1[1],I0[1]}), .S(S), .O(inst1_O));
Mux4 inst2 (.I({I3[2],I2[2],I1[2],I0[2]}), .S(S), .O(inst2_O));
Mux4 inst3 (.I({I3[3],I2[3],I1[3],I0[3]}), .S(S), .O(inst3_O));
assign O = {inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

