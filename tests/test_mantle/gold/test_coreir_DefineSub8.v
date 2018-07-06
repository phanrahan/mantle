module Invert8_wrapped (input [7:0] I, output [7:0] O);
wire [7:0] inst0_out;
coreir_not inst0 (.in(I), .out(inst0_out));
assign O = inst0_out;
endmodule

module Add8_cin (input [7:0] I0, input [7:0] I1, output [7:0] O, input  CIN);
wire [7:0] inst0_out;
wire [7:0] inst1_out;
coreir_add8 inst0 (.in0(inst1_out), .in1(I1), .out(inst0_out));
coreir_add8 inst1 (.in0({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,CIN}), .in1(I0), .out(inst1_out));
assign O = inst0_out;
endmodule

module Sub8 (input [7:0] I0, input [7:0] I1, output [7:0] O);
wire [7:0] inst0_O;
wire [7:0] inst1_O;
Invert8_wrapped inst0 (.I(I1), .O(inst0_O));
Add8_cin inst1 (.I0(I0), .I1(inst0_O), .O(inst1_O), .CIN(1'b1));
assign O = inst1_O;
endmodule

