module main (input [1:0] J1, output [1:0] J3);
wire  inst0_O;
wire  inst1_O;
SB_LUT4 #(.LUT_INIT(16'h8888)) inst0 (.I0(J1[0]), .I1(J1[1]), .I2(1'b0), .I3(1'b0), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'hEEEE)) inst1 (.I0(J1[0]), .I1(J1[1]), .I2(1'b0), .I3(1'b0), .O(inst1_O));
assign J3 = {inst1_O,inst0_O};
endmodule

