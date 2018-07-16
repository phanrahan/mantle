module DFF_init1_has_ceFalse_has_resetFalse (input  I, output  O, input  CLK, input  RESET);
wire [0:0] inst0_out;
coreir_reg_P #(.init(1)) inst0 (.in({I}), .clk(CLK), .out(inst0_out));
assign O = inst0_out[0];
endmodule

module DFF_init0_has_ceFalse_has_resetFalse (input  I, output  O, input  CLK, input  RESET);
wire [0:0] inst0_out;
coreir_reg_P #(.init(0)) inst0 (.in({I}), .clk(CLK), .out(inst0_out));
assign O = inst0_out[0];
endmodule

module Ring8_0001 (output [7:0] O, input  CLK);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
DFF_init1_has_ceFalse_has_resetFalse inst0 (.I(inst7_O), .O(inst0_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst1 (.I(inst0_O), .O(inst1_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst2 (.I(inst1_O), .O(inst2_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst3 (.I(inst2_O), .O(inst3_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst4 (.I(inst3_O), .O(inst4_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst5 (.I(inst4_O), .O(inst5_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst6 (.I(inst5_O), .O(inst6_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst7 (.I(inst6_O), .O(inst7_O), .CLK(CLK));
assign O = {inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

