module LSL4_2 (input [3:0] I, output [3:0] O);
assign O = {I[1],I[0],1'b0,1'b0};
endmodule

