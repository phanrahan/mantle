module Decode2 (input [1:0] I, output  O);
wire  inst0_O;
LUT2 #(.INIT(4'h1)) inst0 (.I0(I[0]), .I1(I[1]), .O(inst0_O));
assign O = inst0_O;
endmodule

module Decoder2 (input [1:0] I, output [3:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
Decode2 inst0 (.I(I), .O(inst0_O));
Decode2 inst1 (.I(I), .O(inst1_O));
Decode2 inst2 (.I(I), .O(inst2_O));
Decode2 inst3 (.I(I), .O(inst3_O));
assign O = {inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

