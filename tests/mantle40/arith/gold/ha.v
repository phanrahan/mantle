module main (input  A, input  B, output  D2, output  D1, input  CLKIN);
wire  inst0_O;
wire  inst1_CO;
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst0 (.I0(1'b0), .I1(A), .I2(B), .I3(1'b0), .O(inst0_O));
SB_CARRY inst1 (.I0(A), .I1(B), .CI(1'b0), .CO(inst1_CO));
assign D2 = inst1_CO;
assign D1 = inst0_O;
endmodule

