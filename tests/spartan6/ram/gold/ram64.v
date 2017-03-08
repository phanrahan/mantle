module main (output [3:0] LED, input [7:0] SWITCH, input  CLKIN);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
RAM64X1S #(.INIT(64'hAAAAAAAAAAAAAAAA)) inst0 (.A0(SWITCH[0]), .A1(SWITCH[1]), .A2(SWITCH[2]), .A3(SWITCH[3]), .A4(SWITCH[4]), .A5(SWITCH[5]), .D(SWITCH[6]), .O(inst0_O), .WE(SWITCH[7]), .WCLK(CLKIN));
RAM64X1S #(.INIT(64'hCCCCCCCCCCCCCCCC)) inst1 (.A0(SWITCH[0]), .A1(SWITCH[1]), .A2(SWITCH[2]), .A3(SWITCH[3]), .A4(SWITCH[4]), .A5(SWITCH[5]), .D(SWITCH[6]), .O(inst1_O), .WE(SWITCH[7]), .WCLK(CLKIN));
RAM64X1S #(.INIT(64'hF0F0F0F0F0F0F0F0)) inst2 (.A0(SWITCH[0]), .A1(SWITCH[1]), .A2(SWITCH[2]), .A3(SWITCH[3]), .A4(SWITCH[4]), .A5(SWITCH[5]), .D(SWITCH[6]), .O(inst2_O), .WE(SWITCH[7]), .WCLK(CLKIN));
RAM64X1S #(.INIT(64'hFF00FF00FF00FF00)) inst3 (.A0(SWITCH[0]), .A1(SWITCH[1]), .A2(SWITCH[2]), .A3(SWITCH[3]), .A4(SWITCH[4]), .A5(SWITCH[5]), .D(SWITCH[6]), .O(inst3_O), .WE(SWITCH[7]), .WCLK(CLKIN));
assign LED = {inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

