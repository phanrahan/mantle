module Adc2 (input [1:0] I0, input [1:0] I1, input  CIN, output [1:0] O, output  COUT);
wire  inst0_O;
wire  inst1_CO;
wire  inst2_O;
wire  inst3_CO;
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst0 (.I0(1'b0), .I1(I0[0]), .I2(I1[0]), .I3(CIN), .O(inst0_O));
SB_CARRY inst1 (.I0(I0[0]), .I1(I1[0]), .CI(CIN), .CO(inst1_CO));
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst2 (.I0(1'b0), .I1(I0[1]), .I2(I1[1]), .I3(inst1_CO), .O(inst2_O));
SB_CARRY inst3 (.I0(I0[1]), .I1(I1[1]), .CI(inst1_CO), .CO(inst3_CO));
assign O = {inst2_O,inst0_O};
assign COUT = inst3_CO;
endmodule

module main (input  A0, input  A1, input  B0, input  B1, input  CIN, output  D3, output  D2, output  D1, input  CLKIN);
wire [1:0] inst0_O;
wire  inst0_COUT;
Adc2 inst0 (.I0({A1,A0}), .I1({B1,B0}), .CIN(CIN), .O(inst0_O), .COUT(inst0_COUT));
assign D3 = inst0_COUT;
assign D2 = inst0_O[1];
assign D1 = inst0_O[0];
endmodule

