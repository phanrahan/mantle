module Register8 (input [7:0] I, output [7:0] O, input  CLK);
wire  inst0_Q;
wire  inst1_Q;
wire  inst2_Q;
wire  inst3_Q;
wire  inst4_Q;
wire  inst5_Q;
wire  inst6_Q;
wire  inst7_Q;
SB_DFF inst0 (.C(CLK), .D(I[0]), .Q(inst0_Q));
SB_DFF inst1 (.C(CLK), .D(I[1]), .Q(inst1_Q));
SB_DFF inst2 (.C(CLK), .D(I[2]), .Q(inst2_Q));
SB_DFF inst3 (.C(CLK), .D(I[3]), .Q(inst3_Q));
SB_DFF inst4 (.C(CLK), .D(I[4]), .Q(inst4_Q));
SB_DFF inst5 (.C(CLK), .D(I[5]), .Q(inst5_Q));
SB_DFF inst6 (.C(CLK), .D(I[6]), .Q(inst6_Q));
SB_DFF inst7 (.C(CLK), .D(I[7]), .Q(inst7_Q));
assign O = {inst7_Q,inst6_Q,inst5_Q,inst4_Q,inst3_Q,inst2_Q,inst1_Q,inst0_Q};
endmodule

