module Decode4 (input [3:0] I, output  O);
wire  inst0_O;
LUT4 #(.INIT(16'h0001)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst0_O));
assign O = inst0_O;
endmodule

module Decoder4 (input [3:0] I, output [15:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
wire  inst8_O;
wire  inst9_O;
wire  inst10_O;
wire  inst11_O;
wire  inst12_O;
wire  inst13_O;
wire  inst14_O;
wire  inst15_O;
Decode4 inst0 (.I(I), .O(inst0_O));
Decode4 inst1 (.I(I), .O(inst1_O));
Decode4 inst2 (.I(I), .O(inst2_O));
Decode4 inst3 (.I(I), .O(inst3_O));
Decode4 inst4 (.I(I), .O(inst4_O));
Decode4 inst5 (.I(I), .O(inst5_O));
Decode4 inst6 (.I(I), .O(inst6_O));
Decode4 inst7 (.I(I), .O(inst7_O));
Decode4 inst8 (.I(I), .O(inst8_O));
Decode4 inst9 (.I(I), .O(inst9_O));
Decode4 inst10 (.I(I), .O(inst10_O));
Decode4 inst11 (.I(I), .O(inst11_O));
Decode4 inst12 (.I(I), .O(inst12_O));
Decode4 inst13 (.I(I), .O(inst13_O));
Decode4 inst14 (.I(I), .O(inst14_O));
Decode4 inst15 (.I(I), .O(inst15_O));
assign O = {inst15_O,inst14_O,inst13_O,inst12_O,inst11_O,inst10_O,inst9_O,inst8_O,inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

