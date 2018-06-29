module TestsCircuit_lsr_4_Bits_BitsType (input [3:0] I0, input [3:0] I1, output [3:0] O0, output [3:0] O1);
wire [3:0] inst0_out;
wire [3:0] inst1_out;
coreir_lshr inst0 (.in0(I0), .in1(I1), .out(inst0_out));
coreir_lshr inst1 (.in0(I0), .in1(I1), .out(inst1_out));
assign O0 = inst0_out;
assign O1 = inst1_out;
endmodule

