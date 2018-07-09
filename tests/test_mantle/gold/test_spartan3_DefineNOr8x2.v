module NOr8 (input [7:0] I, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
LUT4 #(.INIT(16'h0001)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst0_O));
MUXCY inst1 (.DI(1'b1), .CI(1'b0), .S(inst0_O), .O(inst1_O));
LUT4 #(.INIT(16'h0001)) inst2 (.I0(I[4]), .I1(I[5]), .I2(I[6]), .I3(I[7]), .O(inst2_O));
MUXCY inst3 (.DI(1'b1), .CI(inst1_O), .S(inst2_O), .O(inst3_O));
assign O = inst3_O;
endmodule

module NOr8x2 (input [1:0] I0, input [1:0] I1, input [1:0] I2, input [1:0] I3, input [1:0] I4, input [1:0] I5, input [1:0] I6, input [1:0] I7, output [1:0] O);
wire  inst0_O;
wire  inst1_O;
NOr8 inst0 (.I({I7[0],I6[0],I5[0],I4[0],I3[0],I2[0],I1[0],I0[0]}), .O(inst0_O));
NOr8 inst1 (.I({I7[1],I6[1],I5[1],I4[1],I3[1],I2[1],I1[1],I0[1]}), .O(inst1_O));
assign O = {inst1_O,inst0_O};
endmodule

