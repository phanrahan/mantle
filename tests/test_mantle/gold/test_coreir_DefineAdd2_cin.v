module Add2_cin (input [1:0] I0, input [1:0] I1, output [1:0] O, input  CIN);
wire [1:0] inst0_out;
wire [1:0] inst1_out;
coreir_add2 inst0 (.in0(inst1_out), .in1(I1), .out(inst0_out));
coreir_add2 inst1 (.in0({1'b0,CIN}), .in1(I0), .out(inst1_out));
assign O = inst0_out;
endmodule

