module main (output [1:0] LED, input  CLKIN, input [3:0] SWITCH);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
RAM16X1S #(.INIT(16'h1111)) inst0 (.A0(SWITCH[0]), .A1(SWITCH[1]), .A2(SWITCH[2]), .A3(SWITCH[3]), .O(inst0_O), .D(1'b0), .WE(1'b0), .WCLK(CLKIN));
MUXCY inst1 (.DI(inst0_O), .CI(1'b1), .S(inst0_O), .O(inst1_O));
XORCY inst2 (.LI(inst0_O), .CI(1'b1), .O(inst2_O));
RAM16X1S #(.INIT(16'h1111)) inst3 (.A0(SWITCH[0]), .A1(SWITCH[1]), .A2(SWITCH[2]), .A3(SWITCH[3]), .O(inst3_O), .D(1'b0), .WE(1'b0), .WCLK(CLKIN));
MUXCY inst4 (.DI(inst3_O), .CI(inst1_O), .S(inst3_O), .O(inst4_O));
XORCY inst5 (.LI(inst3_O), .CI(inst1_O), .O(inst5_O));
assign LED = {inst5_O,inst2_O};
endmodule

