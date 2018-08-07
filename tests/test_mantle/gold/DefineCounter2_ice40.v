module FullAdder (input  I0, input  I1, input  CIN, output  O, output  COUT);
wire  inst0_O;
wire  inst1_CO;
SB_LUT4 #(.LUT_INIT(16'h9696)) inst0 (.I0(I0), .I1(I1), .I2(CIN), .I3(1'b0), .O(inst0_O));
SB_CARRY inst1 (.I0(I0), .I1(I1), .CI(CIN), .CO(inst1_CO));
assign O = inst0_O;
assign COUT = inst1_CO;
endmodule

module Add2_COUT (input [1:0] I0, input [1:0] I1, output [1:0] O, output  COUT);
wire  inst0_O;
wire  inst0_COUT;
wire  inst1_O;
wire  inst1_COUT;
FullAdder inst0 (.I0(I0[0]), .I1(I1[0]), .CIN(1'b0), .O(inst0_O), .COUT(inst0_COUT));
FullAdder inst1 (.I0(I0[1]), .I1(I1[1]), .CIN(inst0_COUT), .O(inst1_O), .COUT(inst1_COUT));
assign O = {inst1_O,inst0_O};
assign COUT = inst1_COUT;
endmodule

module Register2 (input [1:0] I, output [1:0] O, input  CLK);
wire  inst0_Q;
wire  inst1_Q;
SB_DFF inst0 (.C(CLK), .D(I[0]), .Q(inst0_Q));
SB_DFF inst1 (.C(CLK), .D(I[1]), .Q(inst1_Q));
assign O = {inst1_Q,inst0_Q};
endmodule

module Counter2_COUT (output [1:0] O, output  COUT, input  CLK);
wire [1:0] inst0_O;
wire  inst0_COUT;
wire [1:0] inst1_O;
Add2_COUT inst0 (.I0(inst1_O), .I1({1'b0,1'b1}), .O(inst0_O), .COUT(inst0_COUT));
Register2 inst1 (.I(inst0_O), .O(inst1_O), .CLK(CLK));
assign O = inst1_O;
assign COUT = inst0_COUT;
endmodule

