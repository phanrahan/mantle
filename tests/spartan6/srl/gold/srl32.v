module main (output [0:0] LED, input [5:0] SWITCH, input  CLKIN);
wire  inst0_Q;
wire  inst0_Q31;
SRLC32E #(.INIT(64'h0000000100000001)) inst0 (.A({SWITCH[4],SWITCH[3],SWITCH[2],SWITCH[1],SWITCH[0]}), .D(SWITCH[5]), .Q(inst0_Q), .Q31(inst0_Q31), .CE(1'b1), .CLK(CLKIN));
assign LED = {inst0_Q};
endmodule

