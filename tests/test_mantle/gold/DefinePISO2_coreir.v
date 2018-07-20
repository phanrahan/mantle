module _Mux2 (input [1:0] I, input  S, output  O);
wire  inst0_out;
coreir_bitmux inst0 (.in0(I[0]), .in1(I[1]), .sel(S), .out(inst0_out));
assign O = inst0_out;
endmodule

module DFF_init0_has_ceFalse_has_resetFalse (input  I, output  O, input  CLK);
wire [0:0] inst0_out;
coreir_reg_P #(.init(0)) inst0 (.in({I}), .clk(CLK), .out(inst0_out));
assign O = inst0_out[0];
endmodule

module Register2 (input [1:0] I, output [1:0] O, input  CLK);
wire  inst0_O;
wire  inst1_O;
DFF_init0_has_ceFalse_has_resetFalse inst0 (.I(I[0]), .O(inst0_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst1 (.I(I[1]), .O(inst1_O), .CLK(CLK));
assign O = {inst1_O,inst0_O};
endmodule

module PISO2 (input  SI, input [1:0] PI, input  LOAD, output  O, input  CLK);
wire  inst0_O;
wire  inst1_O;
wire [1:0] inst2_O;
_Mux2 inst0 (.I({PI[0],SI}), .S(LOAD), .O(inst0_O));
_Mux2 inst1 (.I({PI[1],inst2_O[0]}), .S(LOAD), .O(inst1_O));
Register2 inst2 (.I({inst1_O,inst0_O}), .O(inst2_O), .CLK(CLK));
assign O = inst2_O[1];
endmodule

