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

module Mux2xNone (
    input I0,
    input I1,
    input S,
    output O
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
assign O = coreir_commonlib_mux2x1_inst0_out[0];
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

module Register4 (
    input [3:0] I,
    output [3:0] O,
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
assign O = {DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O};
endmodule

module PISO4 (
    input SI,
    input [3:0] PI,
    input LOAD,
    output O,
    input CLK
);
wire Mux2xNone_inst0_I0;
wire Mux2xNone_inst0_I1;
wire Mux2xNone_inst0_S;
wire Mux2xNone_inst0_O;
wire Mux2xNone_inst1_I0;
wire Mux2xNone_inst1_I1;
wire Mux2xNone_inst1_S;
wire Mux2xNone_inst1_O;
wire Mux2xNone_inst2_I0;
wire Mux2xNone_inst2_I1;
wire Mux2xNone_inst2_S;
wire Mux2xNone_inst2_O;
wire Mux2xNone_inst3_I0;
wire Mux2xNone_inst3_I1;
wire Mux2xNone_inst3_S;
wire Mux2xNone_inst3_O;
wire [3:0] Register4_inst0_I;
wire [3:0] Register4_inst0_O;
wire Register4_inst0_CLK;
assign Mux2xNone_inst0_I0 = SI;
assign Mux2xNone_inst0_I1 = PI[0];
assign Mux2xNone_inst0_S = LOAD;
Mux2xNone Mux2xNone_inst0 (
    .I0(Mux2xNone_inst0_I0),
    .I1(Mux2xNone_inst0_I1),
    .S(Mux2xNone_inst0_S),
    .O(Mux2xNone_inst0_O)
);
assign Mux2xNone_inst1_I0 = Register4_inst0_O[0];
assign Mux2xNone_inst1_I1 = PI[1];
assign Mux2xNone_inst1_S = LOAD;
Mux2xNone Mux2xNone_inst1 (
    .I0(Mux2xNone_inst1_I0),
    .I1(Mux2xNone_inst1_I1),
    .S(Mux2xNone_inst1_S),
    .O(Mux2xNone_inst1_O)
);
assign Mux2xNone_inst2_I0 = Register4_inst0_O[1];
assign Mux2xNone_inst2_I1 = PI[2];
assign Mux2xNone_inst2_S = LOAD;
Mux2xNone Mux2xNone_inst2 (
    .I0(Mux2xNone_inst2_I0),
    .I1(Mux2xNone_inst2_I1),
    .S(Mux2xNone_inst2_S),
    .O(Mux2xNone_inst2_O)
);
assign Mux2xNone_inst3_I0 = Register4_inst0_O[2];
assign Mux2xNone_inst3_I1 = PI[3];
assign Mux2xNone_inst3_S = LOAD;
Mux2xNone Mux2xNone_inst3 (
    .I0(Mux2xNone_inst3_I0),
    .I1(Mux2xNone_inst3_I1),
    .S(Mux2xNone_inst3_S),
    .O(Mux2xNone_inst3_O)
);
assign Register4_inst0_I = {Mux2xNone_inst3_O,Mux2xNone_inst2_O,Mux2xNone_inst1_O,Mux2xNone_inst0_O};
assign Register4_inst0_CLK = CLK;
Register4 Register4_inst0 (
    .I(Register4_inst0_I),
    .O(Register4_inst0_O),
    .CLK(Register4_inst0_CLK)
);
assign O = Register4_inst0_O[3];
endmodule

