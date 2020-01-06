module coreir_orr #(parameter width = 1) (input [width-1:0] in, output out);
  assign out = |in;
endmodule

module fold_xor3None (input I0, input I1, input I2, output O);
wire xor_inst0_out;
corebit_xor xor_inst0(.in0(I0), .in1(I1), .out(xor_inst0_out));
corebit_xor xor_inst1(.in0(xor_inst0_out), .in1(I2), .out(O));
endmodule

module Or3xNone (input I0, input I1, input I2, output O);
coreir_orr #(.width(3)) orr_inst0(.in({I2,I1,I0}), .out(O));
endmodule

module FullAdder (input CIN, output COUT, input I0, input I1, output O);
wire and_inst0_out;
wire and_inst1_out;
wire and_inst2_out;
Or3xNone Or3xNone_inst0(.I0(and_inst0_out), .I1(and_inst1_out), .I2(and_inst2_out), .O(COUT));
corebit_and and_inst0(.in0(I0), .in1(I1), .out(and_inst0_out));
corebit_and and_inst1(.in0(I1), .in1(CIN), .out(and_inst1_out));
corebit_and and_inst2(.in0(I0), .in1(CIN), .out(and_inst2_out));
fold_xor3None fold_xor3None_inst0(.I0(I0), .I1(I1), .I2(CIN), .O(O));
endmodule

