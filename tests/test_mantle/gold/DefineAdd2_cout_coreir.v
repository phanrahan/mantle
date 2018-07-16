module Add2_cout (input [1:0] I0, input [1:0] I1, output [1:0] O, output  COUT);
wire [2:0] inst0_out;
coreir_add3 inst0 (.in0({1'b0,I0[1],I0[0]}), .in1({1'b0,I1[1],I1[0]}), .out(inst0_out));
assign O = {inst0_out[1],inst0_out[0]};
assign COUT = inst0_out[2];
endmodule

