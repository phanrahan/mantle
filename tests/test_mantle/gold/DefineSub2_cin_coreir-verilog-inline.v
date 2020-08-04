module Add2_cin (
    input [1:0] I0,
    input [1:0] I1,
    output [1:0] O,
    input CIN
);
assign O = 2'((2'(({1'b0,CIN}) + I0)) + I1);
endmodule

module Sub2_cin (
    input [1:0] I0,
    input [1:0] I1,
    output [1:0] O,
    input CIN
);
wire [1:0] Add2_cin_inst0_I0;
wire [1:0] Add2_cin_inst0_I1;
wire Add2_cin_inst0_CIN;
assign Add2_cin_inst0_I0 = I0;
assign Add2_cin_inst0_I1 = ~ I1;
assign Add2_cin_inst0_CIN = ~ CIN;
Add2_cin Add2_cin_inst0 (
    .I0(Add2_cin_inst0_I0),
    .I1(Add2_cin_inst0_I1),
    .O(O),
    .CIN(Add2_cin_inst0_CIN)
);
endmodule

