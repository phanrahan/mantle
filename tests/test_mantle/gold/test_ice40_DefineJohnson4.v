module Johnson4 (output [3:0] O, input  CLK);
wire  inst0_Q;
wire  inst1_Q;
wire  inst2_Q;
wire  inst3_Q;
wire  inst4_O;
SB_DFF inst0 (.C(CLK), .D(inst4_O), .Q(inst0_Q));
SB_DFF inst1 (.C(CLK), .D(inst0_Q), .Q(inst1_Q));
SB_DFF inst2 (.C(CLK), .D(inst1_Q), .Q(inst2_Q));
SB_DFF inst3 (.C(CLK), .D(inst2_Q), .Q(inst3_Q));
SB_LUT4 #(.LUT_INIT(16'h5555)) inst4 (.I0(inst3_Q), .I1(1'b0), .I2(1'b0), .I3(1'b0), .O(inst4_O));
assign O = {inst3_Q,inst2_Q,inst1_Q,inst0_Q};
endmodule

