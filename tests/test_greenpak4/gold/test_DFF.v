module DFF (input  I, input  CLK, output  O);
wire  inst0_Q;
GP_DFF inst0 (.D(I), .CLK(CLK), .Q(inst0_Q));
assign O = inst0_Q;
endmodule

