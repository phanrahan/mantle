module main (output [0:0] LED, input [6:0] SWITCH);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
LUT6 #(.INIT(64'hAAAAAAAAAAAAAAAA)) inst0 (.I0(SWITCH[0]), .I1(SWITCH[1]), .I2(SWITCH[2]), .I3(SWITCH[3]), .I4(SWITCH[4]), .I5(SWITCH[5]), .O(inst0_O));
LUT6 #(.INIT(64'hAAAAAAAAAAAAAAAA)) inst1 (.I0(SWITCH[0]), .I1(SWITCH[1]), .I2(SWITCH[2]), .I3(SWITCH[3]), .I4(SWITCH[4]), .I5(SWITCH[5]), .O(inst1_O));
MUXF7 inst2 (.I0(inst0_O), .I1(inst1_O), .S(SWITCH[6]), .O(inst2_O));
assign LED = {inst2_O};
endmodule

