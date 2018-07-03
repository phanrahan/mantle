module Mux2 (input [1:0] I, input  S, output  O);
wire  inst0_O;
SB_LUT4 #(.LUT_INIT(16'hCACA)) inst0 (.I0(I[0]), .I1(I[1]), .I2(S), .I3(1'b0), .O(inst0_O));
assign O = inst0_O;
endmodule

module Mux4 (input [3:0] I, input [1:0] S, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
Mux2 inst0 (.I({I[1],I[0]}), .S(S[0]), .O(inst0_O));
Mux2 inst1 (.I({I[3],I[2]}), .S(S[0]), .O(inst1_O));
Mux2 inst2 (.I({inst1_O,inst0_O}), .S(S[1]), .O(inst2_O));
assign O = inst2_O;
endmodule

module Mux8 (input [7:0] I, input [2:0] S, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
Mux4 inst0 (.I({I[3],I[2],I[1],I[0]}), .S({S[1],S[0]}), .O(inst0_O));
Mux4 inst1 (.I({I[7],I[6],I[5],I[4]}), .S({S[1],S[0]}), .O(inst1_O));
Mux2 inst2 (.I({inst1_O,inst0_O}), .S(S[2]), .O(inst2_O));
assign O = inst2_O;
endmodule

module Mux8x2 (input [1:0] I0, input [1:0] I1, input [1:0] I2, input [1:0] I3, input [1:0] I4, input [1:0] I5, input [1:0] I6, input [1:0] I7, input [2:0] S, output [1:0] O);
wire  inst0_O;
wire  inst1_O;
Mux8 inst0 (.I({I7[0],I6[0],I5[0],I4[0],I3[0],I2[0],I1[0],I0[0]}), .S(S), .O(inst0_O));
Mux8 inst1 (.I({I7[1],I6[1],I5[1],I4[1],I3[1],I2[1],I1[1],I0[1]}), .S(S), .O(inst1_O));
assign O = {inst1_O,inst0_O};
endmodule

