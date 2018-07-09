module FixedLSL4_3 (input [3:0] I, output [3:0] O);
assign O = {I[0],1'b0,1'b0,1'b0};
endmodule

