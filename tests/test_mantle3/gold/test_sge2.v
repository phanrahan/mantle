module Sub2_cin1 (input [1:0] I0, input [1:0] I1, output [1:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
LUT2 #(.INIT(4'h9)) inst0 (.I0(I0[0]), .I1(I1[0]), .O(inst0_O));
MUXCY inst1 (.DI(I0[0]), .CI(1'b1), .S(inst0_O), .O(inst1_O));
LUT2 #(.INIT(4'h9)) inst2 (.I0(I0[1]), .I1(I1[1]), .O(inst2_O));
MUXCY inst3 (.DI(I0[1]), .CI(inst1_O), .S(inst2_O), .O(inst3_O));
assign O = {inst2_O,inst0_O};
endmodule

module SGE2 (input signed [1:0] I0, input signed [1:0] I1, output  O);
wire [1:0] inst0_O;
wire  inst1_O;
Sub2_cin1 inst0 (.I0(I0), .I1(I1), .O(inst0_O));
LUT3 #(.INIT(8'h71)) inst1 (.I0(inst0_O[1]), .I1(I0[1]), .I2(I1[1]), .O(inst1_O));
assign O = inst1_O;
endmodule

