module FlatCascade8x6_8000000000000000_1_1_0 (input [7:0] I, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
LUT6 #(.INIT(64'h8000000000000000)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .I4(I[4]), .I5(I[5]), .O(inst0_O));
MUXCY inst1 (.DI(1'b1), .CI(1'b0), .S(inst0_O), .O(inst1_O));
LUT6 #(.INIT(64'h8000000000000000)) inst2 (.I0(I[6]), .I1(I[7]), .I2(1'b1), .I3(1'b1), .I4(1'b1), .I5(1'b1), .O(inst2_O));
MUXCY inst3 (.DI(1'b1), .CI(inst1_O), .S(inst2_O), .O(inst3_O));
assign O = inst3_O;
endmodule

module main (output [0:0] LED, input [7:0] SWITCH);
wire  inst0_O;
FlatCascade8x6_8000000000000000_1_1_0 inst0 (.I(SWITCH), .O(inst0_O));
assign LED = {inst0_O};
endmodule

