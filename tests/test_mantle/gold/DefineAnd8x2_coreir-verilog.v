module coreir_andr #(
    parameter width = 1
) (
    input [width-1:0] in,
    output out
);
  assign out = &in;
endmodule

module And8x2 (
    input [1:0] I0,
    input [1:0] I1,
    input [1:0] I2,
    input [1:0] I3,
    input [1:0] I4,
    input [1:0] I5,
    input [1:0] I6,
    input [1:0] I7,
    output [1:0] O
);
wire andr_inst0_out;
wire andr_inst1_out;
wire [7:0] andr_inst0_in;
assign andr_inst0_in = {I7[0],I6[0],I5[0],I4[0],I3[0],I2[0],I1[0],I0[0]};
coreir_andr #(
    .width(8)
) andr_inst0 (
    .in(andr_inst0_in),
    .out(andr_inst0_out)
);
wire [7:0] andr_inst1_in;
assign andr_inst1_in = {I7[1],I6[1],I5[1],I4[1],I3[1],I2[1],I1[1],I0[1]};
coreir_andr #(
    .width(8)
) andr_inst1 (
    .in(andr_inst1_in),
    .out(andr_inst1_out)
);
assign O = {andr_inst1_out,andr_inst0_out};
endmodule

