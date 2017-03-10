module FlatCascade16x6_8000000000000000_1_0_1 (input [15:0] I, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
LUT6 #(.INIT(64'h8000000000000000)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .I4(I[4]), .I5(I[5]), .O(inst0_O));
MUXCY inst1 (.DI(1'b0), .CI(1'b1), .S(inst0_O), .O(inst1_O));
LUT6 #(.INIT(64'h8000000000000000)) inst2 (.I0(I[6]), .I1(I[7]), .I2(I[8]), .I3(I[9]), .I4(I[10]), .I5(I[11]), .O(inst2_O));
MUXCY inst3 (.DI(1'b0), .CI(inst1_O), .S(inst2_O), .O(inst3_O));
LUT6 #(.INIT(64'h8000000000000000)) inst4 (.I0(I[12]), .I1(I[13]), .I2(I[14]), .I3(I[15]), .I4(1'b1), .I5(1'b1), .O(inst4_O));
MUXCY inst5 (.DI(1'b0), .CI(inst3_O), .S(inst4_O), .O(inst5_O));
assign O = inst5_O;
endmodule

module main (output [0:0] LED, input [7:0] SWITCH);
wire  inst0_O;
FlatCascade16x6_8000000000000000_1_0_1 inst0 (.I({SWITCH[7],SWITCH[6],SWITCH[5],SWITCH[4],SWITCH[3],SWITCH[2],SWITCH[1],SWITCH[0],SWITCH[7],SWITCH[6],SWITCH[5],SWITCH[4],SWITCH[3],SWITCH[2],SWITCH[1],SWITCH[0]}), .O(inst0_O));
assign LED = {inst0_O};
endmodule

