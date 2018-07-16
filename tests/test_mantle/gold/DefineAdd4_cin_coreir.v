module Add4_cin (input [3:0] I0, input [3:0] I1, output [3:0] O, input  CIN);
wire [3:0] inst0_out;
wire [3:0] inst1_out;
coreir_add4 inst0 (.in0(inst1_out), .in1(I1), .out(inst0_out));
coreir_add4 inst1 (.in0({1'b0,1'b0,1'b0,CIN}), .in1(I0), .out(inst1_out));
assign O = inst0_out;
endmodule

