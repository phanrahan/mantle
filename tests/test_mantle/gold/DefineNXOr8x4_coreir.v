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

module fold_xor84 (input [3:0] I0, input [3:0] I1, input [3:0] I2, input [3:0] I3, input [3:0] I4, input [3:0] I5, input [3:0] I6, input [3:0] I7, output [3:0] O);
wire [3:0] inst0_O;
wire [3:0] inst1_O;
wire [3:0] inst2_O;
wire [3:0] inst3_O;
wire [3:0] inst4_O;
wire [3:0] inst5_O;
wire [3:0] inst6_O;
xor4_wrapped inst0 (.I0(I0), .I1(I1), .O(inst0_O));
xor4_wrapped inst1 (.I0(inst0_O), .I1(I2), .O(inst1_O));
xor4_wrapped inst2 (.I0(inst1_O), .I1(I3), .O(inst2_O));
xor4_wrapped inst3 (.I0(inst2_O), .I1(I4), .O(inst3_O));
xor4_wrapped inst4 (.I0(inst3_O), .I1(I5), .O(inst4_O));
xor4_wrapped inst5 (.I0(inst4_O), .I1(I6), .O(inst5_O));
xor4_wrapped inst6 (.I0(inst5_O), .I1(I7), .O(inst6_O));
assign O = inst6_O;
endmodule

module NXOr84 (input [3:0] in0, input [3:0] in1, input [3:0] in2, input [3:0] in3, input [3:0] in4, input [3:0] in5, input [3:0] in6, input [3:0] in7, output [3:0] out);
wire [3:0] inst0_O;
wire [3:0] inst1_O;
Invert4_wrapped inst0 (.I(inst1_O), .O(inst0_O));
fold_xor84 inst1 (.I0(in0), .I1(in1), .I2(in2), .I3(in3), .I4(in4), .I5(in5), .I6(in6), .I7(in7), .O(inst1_O));
assign out = inst0_O;
endmodule

