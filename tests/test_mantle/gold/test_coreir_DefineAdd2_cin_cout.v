module Add2_cout_cin (input [1:0] I0, input [1:0] I1, output [1:0] O, output  COUT, input  CIN);
wire [2:0] inst0_out;
wire [2:0] inst1_out;
coreir_add3 inst0 (.in0(inst1_out), .in1({1'b0,I1[1],I1[0]}), .out(inst0_out));
coreir_add3 inst1 (.in0({1'b0,1'b0,CIN}), .in1({1'b0,I0[1],I0[0]}), .out(inst1_out));
assign O = {inst0_out[1],inst0_out[0]};
assign COUT = inst0_out[2];
endmodule

