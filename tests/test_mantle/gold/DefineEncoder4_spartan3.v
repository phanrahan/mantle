module Or2 (input [1:0] I, output  O);
wire  inst0_O;
LUT2 #(.INIT(4'h1)) inst0 (.I0(I[0]), .I1(I[1]), .O(inst0_O));
assign O = inst0_O;
endmodule

module Encoder4 (input [3:0] I, output [1:0] O);
wire  inst0_O;
wire  inst1_O;
Or2 inst0 (.I({I[3],I[1]}), .O(inst0_O));
Or2 inst1 (.I({I[3],I[2]}), .O(inst1_O));
assign O = {inst1_O,inst0_O};
endmodule

