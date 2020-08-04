module coreir_eq #(
    parameter width = 1
) (
    input [width-1:0] in0,
    input [width-1:0] in1,
    output out
);
  assign out = in0 == in1;
endmodule

module corebit_not (
    input in,
    output out
);
  assign out = ~in;
endmodule

module NE2 (
    input [1:0] I0,
    input [1:0] I1,
    output O
);
wire [1:0] coreir_eq_2_inst0_in0;
wire [1:0] coreir_eq_2_inst0_in1;
wire coreir_eq_2_inst0_out;
wire not_inst0_in;
wire not_inst0_out;
assign coreir_eq_2_inst0_in0 = I0;
assign coreir_eq_2_inst0_in1 = I1;
coreir_eq #(
    .width(2)
) coreir_eq_2_inst0 (
    .in0(coreir_eq_2_inst0_in0),
    .in1(coreir_eq_2_inst0_in1),
    .out(coreir_eq_2_inst0_out)
);
assign not_inst0_in = coreir_eq_2_inst0_out;
corebit_not not_inst0 (
    .in(not_inst0_in),
    .out(not_inst0_out)
);
assign O = not_inst0_out;
endmodule

