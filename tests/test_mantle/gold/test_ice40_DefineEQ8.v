module EQ8 (input [7:0] I0, input [7:0] I1, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
SB_LUT4 #(.LUT_INIT(16'h8282)) inst0 (.I0(1'b1), .I1(I0[0]), .I2(I1[0]), .I3(1'b0), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'h8282)) inst1 (.I0(inst0_O), .I1(I0[1]), .I2(I1[1]), .I3(1'b0), .O(inst1_O));
SB_LUT4 #(.LUT_INIT(16'h8282)) inst2 (.I0(inst1_O), .I1(I0[2]), .I2(I1[2]), .I3(1'b0), .O(inst2_O));
SB_LUT4 #(.LUT_INIT(16'h8282)) inst3 (.I0(inst2_O), .I1(I0[3]), .I2(I1[3]), .I3(1'b0), .O(inst3_O));
SB_LUT4 #(.LUT_INIT(16'h8282)) inst4 (.I0(inst3_O), .I1(I0[4]), .I2(I1[4]), .I3(1'b0), .O(inst4_O));
SB_LUT4 #(.LUT_INIT(16'h8282)) inst5 (.I0(inst4_O), .I1(I0[5]), .I2(I1[5]), .I3(1'b0), .O(inst5_O));
SB_LUT4 #(.LUT_INIT(16'h8282)) inst6 (.I0(inst5_O), .I1(I0[6]), .I2(I1[6]), .I3(1'b0), .O(inst6_O));
SB_LUT4 #(.LUT_INIT(16'h8282)) inst7 (.I0(inst6_O), .I1(I0[7]), .I2(I1[7]), .I3(1'b0), .O(inst7_O));
assign O = inst7_O;
endmodule

