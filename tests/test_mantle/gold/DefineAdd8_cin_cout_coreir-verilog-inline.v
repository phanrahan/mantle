module Add8_cout_cin (input [7:0] I0, input [7:0] I1, output [7:0] O, output COUT, input CIN);
wire [8:0] coreir_add9_inst0_out;
assign coreir_add9_inst0_out = (({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,CIN}) + ({1'b0,I0[7],I0[6],I0[5],I0[4],I0[3],I0[2],I0[1],I0[0]})) + ({1'b0,I1[7],I1[6],I1[5],I1[4],I1[3],I1[2],I1[1],I1[0]});
assign O = {coreir_add9_inst0_out[7],coreir_add9_inst0_out[6],coreir_add9_inst0_out[5],coreir_add9_inst0_out[4],coreir_add9_inst0_out[3],coreir_add9_inst0_out[2],coreir_add9_inst0_out[1],coreir_add9_inst0_out[0]};
assign COUT = coreir_add9_inst0_out[8];
endmodule

