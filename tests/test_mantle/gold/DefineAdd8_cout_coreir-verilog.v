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

module Add8_cout (
    input [7:0] I0,
    input [7:0] I1,
    output [7:0] O,
    output COUT
);
wire bit_const_0_None_out;
wire [8:0] coreir_add9_inst0_out;
corebit_const #(
    .value(1'b0)
) bit_const_0_None (
    .out(bit_const_0_None_out)
);
coreir_add #(
    .width(9)
) coreir_add9_inst0 (
    .in0({bit_const_0_None_out,I0[7:0]}),
    .in1({bit_const_0_None_out,I1[7:0]}),
    .out(coreir_add9_inst0_out)
);
assign O = coreir_add9_inst0_out[7:0];
assign COUT = coreir_add9_inst0_out[8];
endmodule

