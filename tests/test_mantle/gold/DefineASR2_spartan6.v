module Mux2 (input [1:0] I, input  S, output  O);
wire  inst0_O;
LUT3 #(.INIT(8'hCA)) inst0 (.I0(I[0]), .I1(I[1]), .I2(S), .O(inst0_O));
assign O = inst0_O;
endmodule

module ASR2_1 (input [1:0] I, input  S, output [1:0] O);
wire  inst0_O;
wire  inst1_O;
Mux2 inst0 (.I(I), .S(S), .O(inst0_O));
Mux2 inst1 (.I({I[1],I[1]}), .S(S), .O(inst1_O));
assign O = {inst1_O,inst0_O};
endmodule

module ASR2 (input [1:0] I, input [0:0] S, output [1:0] O);
wire [1:0] inst0_O;
ASR2_1 inst0 (.I(I), .S(S[0]), .O(inst0_O));
assign O = inst0_O;
endmodule

