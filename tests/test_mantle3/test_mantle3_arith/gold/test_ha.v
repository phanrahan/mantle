module HalfAdder (input  I0, input  I1, output  O, output  COUT);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
LUT1 #(.INIT(2'h2)) inst0 (.I0(I0), .O(inst0_O));
MUXCY inst1 (.DI(I0), .CI(I1), .S(inst0_O), .O(inst1_O));
XORCY inst2 (.LI(inst0_O), .CI(I1), .O(inst2_O));
assign O = inst2_O;
assign COUT = inst1_O;
endmodule

