module coreir_reg #(
    parameter width = 1,
    parameter clk_posedge = 1,
    parameter init = 1
) (
    input clk,
    input [width-1:0] in,
    output [width-1:0] out
);
  reg [width-1:0] outReg=init;
  wire real_clk;
  assign real_clk = clk_posedge ? clk : ~clk;
  always @(posedge real_clk) begin
    outReg <= in;
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

module coreir_const #(
    parameter width = 1,
    parameter value = 1
) (
    output [width-1:0] out
);
  assign out = value;
endmodule

module coreir_add #(
    parameter width = 1
) (
    input [width-1:0] in0,
    input [width-1:0] in1,
    output [width-1:0] out
);
  assign out = in0 + in1;
endmodule

module corebit_const #(
    parameter value = 1
) (
    output out
);
  assign out = value;
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
assign coreir_commonlib_mux2x8_inst0_in_data = '{I1,I0};
assign coreir_commonlib_mux2x8_inst0_in_sel = S;
commonlib_muxn__N2__width8 coreir_commonlib_mux2x8_inst0 (
    .in_data(coreir_commonlib_mux2x8_inst0_in_data),
    .in_sel(coreir_commonlib_mux2x8_inst0_in_sel),
    .out(coreir_commonlib_mux2x8_inst0_out)
);
assign O = coreir_commonlib_mux2x8_inst0_out;
endmodule

module DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse (
    input I,
    output O,
    input CLK
);
wire reg_P_inst0_clk;
wire [0:0] reg_P_inst0_in;
wire [0:0] reg_P_inst0_out;
assign reg_P_inst0_clk = CLK;
assign reg_P_inst0_in = I;
coreir_reg #(
    .clk_posedge(1'b1),
    .init(1'h0),
    .width(1)
) reg_P_inst0 (
    .clk(reg_P_inst0_clk),
    .in(reg_P_inst0_in),
    .out(reg_P_inst0_out)
);
assign O = reg_P_inst0_out[0];
endmodule

module Register8 (
    input [7:0] I,
    output [7:0] O,
    input CLK
);
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_I;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_CLK;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_I;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_CLK;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_I;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_CLK;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_I;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_CLK;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst4_I;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst4_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst4_CLK;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst5_I;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst5_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst5_CLK;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst6_I;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst6_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst6_CLK;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst7_I;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst7_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst7_CLK;
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_I = I[0];
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_CLK = CLK;
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0 (
    .I(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_I),
    .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O),
    .CLK(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_CLK)
);
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_I = I[1];
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_CLK = CLK;
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1 (
    .I(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_I),
    .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O),
    .CLK(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_CLK)
);
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_I = I[2];
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_CLK = CLK;
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2 (
    .I(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_I),
    .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_O),
    .CLK(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_CLK)
);
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_I = I[3];
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_CLK = CLK;
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3 (
    .I(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_I),
    .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_O),
    .CLK(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_CLK)
);
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst4_I = I[4];
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst4_CLK = CLK;
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst4 (
    .I(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst4_I),
    .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst4_O),
    .CLK(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst4_CLK)
);
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst5_I = I[5];
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst5_CLK = CLK;
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst5 (
    .I(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst5_I),
    .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst5_O),
    .CLK(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst5_CLK)
);
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst6_I = I[6];
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst6_CLK = CLK;
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst6 (
    .I(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst6_I),
    .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst6_O),
    .CLK(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst6_CLK)
);
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst7_I = I[7];
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst7_CLK = CLK;
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst7 (
    .I(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst7_I),
    .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst7_O),
    .CLK(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst7_CLK)
);
assign O = {DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst7_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst6_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst5_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst4_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O};
endmodule

module Add8_cout (
    input [7:0] I0,
    input [7:0] I1,
    output [7:0] O,
    output COUT
);
wire bit_const_0_None_out;
wire [8:0] coreir_add9_inst0_in0;
wire [8:0] coreir_add9_inst0_in1;
wire [8:0] coreir_add9_inst0_out;
corebit_const #(
    .value(1'b0)
) bit_const_0_None (
    .out(bit_const_0_None_out)
);
assign coreir_add9_inst0_in0 = {bit_const_0_None_out,I0[7:0]};
assign coreir_add9_inst0_in1 = {bit_const_0_None_out,I1[7:0]};
coreir_add #(
    .width(9)
) coreir_add9_inst0 (
    .in0(coreir_add9_inst0_in0),
    .in1(coreir_add9_inst0_in1),
    .out(coreir_add9_inst0_out)
);
assign O = coreir_add9_inst0_out[7:0];
assign COUT = coreir_add9_inst0_out[8];
endmodule

module CounterLoad8_COUT (
    input [7:0] DATA,
    input LOAD,
    output [7:0] O,
    output COUT,
    input CLK
);
wire [7:0] Add8_cout_inst0_I0;
wire [7:0] Add8_cout_inst0_I1;
wire [7:0] Add8_cout_inst0_O;
wire Add8_cout_inst0_COUT;
wire [7:0] Mux2x8_inst0_I0;
wire [7:0] Mux2x8_inst0_I1;
wire Mux2x8_inst0_S;
wire [7:0] Mux2x8_inst0_O;
wire [7:0] Register8_inst0_I;
wire [7:0] Register8_inst0_O;
wire Register8_inst0_CLK;
wire [7:0] const_1_8_out;
assign Add8_cout_inst0_I0 = Register8_inst0_O;
assign Add8_cout_inst0_I1 = const_1_8_out;
Add8_cout Add8_cout_inst0 (
    .I0(Add8_cout_inst0_I0),
    .I1(Add8_cout_inst0_I1),
    .O(Add8_cout_inst0_O),
    .COUT(Add8_cout_inst0_COUT)
);
assign Mux2x8_inst0_I0 = Add8_cout_inst0_O;
assign Mux2x8_inst0_I1 = DATA;
assign Mux2x8_inst0_S = LOAD;
Mux2x8 Mux2x8_inst0 (
    .I0(Mux2x8_inst0_I0),
    .I1(Mux2x8_inst0_I1),
    .S(Mux2x8_inst0_S),
    .O(Mux2x8_inst0_O)
);
assign Register8_inst0_I = Mux2x8_inst0_O;
assign Register8_inst0_CLK = CLK;
Register8 Register8_inst0 (
    .I(Register8_inst0_I),
    .O(Register8_inst0_O),
    .CLK(Register8_inst0_CLK)
);
coreir_const #(
    .value(8'h01),
    .width(8)
) const_1_8 (
    .out(const_1_8_out)
);
assign O = Register8_inst0_O;
assign COUT = Add8_cout_inst0_COUT;
endmodule

