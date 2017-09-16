module And2x4 (input [3:0] I0, input [3:0] I1, output [3:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
SB_LUT4 #(.LUT_INIT(16'h8888)) inst0 (.I0(I0[0]), .I1(I1[0]), .I2(1'b0), .I3(1'b0), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'h8888)) inst1 (.I0(I0[1]), .I1(I1[1]), .I2(1'b0), .I3(1'b0), .O(inst1_O));
SB_LUT4 #(.LUT_INIT(16'h8888)) inst2 (.I0(I0[2]), .I1(I1[2]), .I2(1'b0), .I3(1'b0), .O(inst2_O));
SB_LUT4 #(.LUT_INIT(16'h8888)) inst3 (.I0(I0[3]), .I1(I1[3]), .I2(1'b0), .I3(1'b0), .O(inst3_O));
assign O = {inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module main (input [3:0] I0, input [3:0] I1, output [3:0] O);
wire [3:0] inst0_O;
And2x4 inst0 (.I0(I0), .I1(I1), .O(inst0_O));
assign O = inst0_O;
endmodule

