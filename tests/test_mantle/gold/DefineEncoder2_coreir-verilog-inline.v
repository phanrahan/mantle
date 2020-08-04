module Or1xNone (
    input I0,
    output O
);
assign O = | I0;
endmodule

module Encoder2 (
    input [1:0] I,
    output [0:0] O
);
wire Or1xNone_inst0_I0;
assign Or1xNone_inst0_I0 = I[1];
Or1xNone Or1xNone_inst0 (
    .I0(Or1xNone_inst0_I0),
    .O(O)
);
endmodule

