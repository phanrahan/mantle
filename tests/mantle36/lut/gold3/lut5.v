module main (output [0:0] LED, input [4:0] SWITCH);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
LUT4 #(.INIT(16'hAAAA)) inst0 (.I0(SWITCH[0]), .I1(SWITCH[1]), .I2(SWITCH[2]), .I3(SWITCH[3]), .O(inst0_O));
LUT4 #(.INIT(16'hAAAA)) inst1 (.I0(SWITCH[0]), .I1(SWITCH[1]), .I2(SWITCH[2]), .I3(SWITCH[3]), .O(inst1_O));
MUXF5 inst2 (.I0(inst0_O), .I1(inst1_O), .S(SWITCH[4]), .O(inst2_O));
assign LED = {inst2_O};
endmodule

