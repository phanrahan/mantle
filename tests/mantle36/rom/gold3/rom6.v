module main (output [0:0] LED, input [5:0] SWITCH);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
LUT4 #(.INIT(16'hAAAA)) inst0 (.I0(SWITCH[0]), .I1(SWITCH[1]), .I2(SWITCH[2]), .I3(SWITCH[3]), .O(inst0_O));
LUT4 #(.INIT(16'hAAAA)) inst1 (.I0(SWITCH[0]), .I1(SWITCH[1]), .I2(SWITCH[2]), .I3(SWITCH[3]), .O(inst1_O));
MUXF5 inst2 (.I0(inst0_O), .I1(inst1_O), .S(SWITCH[4]), .O(inst2_O));
LUT4 #(.INIT(16'hAAAA)) inst3 (.I0(SWITCH[0]), .I1(SWITCH[1]), .I2(SWITCH[2]), .I3(SWITCH[3]), .O(inst3_O));
LUT4 #(.INIT(16'hAAAA)) inst4 (.I0(SWITCH[0]), .I1(SWITCH[1]), .I2(SWITCH[2]), .I3(SWITCH[3]), .O(inst4_O));
MUXF5 inst5 (.I0(inst3_O), .I1(inst4_O), .S(SWITCH[4]), .O(inst5_O));
MUXF6 inst6 (.I0(inst2_O), .I1(inst5_O), .S(SWITCH[5]), .O(inst6_O));
assign LED = {inst6_O};
endmodule

