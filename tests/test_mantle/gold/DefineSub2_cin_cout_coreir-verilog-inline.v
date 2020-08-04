module Add2_cout_cin (
    input [1:0] I0,
    input [1:0] I1,
    output [1:0] O,
    output COUT,
    input CIN
);
wire [2:0] coreir_add3_inst0_out;
assign coreir_add3_inst0_out = 3'((3'(({1'b0,1'b0,CIN}) + ({1'b0,I0[1:0]}))) + ({1'b0,I1[1:0]}));
assign O = coreir_add3_inst0_out[1:0];
assign COUT = coreir_add3_inst0_out[2];
endmodule

module Sub2_cout_cin (
    input [1:0] I0,
    input [1:0] I1,
    output [1:0] O,
    output COUT,
    input CIN
);
wire [1:0] Add2_cout_cin_inst0_I0;
wire [1:0] Add2_cout_cin_inst0_I1;
wire Add2_cout_cin_inst0_CIN;
assign Add2_cout_cin_inst0_I0 = I0;
assign Add2_cout_cin_inst0_I1 = ~ I1;
assign Add2_cout_cin_inst0_CIN = ~ CIN;
Add2_cout_cin Add2_cout_cin_inst0 (
    .I0(Add2_cout_cin_inst0_I0),
    .I1(Add2_cout_cin_inst0_I1),
    .O(O),
    .COUT(COUT),
    .CIN(Add2_cout_cin_inst0_CIN)
);
endmodule

