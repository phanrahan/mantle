module FixedLSL8_4 (input [7:0] I, output [7:0] O);
assign O = {I[3],I[2],I[1],I[0],1'b0,1'b0,1'b0,1'b0};
endmodule

