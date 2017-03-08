module FlatCascade8x2_8 (input [7:0] I, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
SB_LUT4 #(.LUT_INIT(16'h8888)) inst0 (.I0(1'b1), .I1(I[0]), .I2(1'b0), .I3(1'b0), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'h8888)) inst1 (.I0(inst0_O), .I1(I[1]), .I2(1'b0), .I3(1'b0), .O(inst1_O));
SB_LUT4 #(.LUT_INIT(16'h8888)) inst2 (.I0(inst1_O), .I1(I[2]), .I2(1'b0), .I3(1'b0), .O(inst2_O));
SB_LUT4 #(.LUT_INIT(16'h8888)) inst3 (.I0(inst2_O), .I1(I[3]), .I2(1'b0), .I3(1'b0), .O(inst3_O));
SB_LUT4 #(.LUT_INIT(16'h8888)) inst4 (.I0(inst3_O), .I1(I[4]), .I2(1'b0), .I3(1'b0), .O(inst4_O));
SB_LUT4 #(.LUT_INIT(16'h8888)) inst5 (.I0(inst4_O), .I1(I[5]), .I2(1'b0), .I3(1'b0), .O(inst5_O));
SB_LUT4 #(.LUT_INIT(16'h8888)) inst6 (.I0(inst5_O), .I1(I[6]), .I2(1'b0), .I3(1'b0), .O(inst6_O));
SB_LUT4 #(.LUT_INIT(16'h8888)) inst7 (.I0(inst6_O), .I1(I[7]), .I2(1'b0), .I3(1'b0), .O(inst7_O));
assign O = inst7_O;
endmodule

module main (input [7:0] J1, output  D5);
wire  inst0_O;
FlatCascade8x2_8 inst0 (.I(J1), .O(inst0_O));
assign D5 = inst0_O;
endmodule

