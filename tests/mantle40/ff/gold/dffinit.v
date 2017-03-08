module main (input  SWITCH, output  D1, input  CLKIN);
wire  inst0_Q;
wire  inst1_O;
wire  inst2_O;
SB_DFF inst0 (.C(CLKIN), .D(inst1_O), .Q(inst0_Q));
SB_LUT4 #(.LUT_INIT(16'h5555)) inst1 (.I0(SWITCH), .I1(1'b0), .I2(1'b0), .I3(1'b0), .O(inst1_O));
SB_LUT4 #(.LUT_INIT(16'h5555)) inst2 (.I0(inst0_Q), .I1(1'b0), .I2(1'b0), .I3(1'b0), .O(inst2_O));
assign D1 = inst2_O;
endmodule

