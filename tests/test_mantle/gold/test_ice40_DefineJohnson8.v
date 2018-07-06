module Johnson8 (output [7:0] O, input  CLK);
wire  inst0_Q;
wire  inst1_Q;
wire  inst2_Q;
wire  inst3_Q;
wire  inst4_Q;
wire  inst5_Q;
wire  inst6_Q;
wire  inst7_Q;
wire  inst8_O;
SB_DFF inst0 (.C(CLK), .D(inst8_O), .Q(inst0_Q));
SB_DFF inst1 (.C(CLK), .D(inst0_Q), .Q(inst1_Q));
SB_DFF inst2 (.C(CLK), .D(inst1_Q), .Q(inst2_Q));
SB_DFF inst3 (.C(CLK), .D(inst2_Q), .Q(inst3_Q));
SB_DFF inst4 (.C(CLK), .D(inst3_Q), .Q(inst4_Q));
SB_DFF inst5 (.C(CLK), .D(inst4_Q), .Q(inst5_Q));
SB_DFF inst6 (.C(CLK), .D(inst5_Q), .Q(inst6_Q));
SB_DFF inst7 (.C(CLK), .D(inst6_Q), .Q(inst7_Q));
SB_LUT4 #(.LUT_INIT(16'h5555)) inst8 (.I0(inst7_Q), .I1(1'b0), .I2(1'b0), .I3(1'b0), .O(inst8_O));
assign O = {inst7_Q,inst6_Q,inst5_Q,inst4_Q,inst3_Q,inst2_Q,inst1_Q,inst0_Q};
endmodule

