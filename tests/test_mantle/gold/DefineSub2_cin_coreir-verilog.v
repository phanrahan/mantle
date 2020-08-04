module coreir_not #(
    parameter width = 1
) (
    input [width-1:0] in,
    output [width-1:0] out
);
  assign out = ~in;
endmodule

module coreir_add #(
    parameter width = 1
) (
    input [width-1:0] in0,
    input [width-1:0] in1,
    output [width-1:0] out
);
  assign out = in0 + in1;
endmodule

module corebit_not (
    input in,
    output out
);
  assign out = ~in;
endmodule

module corebit_const #(
    parameter value = 1
) (
    output out
);
  assign out = value;
endmodule

module Add2_cin (
    input [1:0] I0,
    input [1:0] I1,
    output [1:0] O,
    input CIN
);
wire bit_const_0_None_out;
wire [1:0] coreir_add2_inst0_in0;
wire [1:0] coreir_add2_inst0_in1;
wire [1:0] coreir_add2_inst0_out;
wire [1:0] coreir_add2_inst1_in0;
wire [1:0] coreir_add2_inst1_in1;
wire [1:0] coreir_add2_inst1_out;
corebit_const #(
    .value(1'b0)
) bit_const_0_None (
    .out(bit_const_0_None_out)
);
assign coreir_add2_inst0_in0 = coreir_add2_inst1_out;
assign coreir_add2_inst0_in1 = I1;
coreir_add #(
    .width(2)
) coreir_add2_inst0 (
    .in0(coreir_add2_inst0_in0),
    .in1(coreir_add2_inst0_in1),
    .out(coreir_add2_inst0_out)
);
assign coreir_add2_inst1_in0 = {bit_const_0_None_out,CIN};
assign coreir_add2_inst1_in1 = I0;
coreir_add #(
    .width(2)
) coreir_add2_inst1 (
    .in0(coreir_add2_inst1_in0),
    .in1(coreir_add2_inst1_in1),
    .out(coreir_add2_inst1_out)
);
assign O = coreir_add2_inst0_out;
endmodule

module Sub2_cin (
    input [1:0] I0,
    input [1:0] I1,
    output [1:0] O,
    input CIN
);
wire [1:0] Add2_cin_inst0_I0;
wire [1:0] Add2_cin_inst0_I1;
wire [1:0] Add2_cin_inst0_O;
wire Add2_cin_inst0_CIN;
wire [1:0] Invert2_inst0_in;
wire [1:0] Invert2_inst0_out;
wire not_inst0_in;
wire not_inst0_out;
assign Add2_cin_inst0_I0 = I0;
assign Add2_cin_inst0_I1 = Invert2_inst0_out;
assign Add2_cin_inst0_CIN = not_inst0_out;
Add2_cin Add2_cin_inst0 (
    .I0(Add2_cin_inst0_I0),
    .I1(Add2_cin_inst0_I1),
    .O(Add2_cin_inst0_O),
    .CIN(Add2_cin_inst0_CIN)
);
assign Invert2_inst0_in = I1;
coreir_not #(
    .width(2)
) Invert2_inst0 (
    .in(Invert2_inst0_in),
    .out(Invert2_inst0_out)
);
assign not_inst0_in = CIN;
corebit_not not_inst0 (
    .in(not_inst0_in),
    .out(not_inst0_out)
);
assign O = Add2_cin_inst0_O;
endmodule

