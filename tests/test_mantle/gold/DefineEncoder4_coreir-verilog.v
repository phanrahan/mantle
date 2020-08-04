module corebit_or (
    input in0,
    input in1,
    output out
);
  assign out = in0 | in1;
endmodule

module Encoder4 (
    input [3:0] I,
    output [1:0] O
);
wire or_inst0_in0;
wire or_inst0_in1;
wire or_inst0_out;
wire or_inst1_in0;
wire or_inst1_in1;
wire or_inst1_out;
assign or_inst0_in0 = I[1];
assign or_inst0_in1 = I[3];
corebit_or or_inst0 (
    .in0(or_inst0_in0),
    .in1(or_inst0_in1),
    .out(or_inst0_out)
);
assign or_inst1_in0 = I[2];
assign or_inst1_in1 = I[3];
corebit_or or_inst1 (
    .in0(or_inst1_in0),
    .in1(or_inst1_in1),
    .out(or_inst1_out)
);
assign O = {or_inst1_out,or_inst0_out};
endmodule

