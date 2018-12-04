module Decode4 (input [3:0] I, output  O);
wire  LUT4_inst0_O;
LUT4 #(.INIT(16'h0001)) LUT4_inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(LUT4_inst0_O));
assign O = LUT4_inst0_O;
endmodule

module Decoder4 (input [3:0] I, output [15:0] O);
wire  Decode4_inst0_O;
wire  Decode4_inst1_O;
wire  Decode4_inst2_O;
wire  Decode4_inst3_O;
wire  Decode4_inst4_O;
wire  Decode4_inst5_O;
wire  Decode4_inst6_O;
wire  Decode4_inst7_O;
wire  Decode4_inst8_O;
wire  Decode4_inst9_O;
wire  Decode4_inst10_O;
wire  Decode4_inst11_O;
wire  Decode4_inst12_O;
wire  Decode4_inst13_O;
wire  Decode4_inst14_O;
wire  Decode4_inst15_O;
Decode4 Decode4_inst0 (.I(I), .O(Decode4_inst0_O));
Decode4 Decode4_inst1 (.I(I), .O(Decode4_inst1_O));
Decode4 Decode4_inst2 (.I(I), .O(Decode4_inst2_O));
Decode4 Decode4_inst3 (.I(I), .O(Decode4_inst3_O));
Decode4 Decode4_inst4 (.I(I), .O(Decode4_inst4_O));
Decode4 Decode4_inst5 (.I(I), .O(Decode4_inst5_O));
Decode4 Decode4_inst6 (.I(I), .O(Decode4_inst6_O));
Decode4 Decode4_inst7 (.I(I), .O(Decode4_inst7_O));
Decode4 Decode4_inst8 (.I(I), .O(Decode4_inst8_O));
Decode4 Decode4_inst9 (.I(I), .O(Decode4_inst9_O));
Decode4 Decode4_inst10 (.I(I), .O(Decode4_inst10_O));
Decode4 Decode4_inst11 (.I(I), .O(Decode4_inst11_O));
Decode4 Decode4_inst12 (.I(I), .O(Decode4_inst12_O));
Decode4 Decode4_inst13 (.I(I), .O(Decode4_inst13_O));
Decode4 Decode4_inst14 (.I(I), .O(Decode4_inst14_O));
Decode4 Decode4_inst15 (.I(I), .O(Decode4_inst15_O));
assign O = {Decode4_inst15_O,Decode4_inst14_O,Decode4_inst13_O,Decode4_inst12_O,Decode4_inst11_O,Decode4_inst10_O,Decode4_inst9_O,Decode4_inst8_O,Decode4_inst7_O,Decode4_inst6_O,Decode4_inst5_O,Decode4_inst4_O,Decode4_inst3_O,Decode4_inst2_O,Decode4_inst1_O,Decode4_inst0_O};
endmodule

