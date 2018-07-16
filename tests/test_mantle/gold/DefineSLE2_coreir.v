module SLE2 (input [1:0] I0, input [1:0] I1, output  O);
wire  inst0_out;
coreir_sle inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

