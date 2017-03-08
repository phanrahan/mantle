module main (output [1:0] LED, input [7:0] SWITCH, input  CLKIN);
wire  inst0_SPO;
wire  inst0_DPO;
RAM128X1D #(.INIT(128'h33333333333333333333333333333333)) inst0 (.A({SWITCH[6],SWITCH[5],SWITCH[4],SWITCH[3],SWITCH[2],SWITCH[1],SWITCH[0]}), .DPRA({1'b0,1'b0,1'b0,1'b1,1'b0,1'b0,1'b1}), .D(SWITCH[7]), .SPO(inst0_SPO), .DPO(inst0_DPO), .WE(1'b0), .WCLK(CLKIN));
assign LED = {inst0_DPO,inst0_SPO};
endmodule

