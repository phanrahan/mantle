module _Mux2 (input [1:0] I, input  S, output  O);
wire  inst0_out;
coreir_bitmux inst0 (.in0(I[0]), .in1(I[1]), .sel(S), .out(inst0_out));
assign O = inst0_out;
endmodule

module DFF_init0_has_ceFalse_has_resetFalse (input  I, output  O, input  CLK, input  RESET);
wire [0:0] inst0_out;
coreir_reg_P #(.init(0)) inst0 (.in({I}), .clk(CLK), .out(inst0_out));
assign O = inst0_out[0];
endmodule

module Register8 (input [7:0] I, output [7:0] O, input  CLK);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
DFF_init0_has_ceFalse_has_resetFalse inst0 (.I(I[0]), .O(inst0_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst1 (.I(I[1]), .O(inst1_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst2 (.I(I[2]), .O(inst2_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst3 (.I(I[3]), .O(inst3_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst4 (.I(I[4]), .O(inst4_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst5 (.I(I[5]), .O(inst5_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst6 (.I(I[6]), .O(inst6_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst7 (.I(I[7]), .O(inst7_O), .CLK(CLK));
assign O = {inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module PISO8 (input  SI, input [7:0] PI, input  LOAD, output  O, input  CLK);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
wire [7:0] inst8_O;
_Mux2 inst0 (.I({PI[0],SI}), .S(LOAD), .O(inst0_O));
_Mux2 inst1 (.I({PI[1],inst8_O[0]}), .S(LOAD), .O(inst1_O));
_Mux2 inst2 (.I({PI[2],inst8_O[1]}), .S(LOAD), .O(inst2_O));
_Mux2 inst3 (.I({PI[3],inst8_O[2]}), .S(LOAD), .O(inst3_O));
_Mux2 inst4 (.I({PI[4],inst8_O[3]}), .S(LOAD), .O(inst4_O));
_Mux2 inst5 (.I({PI[5],inst8_O[4]}), .S(LOAD), .O(inst5_O));
_Mux2 inst6 (.I({PI[6],inst8_O[5]}), .S(LOAD), .O(inst6_O));
_Mux2 inst7 (.I({PI[7],inst8_O[6]}), .S(LOAD), .O(inst7_O));
Register8 inst8 (.I({inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O}), .O(inst8_O), .CLK(CLK));
assign O = inst8_O[7];
endmodule

