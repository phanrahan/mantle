module Decode2 (input [1:0] I, output  O);
wire  LUT2_inst0_O;
LUT2 #(.INIT(4'h1)) LUT2_inst0 (.I0(I[0]), .I1(I[1]), .O(LUT2_inst0_O));
assign O = LUT2_inst0_O;
endmodule

module Decoder2 (input [1:0] I, output [3:0] O);
wire  Decode2_inst0_O;
wire  Decode2_inst1_O;
wire  Decode2_inst2_O;
wire  Decode2_inst3_O;
Decode2 Decode2_inst0 (.I(I), .O(Decode2_inst0_O));
Decode2 Decode2_inst1 (.I(I), .O(Decode2_inst1_O));
Decode2 Decode2_inst2 (.I(I), .O(Decode2_inst2_O));
Decode2 Decode2_inst3 (.I(I), .O(Decode2_inst3_O));
assign O = {Decode2_inst3_O,Decode2_inst2_O,Decode2_inst1_O,Decode2_inst0_O};
endmodule

