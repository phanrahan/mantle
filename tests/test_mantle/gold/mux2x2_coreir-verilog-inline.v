module coreir_mux #(parameter width = 1) (input [width-1:0] in0, input [width-1:0] in1, input sel, output [width-1:0] out);
  assign out = sel ? in1 : in0;
endmodule

module commonlib_muxn__N2__width2 (input [1:0] in_data_0, input [1:0] in_data_1, input [0:0] in_sel, output [1:0] out);
coreir_mux #(.width(2)) _join(.in0(in_data_0), .in1(in_data_1), .out(out), .sel(in_sel[0]));
endmodule

module Mux2x2 (input [1:0] I0, input [1:0] I1, output [1:0] O, input S);
commonlib_muxn__N2__width2 coreir_commonlib_mux2x2_inst0(.in_data_0(I0), .in_data_1(I1), .in_sel(S), .out(O));
endmodule

