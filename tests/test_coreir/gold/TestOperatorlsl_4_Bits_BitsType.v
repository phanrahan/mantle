module TestOperatorlsl_4_Bits_BitsType (input [3:0] I0, input [3:0] I1, output [3:0] O);
wire [3:0] inst0_out;
coreir_shl inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule
