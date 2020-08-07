module coreir_mux #(
    parameter width = 1
) (
    input [width-1:0] in0,
    input [width-1:0] in1,
    input sel,
    output [width-1:0] out
);
  assign out = sel ? in1 : in0;
endmodule

module commonlib_muxn__N2__width8 (
    input [7:0] in_data [1:0],
    input [0:0] in_sel,
    output [7:0] out
);
wire [7:0] _join_in0;
wire [7:0] _join_in1;
wire _join_sel;
wire [7:0] _join_out;
assign _join_in0 = in_data[0];
assign _join_in1 = in_data[1];
assign _join_sel = in_sel[0];
coreir_mux #(
    .width(8)
) _join (
    .in0(_join_in0),
    .in1(_join_in1),
    .sel(_join_sel),
    .out(_join_out)
);
assign out = _join_out;
endmodule

module Mux2x8 (
    input [7:0] I0,
    input [7:0] I1,
    input S,
    output [7:0] O
);
wire [7:0] coreir_commonlib_mux2x8_inst0_in_data [1:0];
wire [0:0] coreir_commonlib_mux2x8_inst0_in_sel;
wire [7:0] coreir_commonlib_mux2x8_inst0_out;
assign coreir_commonlib_mux2x8_inst0_in_data[1] = I1;
assign coreir_commonlib_mux2x8_inst0_in_data[0] = I0;
assign coreir_commonlib_mux2x8_inst0_in_sel[0] = S;
commonlib_muxn__N2__width8 coreir_commonlib_mux2x8_inst0 (
    .in_data(coreir_commonlib_mux2x8_inst0_in_data),
    .in_sel(coreir_commonlib_mux2x8_inst0_in_sel),
    .out(coreir_commonlib_mux2x8_inst0_out)
);
assign O = coreir_commonlib_mux2x8_inst0_out;
endmodule

