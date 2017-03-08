module main (output [0:0] LED, input [1:0] SWITCH, input  CLKIN);
wire  inst0_Q;
FDRSE #(.INIT(1'h0)) inst0 (.C(CLKIN), .CE(1'b1), .R(SWITCH[1]), .S(SWITCH[0]), .D(inst0_Q), .Q(inst0_Q));
assign LED = {inst0_Q};
endmodule

