module commonlib_muxn__N2__width8 (
    input [7:0] in_data_0,
    input [7:0] in_data_1,
    input [0:0] in_sel,
    output [7:0] out
);
assign out = in_sel[0] ? in_data_1 : in_data_0;
endmodule

module Mux2x8 (
    input [7:0] I0,
    input [7:0] I1,
    input S,
    output [7:0] O
);
commonlib_muxn__N2__width8 coreir_commonlib_mux2x8_inst0 (
    .in_data_0(I0),
    .in_data_1(I1),
    .in_sel(S),
    .out(O)
);
endmodule

