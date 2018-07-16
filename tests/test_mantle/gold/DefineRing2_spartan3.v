module Ring2_0001 (output [1:0] O, input  CLK);
wire  inst0_Q;
wire  inst1_Q;
FDRSE #(.INIT(1'h1)) inst0 (.C(CLK), .CE(1'b1), .R(1'b0), .S(1'b0), .D(inst1_Q), .Q(inst0_Q));
FDRSE #(.INIT(1'h0)) inst1 (.C(CLK), .CE(1'b1), .R(1'b0), .S(1'b0), .D(inst0_Q), .Q(inst1_Q));
assign O = {inst1_Q,inst0_Q};
endmodule

