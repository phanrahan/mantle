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

