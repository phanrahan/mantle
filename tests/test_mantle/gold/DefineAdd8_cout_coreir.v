module Add8_cout (input [7:0] I0, input [7:0] I1, output [7:0] O, output  COUT);
wire [8:0] inst0_out;
coreir_add9 inst0 (.in0({1'b0,I0[7],I0[6],I0[5],I0[4],I0[3],I0[2],I0[1],I0[0]}), .in1({1'b0,I1[7],I1[6],I1[5],I1[4],I1[3],I1[2],I1[1],I1[0]}), .out(inst0_out));
assign O = {inst0_out[7],inst0_out[6],inst0_out[5],inst0_out[4],inst0_out[3],inst0_out[2],inst0_out[1],inst0_out[0]};
assign COUT = inst0_out[8];
endmodule

