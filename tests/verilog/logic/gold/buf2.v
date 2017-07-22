module Buf2 (input [1:0] I0, output [1:0] O);
wire  inst0_0;
wire  inst1_0;
buf inst0 (inst0_0, I0[0]);
buf inst1 (inst1_0, I0[1]);
assign O = {inst1_0,inst0_0};
endmodule

module main (input  I0, input  I1, output  O0, output  O1);
wire [1:0] inst0_O;
Buf2 inst0 (.I0({I1,I0}), .O(inst0_O));
assign O0 = inst0_O[0];
assign O1 = inst0_O[1];
endmodule

