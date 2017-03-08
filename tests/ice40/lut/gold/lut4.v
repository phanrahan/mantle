module main (input  I0, input  I1, input  I2, input  I3, output  D0, input  CLKIN);
wire  inst0_O;
SB_LUT4 #(.LUT_INIT(16'h8000)) inst0 (.I0(I0), .I1(I1), .I2(I2), .I3(I3), .O(inst0_O));
assign D0 = inst0_O;
endmodule

