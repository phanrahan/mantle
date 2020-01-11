module Add2_cout_cin (input CIN, output COUT, input [1:0] I0, input [1:0] I1, output [1:0] O);
wire [2:0] coreir_add3_inst0_out;
assign coreir_add3_inst0_out = (({1'b0,1'b0,CIN}) + ({1'b0,I0[1],I0[0]})) + ({1'b0,I1[1],I1[0]});
assign COUT = coreir_add3_inst0_out[2];
assign O = {coreir_add3_inst0_out[1],coreir_add3_inst0_out[0]};
endmodule

module Sub2_cout_cin (input CIN, output COUT, input [1:0] I0, input [1:0] I1, output [1:0] O);
wire not_inst0_out;
Add2_cout_cin Add2_cout_cin_inst0(.CIN(not_inst0_out), .COUT(COUT), .I0(I0), .I1(~ I1), .O(O));
corebit_not not_inst0(.in(CIN), .out(not_inst0_out));
endmodule

