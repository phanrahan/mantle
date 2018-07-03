module EQ2 (input [1:0] I0, input [1:0] I1, output  O);
wire  inst0_O5;
wire  inst0_O6;
wire  inst1_O;
LUT6_2 #(.INIT(64'h9009900990099009)) inst0 (.I0(I0[0]), .I1(I1[0]), .I2(I0[1]), .I3(I1[1]), .I5(1'b1), .O5(inst0_O5), .O6(inst0_O6));
MUXCY inst1 (.DI(inst0_O5), .CI(1'b1), .S(inst0_O6), .O(inst1_O));
assign O = inst1_O;
endmodule

