module NE2 (input [1:0] I0, input [1:0] I1, output  O);
wire  inst0_O;
wire  inst1_O;
LUT4 #(.INIT(16'h6FF6)) inst0 (.I0(I0[0]), .I1(I1[0]), .I2(I0[1]), .I3(I1[1]), .O(inst0_O));
MUXCY inst1 (.DI(1'b0), .CI(1'b1), .S(inst0_O), .O(inst1_O));
assign O = inst1_O;
endmodule

