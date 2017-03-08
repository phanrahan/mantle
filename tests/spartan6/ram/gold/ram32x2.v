module main (output [1:0] LED, input [7:0] SWITCH, input  CLKIN);
wire  inst0_O0;
wire  inst0_O1;
RAM32X2S #(.INIT_00(32'hAAAAAAAA), .INIT_01(32'h55555555)) inst0 (.A0(SWITCH[0]), .A1(SWITCH[1]), .A2(SWITCH[2]), .A3(SWITCH[3]), .A4(SWITCH[4]), .D0(SWITCH[5]), .D1(SWITCH[6]), .O0(inst0_O0), .O1(inst0_O1), .WE(SWITCH[7]), .WCLK(CLKIN));
assign LED = {inst0_O1,inst0_O0};
endmodule

