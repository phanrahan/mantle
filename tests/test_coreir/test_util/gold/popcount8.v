module xor_wrapped (input  I0, input  I1, output  O);
wire  inst0_out;
coreir_xor inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

module fold_xor3None (input  I0, input  I1, input  I2, output  O);
wire  inst0_O;
wire  inst1_O;
xor_wrapped inst0 (.I0(I0), .I1(I1), .O(inst0_O));
xor_wrapped inst1 (.I0(inst0_O), .I1(I2), .O(inst1_O));
assign O = inst1_O;
endmodule

module and_wrapped (input  I0, input  I1, output  O);
wire  inst0_out;
coreir_and inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

module Or3xNone (input  I0, input  I1, input  I2, output  O);
wire  inst0_out;
orr inst0 (.in({I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module Op (input  I0, input  I1, input  I2, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
and_wrapped inst0 (.I0(I0), .I1(I1), .O(inst0_O));
and_wrapped inst1 (.I0(I1), .I1(I2), .O(inst1_O));
and_wrapped inst2 (.I0(I2), .I1(I0), .O(inst2_O));
Or3xNone inst3 (.I0(inst0_O), .I1(inst1_O), .I2(inst2_O), .O(inst3_O));
assign O = inst3_O;
endmodule

module PopCount8 (input [7:0] I, output [3:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
wire  inst8_O;
wire  inst9_O;
wire  inst10_O;
wire  inst11_O;
wire  inst12_O;
wire  inst13_O;
fold_xor3None inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .O(inst0_O));
Op inst1 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .O(inst1_O));
fold_xor3None inst2 (.I0(I[3]), .I1(I[4]), .I2(I[5]), .O(inst2_O));
Op inst3 (.I0(I[3]), .I1(I[4]), .I2(I[5]), .O(inst3_O));
fold_xor3None inst4 (.I0(inst0_O), .I1(inst2_O), .I2(I[6]), .O(inst4_O));
Op inst5 (.I0(inst0_O), .I1(inst2_O), .I2(I[6]), .O(inst5_O));
fold_xor3None inst6 (.I0(inst1_O), .I1(inst3_O), .I2(inst5_O), .O(inst6_O));
Op inst7 (.I0(inst1_O), .I1(inst3_O), .I2(inst5_O), .O(inst7_O));
fold_xor3None inst8 (.I0(inst4_O), .I1(I[7]), .I2(1'b0), .O(inst8_O));
Op inst9 (.I0(inst4_O), .I1(I[7]), .I2(1'b0), .O(inst9_O));
fold_xor3None inst10 (.I0(inst6_O), .I1(inst9_O), .I2(1'b0), .O(inst10_O));
Op inst11 (.I0(inst6_O), .I1(inst9_O), .I2(1'b0), .O(inst11_O));
fold_xor3None inst12 (.I0(inst7_O), .I1(inst11_O), .I2(1'b0), .O(inst12_O));
Op inst13 (.I0(inst7_O), .I1(inst11_O), .I2(1'b0), .O(inst13_O));
assign O = {inst13_O,inst12_O,inst10_O,inst8_O};
endmodule

