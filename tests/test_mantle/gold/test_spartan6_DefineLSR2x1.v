module FixedLSR2_1 (input [1:0] I, output [1:0] O);
assign O = {1'b0,I[1]};
endmodule

