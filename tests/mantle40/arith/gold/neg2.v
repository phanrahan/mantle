module Invert2 (input [1:0] I, output [1:0] O);
wire  inst0_O;
wire  inst1_O;
SB_LUT4 #(.LUT_INIT(16'h5555)) inst0 (.I0(I[0]), .I1(1'b0), .I2(1'b0), .I3(1'b0), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'h5555)) inst1 (.I0(I[1]), .I1(1'b0), .I2(1'b0), .I3(1'b0), .O(inst1_O));
assign O = {inst1_O,inst0_O};
endmodule

module Addcin2 (input [1:0] I0, input [1:0] I1, input  CIN, output [1:0] O);
wire  inst0_O;
wire  inst1_CO;
wire  inst2_O;
wire  inst3_CO;
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst0 (.I0(1'b0), .I1(I0[0]), .I2(I1[0]), .I3(CIN), .O(inst0_O));
SB_CARRY inst1 (.I0(I0[0]), .I1(I1[0]), .CI(CIN), .CO(inst1_CO));
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst2 (.I0(1'b0), .I1(I0[1]), .I2(I1[1]), .I3(inst1_CO), .O(inst2_O));
SB_CARRY inst3 (.I0(I0[1]), .I1(I1[1]), .CI(inst1_CO), .CO(inst3_CO));
assign O = {inst2_O,inst0_O};
endmodule

module main (input  I0, input  I1, output  D2, output  D1);
wire [1:0] inst0_O;
wire [1:0] inst1_O;
Invert2 inst0 (.I({I1,I0}), .O(inst0_O));
Addcin2 inst1 (.I0({1'b0,1'b0}), .I1(inst0_O), .CIN(1'b1), .O(inst1_O));
assign D2 = inst1_O[1];
assign D1 = inst1_O[0];
endmodule

