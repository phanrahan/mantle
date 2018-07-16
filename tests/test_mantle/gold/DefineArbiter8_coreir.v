module Add8 (input [7:0] I0, input [7:0] I1, output [7:0] O);
wire [7:0] inst0_out;
coreir_add8 inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT2_2 (input  I0, input  I1, output  O);
wire  inst0_out;
coreir_lut2 inst0 (.in({I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module Arbiter8 (input [7:0] I, output [7:0] O);
wire [7:0] inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
wire  inst8_O;
Add8 inst0 (.I0(I), .I1({1'b1,1'b1,1'b1,1'b1,1'b1,1'b1,1'b1,1'b1}), .O(inst0_O));
LUT2_2 inst1 (.I0(I[0]), .I1(inst0_O[0]), .O(inst1_O));
LUT2_2 inst2 (.I0(I[1]), .I1(inst0_O[1]), .O(inst2_O));
LUT2_2 inst3 (.I0(I[2]), .I1(inst0_O[2]), .O(inst3_O));
LUT2_2 inst4 (.I0(I[3]), .I1(inst0_O[3]), .O(inst4_O));
LUT2_2 inst5 (.I0(I[4]), .I1(inst0_O[4]), .O(inst5_O));
LUT2_2 inst6 (.I0(I[5]), .I1(inst0_O[5]), .O(inst6_O));
LUT2_2 inst7 (.I0(I[6]), .I1(inst0_O[6]), .O(inst7_O));
LUT2_2 inst8 (.I0(I[7]), .I1(inst0_O[7]), .O(inst8_O));
assign O = {inst8_O,inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O};
endmodule

