module Invert4_wrapped (input [3:0] I, output [3:0] O);
wire [3:0] inst0_out;
coreir_not inst0 (.in(I), .out(inst0_out));
assign O = inst0_out;
endmodule

module xor4_wrapped (input [3:0] I0, input [3:0] I1, output [3:0] O);
wire [3:0] inst0_out;
coreir_xor inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

module NXOr24 (input [3:0] in0, input [3:0] in1, output [3:0] out);
wire [3:0] inst0_O;
wire [3:0] inst1_O;
Invert4_wrapped inst0 (.I(inst1_O), .O(inst0_O));
xor4_wrapped inst1 (.I0(in0), .I1(in1), .O(inst1_O));
assign out = inst0_O;
endmodule

module TestsCircuit_nxor_4_UInt_UIntType (input [3:0] I0, input [3:0] I1, output [3:0] O0, output [3:0] O1);
wire [3:0] inst0_out;
NXOr24 inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O0 = inst0_out;
assign O1 = {1'b0,1'b0,1'b0,1'b0};
endmodule

