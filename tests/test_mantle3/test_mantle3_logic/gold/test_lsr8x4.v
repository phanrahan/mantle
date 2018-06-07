module FixedLSR8_4 (input [7:0] I, output [7:0] O);
assign O = {1'b0,1'b0,1'b0,1'b0,I[7],I[6],I[5],I[4]};
endmodule

