module Negate4 (input [3:0] I, output [3:0] O);
wire [3:0] inst0_out;
coreir_Negate4 inst0 (.in(I), .out(inst0_out));
assign O = inst0_out;
endmodule

