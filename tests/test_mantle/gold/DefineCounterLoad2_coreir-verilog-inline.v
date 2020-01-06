module coreir_reg #(parameter width = 1, parameter clk_posedge = 1, parameter init = 1) (input clk, input [width-1:0] in, output [width-1:0] out);
  reg [width-1:0] outReg=init;
  wire real_clk;
  assign real_clk = clk_posedge ? clk : ~clk;
  always @(posedge real_clk) begin
    outReg <= in;
  end
  assign out = outReg;
endmodule

module coreir_mux #(parameter width = 1) (input [width-1:0] in0, input [width-1:0] in1, input sel, output [width-1:0] out);
  assign out = sel ? in1 : in0;
endmodule

module coreir_const #(parameter width = 1, parameter value = 1) (output [width-1:0] out);
  assign out = value;
endmodule

module coreir_add #(parameter width = 1) (input [width-1:0] in0, input [width-1:0] in1, output [width-1:0] out);
  assign out = in0 + in1;
endmodule

module corebit_const #(parameter value = 1) (output out);
  assign out = value;
endmodule

module commonlib_muxn__N2__width2 (input [1:0] in_data_0, input [1:0] in_data_1, input [0:0] in_sel, output [1:0] out);
wire [1:0] _join_out;
coreir_mux #(.width(2)) _join(.in0(in_data_0), .in1(in_data_1), .out(_join_out), .sel(in_sel[0]));
assign out = _join_out;
endmodule

module Mux2x2 (input [1:0] I0, input [1:0] I1, output [1:0] O, input S);
wire [1:0] coreir_commonlib_mux2x2_inst0_out;
commonlib_muxn__N2__width2 coreir_commonlib_mux2x2_inst0(.in_data_0(I0), .in_data_1(I1), .in_sel(S), .out(coreir_commonlib_mux2x2_inst0_out));
assign O = coreir_commonlib_mux2x2_inst0_out;
endmodule

module DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse (input CLK, input I, output O);
wire [0:0] reg_P_inst0_out;
coreir_reg #(.clk_posedge(1'b1), .init(1'h0), .width(1)) reg_P_inst0(.clk(CLK), .in(I), .out(reg_P_inst0_out));
assign O = reg_P_inst0_out[0];
endmodule

module Register2 (input CLK, input [1:0] I, output [1:0] O);
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O;
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0(.CLK(CLK), .I(I[0]), .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O));
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1(.CLK(CLK), .I(I[1]), .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O));
assign O = {DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O};
endmodule

module Add2_cout (output COUT, input [1:0] I0, input [1:0] I1, output [1:0] O);
wire bit_const_0_None_out;
wire [2:0] coreir_add3_inst0_out;
corebit_const #(.value(1'b0)) bit_const_0_None(.out(bit_const_0_None_out));
coreir_add #(.width(3)) coreir_add3_inst0(.in0({bit_const_0_None_out,I0[1],I0[0]}), .in1({bit_const_0_None_out,I1[1],I1[0]}), .out(coreir_add3_inst0_out));
assign COUT = coreir_add3_inst0_out[2];
assign O = {coreir_add3_inst0_out[1],coreir_add3_inst0_out[0]};
endmodule

module CounterLoad2_COUT (input CLK, output COUT, input [1:0] DATA, input LOAD, output [1:0] O);
wire Add2_cout_inst0_COUT;
wire [1:0] Add2_cout_inst0_O;
wire [1:0] Mux2x2_inst0_O;
wire [1:0] Register2_inst0_O;
wire [1:0] const_1_2_out;
Add2_cout Add2_cout_inst0(.COUT(Add2_cout_inst0_COUT), .I0(Register2_inst0_O), .I1(const_1_2_out), .O(Add2_cout_inst0_O));
Mux2x2 Mux2x2_inst0(.I0(Add2_cout_inst0_O), .I1(DATA), .O(Mux2x2_inst0_O), .S(LOAD));
Register2 Register2_inst0(.CLK(CLK), .I(Mux2x2_inst0_O), .O(Register2_inst0_O));
coreir_const #(.value(2'h1), .width(2)) const_1_2(.out(const_1_2_out));
assign COUT = Add2_cout_inst0_COUT;
assign O = Register2_inst0_O;
endmodule

