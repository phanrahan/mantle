module Or1 (input [0:0] I, output  O);
wire  inst0_O;
LUT1 #(.INIT(2'h1)) inst0 (.I0(I[0]), .O(inst0_O));
assign O = inst0_O;
endmodule

module Encoder2 (input [1:0] I, output [0:0] O);
wire  inst0_O;
Or1 inst0 (.I({I[1]}), .O(inst0_O));
assign O = {inst0_O};
endmodule

