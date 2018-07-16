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

module Ring2_0001 (output [1:0] O, input  CLK);
wire  inst0_O;
wire  inst1_O;
DFF_init1_has_ceFalse_has_resetFalse inst0 (.I(inst1_O), .O(inst0_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse inst1 (.I(inst0_O), .O(inst1_O), .CLK(CLK));
assign O = {inst1_O,inst0_O};
endmodule

