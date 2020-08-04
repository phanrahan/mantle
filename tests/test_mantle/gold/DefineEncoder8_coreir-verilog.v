module coreir_orr #(
    parameter width = 1
) (
    input [width-1:0] in,
    output out
);
  assign out = |in;
endmodule

module Or4xNone (
    input I0,
    input I1,
    input I2,
    input I3,
    output O
);
wire [3:0] orr_inst0_in;
wire orr_inst0_out;
assign orr_inst0_in = {I3,I2,I1,I0};
coreir_orr #(
    .width(4)
) orr_inst0 (
    .in(orr_inst0_in),
    .out(orr_inst0_out)
);
assign O = orr_inst0_out;
endmodule

module Encoder8 (
    input [7:0] I,
    output [2:0] O
);
wire Or4xNone_inst0_I0;
wire Or4xNone_inst0_I1;
wire Or4xNone_inst0_I2;
wire Or4xNone_inst0_I3;
wire Or4xNone_inst0_O;
wire Or4xNone_inst1_I0;
wire Or4xNone_inst1_I1;
wire Or4xNone_inst1_I2;
wire Or4xNone_inst1_I3;
wire Or4xNone_inst1_O;
wire Or4xNone_inst2_I0;
wire Or4xNone_inst2_I1;
wire Or4xNone_inst2_I2;
wire Or4xNone_inst2_I3;
wire Or4xNone_inst2_O;
assign Or4xNone_inst0_I0 = I[1];
assign Or4xNone_inst0_I1 = I[3];
assign Or4xNone_inst0_I2 = I[5];
assign Or4xNone_inst0_I3 = I[7];
Or4xNone Or4xNone_inst0 (
    .I0(Or4xNone_inst0_I0),
    .I1(Or4xNone_inst0_I1),
    .I2(Or4xNone_inst0_I2),
    .I3(Or4xNone_inst0_I3),
    .O(Or4xNone_inst0_O)
);
assign Or4xNone_inst1_I0 = I[2];
assign Or4xNone_inst1_I1 = I[3];
assign Or4xNone_inst1_I2 = I[6];
assign Or4xNone_inst1_I3 = I[7];
Or4xNone Or4xNone_inst1 (
    .I0(Or4xNone_inst1_I0),
    .I1(Or4xNone_inst1_I1),
    .I2(Or4xNone_inst1_I2),
    .I3(Or4xNone_inst1_I3),
    .O(Or4xNone_inst1_O)
);
assign Or4xNone_inst2_I0 = I[4];
assign Or4xNone_inst2_I1 = I[5];
assign Or4xNone_inst2_I2 = I[6];
assign Or4xNone_inst2_I3 = I[7];
Or4xNone Or4xNone_inst2 (
    .I0(Or4xNone_inst2_I0),
    .I1(Or4xNone_inst2_I1),
    .I2(Or4xNone_inst2_I2),
    .I3(Or4xNone_inst2_I3),
    .O(Or4xNone_inst2_O)
);
assign O = {Or4xNone_inst2_O,Or4xNone_inst1_O,Or4xNone_inst0_O};
endmodule

