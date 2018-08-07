module Add2_cout (input [1:0] I0, input [1:0] I1, output [1:0] O, output  COUT);
wire [2:0] inst0_out;
coreir_add3 inst0 (.in0({1'b0,I0[1],I0[0]}), .in1({1'b0,I1[1],I1[0]}), .out(inst0_out));
assign O = {inst0_out[1],inst0_out[0]};
assign COUT = inst0_out[2];
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

module Counter2_COUT (output [1:0] O, output  COUT, input  CLK);
wire [1:0] inst0_O;
wire  inst0_COUT;
wire [1:0] inst1_O;
Add2_cout inst0 (.I0(inst1_O), .I1({1'b0,1'b1}), .O(inst0_O), .COUT(inst0_COUT));
Register2 inst1 (.I(inst0_O), .O(inst1_O), .CLK(CLK));
assign O = inst1_O;
assign COUT = inst0_COUT;
endmodule

