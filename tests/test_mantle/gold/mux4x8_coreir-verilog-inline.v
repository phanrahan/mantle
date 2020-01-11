module commonlib_muxn__N2__width8 (input [7:0] in_data_0, input [7:0] in_data_1, input [0:0] in_sel, output [7:0] out);
assign out = in_sel[0] ? in_data_1 : in_data_0;
endmodule

module commonlib_muxn__N4__width8 (input [7:0] in_data_0, input [7:0] in_data_1, input [7:0] in_data_2, input [7:0] in_data_3, input [1:0] in_sel, output [7:0] out);
wire [7:0] muxN_0_out;
wire [7:0] muxN_1_out;
commonlib_muxn__N2__width8 muxN_0(.in_data_0(in_data_0), .in_data_1(in_data_1), .in_sel(in_sel[1 - 1:0]), .out(muxN_0_out));
commonlib_muxn__N2__width8 muxN_1(.in_data_0(in_data_2), .in_data_1(in_data_3), .in_sel(in_sel[1 - 1:0]), .out(muxN_1_out));
assign out = in_sel[1] ? muxN_1_out : muxN_0_out;
endmodule

module Mux4x8 (input [7:0] I0, input [7:0] I1, input [7:0] I2, input [7:0] I3, output [7:0] O, input [1:0] S);
commonlib_muxn__N4__width8 coreir_commonlib_mux4x8_inst0(.in_data_0(I0), .in_data_1(I1), .in_data_2(I2), .in_data_3(I3), .in_sel(S), .out(O));
endmodule

