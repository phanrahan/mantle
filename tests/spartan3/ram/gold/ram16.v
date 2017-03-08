module main (output [0:0] LED, input  CLKIN, input [5:0] SWITCH);
wire  inst0_O;
RAM16X1S #(.INIT(16'h1111)) inst0 (.A0(SWITCH[0]), .A1(SWITCH[1]), .A2(SWITCH[2]), .A3(SWITCH[3]), .O(inst0_O), .D(SWITCH[4]), .WE(SWITCH[5]), .WCLK(CLKIN));
assign LED = {inst0_O};
endmodule

