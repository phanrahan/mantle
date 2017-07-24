module main (input [1:0] J1, output  D5);
wire  inst0_O;
SB_LUT4 #(.LUT_INIT(16'h1111)) inst0 (.I0(J1[0]), .I1(J1[1]), .I2(1'b0), .I3(1'b0), .O(inst0_O));
assign D5 = inst0_O;
endmodule

