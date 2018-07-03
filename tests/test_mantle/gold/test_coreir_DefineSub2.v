module Invert2_wrapped (input [1:0] I, output [1:0] O);
wire [1:0] inst0_out;
coreir_not inst0 (.in(I), .out(inst0_out));
assign O = inst0_out;
endmodule

module Add2_cin (input [1:0] I0, input [1:0] I1, output [1:0] O, input  CIN);
wire [1:0] inst0_out;
wire [1:0] inst1_out;
coreir_add2 inst0 (.in0(inst1_out), .in1(I1), .out(inst0_out));
coreir_add2 inst1 (.in0({1'b0,CIN}), .in1(I0), .out(inst1_out));
assign O = inst0_out;
endmodule

module Sub2 (input [1:0] I0, input [1:0] I1, output [1:0] O);
wire [1:0] inst0_O;
wire [1:0] inst1_O;
Invert2_wrapped inst0 (.I(I1), .O(inst0_O));
Add2_cin inst1 (.I0(I0), .I1(inst0_O), .O(inst1_O), .CIN(1'b1));
assign O = inst1_O;
endmodule

