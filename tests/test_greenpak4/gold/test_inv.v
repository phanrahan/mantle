module INV (input  I, output  O);
wire  inst0_OUT;
GP_INV inst0 (.IN(I), .OUT(inst0_OUT));
assign O = inst0_OUT;
endmodule

