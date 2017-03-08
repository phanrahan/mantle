module main (input  D, output  Q, input  CLKIN);
wire  inst0_Q;
SB_DFF inst0 (.C(CLKIN), .D(D), .Q(inst0_Q));
assign Q = inst0_Q;
endmodule

