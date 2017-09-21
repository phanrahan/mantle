module fold_or4None (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_out;
wire  inst1_out;
wire  inst2_out;
coreir_bitor inst0 (.in0(I0), .in1(I1), .out(inst0_out));
coreir_bitor inst1 (.in0(inst0_out), .in1(I2), .out(inst1_out));
coreir_bitor inst2 (.in0(inst1_out), .in1(I3), .out(inst2_out));
assign O = inst2_out;
endmodule

