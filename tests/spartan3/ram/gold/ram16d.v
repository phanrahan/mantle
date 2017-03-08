module main (output [1:0] LED, input  CLKIN, input [5:0] SWITCH);
wire  inst0_SPO;
wire  inst0_DPO;
RAM16X1D #(.INIT(16'h1111)) inst0 (.A0(SWITCH[0]), .A1(SWITCH[1]), .A2(1'b0), .A3(1'b0), .DPRA0(SWITCH[2]), .DPRA1(SWITCH[3]), .DPRA2(1'b0), .DPRA3(1'b0), .SPO(inst0_SPO), .DPO(inst0_DPO), .D(SWITCH[4]), .WE(SWITCH[5]), .WCLK(CLKIN));
assign LED = {inst0_DPO,inst0_SPO};
endmodule

