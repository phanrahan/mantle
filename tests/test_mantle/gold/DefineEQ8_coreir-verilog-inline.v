module coreir_eq #(parameter width = 1) (input [width-1:0] in0, input [width-1:0] in1, output out);
  assign out = in0 == in1;
endmodule

module coreir_eq_8_wrapped (input [7:0] I0, input [7:0] I1, output O);
coreir_eq #(.width(8)) coreir_eq_8_inst0(.in0(I0), .in1(I1), .out(O));
endmodule

