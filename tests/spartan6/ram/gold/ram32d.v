module main (output [1:0] LED, input [7:0] SWITCH, input  CLKIN);
wire  inst0_SPO;
wire  inst0_DPO;
RAM32X1D #(.INIT(32'hAAAAAAAA)) inst0 (.A0(SWITCH[0]), .A1(SWITCH[1]), .A2(SWITCH[2]), .A3(SWITCH[3]), .A4(SWITCH[4]), .DPRA0(1'b0), .DPRA1(1'b1), .DPRA2(1'b0), .DPRA3(1'b0), .DPRA4(1'b0), .D(SWITCH[6]), .SPO(inst0_SPO), .DPO(inst0_DPO), .WE(SWITCH[7]), .WCLK(CLKIN));
assign LED = {inst0_DPO,inst0_SPO};
endmodule

