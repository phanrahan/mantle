module main (input  I0, input  I1, input  I2, input  I3, input  I4, output  D0);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
SB_LUT4 #(.LUT_INIT(16'h0000)) inst0 (.I0(I0), .I1(I1), .I2(I2), .I3(I3), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'h8000)) inst1 (.I0(I0), .I1(I1), .I2(I2), .I3(I3), .O(inst1_O));
SB_LUT4 #(.LUT_INIT(16'hCACA)) inst2 (.I0(inst0_O), .I1(inst1_O), .I2(I4), .I3(1'b0), .O(inst2_O));
assign D0 = inst2_O;
endmodule

