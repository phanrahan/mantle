module main (output [0:0] LED, input [6:0] SWITCH, input  CLKIN);
wire  inst0_O;
RAM128X1S #(.INIT(128'hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA)) inst0 (.A0(SWITCH[0]), .A1(SWITCH[1]), .A2(SWITCH[2]), .A3(SWITCH[3]), .A4(SWITCH[4]), .A5(SWITCH[5]), .A6(SWITCH[6]), .D(1'b0), .O(inst0_O), .WE(1'b0), .WCLK(CLKIN));
assign LED = {inst0_O};
endmodule

