module Add4_cout_cin (
    input [3:0] I0,
    input [3:0] I1,
    output [3:0] O,
    output COUT,
    input CIN
);
wire [4:0] coreir_add5_inst0_out;
assign coreir_add5_inst0_out = 5'((5'(({1'b0,1'b0,1'b0,1'b0,CIN}) + ({1'b0,I0[3],I0[2],I0[1],I0[0]}))) + ({1'b0,I1[3],I1[2],I1[1],I1[0]}));
assign O = {coreir_add5_inst0_out[3],coreir_add5_inst0_out[2],coreir_add5_inst0_out[1],coreir_add5_inst0_out[0]};
assign COUT = coreir_add5_inst0_out[4];
endmodule

module Sub4_cout (
    input [3:0] I0,
    input [3:0] I1,
    output [3:0] O,
    output COUT
);
Add4_cout_cin Add4_cout_cin_inst0 (
    .I0(I0),
    .I1(~ I1),
    .O(O),
    .COUT(COUT),
    .CIN(1'b1)
);
endmodule

