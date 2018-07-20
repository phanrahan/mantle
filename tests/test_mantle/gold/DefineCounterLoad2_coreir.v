module Add2_cout (input [1:0] I0, input [1:0] I1, output [1:0] O, output  COUT);
wire [2:0] inst0_out;
coreir_add3 inst0 (.in0({1'b0,I0[1],I0[0]}), .in1({1'b0,I1[1],I1[0]}), .out(inst0_out));
assign O = {inst0_out[1],inst0_out[0]};
assign COUT = inst0_out[2];
endmodule

module _Mux2 (input [1:0] I, input  S, output  O);
wire  inst0_out;
coreir_bitmux inst0 (.in0(I[0]), .in1(I[1]), .sel(S), .out(inst0_out));
assign O = inst0_out;
endmodule

module Mux2x2 (input [1:0] I0, input [1:0] I1, input  S, output [1:0] O);
wire  inst0_O;
wire  inst1_O;
_Mux2 inst0 (.I({I1[0],I0[0]}), .S(S), .O(inst0_O));
_Mux2 inst1 (.I({I1[1],I0[1]}), .S(S), .O(inst1_O));
assign O = {inst1_O,inst0_O};
endmodule

module DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse (input  I, output  O, input  CLK);
wire [0:0] inst0_out;
coreir_reg_P #(.init(0)) inst0 (.in({I}), .clk(CLK), .out(inst0_out));
assign O = inst0_out[0];
endmodule

module Register2 (input [1:0] I, output [1:0] O, input  CLK);
wire  inst0_O;
wire  inst1_O;
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse inst0 (.I(I[0]), .O(inst0_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse inst1 (.I(I[1]), .O(inst1_O), .CLK(CLK));
assign O = {inst1_O,inst0_O};
endmodule

module CounterLoad2 (input [1:0] DATA, input  LOAD, output [1:0] O, output  COUT, input  CLK);
wire [1:0] inst0_O;
wire  inst0_COUT;
wire [1:0] inst1_O;
wire [1:0] inst2_O;
Add2_cout inst0 (.I0(inst2_O), .I1({1'b0,1'b1}), .O(inst0_O), .COUT(inst0_COUT));
Mux2x2 inst1 (.I0(inst0_O), .I1(DATA), .S(LOAD), .O(inst1_O));
Register2 inst2 (.I(inst1_O), .O(inst2_O), .CLK(CLK));
assign O = inst2_O;
assign COUT = inst0_COUT;
endmodule

