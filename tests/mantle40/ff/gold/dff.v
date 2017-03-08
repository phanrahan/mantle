module main (input  SWITCH, output  D1, input  CLKIN);
wire  inst0_Q;
SB_DFF inst0 (.C(CLKIN), .D(SWITCH), .Q(inst0_Q));
assign D1 = inst0_Q;
endmodule

