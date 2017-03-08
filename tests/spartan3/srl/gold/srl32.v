module main (output [0:0] LED, input  CLKIN, input [5:0] SWITCH);
wire  inst0_Q;
wire  inst0_Q15;
wire  inst1_Q;
wire  inst1_Q15;
wire  inst2_O;
SRLC16E #(.INIT(16'h0001)) inst0 (.A0(SWITCH[0]), .A1(SWITCH[1]), .A2(SWITCH[2]), .A3(SWITCH[3]), .D(SWITCH[5]), .Q(inst0_Q), .Q15(inst0_Q15), .CE(1'b1), .CLK(CLKIN));
SRLC16E #(.INIT(16'h0000)) inst1 (.A0(SWITCH[0]), .A1(SWITCH[1]), .A2(SWITCH[2]), .A3(SWITCH[3]), .D(inst0_Q15), .Q(inst1_Q), .Q15(inst1_Q15), .CE(1'b1), .CLK(CLKIN));
MUXF5 inst2 (.I0(inst0_Q), .I1(inst1_Q), .S(SWITCH[4]), .O(inst2_O));
assign LED = {inst2_O};
endmodule

