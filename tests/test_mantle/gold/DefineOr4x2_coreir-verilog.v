module coreir_orr #(
    parameter width = 1
) (
    input [width-1:0] in,
    output out
);
  assign out = |in;
endmodule

module Or4x2 (
    input [1:0] I0,
    input [1:0] I1,
    input [1:0] I2,
    input [1:0] I3,
    output [1:0] O
);
wire orr_inst0_out;
wire orr_inst1_out;
coreir_orr #(
    .width(4)
) orr_inst0 (
    .in({I3[0],I2[0],I1[0],I0[0]}),
    .out(orr_inst0_out)
);
coreir_orr #(
    .width(4)
) orr_inst1 (
    .in({I3[1],I2[1],I1[1],I0[1]}),
    .out(orr_inst1_out)
);
assign O = {orr_inst1_out,orr_inst0_out};
endmodule

