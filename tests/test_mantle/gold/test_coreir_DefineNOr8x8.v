module Invert8_wrapped (input [7:0] I, output [7:0] O);
wire [7:0] inst0_out;
coreir_not inst0 (.in(I), .out(inst0_out));
assign O = inst0_out;
endmodule

module Or8x8 (input [7:0] I0, input [7:0] I1, input [7:0] I2, input [7:0] I3, input [7:0] I4, input [7:0] I5, input [7:0] I6, input [7:0] I7, output [7:0] O);
wire  inst0_out;
wire  inst1_out;
wire  inst2_out;
wire  inst3_out;
wire  inst4_out;
wire  inst5_out;
wire  inst6_out;
wire  inst7_out;
orr inst0 (.in({I7[0],I6[0],I5[0],I4[0],I3[0],I2[0],I1[0],I0[0]}), .out(inst0_out));
orr inst1 (.in({I7[1],I6[1],I5[1],I4[1],I3[1],I2[1],I1[1],I0[1]}), .out(inst1_out));
orr inst2 (.in({I7[2],I6[2],I5[2],I4[2],I3[2],I2[2],I1[2],I0[2]}), .out(inst2_out));
orr inst3 (.in({I7[3],I6[3],I5[3],I4[3],I3[3],I2[3],I1[3],I0[3]}), .out(inst3_out));
orr inst4 (.in({I7[4],I6[4],I5[4],I4[4],I3[4],I2[4],I1[4],I0[4]}), .out(inst4_out));
orr inst5 (.in({I7[5],I6[5],I5[5],I4[5],I3[5],I2[5],I1[5],I0[5]}), .out(inst5_out));
orr inst6 (.in({I7[6],I6[6],I5[6],I4[6],I3[6],I2[6],I1[6],I0[6]}), .out(inst6_out));
orr inst7 (.in({I7[7],I6[7],I5[7],I4[7],I3[7],I2[7],I1[7],I0[7]}), .out(inst7_out));
assign O = {inst7_out,inst6_out,inst5_out,inst4_out,inst3_out,inst2_out,inst1_out,inst0_out};
endmodule

module NOr88 (input [7:0] I0, input [7:0] I1, input [7:0] I2, input [7:0] I3, input [7:0] I4, input [7:0] I5, input [7:0] I6, input [7:0] I7, output [7:0] O);
wire [7:0] inst0_O;
wire [7:0] inst1_O;
Invert8_wrapped inst0 (.I(inst1_O), .O(inst0_O));
Or8x8 inst1 (.I0(I0), .I1(I1), .I2(I2), .I3(I3), .I4(I4), .I5(I5), .I6(I6), .I7(I7), .O(inst1_O));
assign O = inst0_O;
endmodule

