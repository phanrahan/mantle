module Add4_cout (input [3:0] I0, input [3:0] I1, output [3:0] O, output  COUT);
wire [4:0] inst0_out;
coreir_add5 inst0 (.in0({1'b0,I0[3],I0[2],I0[1],I0[0]}), .in1({1'b0,I1[3],I1[2],I1[1],I1[0]}), .out(inst0_out));
assign O = {inst0_out[3],inst0_out[2],inst0_out[1],inst0_out[0]};
assign COUT = inst0_out[4];
endmodule

