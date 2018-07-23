module Invert4_wrapped (input [3:0] I, output [3:0] O);
wire [3:0] inst0_out;
coreir_not inst0 (.in(I), .out(inst0_out));
assign O = inst0_out;
endmodule

module TestsCircuit_invert_4_SInt_SIntType (input signed [3:0] I, output signed [3:0] O0, output signed [3:0] O1);
wire [3:0] inst0_O;
wire [3:0] inst1_O;
Invert4_wrapped inst0 (.I(I), .O(inst0_O));
Invert4_wrapped inst1 (.I(I), .O(inst1_O));
assign O0 = inst0_O;
assign O1 = inst1_O;
endmodule

