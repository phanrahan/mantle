module Or4xNone (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_out;
orr inst0 (.in({I3,I2,I1,I0}), .out(inst0_out));
assign O = inst0_out;
endmodule

module Encoder8 (input [7:0] I, output [2:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
Or4xNone inst0 (.I0(I[1]), .I1(I[3]), .I2(I[5]), .I3(I[7]), .O(inst0_O));
Or4xNone inst1 (.I0(I[2]), .I1(I[3]), .I2(I[6]), .I3(I[7]), .O(inst1_O));
Or4xNone inst2 (.I0(I[4]), .I1(I[5]), .I2(I[6]), .I3(I[7]), .O(inst2_O));
assign O = {inst2_O,inst1_O,inst0_O};
endmodule

