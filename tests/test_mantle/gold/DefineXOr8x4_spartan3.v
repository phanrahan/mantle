module XOr8 (input [7:0] I, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
LUT2 #(.INIT(4'h6)) inst0 (.I0(1'b0), .I1(I[0]), .O(inst0_O));
LUT2 #(.INIT(4'h6)) inst1 (.I0(inst0_O), .I1(I[1]), .O(inst1_O));
LUT2 #(.INIT(4'h6)) inst2 (.I0(inst1_O), .I1(I[2]), .O(inst2_O));
LUT2 #(.INIT(4'h6)) inst3 (.I0(inst2_O), .I1(I[3]), .O(inst3_O));
LUT2 #(.INIT(4'h6)) inst4 (.I0(inst3_O), .I1(I[4]), .O(inst4_O));
LUT2 #(.INIT(4'h6)) inst5 (.I0(inst4_O), .I1(I[5]), .O(inst5_O));
LUT2 #(.INIT(4'h6)) inst6 (.I0(inst5_O), .I1(I[6]), .O(inst6_O));
LUT2 #(.INIT(4'h6)) inst7 (.I0(inst6_O), .I1(I[7]), .O(inst7_O));
assign O = inst7_O;
endmodule

module XOr8x4 (input [3:0] I0, input [3:0] I1, input [3:0] I2, input [3:0] I3, input [3:0] I4, input [3:0] I5, input [3:0] I6, input [3:0] I7, output [3:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
XOr8 inst0 (.I({I7[0],I6[0],I5[0],I4[0],I3[0],I2[0],I1[0],I0[0]}), .O(inst0_O));
XOr8 inst1 (.I({I7[1],I6[1],I5[1],I4[1],I3[1],I2[1],I1[1],I0[1]}), .O(inst1_O));
XOr8 inst2 (.I({I7[2],I6[2],I5[2],I4[2],I3[2],I2[2],I1[2],I0[2]}), .O(inst2_O));
XOr8 inst3 (.I({I7[3],I6[3],I5[3],I4[3],I3[3],I2[3],I1[3],I0[3]}), .O(inst3_O));
assign O = {inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

