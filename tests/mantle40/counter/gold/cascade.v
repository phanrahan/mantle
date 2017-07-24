module main (input  I0, input  I1, input  I2, input  I3, output  D1);
wire  inst0_O;
wire  inst1_O;
SB_LUT4 #(.LUT_INIT(16'h8000)) inst0 (.I0(I0), .I1(I1), .I2(I2), .I3(I3), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'h8000)) inst1 (.I0(I0), .I1(I1), .I2(I2), .I3(inst0_O), .O(inst1_O));
assign D1 = inst1_O;
endmodule

