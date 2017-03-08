module main (output [0:0] LED, input [4:0] SWITCH, input  CLKIN);
wire  inst0_Q;
SRL16E #(.INIT(16'h0001)) inst0 (.A0(SWITCH[0]), .A1(SWITCH[1]), .A2(SWITCH[2]), .A3(SWITCH[3]), .D(SWITCH[4]), .Q(inst0_Q), .CE(1'b1), .CLK(CLKIN));
assign LED = {inst0_Q};
endmodule

