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

module Or3xNone (input  I0, input  I1, input  I2, output  O);
wire  inst0_out;
orr inst0 (.in({I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module and_wrapped (input  I0, input  I1, output  O);
wire  inst0_out;
coreir_and inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

module FullAdder (input  I0, input  I1, input  CIN, output  O, output  COUT);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
fold_xor3None inst0 (.I0(I0), .I1(I1), .I2(CIN), .O(inst0_O));
Or3xNone inst1 (.I0(inst2_O), .I1(inst3_O), .I2(inst4_O), .O(inst1_O));
and_wrapped inst2 (.I0(I0), .I1(I1), .O(inst2_O));
and_wrapped inst3 (.I0(I1), .I1(CIN), .O(inst3_O));
and_wrapped inst4 (.I0(I0), .I1(CIN), .O(inst4_O));
assign O = inst0_O;
assign COUT = inst1_O;
endmodule

