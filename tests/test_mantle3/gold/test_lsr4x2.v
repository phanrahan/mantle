module FixedLSR4_2 (input [3:0] I, output [3:0] O);
assign O = {1'b0,1'b0,I[3],I[2]};
endmodule

