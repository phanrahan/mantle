module main (output [0:0] LED, input [7:0] SWITCH, input  CLKIN);
wire  inst0_O;
RAM256X1S #(.INIT(256'hFFFFFFFFFFFFFFFF5555555555555555FFFFFFFFFFFFFFFFAAAAAAAAAAAAAAAA)) inst0 (.A(SWITCH), .D(1'b0), .O(inst0_O), .WE(1'b0), .WCLK(CLKIN));
assign LED = {inst0_O};
endmodule

