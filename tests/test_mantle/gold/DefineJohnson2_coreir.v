module DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse (input  I, output  O, input  CLK);
wire [0:0] inst0_out;
coreir_reg_P #(.init(0)) inst0 (.in({I}), .clk(CLK), .out(inst0_out));
assign O = inst0_out[0];
endmodule

module Johnson2 (output [1:0] O, input  CLK);
wire  inst0_O;
wire  inst1_O;
wire  inst2_out;
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse inst0 (.I(inst2_out), .O(inst0_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse inst1 (.I(inst0_O), .O(inst1_O), .CLK(CLK));
coreir_bitnot inst2 (.in(inst1_O), .out(inst2_out));
assign O = {inst1_O,inst0_O};
endmodule

