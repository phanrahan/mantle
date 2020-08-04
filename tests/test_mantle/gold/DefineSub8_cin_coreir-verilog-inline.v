module Add8_cin (
    input [7:0] I0,
    input [7:0] I1,
    output [7:0] O,
    input CIN
);
assign O = 8'((8'(({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,CIN}) + I0)) + I1);
endmodule

module Sub8_cin (
    input [7:0] I0,
    input [7:0] I1,
    output [7:0] O,
    input CIN
);
wire [7:0] Add8_cin_inst0_I0;
wire [7:0] Add8_cin_inst0_I1;
wire Add8_cin_inst0_CIN;
assign Add8_cin_inst0_I0 = I0;
assign Add8_cin_inst0_I1 = ~ I1;
assign Add8_cin_inst0_CIN = ~ CIN;
Add8_cin Add8_cin_inst0 (
    .I0(Add8_cin_inst0_I0),
    .I1(Add8_cin_inst0_I1),
    .O(O),
    .CIN(Add8_cin_inst0_CIN)
);
endmodule

