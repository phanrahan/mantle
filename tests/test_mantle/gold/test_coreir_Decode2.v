module EQ2 (input [1:0] I0, input [1:0] I1, output  O);
wire  inst0_out;
coreir_eq inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

module Decode02 (input [1:0] I, output  O);
wire  inst0_O;
EQ2 inst0 (.I0(I), .I1({1'b0,1'b0}), .O(inst0_O));
assign O = inst0_O;
endmodule

