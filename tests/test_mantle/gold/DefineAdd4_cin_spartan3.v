module Add4_cin (input [3:0] I0, input [3:0] I1, input  CIN, output [3:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
wire  inst8_O;
wire  inst9_O;
wire  inst10_O;
wire  inst11_O;
LUT2 #(.INIT(4'h6)) inst0 (.I0(I0[0]), .I1(I1[0]), .O(inst0_O));
MUXCY inst1 (.DI(I0[0]), .CI(CIN), .S(inst0_O), .O(inst1_O));
XORCY inst2 (.LI(inst0_O), .CI(CIN), .O(inst2_O));
LUT2 #(.INIT(4'h6)) inst3 (.I0(I0[1]), .I1(I1[1]), .O(inst3_O));
MUXCY inst4 (.DI(I0[1]), .CI(inst1_O), .S(inst3_O), .O(inst4_O));
XORCY inst5 (.LI(inst3_O), .CI(inst1_O), .O(inst5_O));
LUT2 #(.INIT(4'h6)) inst6 (.I0(I0[2]), .I1(I1[2]), .O(inst6_O));
MUXCY inst7 (.DI(I0[2]), .CI(inst4_O), .S(inst6_O), .O(inst7_O));
XORCY inst8 (.LI(inst6_O), .CI(inst4_O), .O(inst8_O));
LUT2 #(.INIT(4'h6)) inst9 (.I0(I0[3]), .I1(I1[3]), .O(inst9_O));
MUXCY inst10 (.DI(I0[3]), .CI(inst7_O), .S(inst9_O), .O(inst10_O));
XORCY inst11 (.LI(inst9_O), .CI(inst7_O), .O(inst11_O));
assign O = {inst11_O,inst8_O,inst5_O,inst2_O};
endmodule

