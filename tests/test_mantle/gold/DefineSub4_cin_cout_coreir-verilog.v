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

module Add4_cout_cin (
    input [3:0] I0,
    input [3:0] I1,
    output [3:0] O,
    output COUT,
    input CIN
);
wire bit_const_0_None_out;
wire [4:0] coreir_add5_inst0_out;
wire [4:0] coreir_add5_inst1_out;
corebit_const #(
    .value(1'b0)
) bit_const_0_None (
    .out(bit_const_0_None_out)
);
coreir_add #(
    .width(5)
) coreir_add5_inst0 (
    .in0(coreir_add5_inst1_out),
    .in1({bit_const_0_None_out,I1[3:0]}),
    .out(coreir_add5_inst0_out)
);
coreir_add #(
    .width(5)
) coreir_add5_inst1 (
    .in0({bit_const_0_None_out,bit_const_0_None_out,bit_const_0_None_out,bit_const_0_None_out,CIN}),
    .in1({bit_const_0_None_out,I0[3:0]}),
    .out(coreir_add5_inst1_out)
);
assign O = coreir_add5_inst0_out[3:0];
assign COUT = coreir_add5_inst0_out[4];
endmodule

module Sub4_cout_cin (
    input [3:0] I0,
    input [3:0] I1,
    output [3:0] O,
    output COUT,
    input CIN
);
wire [3:0] Add4_cout_cin_inst0_O;
wire Add4_cout_cin_inst0_COUT;
wire [3:0] Invert4_inst0_out;
wire not_inst0_out;
Add4_cout_cin Add4_cout_cin_inst0 (
    .I0(I0),
    .I1(Invert4_inst0_out),
    .O(Add4_cout_cin_inst0_O),
    .COUT(Add4_cout_cin_inst0_COUT),
    .CIN(not_inst0_out)
);
coreir_not #(
    .width(4)
) Invert4_inst0 (
    .in(I1),
    .out(Invert4_inst0_out)
);
corebit_not not_inst0 (
    .in(CIN),
    .out(not_inst0_out)
);
assign O = Add4_cout_cin_inst0_O;
assign COUT = Add4_cout_cin_inst0_COUT;
endmodule

