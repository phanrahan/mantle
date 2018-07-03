module Negate2 (input [1:0] I, output [1:0] O);
wire [1:0] inst0_out;
coreir_Negate2 inst0 (.in(I), .out(inst0_out));
assign O = inst0_out;
endmodule

