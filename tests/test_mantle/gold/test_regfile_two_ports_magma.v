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
    input [3:0] in_data [1:0],
    input [0:0] in_sel,
    output [3:0] out
);
wire [3:0] _join_in0;
wire [3:0] _join_in1;
wire _join_sel;
wire [3:0] _join_out;
assign _join_in0 = in_data[0];
assign _join_in1 = in_data[1];
assign _join_sel = in_sel[0];
coreir_mux #(
    .width(4)
) _join (
    .in0(_join_in0),
    .in1(_join_in1),
    .sel(_join_sel),
    .out(_join_out)
);
assign out = _join_out;
endmodule

module commonlib_muxn__N4__width4 (
    input [3:0] in_data [3:0],
    input [1:0] in_sel,
    output [3:0] out
);
wire [3:0] _join_in0;
wire [3:0] _join_in1;
wire _join_sel;
wire [3:0] _join_out;
wire [3:0] muxN_0_in_data [1:0];
wire [0:0] muxN_0_in_sel;
wire [3:0] muxN_0_out;
wire [3:0] muxN_1_in_data [1:0];
wire [0:0] muxN_1_in_sel;
wire [3:0] muxN_1_out;
wire [1:0] sel_slice0_in;
wire [0:0] sel_slice0_out;
wire [1:0] sel_slice1_in;
wire [0:0] sel_slice1_out;
assign _join_in0 = muxN_0_out;
assign _join_in1 = muxN_1_out;
assign _join_sel = in_sel[1];
coreir_mux #(
    .width(4)
) _join (
    .in0(_join_in0),
    .in1(_join_in1),
    .sel(_join_sel),
    .out(_join_out)
);
assign muxN_0_in_data[1] = in_data[1];
assign muxN_0_in_data[0] = in_data[0];
assign muxN_0_in_sel = sel_slice0_out;
commonlib_muxn__N2__width4 muxN_0 (
    .in_data(muxN_0_in_data),
    .in_sel(muxN_0_in_sel),
    .out(muxN_0_out)
);
assign muxN_1_in_data[1] = in_data[3];
assign muxN_1_in_data[0] = in_data[2];
assign muxN_1_in_sel = sel_slice1_out;
commonlib_muxn__N2__width4 muxN_1 (
    .in_data(muxN_1_in_data),
    .in_sel(muxN_1_in_sel),
    .out(muxN_1_out)
);
assign sel_slice0_in = in_sel;
coreir_slice #(
    .hi(1),
    .lo(0),
    .width(2)
) sel_slice0 (
    .in(sel_slice0_in),
    .out(sel_slice0_out)
);
assign sel_slice1_in = in_sel;
coreir_slice #(
    .hi(1),
    .lo(0),
    .width(2)
) sel_slice1 (
    .in(sel_slice1_in),
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
wire [3:0] coreir_commonlib_mux4x4_inst0_in_data [3:0];
wire [1:0] coreir_commonlib_mux4x4_inst0_in_sel;
wire [3:0] coreir_commonlib_mux4x4_inst0_out;
assign coreir_commonlib_mux4x4_inst0_in_data[3] = I3;
assign coreir_commonlib_mux4x4_inst0_in_data[2] = I2;
assign coreir_commonlib_mux4x4_inst0_in_data[1] = I1;
assign coreir_commonlib_mux4x4_inst0_in_data[0] = I0;
assign coreir_commonlib_mux4x4_inst0_in_sel = S;
commonlib_muxn__N4__width4 coreir_commonlib_mux4x4_inst0 (
    .in_data(coreir_commonlib_mux4x4_inst0_in_data),
    .in_sel(coreir_commonlib_mux4x4_inst0_in_sel),
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
wire [3:0] coreir_commonlib_mux2x4_inst0_in_data [1:0];
wire [0:0] coreir_commonlib_mux2x4_inst0_in_sel;
wire [3:0] coreir_commonlib_mux2x4_inst0_out;
assign coreir_commonlib_mux2x4_inst0_in_data[1] = I1;
assign coreir_commonlib_mux2x4_inst0_in_data[0] = I0;
assign coreir_commonlib_mux2x4_inst0_in_sel[0] = S;
commonlib_muxn__N2__width4 coreir_commonlib_mux2x4_inst0 (
    .in_data(coreir_commonlib_mux2x4_inst0_in_data),
    .in_sel(coreir_commonlib_mux2x4_inst0_in_sel),
    .out(coreir_commonlib_mux2x4_inst0_out)
);
assign O = coreir_commonlib_mux2x4_inst0_out;
endmodule

module my_regfile (
    input ASYNCRESET,
    input CLK,
    input [1:0] read_0_addr,
    output [3:0] read_0_data,
    input [1:0] read_1_addr,
    output [3:0] read_1_data,
    input [1:0] write_0_addr,
    input [3:0] write_0_data,
    input [1:0] write_1_addr,
    input [3:0] write_1_data
);
wire [3:0] Mux2xBits4_inst0_I0;
wire [3:0] Mux2xBits4_inst0_I1;
wire Mux2xBits4_inst0_S;
wire [3:0] Mux2xBits4_inst0_O;
wire [3:0] Mux2xBits4_inst1_I0;
wire [3:0] Mux2xBits4_inst1_I1;
wire Mux2xBits4_inst1_S;
wire [3:0] Mux2xBits4_inst1_O;
wire [3:0] Mux2xBits4_inst10_I0;
wire [3:0] Mux2xBits4_inst10_I1;
wire Mux2xBits4_inst10_S;
wire [3:0] Mux2xBits4_inst10_O;
wire [3:0] Mux2xBits4_inst11_I0;
wire [3:0] Mux2xBits4_inst11_I1;
wire Mux2xBits4_inst11_S;
wire [3:0] Mux2xBits4_inst11_O;
wire [3:0] Mux2xBits4_inst2_I0;
wire [3:0] Mux2xBits4_inst2_I1;
wire Mux2xBits4_inst2_S;
wire [3:0] Mux2xBits4_inst2_O;
wire [3:0] Mux2xBits4_inst3_I0;
wire [3:0] Mux2xBits4_inst3_I1;
wire Mux2xBits4_inst3_S;
wire [3:0] Mux2xBits4_inst3_O;
wire [3:0] Mux2xBits4_inst4_I0;
wire [3:0] Mux2xBits4_inst4_I1;
wire Mux2xBits4_inst4_S;
wire [3:0] Mux2xBits4_inst4_O;
wire [3:0] Mux2xBits4_inst5_I0;
wire [3:0] Mux2xBits4_inst5_I1;
wire Mux2xBits4_inst5_S;
wire [3:0] Mux2xBits4_inst5_O;
wire [3:0] Mux2xBits4_inst6_I0;
wire [3:0] Mux2xBits4_inst6_I1;
wire Mux2xBits4_inst6_S;
wire [3:0] Mux2xBits4_inst6_O;
wire [3:0] Mux2xBits4_inst7_I0;
wire [3:0] Mux2xBits4_inst7_I1;
wire Mux2xBits4_inst7_S;
wire [3:0] Mux2xBits4_inst7_O;
wire [3:0] Mux2xBits4_inst8_I0;
wire [3:0] Mux2xBits4_inst8_I1;
wire Mux2xBits4_inst8_S;
wire [3:0] Mux2xBits4_inst8_O;
wire [3:0] Mux2xBits4_inst9_I0;
wire [3:0] Mux2xBits4_inst9_I1;
wire Mux2xBits4_inst9_S;
wire [3:0] Mux2xBits4_inst9_O;
wire [3:0] Mux4xBits4_inst0_I0;
wire [3:0] Mux4xBits4_inst0_I1;
wire [3:0] Mux4xBits4_inst0_I2;
wire [3:0] Mux4xBits4_inst0_I3;
wire [1:0] Mux4xBits4_inst0_S;
wire [3:0] Mux4xBits4_inst0_O;
wire [3:0] Mux4xBits4_inst1_I0;
wire [3:0] Mux4xBits4_inst1_I1;
wire [3:0] Mux4xBits4_inst1_I2;
wire [3:0] Mux4xBits4_inst1_I3;
wire [1:0] Mux4xBits4_inst1_S;
wire [3:0] Mux4xBits4_inst1_O;
wire [1:0] const_0_2_out;
wire [1:0] const_1_2_out;
wire [1:0] const_2_2_out;
wire [1:0] const_3_2_out;
wire [1:0] magma_Bits_2_eq_inst0_in0;
wire [1:0] magma_Bits_2_eq_inst0_in1;
wire magma_Bits_2_eq_inst0_out;
wire [1:0] magma_Bits_2_eq_inst1_in0;
wire [1:0] magma_Bits_2_eq_inst1_in1;
wire magma_Bits_2_eq_inst1_out;
wire [1:0] magma_Bits_2_eq_inst10_in0;
wire [1:0] magma_Bits_2_eq_inst10_in1;
wire magma_Bits_2_eq_inst10_out;
wire [1:0] magma_Bits_2_eq_inst11_in0;
wire [1:0] magma_Bits_2_eq_inst11_in1;
wire magma_Bits_2_eq_inst11_out;
wire [1:0] magma_Bits_2_eq_inst2_in0;
wire [1:0] magma_Bits_2_eq_inst2_in1;
wire magma_Bits_2_eq_inst2_out;
wire [1:0] magma_Bits_2_eq_inst3_in0;
wire [1:0] magma_Bits_2_eq_inst3_in1;
wire magma_Bits_2_eq_inst3_out;
wire [1:0] magma_Bits_2_eq_inst4_in0;
wire [1:0] magma_Bits_2_eq_inst4_in1;
wire magma_Bits_2_eq_inst4_out;
wire [1:0] magma_Bits_2_eq_inst5_in0;
wire [1:0] magma_Bits_2_eq_inst5_in1;
wire magma_Bits_2_eq_inst5_out;
wire [1:0] magma_Bits_2_eq_inst6_in0;
wire [1:0] magma_Bits_2_eq_inst6_in1;
wire magma_Bits_2_eq_inst6_out;
wire [1:0] magma_Bits_2_eq_inst7_in0;
wire [1:0] magma_Bits_2_eq_inst7_in1;
wire magma_Bits_2_eq_inst7_out;
wire [1:0] magma_Bits_2_eq_inst8_in0;
wire [1:0] magma_Bits_2_eq_inst8_in1;
wire magma_Bits_2_eq_inst8_out;
wire [1:0] magma_Bits_2_eq_inst9_in0;
wire [1:0] magma_Bits_2_eq_inst9_in1;
wire magma_Bits_2_eq_inst9_out;
wire reg_PR_inst0_clk;
wire reg_PR_inst0_arst;
wire [3:0] reg_PR_inst0_in;
wire [3:0] reg_PR_inst0_out;
wire reg_PR_inst1_clk;
wire reg_PR_inst1_arst;
wire [3:0] reg_PR_inst1_in;
wire [3:0] reg_PR_inst1_out;
wire reg_PR_inst2_clk;
wire reg_PR_inst2_arst;
wire [3:0] reg_PR_inst2_in;
wire [3:0] reg_PR_inst2_out;
wire reg_PR_inst3_clk;
wire reg_PR_inst3_arst;
wire [3:0] reg_PR_inst3_in;
wire [3:0] reg_PR_inst3_out;
assign Mux2xBits4_inst0_I0 = reg_PR_inst0_out;
assign Mux2xBits4_inst0_I1 = write_0_data;
assign Mux2xBits4_inst0_S = magma_Bits_2_eq_inst0_out;
Mux2xBits4 Mux2xBits4_inst0 (
    .I0(Mux2xBits4_inst0_I0),
    .I1(Mux2xBits4_inst0_I1),
    .S(Mux2xBits4_inst0_S),
    .O(Mux2xBits4_inst0_O)
);
assign Mux2xBits4_inst1_I0 = reg_PR_inst1_out;
assign Mux2xBits4_inst1_I1 = write_0_data;
assign Mux2xBits4_inst1_S = magma_Bits_2_eq_inst1_out;
Mux2xBits4 Mux2xBits4_inst1 (
    .I0(Mux2xBits4_inst1_I0),
    .I1(Mux2xBits4_inst1_I1),
    .S(Mux2xBits4_inst1_S),
    .O(Mux2xBits4_inst1_O)
);
assign Mux2xBits4_inst10_I0 = Mux2xBits4_inst4_O;
assign Mux2xBits4_inst10_I1 = write_1_data;
assign Mux2xBits4_inst10_S = magma_Bits_2_eq_inst10_out;
Mux2xBits4 Mux2xBits4_inst10 (
    .I0(Mux2xBits4_inst10_I0),
    .I1(Mux2xBits4_inst10_I1),
    .S(Mux2xBits4_inst10_S),
    .O(Mux2xBits4_inst10_O)
);
assign Mux2xBits4_inst11_I0 = Mux2xBits4_inst5_O;
assign Mux2xBits4_inst11_I1 = write_1_data;
assign Mux2xBits4_inst11_S = magma_Bits_2_eq_inst11_out;
Mux2xBits4 Mux2xBits4_inst11 (
    .I0(Mux2xBits4_inst11_I0),
    .I1(Mux2xBits4_inst11_I1),
    .S(Mux2xBits4_inst11_S),
    .O(Mux2xBits4_inst11_O)
);
assign Mux2xBits4_inst2_I0 = reg_PR_inst2_out;
assign Mux2xBits4_inst2_I1 = write_0_data;
assign Mux2xBits4_inst2_S = magma_Bits_2_eq_inst2_out;
Mux2xBits4 Mux2xBits4_inst2 (
    .I0(Mux2xBits4_inst2_I0),
    .I1(Mux2xBits4_inst2_I1),
    .S(Mux2xBits4_inst2_S),
    .O(Mux2xBits4_inst2_O)
);
assign Mux2xBits4_inst3_I0 = reg_PR_inst3_out;
assign Mux2xBits4_inst3_I1 = write_0_data;
assign Mux2xBits4_inst3_S = magma_Bits_2_eq_inst3_out;
Mux2xBits4 Mux2xBits4_inst3 (
    .I0(Mux2xBits4_inst3_I0),
    .I1(Mux2xBits4_inst3_I1),
    .S(Mux2xBits4_inst3_S),
    .O(Mux2xBits4_inst3_O)
);
assign Mux2xBits4_inst4_I0 = Mux4xBits4_inst0_O;
assign Mux2xBits4_inst4_I1 = write_0_data;
assign Mux2xBits4_inst4_S = magma_Bits_2_eq_inst4_out;
Mux2xBits4 Mux2xBits4_inst4 (
    .I0(Mux2xBits4_inst4_I0),
    .I1(Mux2xBits4_inst4_I1),
    .S(Mux2xBits4_inst4_S),
    .O(Mux2xBits4_inst4_O)
);
assign Mux2xBits4_inst5_I0 = Mux4xBits4_inst1_O;
assign Mux2xBits4_inst5_I1 = write_0_data;
assign Mux2xBits4_inst5_S = magma_Bits_2_eq_inst5_out;
Mux2xBits4 Mux2xBits4_inst5 (
    .I0(Mux2xBits4_inst5_I0),
    .I1(Mux2xBits4_inst5_I1),
    .S(Mux2xBits4_inst5_S),
    .O(Mux2xBits4_inst5_O)
);
assign Mux2xBits4_inst6_I0 = Mux2xBits4_inst0_O;
assign Mux2xBits4_inst6_I1 = write_1_data;
assign Mux2xBits4_inst6_S = magma_Bits_2_eq_inst6_out;
Mux2xBits4 Mux2xBits4_inst6 (
    .I0(Mux2xBits4_inst6_I0),
    .I1(Mux2xBits4_inst6_I1),
    .S(Mux2xBits4_inst6_S),
    .O(Mux2xBits4_inst6_O)
);
assign Mux2xBits4_inst7_I0 = Mux2xBits4_inst1_O;
assign Mux2xBits4_inst7_I1 = write_1_data;
assign Mux2xBits4_inst7_S = magma_Bits_2_eq_inst7_out;
Mux2xBits4 Mux2xBits4_inst7 (
    .I0(Mux2xBits4_inst7_I0),
    .I1(Mux2xBits4_inst7_I1),
    .S(Mux2xBits4_inst7_S),
    .O(Mux2xBits4_inst7_O)
);
assign Mux2xBits4_inst8_I0 = Mux2xBits4_inst2_O;
assign Mux2xBits4_inst8_I1 = write_1_data;
assign Mux2xBits4_inst8_S = magma_Bits_2_eq_inst8_out;
Mux2xBits4 Mux2xBits4_inst8 (
    .I0(Mux2xBits4_inst8_I0),
    .I1(Mux2xBits4_inst8_I1),
    .S(Mux2xBits4_inst8_S),
    .O(Mux2xBits4_inst8_O)
);
assign Mux2xBits4_inst9_I0 = Mux2xBits4_inst3_O;
assign Mux2xBits4_inst9_I1 = write_1_data;
assign Mux2xBits4_inst9_S = magma_Bits_2_eq_inst9_out;
Mux2xBits4 Mux2xBits4_inst9 (
    .I0(Mux2xBits4_inst9_I0),
    .I1(Mux2xBits4_inst9_I1),
    .S(Mux2xBits4_inst9_S),
    .O(Mux2xBits4_inst9_O)
);
assign Mux4xBits4_inst0_I0 = reg_PR_inst0_out;
assign Mux4xBits4_inst0_I1 = reg_PR_inst1_out;
assign Mux4xBits4_inst0_I2 = reg_PR_inst2_out;
assign Mux4xBits4_inst0_I3 = reg_PR_inst3_out;
assign Mux4xBits4_inst0_S = read_0_addr;
Mux4xBits4 Mux4xBits4_inst0 (
    .I0(Mux4xBits4_inst0_I0),
    .I1(Mux4xBits4_inst0_I1),
    .I2(Mux4xBits4_inst0_I2),
    .I3(Mux4xBits4_inst0_I3),
    .S(Mux4xBits4_inst0_S),
    .O(Mux4xBits4_inst0_O)
);
assign Mux4xBits4_inst1_I0 = reg_PR_inst0_out;
assign Mux4xBits4_inst1_I1 = reg_PR_inst1_out;
assign Mux4xBits4_inst1_I2 = reg_PR_inst2_out;
assign Mux4xBits4_inst1_I3 = reg_PR_inst3_out;
assign Mux4xBits4_inst1_S = read_1_addr;
Mux4xBits4 Mux4xBits4_inst1 (
    .I0(Mux4xBits4_inst1_I0),
    .I1(Mux4xBits4_inst1_I1),
    .I2(Mux4xBits4_inst1_I2),
    .I3(Mux4xBits4_inst1_I3),
    .S(Mux4xBits4_inst1_S),
    .O(Mux4xBits4_inst1_O)
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
assign magma_Bits_2_eq_inst0_in0 = write_0_addr;
assign magma_Bits_2_eq_inst0_in1 = const_0_2_out;
coreir_eq #(
    .width(2)
) magma_Bits_2_eq_inst0 (
    .in0(magma_Bits_2_eq_inst0_in0),
    .in1(magma_Bits_2_eq_inst0_in1),
    .out(magma_Bits_2_eq_inst0_out)
);
assign magma_Bits_2_eq_inst1_in0 = write_0_addr;
assign magma_Bits_2_eq_inst1_in1 = const_1_2_out;
coreir_eq #(
    .width(2)
) magma_Bits_2_eq_inst1 (
    .in0(magma_Bits_2_eq_inst1_in0),
    .in1(magma_Bits_2_eq_inst1_in1),
    .out(magma_Bits_2_eq_inst1_out)
);
assign magma_Bits_2_eq_inst10_in0 = write_1_addr;
assign magma_Bits_2_eq_inst10_in1 = read_0_addr;
coreir_eq #(
    .width(2)
) magma_Bits_2_eq_inst10 (
    .in0(magma_Bits_2_eq_inst10_in0),
    .in1(magma_Bits_2_eq_inst10_in1),
    .out(magma_Bits_2_eq_inst10_out)
);
assign magma_Bits_2_eq_inst11_in0 = write_1_addr;
assign magma_Bits_2_eq_inst11_in1 = read_1_addr;
coreir_eq #(
    .width(2)
) magma_Bits_2_eq_inst11 (
    .in0(magma_Bits_2_eq_inst11_in0),
    .in1(magma_Bits_2_eq_inst11_in1),
    .out(magma_Bits_2_eq_inst11_out)
);
assign magma_Bits_2_eq_inst2_in0 = write_0_addr;
assign magma_Bits_2_eq_inst2_in1 = const_2_2_out;
coreir_eq #(
    .width(2)
) magma_Bits_2_eq_inst2 (
    .in0(magma_Bits_2_eq_inst2_in0),
    .in1(magma_Bits_2_eq_inst2_in1),
    .out(magma_Bits_2_eq_inst2_out)
);
assign magma_Bits_2_eq_inst3_in0 = write_0_addr;
assign magma_Bits_2_eq_inst3_in1 = const_3_2_out;
coreir_eq #(
    .width(2)
) magma_Bits_2_eq_inst3 (
    .in0(magma_Bits_2_eq_inst3_in0),
    .in1(magma_Bits_2_eq_inst3_in1),
    .out(magma_Bits_2_eq_inst3_out)
);
assign magma_Bits_2_eq_inst4_in0 = write_0_addr;
assign magma_Bits_2_eq_inst4_in1 = read_0_addr;
coreir_eq #(
    .width(2)
) magma_Bits_2_eq_inst4 (
    .in0(magma_Bits_2_eq_inst4_in0),
    .in1(magma_Bits_2_eq_inst4_in1),
    .out(magma_Bits_2_eq_inst4_out)
);
assign magma_Bits_2_eq_inst5_in0 = write_0_addr;
assign magma_Bits_2_eq_inst5_in1 = read_1_addr;
coreir_eq #(
    .width(2)
) magma_Bits_2_eq_inst5 (
    .in0(magma_Bits_2_eq_inst5_in0),
    .in1(magma_Bits_2_eq_inst5_in1),
    .out(magma_Bits_2_eq_inst5_out)
);
assign magma_Bits_2_eq_inst6_in0 = write_1_addr;
assign magma_Bits_2_eq_inst6_in1 = const_0_2_out;
coreir_eq #(
    .width(2)
) magma_Bits_2_eq_inst6 (
    .in0(magma_Bits_2_eq_inst6_in0),
    .in1(magma_Bits_2_eq_inst6_in1),
    .out(magma_Bits_2_eq_inst6_out)
);
assign magma_Bits_2_eq_inst7_in0 = write_1_addr;
assign magma_Bits_2_eq_inst7_in1 = const_1_2_out;
coreir_eq #(
    .width(2)
) magma_Bits_2_eq_inst7 (
    .in0(magma_Bits_2_eq_inst7_in0),
    .in1(magma_Bits_2_eq_inst7_in1),
    .out(magma_Bits_2_eq_inst7_out)
);
assign magma_Bits_2_eq_inst8_in0 = write_1_addr;
assign magma_Bits_2_eq_inst8_in1 = const_2_2_out;
coreir_eq #(
    .width(2)
) magma_Bits_2_eq_inst8 (
    .in0(magma_Bits_2_eq_inst8_in0),
    .in1(magma_Bits_2_eq_inst8_in1),
    .out(magma_Bits_2_eq_inst8_out)
);
assign magma_Bits_2_eq_inst9_in0 = write_1_addr;
assign magma_Bits_2_eq_inst9_in1 = const_3_2_out;
coreir_eq #(
    .width(2)
) magma_Bits_2_eq_inst9 (
    .in0(magma_Bits_2_eq_inst9_in0),
    .in1(magma_Bits_2_eq_inst9_in1),
    .out(magma_Bits_2_eq_inst9_out)
);
assign reg_PR_inst0_clk = CLK;
assign reg_PR_inst0_arst = ASYNCRESET;
assign reg_PR_inst0_in = Mux2xBits4_inst6_O;
coreir_reg_arst #(
    .arst_posedge(1'b1),
    .clk_posedge(1'b1),
    .init(4'h0),
    .width(4)
) reg_PR_inst0 (
    .clk(reg_PR_inst0_clk),
    .arst(reg_PR_inst0_arst),
    .in(reg_PR_inst0_in),
    .out(reg_PR_inst0_out)
);
assign reg_PR_inst1_clk = CLK;
assign reg_PR_inst1_arst = ASYNCRESET;
assign reg_PR_inst1_in = Mux2xBits4_inst7_O;
coreir_reg_arst #(
    .arst_posedge(1'b1),
    .clk_posedge(1'b1),
    .init(4'h0),
    .width(4)
) reg_PR_inst1 (
    .clk(reg_PR_inst1_clk),
    .arst(reg_PR_inst1_arst),
    .in(reg_PR_inst1_in),
    .out(reg_PR_inst1_out)
);
assign reg_PR_inst2_clk = CLK;
assign reg_PR_inst2_arst = ASYNCRESET;
assign reg_PR_inst2_in = Mux2xBits4_inst8_O;
coreir_reg_arst #(
    .arst_posedge(1'b1),
    .clk_posedge(1'b1),
    .init(4'h0),
    .width(4)
) reg_PR_inst2 (
    .clk(reg_PR_inst2_clk),
    .arst(reg_PR_inst2_arst),
    .in(reg_PR_inst2_in),
    .out(reg_PR_inst2_out)
);
assign reg_PR_inst3_clk = CLK;
assign reg_PR_inst3_arst = ASYNCRESET;
assign reg_PR_inst3_in = Mux2xBits4_inst9_O;
coreir_reg_arst #(
    .arst_posedge(1'b1),
    .clk_posedge(1'b1),
    .init(4'h0),
    .width(4)
) reg_PR_inst3 (
    .clk(reg_PR_inst3_clk),
    .arst(reg_PR_inst3_arst),
    .in(reg_PR_inst3_in),
    .out(reg_PR_inst3_out)
);
assign read_0_data = Mux2xBits4_inst10_O;
assign read_1_data = Mux2xBits4_inst11_O;
endmodule

module test_regfile_two_ports_magma (
    input [1:0] write_addr0,
    input [3:0] write_data0,
    input [1:0] write_addr1,
    input [3:0] write_data1,
    input [1:0] read_addr0,
    output [3:0] read_data0,
    input [1:0] read_addr1,
    output [3:0] read_data1,
    input CLK,
    input ASYNCRESET
);
wire my_regfile_ASYNCRESET;
wire my_regfile_CLK;
wire [1:0] my_regfile_read_0_addr;
wire [3:0] my_regfile_read_0_data;
wire [1:0] my_regfile_read_1_addr;
wire [3:0] my_regfile_read_1_data;
wire [1:0] my_regfile_write_0_addr;
wire [3:0] my_regfile_write_0_data;
wire [1:0] my_regfile_write_1_addr;
wire [3:0] my_regfile_write_1_data;
assign my_regfile_ASYNCRESET = ASYNCRESET;
assign my_regfile_CLK = CLK;
assign my_regfile_read_0_addr = read_addr0;
assign my_regfile_read_1_addr = read_addr1;
assign my_regfile_write_0_addr = write_addr0;
assign my_regfile_write_0_data = write_data0;
assign my_regfile_write_1_addr = write_addr1;
assign my_regfile_write_1_data = write_data1;
my_regfile my_regfile (
    .ASYNCRESET(my_regfile_ASYNCRESET),
    .CLK(my_regfile_CLK),
    .read_0_addr(my_regfile_read_0_addr),
    .read_0_data(my_regfile_read_0_data),
    .read_1_addr(my_regfile_read_1_addr),
    .read_1_data(my_regfile_read_1_data),
    .write_0_addr(my_regfile_write_0_addr),
    .write_0_data(my_regfile_write_0_data),
    .write_1_addr(my_regfile_write_1_addr),
    .write_1_data(my_regfile_write_1_data)
);
assign read_data0 = my_regfile_read_0_data;
assign read_data1 = my_regfile_read_1_data;
endmodule

