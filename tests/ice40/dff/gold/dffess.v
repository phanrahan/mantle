module main (input  I0, input  CE, input  SET, output  D0, input  CLKIN);
wire  inst0_Q;
SB_DFFESS inst0 (.C(CLKIN), .S(SET), .E(CE), .D(I0), .Q(inst0_Q));
assign D0 = inst0_Q;
endmodule

