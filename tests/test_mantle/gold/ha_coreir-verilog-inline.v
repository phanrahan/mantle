module HalfAdder (input CIN, output COUT, input I, output O);
corebit_and and_inst0(.in0(I), .in1(CIN), .out(COUT));
corebit_xor xor_inst0(.in0(I), .in1(CIN), .out(O));
endmodule

