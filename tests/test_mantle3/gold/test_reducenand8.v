module NAnd8 (input [7:0] I, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
LUT4 #(.INIT(16'h8000)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst0_O));
MUXCY inst1 (.DI(1'b0), .CI(1'b1), .S(inst0_O), .O(inst1_O));
LUT4 #(.INIT(16'h8000)) inst2 (.I0(I[4]), .I1(I[5]), .I2(I[6]), .I3(I[7]), .O(inst2_O));
MUXCY inst3 (.DI(1'b0), .CI(inst1_O), .S(inst2_O), .O(inst3_O));
assign O = inst3_O;
endmodule

