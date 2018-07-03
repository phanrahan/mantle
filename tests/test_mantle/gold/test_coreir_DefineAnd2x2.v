module and2_wrapped (input [1:0] I0, input [1:0] I1, output [1:0] O);
wire [1:0] inst0_out;
coreir_and inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

