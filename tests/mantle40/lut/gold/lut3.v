module main (input  I0, input  I1, input  I2, output  D0);
wire  inst0_O;
SB_LUT4 #(.LUT_INIT(16'h8080)) inst0 (.I0(I0), .I1(I1), .I2(I2), .I3(1'b0), .O(inst0_O));
assign D0 = inst0_O;
endmodule

