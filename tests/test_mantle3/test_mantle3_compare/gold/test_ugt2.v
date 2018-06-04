module Invert2 (input [1:0] I, output [1:0] O);
wire  inst0_O;
wire  inst1_O;
LUT1 #(.INIT(2'h1)) inst0 (.I0(I[0]), .O(inst0_O));
LUT1 #(.INIT(2'h1)) inst1 (.I0(I[1]), .O(inst1_O));
assign O = {inst1_O,inst0_O};
endmodule

module FullAdder (input  I0, input  I1, input  CIN, output  O, output  COUT);
wire  inst0_O;
wire  inst1_LO;
wire  inst2_O;
wire  inst3_O;
LUT2 #(.INIT(4'h6)) inst0 (.I0(I0), .I1(I1), .O(inst0_O));
MULT_AND inst1 (.I0(I0), .I1(I1), .LO(inst1_LO));
MUXCY inst2 (.DI(inst1_LO), .CI(CIN), .S(inst0_O), .O(inst2_O));
XORCY inst3 (.LI(inst0_O), .CI(CIN), .O(inst3_O));
assign O = inst3_O;
assign COUT = inst2_O;
endmodule

module Add2CinCout (input [1:0] I0, input [1:0] I1, input  CIN, output [1:0] O, output  COUT);
wire  inst0_O;
wire  inst0_COUT;
wire  inst1_O;
wire  inst1_COUT;
FullAdder inst0 (.I0(I0[0]), .I1(I1[0]), .CIN(CIN), .O(inst0_O), .COUT(inst0_COUT));
FullAdder inst1 (.I0(I0[1]), .I1(I1[1]), .CIN(inst0_COUT), .O(inst1_O), .COUT(inst1_COUT));
assign O = {inst1_O,inst0_O};
assign COUT = inst1_COUT;
endmodule

module Sub2Cout (input [1:0] I0, input [1:0] I1, output [1:0] O, output  COUT);
wire [1:0] inst0_O;
wire [1:0] inst1_O;
wire  inst1_COUT;
Invert2 inst0 (.I(I1), .O(inst0_O));
Add2CinCout inst1 (.I0(I0), .I1(inst0_O), .CIN(1'b1), .O(inst1_O), .COUT(inst1_COUT));
assign O = inst1_O;
assign COUT = inst1_COUT;
endmodule

module UGT2 (input [1:0] I0, input [1:0] I1, output  O);
wire [1:0] inst0_O;
wire  inst0_COUT;
wire  inst1_O;
Sub2Cout inst0 (.I0(I1), .I1(I0), .O(inst0_O), .COUT(inst0_COUT));
LUT1 #(.INIT(2'h1)) inst1 (.I0(inst0_COUT), .O(inst1_O));
assign O = inst1_O;
endmodule

