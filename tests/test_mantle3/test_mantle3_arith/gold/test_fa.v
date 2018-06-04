module FullAdder (input  I0, input  I1, input  CIN, output  O, output  COUT);
wire  inst0_O;
wire  inst1_LO;
wire  inst2_O;
wire  inst3_O;
LUT2 #(.INIT(4'h6)) inst0 (.I0(I0), .I1(I1), .O(inst0_O));
MULT_AND inst1 (.I0(I0), .I1(I1), .LO(inst1_LO));
MUXCY inst2 (.DI(inst1_LO), .CI(CIN), .S(inst0_O), .O(inst2_O));
XORCY inst3 (.LI(inst0_O), .CI(CIN), .O(inst3_O));
assign O = inst3_O;
assign COUT = inst2_O;
endmodule

