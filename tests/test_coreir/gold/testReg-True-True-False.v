module coreir_reg_arst #(
    parameter width = 1,
    parameter arst_posedge = 1,
    parameter clk_posedge = 1,
    parameter init = 1
) (
    input clk,
    input arst,
    input [width-1:0] in,
    output [width-1:0] out
);
  reg [width-1:0] outReg;
  wire real_rst;
  assign real_rst = arst_posedge ? arst : ~arst;
  wire real_clk;
  assign real_clk = clk_posedge ? clk : ~clk;
  always @(posedge real_clk, posedge real_rst) begin
    if (real_rst) outReg <= init;
    else outReg <= in;
  end
  assign out = outReg;
endmodule

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

module commonlib_muxn__N2__width1 (
    input [0:0] in_data [1:0],
    input [0:0] in_sel,
    output [0:0] out
);
wire [0:0] _join_in0;
wire [0:0] _join_in1;
wire _join_sel;
wire [0:0] _join_out;
assign _join_in0 = in_data[0];
assign _join_in1 = in_data[1];
assign _join_sel = in_sel[0];
coreir_mux #(
    .width(1)
) _join (
    .in0(_join_in0),
    .in1(_join_in1),
    .sel(_join_sel),
    .out(_join_out)
);
assign out = _join_out;
endmodule

module Mux2xOutBits1 (
    input [0:0] I0,
    input [0:0] I1,
    input S,
    output [0:0] O
);
wire [0:0] coreir_commonlib_mux2x1_inst0_in_data [1:0];
wire [0:0] coreir_commonlib_mux2x1_inst0_in_sel;
wire [0:0] coreir_commonlib_mux2x1_inst0_out;
assign coreir_commonlib_mux2x1_inst0_in_data[1] = I1;
assign coreir_commonlib_mux2x1_inst0_in_data[0] = I0;
assign coreir_commonlib_mux2x1_inst0_in_sel[0] = S;
commonlib_muxn__N2__width1 coreir_commonlib_mux2x1_inst0 (
    .in_data(coreir_commonlib_mux2x1_inst0_in_data),
    .in_sel(coreir_commonlib_mux2x1_inst0_in_sel),
    .out(coreir_commonlib_mux2x1_inst0_out)
);
assign O = coreir_commonlib_mux2x1_inst0_out;
endmodule

module Register_has_ce_True_has_reset_False_has_async_reset_True_has_async_resetn_False_type_Bits_n_1 (
    input [0:0] I,
    output [0:0] O,
    input CLK,
    input CE,
    input ASYNCRESET
);
wire [0:0] enable_mux_I0;
wire [0:0] enable_mux_I1;
wire enable_mux_S;
wire [0:0] enable_mux_O;
wire value_clk;
wire value_arst;
wire [0:0] value_in;
wire [0:0] value_out;
assign enable_mux_I0 = value_out;
assign enable_mux_I1 = I;
assign enable_mux_S = CE;
Mux2xOutBits1 enable_mux (
    .I0(enable_mux_I0),
    .I1(enable_mux_I1),
    .S(enable_mux_S),
    .O(enable_mux_O)
);
assign value_clk = CLK;
assign value_arst = ASYNCRESET;
assign value_in = enable_mux_O;
coreir_reg_arst #(
    .arst_posedge(1'b1),
    .clk_posedge(1'b1),
    .init(1'h0),
    .width(1)
) value (
    .clk(value_clk),
    .arst(value_arst),
    .in(value_in),
    .out(value_out)
);
assign O = value_out;
endmodule

module test (
    input clk,
    input [0:0] In0,
    output [0:0] Out0,
    input CLK,
    input CE,
    input ASYNCRESET
);
wire [0:0] Register_has_ce_True_has_reset_False_has_async_reset_True_has_async_resetn_False_type_Bits_n_1_inst0_I;
wire [0:0] Register_has_ce_True_has_reset_False_has_async_reset_True_has_async_resetn_False_type_Bits_n_1_inst0_O;
wire Register_has_ce_True_has_reset_False_has_async_reset_True_has_async_resetn_False_type_Bits_n_1_inst0_CLK;
wire Register_has_ce_True_has_reset_False_has_async_reset_True_has_async_resetn_False_type_Bits_n_1_inst0_CE;
wire Register_has_ce_True_has_reset_False_has_async_reset_True_has_async_resetn_False_type_Bits_n_1_inst0_ASYNCRESET;
assign Register_has_ce_True_has_reset_False_has_async_reset_True_has_async_resetn_False_type_Bits_n_1_inst0_I = In0;
assign Register_has_ce_True_has_reset_False_has_async_reset_True_has_async_resetn_False_type_Bits_n_1_inst0_CLK = clk;
assign Register_has_ce_True_has_reset_False_has_async_reset_True_has_async_resetn_False_type_Bits_n_1_inst0_CE = CE;
assign Register_has_ce_True_has_reset_False_has_async_reset_True_has_async_resetn_False_type_Bits_n_1_inst0_ASYNCRESET = ASYNCRESET;
Register_has_ce_True_has_reset_False_has_async_reset_True_has_async_resetn_False_type_Bits_n_1 Register_has_ce_True_has_reset_False_has_async_reset_True_has_async_resetn_False_type_Bits_n_1_inst0 (
    .I(Register_has_ce_True_has_reset_False_has_async_reset_True_has_async_resetn_False_type_Bits_n_1_inst0_I),
    .O(Register_has_ce_True_has_reset_False_has_async_reset_True_has_async_resetn_False_type_Bits_n_1_inst0_O),
    .CLK(Register_has_ce_True_has_reset_False_has_async_reset_True_has_async_resetn_False_type_Bits_n_1_inst0_CLK),
    .CE(Register_has_ce_True_has_reset_False_has_async_reset_True_has_async_resetn_False_type_Bits_n_1_inst0_CE),
    .ASYNCRESET(Register_has_ce_True_has_reset_False_has_async_reset_True_has_async_resetn_False_type_Bits_n_1_inst0_ASYNCRESET)
);
assign Out0 = Register_has_ce_True_has_reset_False_has_async_reset_True_has_async_resetn_False_type_Bits_n_1_inst0_O;
endmodule

