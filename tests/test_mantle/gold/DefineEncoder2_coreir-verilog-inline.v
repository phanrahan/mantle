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
wire Or1xNone_inst0_O;
Or1xNone Or1xNone_inst0 (
    .I0(I[1]),
    .O(Or1xNone_inst0_O)
);
assign O[0] = Or1xNone_inst0_O;
endmodule

