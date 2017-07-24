module Addcout4 (input [3:0] I0, input [3:0] I1, output [3:0] O, output  COUT);
wire  inst0_O;
wire  inst1_CO;
wire  inst2_O;
wire  inst3_CO;
wire  inst4_O;
wire  inst5_CO;
wire  inst6_O;
wire  inst7_CO;
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst0 (.I0(1'b0), .I1(I0[0]), .I2(I1[0]), .I3(1'b0), .O(inst0_O));
SB_CARRY inst1 (.I0(I0[0]), .I1(I1[0]), .CI(1'b0), .CO(inst1_CO));
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst2 (.I0(1'b0), .I1(I0[1]), .I2(I1[1]), .I3(inst1_CO), .O(inst2_O));
SB_CARRY inst3 (.I0(I0[1]), .I1(I1[1]), .CI(inst1_CO), .CO(inst3_CO));
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst4 (.I0(1'b0), .I1(I0[2]), .I2(I1[2]), .I3(inst3_CO), .O(inst4_O));
SB_CARRY inst5 (.I0(I0[2]), .I1(I1[2]), .CI(inst3_CO), .CO(inst5_CO));
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst6 (.I0(1'b0), .I1(I0[3]), .I2(I1[3]), .I3(inst5_CO), .O(inst6_O));
SB_CARRY inst7 (.I0(I0[3]), .I1(I1[3]), .CI(inst5_CO), .CO(inst7_CO));
assign O = {inst6_O,inst4_O,inst2_O,inst0_O};
assign COUT = inst7_CO;
endmodule

module Register4R (input [3:0] I, output [3:0] O, input  CLK, input  RESET);
wire  inst0_Q;
wire  inst1_Q;
wire  inst2_Q;
wire  inst3_Q;
SB_DFFSR inst0 (.C(CLK), .R(RESET), .D(I[0]), .Q(inst0_Q));
SB_DFFSR inst1 (.C(CLK), .R(RESET), .D(I[1]), .Q(inst1_Q));
SB_DFFSR inst2 (.C(CLK), .R(RESET), .D(I[2]), .Q(inst2_Q));
SB_DFFSR inst3 (.C(CLK), .R(RESET), .D(I[3]), .Q(inst3_Q));
assign O = {inst3_Q,inst2_Q,inst1_Q,inst0_Q};
endmodule

module Counter4R (output [3:0] O, output  COUT, input  CLK, input  RESET);
wire [3:0] inst0_O;
wire  inst0_COUT;
wire [3:0] inst1_O;
Addcout4 inst0 (.I0(inst1_O), .I1({1'b0,1'b0,1'b0,1'b1}), .O(inst0_O), .COUT(inst0_COUT));
Register4R inst1 (.I(inst0_O), .O(inst1_O), .CLK(CLK), .RESET(RESET));
assign O = inst1_O;
assign COUT = inst0_COUT;
endmodule

module CounterModM4 (output [3:0] O, output  COUT, input  CLK);
wire [3:0] inst0_O;
wire  inst0_COUT;
wire  inst1_O;
Counter4R inst0 (.O(inst0_O), .COUT(inst0_COUT), .CLK(CLK), .RESET(inst1_O));
SB_LUT4 #(.LUT_INIT(16'h0200)) inst1 (.I0(inst0_O[0]), .I1(inst0_O[1]), .I2(inst0_O[2]), .I3(inst0_O[3]), .O(inst1_O));
assign O = inst0_O;
assign COUT = inst1_O;
endmodule

module main (output [5:0] J3, input  CLKIN);
wire [3:0] inst0_O;
wire  inst0_COUT;
CounterModM4 inst0 (.O(inst0_O), .COUT(inst0_COUT), .CLK(CLKIN));
assign J3 = {inst0_COUT,inst0_O[3],inst0_O[2],inst0_O[1],inst0_O[0],CLKIN};
endmodule

