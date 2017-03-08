module main (input  A0, input  A1, input  B0, input  B1, output  D3, output  D2, output  D1);
wire  inst0_O;
wire  inst1_CO;
wire  inst2_O;
wire  inst3_CO;
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst0 (.I0(1'b0), .I1(A0), .I2(B0), .I3(1'b0), .O(inst0_O));
SB_CARRY inst1 (.I0(A0), .I1(B0), .CI(1'b0), .CO(inst1_CO));
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst2 (.I0(1'b0), .I1(A1), .I2(B1), .I3(inst1_CO), .O(inst2_O));
SB_CARRY inst3 (.I0(A1), .I1(B1), .CI(inst1_CO), .CO(inst3_CO));
assign D3 = inst3_CO;
assign D2 = inst2_O;
assign D1 = inst0_O;
endmodule

