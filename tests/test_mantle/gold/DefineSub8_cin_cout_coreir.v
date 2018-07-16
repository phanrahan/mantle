module Invert8_wrapped (input [7:0] I, output [7:0] O);
wire [7:0] inst0_out;
coreir_not inst0 (.in(I), .out(inst0_out));
assign O = inst0_out;
endmodule

module Add8_cout_cin (input [7:0] I0, input [7:0] I1, output [7:0] O, output  COUT, input  CIN);
wire [8:0] inst0_out;
wire [8:0] inst1_out;
coreir_add9 inst0 (.in0(inst1_out), .in1({1'b0,I1[7],I1[6],I1[5],I1[4],I1[3],I1[2],I1[1],I1[0]}), .out(inst0_out));
coreir_add9 inst1 (.in0({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,CIN}), .in1({1'b0,I0[7],I0[6],I0[5],I0[4],I0[3],I0[2],I0[1],I0[0]}), .out(inst1_out));
assign O = {inst0_out[7],inst0_out[6],inst0_out[5],inst0_out[4],inst0_out[3],inst0_out[2],inst0_out[1],inst0_out[0]};
assign COUT = inst0_out[8];
endmodule

module Sub8_cout_cin (input [7:0] I0, input [7:0] I1, output [7:0] O, output  COUT, input  CIN);
wire [7:0] inst0_O;
wire [7:0] inst1_O;
wire  inst1_COUT;
wire  inst2_out;
Invert8_wrapped inst0 (.I(I1), .O(inst0_O));
Add8_cout_cin inst1 (.I0(I0), .I1(inst0_O), .O(inst1_O), .COUT(inst1_COUT), .CIN(inst2_out));
coreir_bitnot inst2 (.in(CIN), .out(inst2_out));
assign O = inst1_O;
assign COUT = inst1_COUT;
endmodule

