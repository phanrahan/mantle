module SISO8 (input  I, output  O, input  CLK);
wire  inst0_Q;
wire  inst1_Q;
wire  inst2_Q;
wire  inst3_Q;
wire  inst4_Q;
wire  inst5_Q;
wire  inst6_Q;
wire  inst7_Q;
FDRSE #(.INIT(1'h0)) inst0 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(I), .Q(inst0_Q));
FDRSE #(.INIT(1'h0)) inst1 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(inst0_Q), .Q(inst1_Q));
FDRSE #(.INIT(1'h0)) inst2 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(inst1_Q), .Q(inst2_Q));
FDRSE #(.INIT(1'h0)) inst3 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(inst2_Q), .Q(inst3_Q));
FDRSE #(.INIT(1'h0)) inst4 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(inst3_Q), .Q(inst4_Q));
FDRSE #(.INIT(1'h0)) inst5 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(inst4_Q), .Q(inst5_Q));
FDRSE #(.INIT(1'h0)) inst6 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(inst5_Q), .Q(inst6_Q));
FDRSE #(.INIT(1'h0)) inst7 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(inst6_Q), .Q(inst7_Q));
assign O = inst7_Q;
endmodule

