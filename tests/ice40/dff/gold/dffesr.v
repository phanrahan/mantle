module main (input  I0, input  CE, input  RESET, output  D0, input  CLKIN);
wire  inst0_Q;
SB_DFFESR inst0 (.C(CLKIN), .R(RESET), .E(CE), .D(I0), .Q(inst0_Q));
assign D0 = inst0_Q;
endmodule

