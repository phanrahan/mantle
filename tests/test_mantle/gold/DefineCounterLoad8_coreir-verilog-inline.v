module coreir_reg #(parameter width = 1, parameter clk_posedge = 1, parameter init = 1) (input clk, input [width-1:0] in, output [width-1:0] out);
  reg [width-1:0] outReg=init;
  wire real_clk;
  assign real_clk = clk_posedge ? clk : ~clk;
  always @(posedge real_clk) begin
    outReg <= in;
  end
  assign out = outReg;
endmodule

module commonlib_muxn__N2__width8 (input [7:0] in_data_0, input [7:0] in_data_1, input [0:0] in_sel, output [7:0] out);
assign out = in_sel[0] ? in_data_1 : in_data_0;
endmodule

module Mux2x8 (input [7:0] I0, input [7:0] I1, output [7:0] O, input S);
commonlib_muxn__N2__width8 coreir_commonlib_mux2x8_inst0(.in_data_0(I0), .in_data_1(I1), .in_sel(S), .out(O));
endmodule

module DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse (input CLK, input I, output O);
wire [0:0] reg_P_inst0_out;
coreir_reg #(.clk_posedge(1'b1), .init(1'h0), .width(1)) reg_P_inst0(.clk(CLK), .in(I), .out(reg_P_inst0_out));
assign O = reg_P_inst0_out[0];
endmodule

module Register8 (input CLK, input [7:0] I, output [7:0] O);
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst4_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst5_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst6_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst7_O;
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0(.CLK(CLK), .I(I[0]), .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O));
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1(.CLK(CLK), .I(I[1]), .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O));
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2(.CLK(CLK), .I(I[2]), .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_O));
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3(.CLK(CLK), .I(I[3]), .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_O));
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst4(.CLK(CLK), .I(I[4]), .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst4_O));
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst5(.CLK(CLK), .I(I[5]), .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst5_O));
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst6(.CLK(CLK), .I(I[6]), .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst6_O));
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst7(.CLK(CLK), .I(I[7]), .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst7_O));
assign O = {DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst7_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst6_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst5_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst4_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O};
endmodule

module Add8_cout (output COUT, input [7:0] I0, input [7:0] I1, output [7:0] O);
wire [8:0] coreir_add9_inst0_out;
assign coreir_add9_inst0_out = ({1'b0,I0[7],I0[6],I0[5],I0[4],I0[3],I0[2],I0[1],I0[0]}) + ({1'b0,I1[7],I1[6],I1[5],I1[4],I1[3],I1[2],I1[1],I1[0]});
assign COUT = coreir_add9_inst0_out[8];
assign O = {coreir_add9_inst0_out[7],coreir_add9_inst0_out[6],coreir_add9_inst0_out[5],coreir_add9_inst0_out[4],coreir_add9_inst0_out[3],coreir_add9_inst0_out[2],coreir_add9_inst0_out[1],coreir_add9_inst0_out[0]};
endmodule

module CounterLoad8_COUT (input CLK, output COUT, input [7:0] DATA, input LOAD, output [7:0] O);
wire [7:0] Add8_cout_inst0_O;
wire [7:0] Mux2x8_inst0_O;
Add8_cout Add8_cout_inst0(.COUT(COUT), .I0(O), .I1(8'h01), .O(Add8_cout_inst0_O));
Mux2x8 Mux2x8_inst0(.I0(Add8_cout_inst0_O), .I1(DATA), .O(Mux2x8_inst0_O), .S(LOAD));
Register8 Register8_inst0(.CLK(CLK), .I(Mux2x8_inst0_O), .O(O));
endmodule

