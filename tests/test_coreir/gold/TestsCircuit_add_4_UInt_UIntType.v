module TestsCircuit_add_4_UInt_UIntType (input [3:0] I0, input [3:0] I1, output [3:0] O0, output [3:0] O1);
wire [3:0] inst0_out;
wire [3:0] inst1_out;
coreir_add4 inst0 (.I0(I0), .I1(I1), .O(inst0_out));
coreir_add4 inst1 (.I0(I0), .I1(I1), .O(inst1_out));
assign O0 = inst0_out;
assign O1 = inst1_out;
endmodule

