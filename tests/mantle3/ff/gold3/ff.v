module main (output [0:0] LED, input  CLKIN, input [0:0] SWITCH);
wire  inst0_Q;
FDRSE #(.INIT(1'h0)) inst0 (.C(CLKIN), .CE(1'b1), .R(1'b0), .S(1'b0), .D(SWITCH[0]), .Q(inst0_Q));
assign LED = {inst0_Q};
endmodule

