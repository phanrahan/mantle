module EQ8 (input [7:0] I0, input [7:0] I1, output  O);
wire  inst0_out;
coreir_eq inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

module NE8 (input [7:0] I0, input [7:0] I1, output  O);
wire  inst0_O;
wire  inst1_out;
EQ8 inst0 (.I0(I0), .I1(I1), .O(inst0_O));
coreir_bitnot inst1 (.in(inst0_O), .out(inst1_out));
assign O = inst1_out;
endmodule

