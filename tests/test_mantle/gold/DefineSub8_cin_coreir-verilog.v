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

module Add8_cin (
    input [7:0] I0,
    input [7:0] I1,
    output [7:0] O,
    input CIN
);
wire bit_const_0_None_out;
wire [7:0] coreir_add8_inst0_in0;
wire [7:0] coreir_add8_inst0_in1;
wire [7:0] coreir_add8_inst0_out;
wire [7:0] coreir_add8_inst1_in0;
wire [7:0] coreir_add8_inst1_in1;
wire [7:0] coreir_add8_inst1_out;
corebit_const #(
    .value(1'b0)
) bit_const_0_None (
    .out(bit_const_0_None_out)
);
assign coreir_add8_inst0_in0 = coreir_add8_inst1_out;
assign coreir_add8_inst0_in1 = I1;
coreir_add #(
    .width(8)
) coreir_add8_inst0 (
    .in0(coreir_add8_inst0_in0),
    .in1(coreir_add8_inst0_in1),
    .out(coreir_add8_inst0_out)
);
assign coreir_add8_inst1_in0 = {bit_const_0_None_out,bit_const_0_None_out,bit_const_0_None_out,bit_const_0_None_out,bit_const_0_None_out,bit_const_0_None_out,bit_const_0_None_out,CIN};
assign coreir_add8_inst1_in1 = I0;
coreir_add #(
    .width(8)
) coreir_add8_inst1 (
    .in0(coreir_add8_inst1_in0),
    .in1(coreir_add8_inst1_in1),
    .out(coreir_add8_inst1_out)
);
assign O = coreir_add8_inst0_out;
endmodule

module Sub8_cin (
    input [7:0] I0,
    input [7:0] I1,
    output [7:0] O,
    input CIN
);
wire [7:0] Add8_cin_inst0_I0;
wire [7:0] Add8_cin_inst0_I1;
wire [7:0] Add8_cin_inst0_O;
wire Add8_cin_inst0_CIN;
wire [7:0] Invert8_inst0_in;
wire [7:0] Invert8_inst0_out;
wire not_inst0_in;
wire not_inst0_out;
assign Add8_cin_inst0_I0 = I0;
assign Add8_cin_inst0_I1 = Invert8_inst0_out;
assign Add8_cin_inst0_CIN = not_inst0_out;
Add8_cin Add8_cin_inst0 (
    .I0(Add8_cin_inst0_I0),
    .I1(Add8_cin_inst0_I1),
    .O(Add8_cin_inst0_O),
    .CIN(Add8_cin_inst0_CIN)
);
assign Invert8_inst0_in = I1;
coreir_not #(
    .width(8)
) Invert8_inst0 (
    .in(Invert8_inst0_in),
    .out(Invert8_inst0_out)
);
assign not_inst0_in = CIN;
corebit_not not_inst0 (
    .in(not_inst0_in),
    .out(not_inst0_out)
);
assign O = Add8_cin_inst0_O;
endmodule

