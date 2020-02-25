module corebit_xor (
    input in0,
    input in1,
    output out
);
  assign out = in0 ^ in1;
endmodule

module corebit_or (
    input in0,
    input in1,
    output out
);
  assign out = in0 | in1;
endmodule

module corebit_and (
    input in0,
    input in1,
    output out
);
  assign out = in0 & in1;
endmodule

module FullAdder (
    input I0,
    input I1,
    input CIN,
    output O,
    output COUT
);
wire magma_Bit_and_inst0_out;
wire magma_Bit_and_inst1_out;
wire magma_Bit_and_inst2_out;
wire magma_Bit_or_inst0_out;
wire magma_Bit_or_inst1_out;
wire magma_Bit_xor_inst0_out;
wire magma_Bit_xor_inst1_out;
corebit_and magma_Bit_and_inst0 (
    .in0(I0),
    .in1(I1),
    .out(magma_Bit_and_inst0_out)
);
corebit_and magma_Bit_and_inst1 (
    .in0(I1),
    .in1(CIN),
    .out(magma_Bit_and_inst1_out)
);
corebit_and magma_Bit_and_inst2 (
    .in0(I0),
    .in1(CIN),
    .out(magma_Bit_and_inst2_out)
);
corebit_or magma_Bit_or_inst0 (
    .in0(magma_Bit_and_inst0_out),
    .in1(magma_Bit_and_inst1_out),
    .out(magma_Bit_or_inst0_out)
);
corebit_or magma_Bit_or_inst1 (
    .in0(magma_Bit_or_inst0_out),
    .in1(magma_Bit_and_inst2_out),
    .out(magma_Bit_or_inst1_out)
);
corebit_xor magma_Bit_xor_inst0 (
    .in0(I0),
    .in1(I1),
    .out(magma_Bit_xor_inst0_out)
);
corebit_xor magma_Bit_xor_inst1 (
    .in0(magma_Bit_xor_inst0_out),
    .in1(CIN),
    .out(magma_Bit_xor_inst1_out)
);
assign O = magma_Bit_xor_inst1_out;
assign COUT = magma_Bit_or_inst1_out;
endmodule

