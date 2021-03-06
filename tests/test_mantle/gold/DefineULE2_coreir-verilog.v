module coreir_ule #(
    parameter width = 1
) (
    input [width-1:0] in0,
    input [width-1:0] in1,
    output out
);
  assign out = in0 <= in1;
endmodule

module coreir_ule2_wrapped (
    input [1:0] I0,
    input [1:0] I1,
    output O
);
wire coreir_ule2_inst0_out;
coreir_ule #(
    .width(2)
) coreir_ule2_inst0 (
    .in0(I0),
    .in1(I1),
    .out(coreir_ule2_inst0_out)
);
assign O = coreir_ule2_inst0_out;
endmodule

