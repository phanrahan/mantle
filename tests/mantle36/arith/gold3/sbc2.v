module Adders2_9_A_cinNone_cout1 (input [1:0] I0, input [1:0] I1, output [1:0] O, output  COUT);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
LUT2 #(.INIT(4'h9)) inst0 (.I0(I0[0]), .I1(I1[0]), .O(inst0_O));
MUXCY inst1 (.DI(I0[0]), .CI(1'b1), .S(inst0_O), .O(inst1_O));
XORCY inst2 (.LI(inst0_O), .CI(1'b1), .O(inst2_O));
LUT2 #(.INIT(4'h9)) inst3 (.I0(I0[1]), .I1(I1[1]), .O(inst3_O));
MUXCY inst4 (.DI(I0[1]), .CI(inst1_O), .S(inst3_O), .O(inst4_O));
XORCY inst5 (.LI(inst3_O), .CI(inst1_O), .O(inst5_O));
assign O = {inst5_O,inst2_O};
assign COUT = inst4_O;
endmodule

module main (output [2:0] LED, input [3:0] SWITCH);
wire [1:0] inst0_O;
wire  inst0_COUT;
Adders2_9_A_cinNone_cout1 inst0 (.I0({SWITCH[1],SWITCH[0]}), .I1({SWITCH[3],SWITCH[2]}), .O(inst0_O), .COUT(inst0_COUT));
assign LED = {inst0_COUT,inst0_O[1],inst0_O[0]};
endmodule

