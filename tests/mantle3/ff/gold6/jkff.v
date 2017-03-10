module main (output [0:0] LED, input [1:0] SWITCH, input  CLKIN);
wire  inst0_Q;
wire  inst1_O;
FDRSE #(.INIT(1'h0)) inst0 (.C(CLKIN), .CE(1'b1), .R(1'b0), .S(1'b0), .D(inst1_O), .Q(inst0_Q));
LUT3 #(.INIT(8'h4E)) inst1 (.I0(inst0_Q), .I1(SWITCH[0]), .I2(SWITCH[1]), .O(inst1_O));
assign LED = {inst0_Q};
endmodule

