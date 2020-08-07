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

module corebit_const #(
    parameter value = 1
) (
    output out
);
  assign out = value;
endmodule

module Add4_cin (
    input [3:0] I0,
    input [3:0] I1,
    output [3:0] O,
    input CIN
);
wire bit_const_0_None_out;
wire [3:0] coreir_add4_inst0_in0;
wire [3:0] coreir_add4_inst0_in1;
wire [3:0] coreir_add4_inst0_out;
wire [3:0] coreir_add4_inst1_in0;
wire [3:0] coreir_add4_inst1_in1;
wire [3:0] coreir_add4_inst1_out;
corebit_const #(
    .value(1'b0)
) bit_const_0_None (
    .out(bit_const_0_None_out)
);
assign coreir_add4_inst0_in0 = coreir_add4_inst1_out;
assign coreir_add4_inst0_in1 = I1;
coreir_add #(
    .width(4)
) coreir_add4_inst0 (
    .in0(coreir_add4_inst0_in0),
    .in1(coreir_add4_inst0_in1),
    .out(coreir_add4_inst0_out)
);
assign coreir_add4_inst1_in0 = {bit_const_0_None_out,bit_const_0_None_out,bit_const_0_None_out,CIN};
assign coreir_add4_inst1_in1 = I0;
coreir_add #(
    .width(4)
) coreir_add4_inst1 (
    .in0(coreir_add4_inst1_in0),
    .in1(coreir_add4_inst1_in1),
    .out(coreir_add4_inst1_out)
);
assign O = coreir_add4_inst0_out;
endmodule

module Sub4 (
    input [3:0] I0,
    input [3:0] I1,
    output [3:0] O
);
wire [3:0] Add4_cin_inst0_I0;
wire [3:0] Add4_cin_inst0_I1;
wire [3:0] Add4_cin_inst0_O;
wire Add4_cin_inst0_CIN;
wire [3:0] Invert4_inst0_in;
wire [3:0] Invert4_inst0_out;
wire bit_const_1_None_out;
assign Add4_cin_inst0_I0 = I0;
assign Add4_cin_inst0_I1 = Invert4_inst0_out;
assign Add4_cin_inst0_CIN = bit_const_1_None_out;
Add4_cin Add4_cin_inst0 (
    .I0(Add4_cin_inst0_I0),
    .I1(Add4_cin_inst0_I1),
    .O(Add4_cin_inst0_O),
    .CIN(Add4_cin_inst0_CIN)
);
assign Invert4_inst0_in = I1;
coreir_not #(
    .width(4)
) Invert4_inst0 (
    .in(Invert4_inst0_in),
    .out(Invert4_inst0_out)
);
corebit_const #(
    .value(1'b1)
) bit_const_1_None (
    .out(bit_const_1_None_out)
);
assign O = Add4_cin_inst0_O;
endmodule

