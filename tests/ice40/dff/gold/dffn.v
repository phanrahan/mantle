module main (input  I0, output  D0, input  CLKIN);
wire  inst0_Q;
SB_DFFN inst0 (.C(CLKIN), .D(I0), .Q(inst0_Q));
assign D0 = inst0_Q;
endmodule

