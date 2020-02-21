module commonlib_muxn__N2__width2 (
    input [1:0] in_data_0,
    input [1:0] in_data_1,
    input [0:0] in_sel,
    output [1:0] out
);
assign out = in_sel[0] ? in_data_1 : in_data_0;
endmodule

module commonlib_muxn__N4__width2 (
    input [1:0] in_data_0,
    input [1:0] in_data_1,
    input [1:0] in_data_2,
    input [1:0] in_data_3,
    input [1:0] in_sel,
    output [1:0] out
);
wire [1:0] muxN_0_out;
wire [1:0] muxN_1_out;
commonlib_muxn__N2__width2 muxN_0 (
    .in_data_0(in_data_0),
    .in_data_1(in_data_1),
    .in_sel(in_sel[1 - 1:0]),
    .out(muxN_0_out)
);
commonlib_muxn__N2__width2 muxN_1 (
    .in_data_0(in_data_2),
    .in_data_1(in_data_3),
    .in_sel(in_sel[1 - 1:0]),
    .out(muxN_1_out)
);
assign out = in_sel[1] ? muxN_1_out : muxN_0_out;
endmodule

module commonlib_muxn__N8__width2 (
    input [1:0] in_data_0,
    input [1:0] in_data_1,
    input [1:0] in_data_2,
    input [1:0] in_data_3,
    input [1:0] in_data_4,
    input [1:0] in_data_5,
    input [1:0] in_data_6,
    input [1:0] in_data_7,
    input [2:0] in_sel,
    output [1:0] out
);
wire [1:0] muxN_0_out;
wire [1:0] muxN_1_out;
commonlib_muxn__N4__width2 muxN_0 (
    .in_data_0(in_data_0),
    .in_data_1(in_data_1),
    .in_data_2(in_data_2),
    .in_data_3(in_data_3),
    .in_sel(in_sel[2 - 1:0]),
    .out(muxN_0_out)
);
commonlib_muxn__N4__width2 muxN_1 (
    .in_data_0(in_data_4),
    .in_data_1(in_data_5),
    .in_data_2(in_data_6),
    .in_data_3(in_data_7),
    .in_sel(in_sel[2 - 1:0]),
    .out(muxN_1_out)
);
assign out = in_sel[2] ? muxN_1_out : muxN_0_out;
endmodule

module Mux8x2 (
    input [1:0] I0,
    input [1:0] I1,
    input [1:0] I2,
    input [1:0] I3,
    input [1:0] I4,
    input [1:0] I5,
    input [1:0] I6,
    input [1:0] I7,
    input [2:0] S,
    output [1:0] O
);
commonlib_muxn__N8__width2 coreir_commonlib_mux8x2_inst0 (
    .in_data_0(I0),
    .in_data_1(I1),
    .in_data_2(I2),
    .in_data_3(I3),
    .in_data_4(I4),
    .in_data_5(I5),
    .in_data_6(I6),
    .in_data_7(I7),
    .in_sel(S),
    .out(O)
);
endmodule

