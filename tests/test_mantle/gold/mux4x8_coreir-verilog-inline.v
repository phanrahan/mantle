module coreir_slice #(parameter hi = 1, parameter lo = 0, parameter width = 1) (input [width-1:0] in, output [hi-lo-1:0] out);
  assign out = in[hi-1:lo];
endmodule

module coreir_mux #(parameter width = 1) (input [width-1:0] in0, input [width-1:0] in1, input sel, output [width-1:0] out);
  assign out = sel ? in1 : in0;
endmodule

module commonlib_muxn__N2__width8 (input [7:0] in_data_0, input [7:0] in_data_1, input [0:0] in_sel, output [7:0] out);
coreir_mux #(.width(8)) _join(.in0(in_data_0), .in1(in_data_1), .out(out), .sel(in_sel[0]));
endmodule

module commonlib_muxn__N4__width8 (input [7:0] in_data_0, input [7:0] in_data_1, input [7:0] in_data_2, input [7:0] in_data_3, input [1:0] in_sel, output [7:0] out);
wire [7:0] muxN_0_out;
wire [7:0] muxN_1_out;
wire [0:0] sel_slice0_out;
wire [0:0] sel_slice1_out;
coreir_mux #(.width(8)) _join(.in0(muxN_0_out), .in1(muxN_1_out), .out(out), .sel(in_sel[1]));
commonlib_muxn__N2__width8 muxN_0(.in_data_0(in_data_0), .in_data_1(in_data_1), .in_sel(sel_slice0_out), .out(muxN_0_out));
commonlib_muxn__N2__width8 muxN_1(.in_data_0(in_data_2), .in_data_1(in_data_3), .in_sel(sel_slice1_out), .out(muxN_1_out));
coreir_slice #(.hi(1), .lo(0), .width(2)) sel_slice0(.in(in_sel), .out(sel_slice0_out));
coreir_slice #(.hi(1), .lo(0), .width(2)) sel_slice1(.in(in_sel), .out(sel_slice1_out));
endmodule

module Mux4x8 (input [7:0] I0, input [7:0] I1, input [7:0] I2, input [7:0] I3, output [7:0] O, input [1:0] S);
commonlib_muxn__N4__width8 coreir_commonlib_mux4x8_inst0(.in_data_0(I0), .in_data_1(I1), .in_data_2(I2), .in_data_3(I3), .in_sel(S), .out(O));
endmodule

