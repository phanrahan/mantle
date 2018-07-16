module Mux2 (input [1:0] I, input  S, output  O);
wire  inst0_O;
SB_LUT4 #(.LUT_INIT(16'hCACA)) inst0 (.I0(I[0]), .I1(I[1]), .I2(S), .I3(1'b0), .O(inst0_O));
assign O = inst0_O;
endmodule

module LSL2_1 (input [1:0] I, input  S, output [1:0] O);
wire  inst0_O;
wire  inst1_O;
Mux2 inst0 (.I({1'b0,I[0]}), .S(S), .O(inst0_O));
Mux2 inst1 (.I({I[0],I[1]}), .S(S), .O(inst1_O));
assign O = {inst1_O,inst0_O};
endmodule

module LSL2 (input [1:0] I, input [0:0] S, input  SI, output [1:0] O);
wire [1:0] inst0_O;
LSL2_1 inst0 (.I(I), .S(S[0]), .O(inst0_O));
assign O = inst0_O;
endmodule

