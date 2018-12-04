module main (input [1:0] I, output  O);
wire  inst0_out;
coreir_and inst0 (.I0(I[0]), .I1(I[1]), .O(inst0_out));
assign O = inst0_out;
endmodule

