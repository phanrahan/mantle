module FullAdder (
    input I0,
    input I1,
    input CIN,
    output O,
    output COUT
);
assign O = (I0 ^ I1) ^ CIN;
assign COUT = ((I0 & I1) | (I1 & CIN)) | (I0 & CIN);
endmodule

