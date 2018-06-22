module EQ8 (input [7:0] I0, input [7:0] I1, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
LUT4 #(.INIT(16'h9009)) inst0 (.I0(I0[0]), .I1(I1[0]), .I2(I0[1]), .I3(I1[1]), .O(inst0_O));
MUXCY inst1 (.DI(1'b0), .CI(1'b1), .S(inst0_O), .O(inst1_O));
LUT4 #(.INIT(16'h9009)) inst2 (.I0(I0[2]), .I1(I1[2]), .I2(I0[3]), .I3(I1[3]), .O(inst2_O));
MUXCY inst3 (.DI(1'b0), .CI(inst1_O), .S(inst2_O), .O(inst3_O));
LUT4 #(.INIT(16'h9009)) inst4 (.I0(I0[4]), .I1(I1[4]), .I2(I0[5]), .I3(I1[5]), .O(inst4_O));
MUXCY inst5 (.DI(1'b0), .CI(inst3_O), .S(inst4_O), .O(inst5_O));
LUT4 #(.INIT(16'h9009)) inst6 (.I0(I0[6]), .I1(I1[6]), .I2(I0[7]), .I3(I1[7]), .O(inst6_O));
MUXCY inst7 (.DI(1'b0), .CI(inst5_O), .S(inst6_O), .O(inst7_O));
assign O = inst7_O;
endmodule

