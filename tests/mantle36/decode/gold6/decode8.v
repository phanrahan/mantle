module main (output [0:0] LED, input [7:0] SWITCH);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
LUT6 #(.INIT(64'h0000000000000008)) inst0 (.I0(SWITCH[0]), .I1(SWITCH[1]), .I2(SWITCH[2]), .I3(SWITCH[3]), .I4(SWITCH[4]), .I5(SWITCH[5]), .O(inst0_O));
LUT6 #(.INIT(64'h0000000000000000)) inst1 (.I0(SWITCH[0]), .I1(SWITCH[1]), .I2(SWITCH[2]), .I3(SWITCH[3]), .I4(SWITCH[4]), .I5(SWITCH[5]), .O(inst1_O));
MUXF7 inst2 (.I0(inst0_O), .I1(inst1_O), .S(SWITCH[6]), .O(inst2_O));
LUT6 #(.INIT(64'h0000000000000000)) inst3 (.I0(SWITCH[0]), .I1(SWITCH[1]), .I2(SWITCH[2]), .I3(SWITCH[3]), .I4(SWITCH[4]), .I5(SWITCH[5]), .O(inst3_O));
LUT6 #(.INIT(64'h0000000000000000)) inst4 (.I0(SWITCH[0]), .I1(SWITCH[1]), .I2(SWITCH[2]), .I3(SWITCH[3]), .I4(SWITCH[4]), .I5(SWITCH[5]), .O(inst4_O));
MUXF7 inst5 (.I0(inst3_O), .I1(inst4_O), .S(SWITCH[6]), .O(inst5_O));
MUXF8 inst6 (.I0(inst2_O), .I1(inst5_O), .S(SWITCH[7]), .O(inst6_O));
assign LED = {inst6_O};
endmodule

