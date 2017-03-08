module main (output [1:0] LED, input  CLKIN, input [3:0] SWITCH);
wire  inst0_O0;
wire  inst0_O1;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
RAM16X2S #(.INIT_00(16'h1111), .INIT_01(16'h1111)) inst0 (.A0(SWITCH[0]), .A1(SWITCH[1]), .A2(SWITCH[2]), .A3(SWITCH[3]), .O0(inst0_O0), .O1(inst0_O1), .D0(1'b0), .D1(1'b0), .WE(1'b0), .WCLK(CLKIN));
MUXCY inst1 (.DI(inst0_O0), .CI(1'b1), .S(inst0_O0), .O(inst1_O));
XORCY inst2 (.LI(inst0_O0), .CI(1'b1), .O(inst2_O));
MUXCY inst3 (.DI(inst0_O1), .CI(inst1_O), .S(inst0_O1), .O(inst3_O));
XORCY inst4 (.LI(inst0_O1), .CI(inst1_O), .O(inst4_O));
assign LED = {inst4_O,inst2_O};
endmodule

