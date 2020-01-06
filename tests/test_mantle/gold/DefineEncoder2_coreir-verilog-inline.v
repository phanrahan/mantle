module coreir_orr #(parameter width = 1) (input [width-1:0] in, output out);
  assign out = |in;
endmodule

module Or1xNone (input I0, output O);
coreir_orr #(.width(1)) orr_inst0(.in(I0), .out(O));
endmodule

module Encoder2 (input [1:0] I, output [0:0] O);
Or1xNone Or1xNone_inst0(.I0(I[1]), .O(O));
endmodule

