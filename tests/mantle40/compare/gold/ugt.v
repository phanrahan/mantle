module Invert8 (input [7:0] I, output [7:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
SB_LUT4 #(.LUT_INIT(16'h5555)) inst0 (.I0(I[0]), .I1(1'b0), .I2(1'b0), .I3(1'b0), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'h5555)) inst1 (.I0(I[1]), .I1(1'b0), .I2(1'b0), .I3(1'b0), .O(inst1_O));
SB_LUT4 #(.LUT_INIT(16'h5555)) inst2 (.I0(I[2]), .I1(1'b0), .I2(1'b0), .I3(1'b0), .O(inst2_O));
SB_LUT4 #(.LUT_INIT(16'h5555)) inst3 (.I0(I[3]), .I1(1'b0), .I2(1'b0), .I3(1'b0), .O(inst3_O));
SB_LUT4 #(.LUT_INIT(16'h5555)) inst4 (.I0(I[4]), .I1(1'b0), .I2(1'b0), .I3(1'b0), .O(inst4_O));
SB_LUT4 #(.LUT_INIT(16'h5555)) inst5 (.I0(I[5]), .I1(1'b0), .I2(1'b0), .I3(1'b0), .O(inst5_O));
SB_LUT4 #(.LUT_INIT(16'h5555)) inst6 (.I0(I[6]), .I1(1'b0), .I2(1'b0), .I3(1'b0), .O(inst6_O));
SB_LUT4 #(.LUT_INIT(16'h5555)) inst7 (.I0(I[7]), .I1(1'b0), .I2(1'b0), .I3(1'b0), .O(inst7_O));
assign O = {inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module Add8 (input [7:0] I0, input [7:0] I1, output [7:0] O, output  COUT);
wire  inst0_O;
wire  inst1_CO;
wire  inst2_O;
wire  inst3_CO;
wire  inst4_O;
wire  inst5_CO;
wire  inst6_O;
wire  inst7_CO;
wire  inst8_O;
wire  inst9_CO;
wire  inst10_O;
wire  inst11_CO;
wire  inst12_O;
wire  inst13_CO;
wire  inst14_O;
wire  inst15_CO;
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst0 (.I0(1'b0), .I1(I0[0]), .I2(I1[0]), .I3(1'b0), .O(inst0_O));
SB_CARRY inst1 (.I0(I0[0]), .I1(I1[0]), .CI(1'b0), .CO(inst1_CO));
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst2 (.I0(1'b0), .I1(I0[1]), .I2(I1[1]), .I3(inst1_CO), .O(inst2_O));
SB_CARRY inst3 (.I0(I0[1]), .I1(I1[1]), .CI(inst1_CO), .CO(inst3_CO));
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst4 (.I0(1'b0), .I1(I0[2]), .I2(I1[2]), .I3(inst3_CO), .O(inst4_O));
SB_CARRY inst5 (.I0(I0[2]), .I1(I1[2]), .CI(inst3_CO), .CO(inst5_CO));
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst6 (.I0(1'b0), .I1(I0[3]), .I2(I1[3]), .I3(inst5_CO), .O(inst6_O));
SB_CARRY inst7 (.I0(I0[3]), .I1(I1[3]), .CI(inst5_CO), .CO(inst7_CO));
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst8 (.I0(1'b0), .I1(I0[4]), .I2(I1[4]), .I3(inst7_CO), .O(inst8_O));
SB_CARRY inst9 (.I0(I0[4]), .I1(I1[4]), .CI(inst7_CO), .CO(inst9_CO));
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst10 (.I0(1'b0), .I1(I0[5]), .I2(I1[5]), .I3(inst9_CO), .O(inst10_O));
SB_CARRY inst11 (.I0(I0[5]), .I1(I1[5]), .CI(inst9_CO), .CO(inst11_CO));
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst12 (.I0(1'b0), .I1(I0[6]), .I2(I1[6]), .I3(inst11_CO), .O(inst12_O));
SB_CARRY inst13 (.I0(I0[6]), .I1(I1[6]), .CI(inst11_CO), .CO(inst13_CO));
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst14 (.I0(1'b0), .I1(I0[7]), .I2(I1[7]), .I3(inst13_CO), .O(inst14_O));
SB_CARRY inst15 (.I0(I0[7]), .I1(I1[7]), .CI(inst13_CO), .CO(inst15_CO));
assign O = {inst14_O,inst12_O,inst10_O,inst8_O,inst6_O,inst4_O,inst2_O,inst0_O};
assign COUT = inst15_CO;
endmodule

module main (input  A0, input  A1, input  B0, input  B1, output  D1);
wire  inst0_O;
wire [7:0] inst1_O;
wire [7:0] inst2_O;
wire  inst2_COUT;
SB_LUT4 #(.LUT_INIT(16'h5555)) inst0 (.I0(inst2_COUT), .I1(1'b0), .I2(1'b0), .I3(1'b0), .O(inst0_O));
Invert8 inst1 (.I({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,A1,A0}), .O(inst1_O));
Add8 inst2 (.I0({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,B1,B0}), .I1(inst1_O), .O(inst2_O), .COUT(inst2_COUT));
assign D1 = inst0_O;
endmodule

