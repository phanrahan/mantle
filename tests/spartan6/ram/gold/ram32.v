module main (output [0:0] LED, input [7:0] SWITCH, input  CLKIN);
wire  inst0_O;
RAM32X1S #(.INIT(32'hAAAAAAAA)) inst0 (.A0(SWITCH[0]), .A1(SWITCH[1]), .A2(SWITCH[2]), .A3(SWITCH[3]), .A4(SWITCH[4]), .D(SWITCH[6]), .O(inst0_O), .WE(SWITCH[7]), .WCLK(CLKIN));
assign LED = {inst0_O};
endmodule

