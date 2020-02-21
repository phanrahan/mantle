module commonlib_muxn__N2__width2 (input [1:0] in_data_0, input [1:0] in_data_1, input [0:0] in_sel, output [1:0] out);
assign out = in_sel[0] ? in_data_1 : in_data_0;
endmodule

module commonlib_muxn__N4__width2 (input [1:0] in_data_0, input [1:0] in_data_1, input [1:0] in_data_2, input [1:0] in_data_3, input [1:0] in_sel, output [1:0] out);
wire [1:0] muxN_0_out;
wire [1:0] muxN_1_out;
commonlib_muxn__N2__width2 muxN_0(.in_data_0(in_data_0), .in_data_1(in_data_1), .in_sel(in_sel[1 - 1:0]), .out(muxN_0_out));
commonlib_muxn__N2__width2 muxN_1(.in_data_0(in_data_2), .in_data_1(in_data_3), .in_sel(in_sel[1 - 1:0]), .out(muxN_1_out));
assign out = in_sel[1] ? muxN_1_out : muxN_0_out;
endmodule

module Mux4x2 (input [1:0] I0, input [1:0] I1, input [1:0] I2, input [1:0] I3, input [1:0] S, output [1:0] O);
commonlib_muxn__N4__width2 coreir_commonlib_mux4x2_inst0(.in_data_0(I0), .in_data_1(I1), .in_data_2(I2), .in_data_3(I3), .in_sel(S), .out(O));
endmodule

