module Add4_cin (
    input [3:0] I0,
    input [3:0] I1,
    output [3:0] O,
    input CIN
);
assign O = 4'((4'(({1'b0,1'b0,1'b0,CIN}) + I0)) + I1);
endmodule

module Sub4 (
    input [3:0] I0,
    input [3:0] I1,
    output [3:0] O
);
wire [3:0] Add4_cin_inst0_I0;
wire [3:0] Add4_cin_inst0_I1;
wire Add4_cin_inst0_CIN;
assign Add4_cin_inst0_I0 = I0;
assign Add4_cin_inst0_I1 = ~ I1;
assign Add4_cin_inst0_CIN = 1'b1;
Add4_cin Add4_cin_inst0 (
    .I0(Add4_cin_inst0_I0),
    .I1(Add4_cin_inst0_I1),
    .O(O),
    .CIN(Add4_cin_inst0_CIN)
);
endmodule

