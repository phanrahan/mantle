module Invert2 (input [1:0] I, output [1:0] O);
wire  inst0_O;
wire  inst1_O;
LUT1 #(.INIT(2'h1)) inst0 (.I0(I[0]), .O(inst0_O));
LUT1 #(.INIT(2'h1)) inst1 (.I0(I[1]), .O(inst1_O));
assign O = {inst1_O,inst0_O};
endmodule

