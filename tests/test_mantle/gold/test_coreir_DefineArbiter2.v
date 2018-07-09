module Add2 (input [1:0] I0, input [1:0] I1, output [1:0] O);
wire [1:0] inst0_out;
coreir_add2 inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT2_2 (input  I0, input  I1, output  O);
wire  inst0_out;
coreir_lut2 inst0 (.in({I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module Arbiter2 (input [1:0] I, output [1:0] O);
wire [1:0] inst0_O;
wire  inst1_O;
wire  inst2_O;
Add2 inst0 (.I0(I), .I1({1'b1,1'b1}), .O(inst0_O));
LUT2_2 inst1 (.I0(I[0]), .I1(inst0_O[0]), .O(inst1_O));
LUT2_2 inst2 (.I0(I[1]), .I1(inst0_O[1]), .O(inst2_O));
assign O = {inst2_O,inst1_O};
endmodule

