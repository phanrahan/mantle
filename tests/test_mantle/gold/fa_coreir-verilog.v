module coreir_orr #(
    parameter width = 1
) (
    input [width-1:0] in,
    output out
);
  assign out = |in;
endmodule

module corebit_xor (
    input in0,
    input in1,
    output out
);
  assign out = in0 ^ in1;
endmodule

module fold_xor3None (
    input I0,
    input I1,
    input I2,
    output O
);
wire xor_inst0_in0;
wire xor_inst0_in1;
wire xor_inst0_out;
wire xor_inst1_in0;
wire xor_inst1_in1;
wire xor_inst1_out;
assign xor_inst0_in0 = I0;
assign xor_inst0_in1 = I1;
corebit_xor xor_inst0 (
    .in0(xor_inst0_in0),
    .in1(xor_inst0_in1),
    .out(xor_inst0_out)
);
assign xor_inst1_in0 = xor_inst0_out;
assign xor_inst1_in1 = I2;
corebit_xor xor_inst1 (
    .in0(xor_inst1_in0),
    .in1(xor_inst1_in1),
    .out(xor_inst1_out)
);
assign O = xor_inst1_out;
endmodule

module corebit_and (
    input in0,
    input in1,
    output out
);
  assign out = in0 & in1;
endmodule

module Or3xNone (
    input I0,
    input I1,
    input I2,
    output O
);
wire [2:0] orr_inst0_in;
wire orr_inst0_out;
assign orr_inst0_in = {I2,I1,I0};
coreir_orr #(
    .width(3)
) orr_inst0 (
    .in(orr_inst0_in),
    .out(orr_inst0_out)
);
assign O = orr_inst0_out;
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
wire Or3xNone_inst0_O;
wire and_inst0_in0;
wire and_inst0_in1;
wire and_inst0_out;
wire and_inst1_in0;
wire and_inst1_in1;
wire and_inst1_out;
wire and_inst2_in0;
wire and_inst2_in1;
wire and_inst2_out;
wire fold_xor3None_inst0_I0;
wire fold_xor3None_inst0_I1;
wire fold_xor3None_inst0_I2;
wire fold_xor3None_inst0_O;
assign Or3xNone_inst0_I0 = and_inst0_out;
assign Or3xNone_inst0_I1 = and_inst1_out;
assign Or3xNone_inst0_I2 = and_inst2_out;
Or3xNone Or3xNone_inst0 (
    .I0(Or3xNone_inst0_I0),
    .I1(Or3xNone_inst0_I1),
    .I2(Or3xNone_inst0_I2),
    .O(Or3xNone_inst0_O)
);
assign and_inst0_in0 = I0;
assign and_inst0_in1 = I1;
corebit_and and_inst0 (
    .in0(and_inst0_in0),
    .in1(and_inst0_in1),
    .out(and_inst0_out)
);
assign and_inst1_in0 = I1;
assign and_inst1_in1 = CIN;
corebit_and and_inst1 (
    .in0(and_inst1_in0),
    .in1(and_inst1_in1),
    .out(and_inst1_out)
);
assign and_inst2_in0 = I0;
assign and_inst2_in1 = CIN;
corebit_and and_inst2 (
    .in0(and_inst2_in0),
    .in1(and_inst2_in1),
    .out(and_inst2_out)
);
assign fold_xor3None_inst0_I0 = I0;
assign fold_xor3None_inst0_I1 = I1;
assign fold_xor3None_inst0_I2 = CIN;
fold_xor3None fold_xor3None_inst0 (
    .I0(fold_xor3None_inst0_I0),
    .I1(fold_xor3None_inst0_I1),
    .I2(fold_xor3None_inst0_I2),
    .O(fold_xor3None_inst0_O)
);
assign O = fold_xor3None_inst0_O;
assign COUT = Or3xNone_inst0_O;
endmodule

