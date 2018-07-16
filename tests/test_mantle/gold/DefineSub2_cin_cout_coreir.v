module Invert2_wrapped (input [1:0] I, output [1:0] O);
wire [1:0] inst0_out;
coreir_not inst0 (.in(I), .out(inst0_out));
assign O = inst0_out;
endmodule

module Add2_cout_cin (input [1:0] I0, input [1:0] I1, output [1:0] O, output  COUT, input  CIN);
wire [2:0] inst0_out;
wire [2:0] inst1_out;
coreir_add3 inst0 (.in0(inst1_out), .in1({1'b0,I1[1],I1[0]}), .out(inst0_out));
coreir_add3 inst1 (.in0({1'b0,1'b0,CIN}), .in1({1'b0,I0[1],I0[0]}), .out(inst1_out));
assign O = {inst0_out[1],inst0_out[0]};
assign COUT = inst0_out[2];
endmodule

module Sub2_cout_cin (input [1:0] I0, input [1:0] I1, output [1:0] O, output  COUT, input  CIN);
wire [1:0] inst0_O;
wire [1:0] inst1_O;
wire  inst1_COUT;
wire  inst2_out;
Invert2_wrapped inst0 (.I(I1), .O(inst0_O));
Add2_cout_cin inst1 (.I0(I0), .I1(inst0_O), .O(inst1_O), .COUT(inst1_COUT), .CIN(inst2_out));
coreir_bitnot inst2 (.in(CIN), .out(inst2_out));
assign O = inst1_O;
assign COUT = inst1_COUT;
endmodule

