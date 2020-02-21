module fold_xor3None (input I0, input I1, input I2, output O);
assign O = (I0 ^ I1) ^ I2;
endmodule

module Or3xNone (input I0, input I1, input I2, output O);
assign O = | ({I2,I1,I0});
endmodule

module FullAdder (input I0, input I1, input CIN, output O, output COUT);
Or3xNone Or3xNone_inst0(.I0(I0 & I1), .I1(I1 & CIN), .I2(I0 & CIN), .O(COUT));
fold_xor3None fold_xor3None_inst0(.I0(I0), .I1(I1), .I2(CIN), .O(O));
endmodule

