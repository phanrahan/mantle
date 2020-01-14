module HalfAdder (input CIN, output COUT, input I, output O);
assign COUT = I & CIN;
assign O = I ^ CIN;
endmodule

