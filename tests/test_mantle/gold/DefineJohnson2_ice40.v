module Johnson2 (output [1:0] O, input  CLK);
wire  inst0_Q;
wire  inst1_Q;
wire  inst2_O;
SB_DFF inst0 (.C(CLK), .D(inst2_O), .Q(inst0_Q));
SB_DFF inst1 (.C(CLK), .D(inst0_Q), .Q(inst1_Q));
SB_LUT4 #(.LUT_INIT(16'h5555)) inst2 (.I0(inst1_Q), .I1(1'b0), .I2(1'b0), .I3(1'b0), .O(inst2_O));
assign O = {inst1_Q,inst0_Q};
endmodule

