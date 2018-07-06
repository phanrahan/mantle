module LUT2_1 (input  I0, input  I1, output  O);
wire  inst0_out;
coreir_lut2 inst0 (.in({I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT2_2 (input  I0, input  I1, output  O);
wire  inst0_out;
coreir_lut2 inst0 (.in({I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT2_4 (input  I0, input  I1, output  O);
wire  inst0_out;
coreir_lut2 inst0 (.in({I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT2_8 (input  I0, input  I1, output  O);
wire  inst0_out;
coreir_lut2 inst0 (.in({I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module Decoder2 (input [1:0] I, output [3:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
LUT2_1 inst0 (.I0(I[0]), .I1(I[1]), .O(inst0_O));
LUT2_2 inst1 (.I0(I[0]), .I1(I[1]), .O(inst1_O));
LUT2_4 inst2 (.I0(I[0]), .I1(I[1]), .O(inst2_O));
LUT2_8 inst3 (.I0(I[0]), .I1(I[1]), .O(inst3_O));
assign O = {inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

