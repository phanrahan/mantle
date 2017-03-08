module main (input  I0, input  RESET, output  D0, input  CLKIN);
wire  inst0_Q;
SB_DFFSR inst0 (.C(CLKIN), .R(RESET), .D(I0), .Q(inst0_Q));
assign D0 = inst0_Q;
endmodule

