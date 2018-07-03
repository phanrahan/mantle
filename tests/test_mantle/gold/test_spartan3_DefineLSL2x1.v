module FixedLSL2_1 (input [1:0] I, output [1:0] O);
assign O = {I[0],1'b0};
endmodule

