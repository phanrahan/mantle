module main (input  I0, input  I1, output  D5, input  CLKIN);
wire  inst0_Q;
wire  inst1_O;
SB_DFF inst0 (.C(CLKIN), .D(inst1_O), .Q(inst0_Q));
SB_LUT4 #(.LUT_INIT(16'h0E0E)) inst1 (.I0(inst0_Q), .I1(I1), .I2(I0), .I3(1'b0), .O(inst1_O));
assign D5 = inst0_Q;
endmodule

