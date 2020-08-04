module fold_xor3None (
    input I0,
    input I1,
    input I2,
    output O
);
assign O = (I0 ^ I1) ^ I2;
endmodule

module Or3xNone (
    input I0,
    input I1,
    input I2,
    output O
);
assign O = | ({I2,I1,I0});
endmodule

module FullAdder (
    input I0,
    input I1,
    input CIN,
    output O,
    output COUT
);
wire Or3xNone_inst0_I0;
wire Or3xNone_inst0_I1;
wire Or3xNone_inst0_I2;
wire fold_xor3None_inst0_I0;
wire fold_xor3None_inst0_I1;
wire fold_xor3None_inst0_I2;
assign Or3xNone_inst0_I0 = I0 & I1;
assign Or3xNone_inst0_I1 = I1 & CIN;
assign Or3xNone_inst0_I2 = I0 & CIN;
Or3xNone Or3xNone_inst0 (
    .I0(Or3xNone_inst0_I0),
    .I1(Or3xNone_inst0_I1),
    .I2(Or3xNone_inst0_I2),
    .O(COUT)
);
assign fold_xor3None_inst0_I0 = I0;
assign fold_xor3None_inst0_I1 = I1;
assign fold_xor3None_inst0_I2 = CIN;
fold_xor3None fold_xor3None_inst0 (
    .I0(fold_xor3None_inst0_I0),
    .I1(fold_xor3None_inst0_I1),
    .I2(fold_xor3None_inst0_I2),
    .O(O)
);
endmodule

