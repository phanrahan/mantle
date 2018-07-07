module Add8_cin (input [7:0] I0, input [7:0] I1, output [7:0] O, input  CIN);
wire [7:0] inst0_out;
wire [7:0] inst1_out;
coreir_add8 inst0 (.in0(inst1_out), .in1(I1), .out(inst0_out));
coreir_add8 inst1 (.in0({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,CIN}), .in1(I0), .out(inst1_out));
assign O = inst0_out;
endmodule

