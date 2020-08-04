module coreir_const #(
    parameter width = 1,
    parameter value = 1
) (
    output [width-1:0] out
);
  assign out = value;
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

module lutN #(
    parameter N = 1,
    parameter init = 1
) (
    input [N-1:0] in,
    output out
);
  assign out = init[in];
endmodule

module LUT2_2 (
    input I0,
    input I1,
    output O
);
wire [1:0] coreir_lut2_inst0_in;
wire coreir_lut2_inst0_out;
assign coreir_lut2_inst0_in = {I1,I0};
lutN #(
    .init(4'h2),
    .N(2)
) coreir_lut2_inst0 (
    .in(coreir_lut2_inst0_in),
    .out(coreir_lut2_inst0_out)
);
assign O = coreir_lut2_inst0_out;
endmodule

module Arbiter4 (
    input [3:0] I,
    output [3:0] O
);
wire LUT2_2_inst0_I0;
wire LUT2_2_inst0_I1;
wire LUT2_2_inst0_O;
wire LUT2_2_inst1_I0;
wire LUT2_2_inst1_I1;
wire LUT2_2_inst1_O;
wire LUT2_2_inst2_I0;
wire LUT2_2_inst2_I1;
wire LUT2_2_inst2_O;
wire LUT2_2_inst3_I0;
wire LUT2_2_inst3_I1;
wire LUT2_2_inst3_O;
wire [3:0] const_15_4_out;
wire [3:0] coreir_add4_inst0_in0;
wire [3:0] coreir_add4_inst0_in1;
wire [3:0] coreir_add4_inst0_out;
assign LUT2_2_inst0_I0 = I[0];
assign LUT2_2_inst0_I1 = coreir_add4_inst0_out[0];
LUT2_2 LUT2_2_inst0 (
    .I0(LUT2_2_inst0_I0),
    .I1(LUT2_2_inst0_I1),
    .O(LUT2_2_inst0_O)
);
assign LUT2_2_inst1_I0 = I[1];
assign LUT2_2_inst1_I1 = coreir_add4_inst0_out[1];
LUT2_2 LUT2_2_inst1 (
    .I0(LUT2_2_inst1_I0),
    .I1(LUT2_2_inst1_I1),
    .O(LUT2_2_inst1_O)
);
assign LUT2_2_inst2_I0 = I[2];
assign LUT2_2_inst2_I1 = coreir_add4_inst0_out[2];
LUT2_2 LUT2_2_inst2 (
    .I0(LUT2_2_inst2_I0),
    .I1(LUT2_2_inst2_I1),
    .O(LUT2_2_inst2_O)
);
assign LUT2_2_inst3_I0 = I[3];
assign LUT2_2_inst3_I1 = coreir_add4_inst0_out[3];
LUT2_2 LUT2_2_inst3 (
    .I0(LUT2_2_inst3_I0),
    .I1(LUT2_2_inst3_I1),
    .O(LUT2_2_inst3_O)
);
coreir_const #(
    .value(4'hf),
    .width(4)
) const_15_4 (
    .out(const_15_4_out)
);
assign coreir_add4_inst0_in0 = I;
assign coreir_add4_inst0_in1 = const_15_4_out;
coreir_add #(
    .width(4)
) coreir_add4_inst0 (
    .in0(coreir_add4_inst0_in0),
    .in1(coreir_add4_inst0_in1),
    .out(coreir_add4_inst0_out)
);
assign O = {LUT2_2_inst3_O,LUT2_2_inst2_O,LUT2_2_inst1_O,LUT2_2_inst0_O};
endmodule

