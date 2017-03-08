module Add4 (input [3:0] I0, input [3:0] I1, output [3:0] O);
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
endmodule

module Arbiter4 (input [3:0] I, output [3:0] O);
wire [3:0] inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
Add4 inst0 (.I0(I), .I1({1'b1,1'b1,1'b1,1'b1}), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'h2222)) inst1 (.I0(I[0]), .I1(inst0_O[0]), .I2(1'b0), .I3(1'b0), .O(inst1_O));
SB_LUT4 #(.LUT_INIT(16'h2222)) inst2 (.I0(I[1]), .I1(inst0_O[1]), .I2(1'b0), .I3(1'b0), .O(inst2_O));
SB_LUT4 #(.LUT_INIT(16'h2222)) inst3 (.I0(I[2]), .I1(inst0_O[2]), .I2(1'b0), .I3(1'b0), .O(inst3_O));
SB_LUT4 #(.LUT_INIT(16'h2222)) inst4 (.I0(I[3]), .I1(inst0_O[3]), .I2(1'b0), .I3(1'b0), .O(inst4_O));
assign O = {inst4_O,inst3_O,inst2_O,inst1_O};
endmodule

module Encoder4 (input [3:0] I, output [1:0] O);
wire  inst0_O;
wire  inst1_O;
SB_LUT4 #(.LUT_INIT(16'hEEEE)) inst0 (.I0(I[1]), .I1(I[3]), .I2(1'b0), .I3(1'b0), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'hEEEE)) inst1 (.I0(I[2]), .I1(I[3]), .I2(1'b0), .I3(1'b0), .O(inst1_O));
assign O = {inst1_O,inst0_O};
endmodule

module main (input [3:0] J1, output [1:0] J3);
wire [3:0] inst0_O;
wire [1:0] inst1_O;
Arbiter4 inst0 (.I(J1), .O(inst0_O));
Encoder4 inst1 (.I(inst0_O), .O(inst1_O));
assign J3 = inst1_O;
endmodule

