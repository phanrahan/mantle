module Add4_cout (input [3:0] I0, input [3:0] I1, output [3:0] O, output  COUT);
wire [4:0] inst0_out;
coreir_add5 inst0 (.in0({1'b0,I0[3],I0[2],I0[1],I0[0]}), .in1({1'b0,I1[3],I1[2],I1[1],I1[0]}), .out(inst0_out));
assign O = {inst0_out[3],inst0_out[2],inst0_out[1],inst0_out[0]};
assign COUT = inst0_out[4];
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

module Counter4 (output [3:0] O, output  COUT, input  CLK);
wire [3:0] inst0_O;
wire  inst0_COUT;
wire [3:0] inst1_O;
Add4_cout inst0 (.I0(inst1_O), .I1({1'b0,1'b0,1'b0,1'b1}), .O(inst0_O), .COUT(inst0_COUT));
Register4 inst1 (.I(inst0_O), .O(inst1_O), .CLK(CLK));
assign O = inst1_O;
assign COUT = inst0_COUT;
endmodule

