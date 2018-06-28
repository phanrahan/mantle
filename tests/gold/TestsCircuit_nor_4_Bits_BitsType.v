module Invert4_wrapped (input [3:0] I, output [3:0] O);
wire [3:0] inst0_out;
coreir_not inst0 (.in(I), .out(inst0_out));
assign O = inst0_out;
endmodule

module or4_wrapped (input [3:0] I0, input [3:0] I1, output [3:0] O);
wire [3:0] inst0_out;
coreir_or inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

module NOr24 (input [3:0] I0, input [3:0] I1, output [3:0] O);
wire [3:0] inst0_O;
wire [3:0] inst1_O;
Invert4_wrapped inst0 (.I(inst1_O), .O(inst0_O));
or4_wrapped inst1 (.I0(I0), .I1(I1), .O(inst1_O));
assign O = inst0_O;
endmodule

module TestsCircuit_nor_4_Bits_BitsType (input [3:0] I0, input [3:0] I1, output [3:0] O);
wire [3:0] inst0_O;
NOr24 inst0 (.I0(I0), .I1(I1), .O(inst0_O));
assign O = inst0_O;
endmodule

