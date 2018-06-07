module Sub2_cin1 (input [1:0] I0, input [1:0] I1, output [1:0] O);
wire  inst0_O5;
wire  inst0_O6;
wire  inst1_O;
wire  inst2_O5;
wire  inst2_O6;
wire  inst3_O;
LUT6_2 #(.INIT(64'h4444444444444443)) inst0 (.I0(I0[0]), .I1(I1[0]), .I5(1'b1), .O5(inst0_O5), .O6(inst0_O6));
MUXCY inst1 (.DI(inst0_O5), .CI(1'b1), .S(inst0_O6), .O(inst1_O));
LUT6_2 #(.INIT(64'h4444444444444443)) inst2 (.I0(I0[1]), .I1(I1[1]), .I5(1'b1), .O5(inst2_O5), .O6(inst2_O6));
MUXCY inst3 (.DI(inst2_O5), .CI(inst1_O), .S(inst2_O6), .O(inst3_O));
assign O = {inst2_O6,inst0_O6};
endmodule

module SLE2 (input signed [1:0] I0, input signed [1:0] I1, output  O);
wire [1:0] inst0_O;
wire  inst1_O;
Sub2_cin1 inst0 (.I0(I1), .I1(I0), .O(inst0_O));
LUT3 #(.INIT(8'h71)) inst1 (.I0(inst0_O[1]), .I1(I1[1]), .I2(I0[1]), .O(inst1_O));
assign O = inst1_O;
endmodule

