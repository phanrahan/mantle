module main (input  I, input  CE, output  D5, input  CLKIN);
wire  inst0_Q;
SB_DFFE inst0 (.C(CLKIN), .E(CE), .D(I), .Q(inst0_Q));
assign D5 = inst0_Q;
endmodule

