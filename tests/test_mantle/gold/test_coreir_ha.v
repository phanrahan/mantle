module xor_wrapped (input  I0, input  I1, output  O);
wire  inst0_out;
coreir_xor inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

module and_wrapped (input  I0, input  I1, output  O);
wire  inst0_out;
coreir_and inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

module HalfAdder (input  I0, input  I1, output  O, output  COUT);
wire  inst0_O;
wire  inst1_O;
xor_wrapped inst0 (.I1(I1), .O(inst0_O));
and_wrapped inst1 (.I0(I0), .I1(I1), .O(inst1_O));
assign O = inst0_O;
assign COUT = inst1_O;
endmodule

