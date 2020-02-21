module coreir_andr #(
    parameter width = 1
) (
    input [width-1:0] in,
    output out
);
  assign out = &in;
endmodule

module And4x8 (
    input [7:0] I0,
    input [7:0] I1,
    input [7:0] I2,
    input [7:0] I3,
    output [7:0] O
);
wire andr_inst0_out;
wire andr_inst1_out;
wire andr_inst2_out;
wire andr_inst3_out;
wire andr_inst4_out;
wire andr_inst5_out;
wire andr_inst6_out;
wire andr_inst7_out;
coreir_andr #(
    .width(4)
) andr_inst0 (
    .in({I3[0],I2[0],I1[0],I0[0]}),
    .out(andr_inst0_out)
);
coreir_andr #(
    .width(4)
) andr_inst1 (
    .in({I3[1],I2[1],I1[1],I0[1]}),
    .out(andr_inst1_out)
);
coreir_andr #(
    .width(4)
) andr_inst2 (
    .in({I3[2],I2[2],I1[2],I0[2]}),
    .out(andr_inst2_out)
);
coreir_andr #(
    .width(4)
) andr_inst3 (
    .in({I3[3],I2[3],I1[3],I0[3]}),
    .out(andr_inst3_out)
);
coreir_andr #(
    .width(4)
) andr_inst4 (
    .in({I3[4],I2[4],I1[4],I0[4]}),
    .out(andr_inst4_out)
);
coreir_andr #(
    .width(4)
) andr_inst5 (
    .in({I3[5],I2[5],I1[5],I0[5]}),
    .out(andr_inst5_out)
);
coreir_andr #(
    .width(4)
) andr_inst6 (
    .in({I3[6],I2[6],I1[6],I0[6]}),
    .out(andr_inst6_out)
);
coreir_andr #(
    .width(4)
) andr_inst7 (
    .in({I3[7],I2[7],I1[7],I0[7]}),
    .out(andr_inst7_out)
);
assign O = {andr_inst7_out,andr_inst6_out,andr_inst5_out,andr_inst4_out,andr_inst3_out,andr_inst2_out,andr_inst1_out,andr_inst0_out};
endmodule

