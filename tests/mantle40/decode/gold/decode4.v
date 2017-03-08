module main (input [3:0] J1, output  D1);
wire  inst0_O;
SB_LUT4 #(.LUT_INIT(16'h0008)) inst0 (.I0(J1[0]), .I1(J1[1]), .I2(J1[2]), .I3(J1[3]), .O(inst0_O));
assign D1 = inst0_O;
endmodule

