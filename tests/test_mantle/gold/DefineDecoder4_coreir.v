module LUT4_1 (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_out;
coreir_lut4 inst0 (.in({I3,I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT4_2 (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_out;
coreir_lut4 inst0 (.in({I3,I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT4_4 (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_out;
coreir_lut4 inst0 (.in({I3,I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT4_8 (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_out;
coreir_lut4 inst0 (.in({I3,I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT4_16 (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_out;
coreir_lut4 inst0 (.in({I3,I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT4_32 (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_out;
coreir_lut4 inst0 (.in({I3,I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT4_64 (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_out;
coreir_lut4 inst0 (.in({I3,I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT4_128 (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_out;
coreir_lut4 inst0 (.in({I3,I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT4_256 (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_out;
coreir_lut4 inst0 (.in({I3,I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT4_512 (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_out;
coreir_lut4 inst0 (.in({I3,I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT4_1024 (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_out;
coreir_lut4 inst0 (.in({I3,I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT4_2048 (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_out;
coreir_lut4 inst0 (.in({I3,I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT4_4096 (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_out;
coreir_lut4 inst0 (.in({I3,I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT4_8192 (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_out;
coreir_lut4 inst0 (.in({I3,I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT4_16384 (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_out;
coreir_lut4 inst0 (.in({I3,I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module LUT4_32768 (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_out;
coreir_lut4 inst0 (.in({I3,I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
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
LUT4_1 inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst0_O));
LUT4_2 inst1 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst1_O));
LUT4_4 inst2 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst2_O));
LUT4_8 inst3 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst3_O));
LUT4_16 inst4 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst4_O));
LUT4_32 inst5 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst5_O));
LUT4_64 inst6 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst6_O));
LUT4_128 inst7 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst7_O));
LUT4_256 inst8 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst8_O));
LUT4_512 inst9 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst9_O));
LUT4_1024 inst10 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst10_O));
LUT4_2048 inst11 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst11_O));
LUT4_4096 inst12 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst12_O));
LUT4_8192 inst13 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst13_O));
LUT4_16384 inst14 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst14_O));
LUT4_32768 inst15 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst15_O));
assign O = {inst15_O,inst14_O,inst13_O,inst12_O,inst11_O,inst10_O,inst9_O,inst8_O,inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

