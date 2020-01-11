module NE8 (input [7:0] I0, input [7:0] I1, output O);
corebit_not not_inst0(.in(I0 == I1), .out(O));
endmodule

