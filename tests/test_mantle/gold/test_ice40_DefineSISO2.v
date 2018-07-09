module SISO2 (input  I, output  O, input  CLK);
wire  inst0_Q;
wire  inst1_Q;
SB_DFF inst0 (.C(CLK), .D(I), .Q(inst0_Q));
SB_DFF inst1 (.C(CLK), .D(inst0_Q), .Q(inst1_Q));
assign O = inst1_Q;
endmodule

