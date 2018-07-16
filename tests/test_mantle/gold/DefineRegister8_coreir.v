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

