module coreir_slice #(
    parameter hi = 1,
    parameter lo = 0,
    parameter width = 1
) (
    input [width-1:0] in,
    output [hi-lo-1:0] out
);
  assign out = in[hi-1:lo];
endmodule

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

module coreir_eq #(
    parameter width = 1
) (
    input [width-1:0] in0,
    input [width-1:0] in1,
    output out
);
  assign out = in0 == in1;
endmodule

module coreir_const #(
    parameter width = 1,
    parameter value = 1
) (
    output [width-1:0] out
);
  assign out = value;
endmodule

module commonlib_muxn__N2__width4 (
    input [3:0] in_data_0,
    input [3:0] in_data_1,
    input [0:0] in_sel,
    output [3:0] out
);
wire [3:0] _join_out;
coreir_mux #(
    .width(4)
) _join (
    .in0(in_data_0),
    .in1(in_data_1),
    .sel(in_sel[0]),
    .out(_join_out)
);
assign out = _join_out;
endmodule

module commonlib_muxn__N4__width4 (
    input [3:0] in_data_0,
    input [3:0] in_data_1,
    input [3:0] in_data_2,
    input [3:0] in_data_3,
    input [1:0] in_sel,
    output [3:0] out
);
wire [3:0] _join_out;
wire [3:0] muxN_0_out;
wire [3:0] muxN_1_out;
wire [0:0] sel_slice0_out;
wire [0:0] sel_slice1_out;
coreir_mux #(
    .width(4)
) _join (
    .in0(muxN_0_out),
    .in1(muxN_1_out),
    .sel(in_sel[1]),
    .out(_join_out)
);
commonlib_muxn__N2__width4 muxN_0 (
    .in_data_0(in_data_0),
    .in_data_1(in_data_1),
    .in_sel(sel_slice0_out),
    .out(muxN_0_out)
);
commonlib_muxn__N2__width4 muxN_1 (
    .in_data_0(in_data_2),
    .in_data_1(in_data_3),
    .in_sel(sel_slice1_out),
    .out(muxN_1_out)
);
coreir_slice #(
    .hi(1),
    .lo(0),
    .width(2)
) sel_slice0 (
    .in(in_sel),
    .out(sel_slice0_out)
);
coreir_slice #(
    .hi(1),
    .lo(0),
    .width(2)
) sel_slice1 (
    .in(in_sel),
    .out(sel_slice1_out)
);
assign out = _join_out;
endmodule

module Mux4xBits4 (
    input [3:0] I0,
    input [3:0] I1,
    input [3:0] I2,
    input [3:0] I3,
    input [1:0] S,
    output [3:0] O
);
wire [3:0] coreir_commonlib_mux4x4_inst0_out;
commonlib_muxn__N4__width4 coreir_commonlib_mux4x4_inst0 (
    .in_data_0(I0),
    .in_data_1(I1),
    .in_data_2(I2),
    .in_data_3(I3),
    .in_sel(S),
    .out(coreir_commonlib_mux4x4_inst0_out)
);
assign O = coreir_commonlib_mux4x4_inst0_out;
endmodule

module Mux2xBits4 (
    input [3:0] I0,
    input [3:0] I1,
    input S,
    output [3:0] O
);
wire [3:0] coreir_commonlib_mux2x4_inst0_out;
commonlib_muxn__N2__width4 coreir_commonlib_mux2x4_inst0 (
    .in_data_0(I0),
    .in_data_1(I1),
    .in_sel(S),
    .out(coreir_commonlib_mux2x4_inst0_out)
);
assign O = coreir_commonlib_mux2x4_inst0_out;
endmodule

module my_regfile (
    input ASYNCRESET,
    input CLK,
    input [1:0] read_0_addr,
    output [3:0] read_0_data,
    input [1:0] write_0_addr,
    input [3:0] write_0_data
);
wire [3:0] Mux2xBits4_inst0_O;
wire [3:0] Mux2xBits4_inst1_O;
wire [3:0] Mux2xBits4_inst2_O;
wire [3:0] Mux2xBits4_inst3_O;
wire [3:0] Mux4xBits4_inst0_O;
wire [1:0] const_0_2_out;
wire [1:0] const_1_2_out;
wire [1:0] const_2_2_out;
wire [1:0] const_3_2_out;
wire magma_Bits_2_eq_inst0_out;
wire magma_Bits_2_eq_inst1_out;
wire magma_Bits_2_eq_inst2_out;
wire magma_Bits_2_eq_inst3_out;
wire [3:0] reg_PR_inst0_out;
wire [3:0] reg_PR_inst1_out;
wire [3:0] reg_PR_inst2_out;
wire [3:0] reg_PR_inst3_out;
Mux2xBits4 Mux2xBits4_inst0 (
    .I0(reg_PR_inst0_out),
    .I1(write_0_data),
    .S(magma_Bits_2_eq_inst0_out),
    .O(Mux2xBits4_inst0_O)
);
Mux2xBits4 Mux2xBits4_inst1 (
    .I0(reg_PR_inst1_out),
    .I1(write_0_data),
    .S(magma_Bits_2_eq_inst1_out),
    .O(Mux2xBits4_inst1_O)
);
Mux2xBits4 Mux2xBits4_inst2 (
    .I0(reg_PR_inst2_out),
    .I1(write_0_data),
    .S(magma_Bits_2_eq_inst2_out),
    .O(Mux2xBits4_inst2_O)
);
Mux2xBits4 Mux2xBits4_inst3 (
    .I0(reg_PR_inst3_out),
    .I1(write_0_data),
    .S(magma_Bits_2_eq_inst3_out),
    .O(Mux2xBits4_inst3_O)
);
Mux4xBits4 Mux4xBits4_inst0 (
    .I0(reg_PR_inst0_out),
    .I1(reg_PR_inst1_out),
    .I2(reg_PR_inst2_out),
    .I3(reg_PR_inst3_out),
    .S(read_0_addr),
    .O(Mux4xBits4_inst0_O)
);
coreir_const #(
    .value(2'h0),
    .width(2)
) const_0_2 (
    .out(const_0_2_out)
);
coreir_const #(
    .value(2'h1),
    .width(2)
) const_1_2 (
    .out(const_1_2_out)
);
coreir_const #(
    .value(2'h2),
    .width(2)
) const_2_2 (
    .out(const_2_2_out)
);
coreir_const #(
    .value(2'h3),
    .width(2)
) const_3_2 (
    .out(const_3_2_out)
);
coreir_eq #(
    .width(2)
) magma_Bits_2_eq_inst0 (
    .in0(write_0_addr),
    .in1(const_0_2_out),
    .out(magma_Bits_2_eq_inst0_out)
);
coreir_eq #(
    .width(2)
) magma_Bits_2_eq_inst1 (
    .in0(write_0_addr),
    .in1(const_1_2_out),
    .out(magma_Bits_2_eq_inst1_out)
);
coreir_eq #(
    .width(2)
) magma_Bits_2_eq_inst2 (
    .in0(write_0_addr),
    .in1(const_2_2_out),
    .out(magma_Bits_2_eq_inst2_out)
);
coreir_eq #(
    .width(2)
) magma_Bits_2_eq_inst3 (
    .in0(write_0_addr),
    .in1(const_3_2_out),
    .out(magma_Bits_2_eq_inst3_out)
);
coreir_reg_arst #(
    .arst_posedge(1'b1),
    .clk_posedge(1'b1),
    .init(4'h0),
    .width(4)
) reg_PR_inst0 (
    .clk(CLK),
    .arst(ASYNCRESET),
    .in(Mux2xBits4_inst0_O),
    .out(reg_PR_inst0_out)
);
coreir_reg_arst #(
    .arst_posedge(1'b1),
    .clk_posedge(1'b1),
    .init(4'h0),
    .width(4)
) reg_PR_inst1 (
    .clk(CLK),
    .arst(ASYNCRESET),
    .in(Mux2xBits4_inst1_O),
    .out(reg_PR_inst1_out)
);
coreir_reg_arst #(
    .arst_posedge(1'b1),
    .clk_posedge(1'b1),
    .init(4'h0),
    .width(4)
) reg_PR_inst2 (
    .clk(CLK),
    .arst(ASYNCRESET),
    .in(Mux2xBits4_inst2_O),
    .out(reg_PR_inst2_out)
);
coreir_reg_arst #(
    .arst_posedge(1'b1),
    .clk_posedge(1'b1),
    .init(4'h0),
    .width(4)
) reg_PR_inst3 (
    .clk(CLK),
    .arst(ASYNCRESET),
    .in(Mux2xBits4_inst3_O),
    .out(reg_PR_inst3_out)
);
assign read_0_data = Mux4xBits4_inst0_O;
endmodule

module test_regfile_basic_magma_False (
    input [1:0] write_addr,
    input [3:0] write_data,
    input [1:0] read_addr,
    output [3:0] read_data,
    input CLK,
    input ASYNCRESET
);
wire [3:0] my_regfile_read_0_data;
my_regfile my_regfile (
    .ASYNCRESET(ASYNCRESET),
    .CLK(CLK),
    .read_0_addr(read_addr),
    .read_0_data(my_regfile_read_0_data),
    .write_0_addr(write_addr),
    .write_0_data(write_data)
);
assign read_data = my_regfile_read_0_data;
endmodule

