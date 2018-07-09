module DFFI (input  I, input  CLK, output  O);
wire  inst0_nQ;
GP_DFFI inst0 (.D(I), .CLK(CLK), .nQ(inst0_nQ));
assign O = inst0_nQ;
endmodule

