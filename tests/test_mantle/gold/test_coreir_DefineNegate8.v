module Negate8 (input [7:0] I, output [7:0] O);
wire [7:0] inst0_out;
coreir_Negate8 inst0 (.in(I), .out(inst0_out));
assign O = inst0_out;
endmodule

