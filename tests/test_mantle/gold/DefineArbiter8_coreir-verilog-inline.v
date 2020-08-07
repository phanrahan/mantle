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
assign coreir_lut2_inst0_in = {I1,I0};
lutN #(
    .init(4'h2),
    .N(2)
) coreir_lut2_inst0 (
    .in(coreir_lut2_inst0_in),
    .out(O)
);
endmodule

module Arbiter8 (
    input [7:0] I,
    output [7:0] O
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
wire LUT2_2_inst4_I0;
wire LUT2_2_inst4_I1;
wire LUT2_2_inst4_O;
wire LUT2_2_inst5_I0;
wire LUT2_2_inst5_I1;
wire LUT2_2_inst5_O;
wire LUT2_2_inst6_I0;
wire LUT2_2_inst6_I1;
wire LUT2_2_inst6_O;
wire LUT2_2_inst7_I0;
wire LUT2_2_inst7_I1;
wire LUT2_2_inst7_O;
wire [7:0] coreir_add8_inst0_out;
assign LUT2_2_inst0_I0 = I[0];
assign LUT2_2_inst0_I1 = coreir_add8_inst0_out[0];
LUT2_2 LUT2_2_inst0 (
    .I0(LUT2_2_inst0_I0),
    .I1(LUT2_2_inst0_I1),
    .O(LUT2_2_inst0_O)
);
assign LUT2_2_inst1_I0 = I[1];
assign LUT2_2_inst1_I1 = coreir_add8_inst0_out[1];
LUT2_2 LUT2_2_inst1 (
    .I0(LUT2_2_inst1_I0),
    .I1(LUT2_2_inst1_I1),
    .O(LUT2_2_inst1_O)
);
assign LUT2_2_inst2_I0 = I[2];
assign LUT2_2_inst2_I1 = coreir_add8_inst0_out[2];
LUT2_2 LUT2_2_inst2 (
    .I0(LUT2_2_inst2_I0),
    .I1(LUT2_2_inst2_I1),
    .O(LUT2_2_inst2_O)
);
assign LUT2_2_inst3_I0 = I[3];
assign LUT2_2_inst3_I1 = coreir_add8_inst0_out[3];
LUT2_2 LUT2_2_inst3 (
    .I0(LUT2_2_inst3_I0),
    .I1(LUT2_2_inst3_I1),
    .O(LUT2_2_inst3_O)
);
assign LUT2_2_inst4_I0 = I[4];
assign LUT2_2_inst4_I1 = coreir_add8_inst0_out[4];
LUT2_2 LUT2_2_inst4 (
    .I0(LUT2_2_inst4_I0),
    .I1(LUT2_2_inst4_I1),
    .O(LUT2_2_inst4_O)
);
assign LUT2_2_inst5_I0 = I[5];
assign LUT2_2_inst5_I1 = coreir_add8_inst0_out[5];
LUT2_2 LUT2_2_inst5 (
    .I0(LUT2_2_inst5_I0),
    .I1(LUT2_2_inst5_I1),
    .O(LUT2_2_inst5_O)
);
assign LUT2_2_inst6_I0 = I[6];
assign LUT2_2_inst6_I1 = coreir_add8_inst0_out[6];
LUT2_2 LUT2_2_inst6 (
    .I0(LUT2_2_inst6_I0),
    .I1(LUT2_2_inst6_I1),
    .O(LUT2_2_inst6_O)
);
assign LUT2_2_inst7_I0 = I[7];
assign LUT2_2_inst7_I1 = coreir_add8_inst0_out[7];
LUT2_2 LUT2_2_inst7 (
    .I0(LUT2_2_inst7_I0),
    .I1(LUT2_2_inst7_I1),
    .O(LUT2_2_inst7_O)
);
assign coreir_add8_inst0_out = 8'(I + 8'hff);
assign O = {LUT2_2_inst7_O,LUT2_2_inst6_O,LUT2_2_inst5_O,LUT2_2_inst4_O,LUT2_2_inst3_O,LUT2_2_inst2_O,LUT2_2_inst1_O,LUT2_2_inst0_O};
endmodule

