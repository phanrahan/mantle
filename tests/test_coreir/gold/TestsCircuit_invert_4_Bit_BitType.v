module TestsCircuit_invert_4_Bit_BitType (input  I, output  O0, output  O1);
wire  inst0_out;
wire  inst1_out;
coreir_bitnot inst0 (.in(I), .out(inst0_out));
coreir_bitnot inst1 (.in(I), .out(inst1_out));
assign O0 = inst0_out;
assign O1 = inst1_out;
endmodule

