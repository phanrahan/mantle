module commonlib_muxn__N2__width4 (input [3:0] in_data_0, input [3:0] in_data_1, input [0:0] in_sel, output [3:0] out);
assign out = in_sel[0] ? in_data_1 : in_data_0;
endmodule

module Mux2x4 (input [3:0] I0, input [3:0] I1, output [3:0] O, input S);
commonlib_muxn__N2__width4 coreir_commonlib_mux2x4_inst0(.in_data_0(I0), .in_data_1(I1), .in_sel(S), .out(O));
endmodule

