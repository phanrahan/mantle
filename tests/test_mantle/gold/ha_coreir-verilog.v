module corebit_xor (
    input in0,
    input in1,
    output out
);
  assign out = in0 ^ in1;
endmodule

module corebit_and (
    input in0,
    input in1,
    output out
);
  assign out = in0 & in1;
endmodule

module HalfAdder (
    input I,
    input CIN,
    output O,
    output COUT
);
wire and_inst0_in0;
wire and_inst0_in1;
wire and_inst0_out;
wire xor_inst0_in0;
wire xor_inst0_in1;
wire xor_inst0_out;
assign and_inst0_in0 = I;
assign and_inst0_in1 = CIN;
corebit_and and_inst0 (
    .in0(and_inst0_in0),
    .in1(and_inst0_in1),
    .out(and_inst0_out)
);
assign xor_inst0_in0 = I;
assign xor_inst0_in1 = CIN;
corebit_xor xor_inst0 (
    .in0(xor_inst0_in0),
    .in1(xor_inst0_in1),
    .out(xor_inst0_out)
);
assign O = xor_inst0_out;
assign COUT = and_inst0_out;
endmodule

