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

module Register4 (input [3:0] I, output [3:0] O, input  CLK);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
DFF_init0_has_ceFalse_has_resetFalse inst0 (.I(I[0]), .O(inst0_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst1 (.I(I[1]), .O(inst1_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst2 (.I(I[2]), .O(inst2_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst3 (.I(I[3]), .O(inst3_O), .CLK(CLK));
assign O = {inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module PISO4 (input  SI, input [3:0] PI, input  LOAD, output  O, input  CLK);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire [3:0] inst4_O;
_Mux2 inst0 (.I({PI[0],SI}), .S(LOAD), .O(inst0_O));
_Mux2 inst1 (.I({PI[1],inst4_O[0]}), .S(LOAD), .O(inst1_O));
_Mux2 inst2 (.I({PI[2],inst4_O[1]}), .S(LOAD), .O(inst2_O));
_Mux2 inst3 (.I({PI[3],inst4_O[2]}), .S(LOAD), .O(inst3_O));
Register4 inst4 (.I({inst3_O,inst2_O,inst1_O,inst0_O}), .O(inst4_O), .CLK(CLK));
assign O = inst4_O[3];
endmodule

