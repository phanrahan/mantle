module xor4_wrapped (input [3:0] I0, input [3:0] I1, output [3:0] O);
wire [3:0] inst0_out;
coreir_xor inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

module TestOperatorxor_4_UInt_UIntType (input [3:0] I0, input [3:0] I1, output [3:0] O);
wire [3:0] inst0_O;
xor4_wrapped inst0 (.I0(I0), .I1(I1), .O(inst0_O));
assign O = inst0_O;
endmodule

