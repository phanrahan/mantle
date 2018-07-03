module Invert2_wrapped (input [1:0] I, output [1:0] O);
wire [1:0] inst0_out;
coreir_not inst0 (.in(I), .out(inst0_out));
assign O = inst0_out;
endmodule

module or2_wrapped (input [1:0] I0, input [1:0] I1, output [1:0] O);
wire [1:0] inst0_out;
coreir_or inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

module NOr22 (input [1:0] I0, input [1:0] I1, output [1:0] O);
wire [1:0] inst0_O;
wire [1:0] inst1_O;
Invert2_wrapped inst0 (.I(inst1_O), .O(inst0_O));
or2_wrapped inst1 (.I0(I0), .I1(I1), .O(inst1_O));
assign O = inst0_O;
endmodule

