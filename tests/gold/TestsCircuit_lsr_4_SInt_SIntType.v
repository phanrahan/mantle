module TestsCircuit_lsr_4_SInt_SIntType (input signed [3:0] I0, input signed [3:0] I1, output signed [3:0] O);
wire [3:0] inst0_out;
coreir_lshr inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

