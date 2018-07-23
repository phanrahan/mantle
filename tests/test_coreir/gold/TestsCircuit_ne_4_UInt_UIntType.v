module EQ4 (input [3:0] I0, input [3:0] I1, output  O);
wire  inst0_out;
coreir_eq inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

module NE4 (input [3:0] I0, input [3:0] I1, output  O);
wire  inst0_O;
wire  inst1_out;
EQ4 inst0 (.I0(I0), .I1(I1), .O(inst0_O));
coreir_bitnot inst1 (.in(inst0_O), .out(inst1_out));
assign O = inst1_out;
endmodule

module TestsCircuit_ne_4_UInt_UIntType (input [3:0] I0, input [3:0] I1, output  O0, output  O1);
wire  inst0_O;
wire  inst1_O;
NE4 inst0 (.I0(I0), .I1(I1), .O(inst0_O));
EQ4 inst1 (.I0(I0), .I1(I1), .O(inst1_O));
assign O0 = inst0_O;
assign O1 = 1'b0;
endmodule

