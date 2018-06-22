module Decode8 (input [7:0] I, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
LUT6 #(.INIT(64'h0000000000000010)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .I4(I[4]), .I5(I[5]), .O(inst0_O));
LUT6 #(.INIT(64'h0000000000000000)) inst1 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .I4(I[4]), .I5(I[5]), .O(inst1_O));
MUXF7 inst2 (.I0(inst0_O), .I1(inst1_O), .S(I[6]), .O(inst2_O));
LUT6 #(.INIT(64'h0000000000000000)) inst3 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .I4(I[4]), .I5(I[5]), .O(inst3_O));
LUT6 #(.INIT(64'h0000000000000000)) inst4 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .I4(I[4]), .I5(I[5]), .O(inst4_O));
MUXF7 inst5 (.I0(inst3_O), .I1(inst4_O), .S(I[6]), .O(inst5_O));
MUXF8 inst6 (.I0(inst2_O), .I1(inst5_O), .S(I[7]), .O(inst6_O));
assign O = inst6_O;
endmodule

