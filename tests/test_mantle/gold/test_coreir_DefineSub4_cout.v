module Invert4_wrapped (input [3:0] I, output [3:0] O);
wire [3:0] inst0_out;
coreir_not inst0 (.in(I), .out(inst0_out));
assign O = inst0_out;
endmodule

module Add4_cout_cin (input [3:0] I0, input [3:0] I1, output [3:0] O, output  COUT, input  CIN);
wire [4:0] inst0_out;
wire [4:0] inst1_out;
coreir_add5 inst0 (.in0(inst1_out), .in1({1'b0,I1[3],I1[2],I1[1],I1[0]}), .out(inst0_out));
coreir_add5 inst1 (.in0({1'b0,1'b0,1'b0,1'b0,CIN}), .in1({1'b0,I0[3],I0[2],I0[1],I0[0]}), .out(inst1_out));
assign O = {inst0_out[3],inst0_out[2],inst0_out[1],inst0_out[0]};
assign COUT = inst0_out[4];
endmodule

module Sub4_cout (input [3:0] I0, input [3:0] I1, output [3:0] O, output  COUT);
wire [3:0] inst0_O;
wire [3:0] inst1_O;
wire  inst1_COUT;
Invert4_wrapped inst0 (.I(I1), .O(inst0_O));
Add4_cout_cin inst1 (.I0(I0), .I1(inst0_O), .O(inst1_O), .COUT(inst1_COUT), .CIN(1'b1));
assign O = inst1_O;
assign COUT = inst1_COUT;
endmodule

