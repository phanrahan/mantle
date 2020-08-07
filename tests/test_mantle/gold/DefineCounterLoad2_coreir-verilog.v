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

module commonlib_muxn__N2__width2 (
    input [1:0] in_data [1:0],
    input [0:0] in_sel,
    output [1:0] out
);
wire [1:0] _join_in0;
wire [1:0] _join_in1;
wire _join_sel;
wire [1:0] _join_out;
assign _join_in0 = in_data[0];
assign _join_in1 = in_data[1];
assign _join_sel = in_sel[0];
coreir_mux #(
    .width(2)
) _join (
    .in0(_join_in0),
    .in1(_join_in1),
    .sel(_join_sel),
    .out(_join_out)
);
assign out = _join_out;
endmodule

module Mux2x2 (
    input [1:0] I0,
    input [1:0] I1,
    input S,
    output [1:0] O
);
wire [1:0] coreir_commonlib_mux2x2_inst0_in_data [1:0];
wire [0:0] coreir_commonlib_mux2x2_inst0_in_sel;
wire [1:0] coreir_commonlib_mux2x2_inst0_out;
assign coreir_commonlib_mux2x2_inst0_in_data[1] = I1;
assign coreir_commonlib_mux2x2_inst0_in_data[0] = I0;
assign coreir_commonlib_mux2x2_inst0_in_sel[0] = S;
commonlib_muxn__N2__width2 coreir_commonlib_mux2x2_inst0 (
    .in_data(coreir_commonlib_mux2x2_inst0_in_data),
    .in_sel(coreir_commonlib_mux2x2_inst0_in_sel),
    .out(coreir_commonlib_mux2x2_inst0_out)
);
assign O = coreir_commonlib_mux2x2_inst0_out;
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
assign reg_P_inst0_in[0] = I;
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

module Register2 (
    input [1:0] I,
    output [1:0] O,
    input CLK
);
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_I;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_CLK;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_I;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_CLK;
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
assign O = {DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O};
endmodule

module Add2_cout (
    input [1:0] I0,
    input [1:0] I1,
    output [1:0] O,
    output COUT
);
wire bit_const_0_None_out;
wire [2:0] coreir_add3_inst0_in0;
wire [2:0] coreir_add3_inst0_in1;
wire [2:0] coreir_add3_inst0_out;
corebit_const #(
    .value(1'b0)
) bit_const_0_None (
    .out(bit_const_0_None_out)
);
assign coreir_add3_inst0_in0 = {bit_const_0_None_out,I0[1:0]};
assign coreir_add3_inst0_in1 = {bit_const_0_None_out,I1[1:0]};
coreir_add #(
    .width(3)
) coreir_add3_inst0 (
    .in0(coreir_add3_inst0_in0),
    .in1(coreir_add3_inst0_in1),
    .out(coreir_add3_inst0_out)
);
assign O = coreir_add3_inst0_out[1:0];
assign COUT = coreir_add3_inst0_out[2];
endmodule

module CounterLoad2_COUT (
    input [1:0] DATA,
    input LOAD,
    output [1:0] O,
    output COUT,
    input CLK
);
wire [1:0] Add2_cout_inst0_I0;
wire [1:0] Add2_cout_inst0_I1;
wire [1:0] Add2_cout_inst0_O;
wire Add2_cout_inst0_COUT;
wire [1:0] Mux2x2_inst0_I0;
wire [1:0] Mux2x2_inst0_I1;
wire Mux2x2_inst0_S;
wire [1:0] Mux2x2_inst0_O;
wire [1:0] Register2_inst0_I;
wire [1:0] Register2_inst0_O;
wire Register2_inst0_CLK;
wire [1:0] const_1_2_out;
assign Add2_cout_inst0_I0 = Register2_inst0_O;
assign Add2_cout_inst0_I1 = const_1_2_out;
Add2_cout Add2_cout_inst0 (
    .I0(Add2_cout_inst0_I0),
    .I1(Add2_cout_inst0_I1),
    .O(Add2_cout_inst0_O),
    .COUT(Add2_cout_inst0_COUT)
);
assign Mux2x2_inst0_I0 = Add2_cout_inst0_O;
assign Mux2x2_inst0_I1 = DATA;
assign Mux2x2_inst0_S = LOAD;
Mux2x2 Mux2x2_inst0 (
    .I0(Mux2x2_inst0_I0),
    .I1(Mux2x2_inst0_I1),
    .S(Mux2x2_inst0_S),
    .O(Mux2x2_inst0_O)
);
assign Register2_inst0_I = Mux2x2_inst0_O;
assign Register2_inst0_CLK = CLK;
Register2 Register2_inst0 (
    .I(Register2_inst0_I),
    .O(Register2_inst0_O),
    .CLK(Register2_inst0_CLK)
);
coreir_const #(
    .value(2'h1),
    .width(2)
) const_1_2 (
    .out(const_1_2_out)
);
assign O = Register2_inst0_O;
assign COUT = Add2_cout_inst0_COUT;
endmodule

