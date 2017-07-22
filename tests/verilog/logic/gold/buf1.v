module Buf1 (input [0:0] I0, output [0:0] O);
wire  inst0_0;
buf inst0 (inst0_0, I0[0]);
assign O = {inst0_0};
endmodule

module main (input [0:0] I, output [0:0] O);
wire [0:0] inst0_O;
Buf1 inst0 (.I0(I), .O(inst0_O));
assign O = inst0_O;
endmodule

