module Ring4_0001 (output [3:0] O, input  CLK);
wire  inst0_Q;
wire  inst1_Q;
wire  inst2_Q;
wire  inst3_Q;
FDRSE #(.INIT(1'h1)) inst0 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(inst3_Q), .Q(inst0_Q));
FDRSE #(.INIT(1'h0)) inst1 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(inst0_Q), .Q(inst1_Q));
FDRSE #(.INIT(1'h0)) inst2 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(inst1_Q), .Q(inst2_Q));
FDRSE #(.INIT(1'h0)) inst3 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(inst2_Q), .Q(inst3_Q));
assign O = {inst3_Q,inst2_Q,inst1_Q,inst0_Q};
endmodule

