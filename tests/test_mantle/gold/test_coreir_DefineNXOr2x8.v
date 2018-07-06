module Invert8_wrapped (input [7:0] I, output [7:0] O);
wire [7:0] inst0_out;
coreir_not inst0 (.in(I), .out(inst0_out));
assign O = inst0_out;
endmodule

module xor8_wrapped (input [7:0] I0, input [7:0] I1, output [7:0] O);
wire [7:0] inst0_out;
coreir_xor inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

module NXOr28 (input [7:0] in0, input [7:0] in1, output [7:0] out);
wire [7:0] inst0_O;
wire [7:0] inst1_O;
Invert8_wrapped inst0 (.I(inst1_O), .O(inst0_O));
xor8_wrapped inst1 (.I0(in0), .I1(in1), .O(inst1_O));
assign out = inst0_O;
endmodule

