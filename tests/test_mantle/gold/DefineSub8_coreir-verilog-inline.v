module Add8_cin (
    input [7:0] I0,
    input [7:0] I1,
    output [7:0] O,
    input CIN
);
assign O = 8'((8'(({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,CIN}) + I0)) + I1);
endmodule

module Sub8 (
    input [7:0] I0,
    input [7:0] I1,
    output [7:0] O
);
wire [7:0] Invert8_inst0_out;
wire bit_const_1_None_out;
Add8_cin Add8_cin_inst0 (
    .I0(I0),
    .I1(Invert8_inst0_out),
    .O(O),
    .CIN(bit_const_1_None_out)
);
assign Invert8_inst0_out = ~ I1;
assign bit_const_1_None_out = 1'b1;
endmodule

