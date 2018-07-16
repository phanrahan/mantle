module Or1xNone (input  I0, output  O);
wire  inst0_out;
orr inst0 (.in({I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module Encoder2 (input [1:0] I, output [0:0] O);
wire  inst0_O;
Or1xNone inst0 (.I0(I[1]), .O(inst0_O));
assign O = {inst0_O};
endmodule

