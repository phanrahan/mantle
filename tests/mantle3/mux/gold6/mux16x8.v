module Mux8 (input [7:0] I, input [2:0] S, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
LUT6 #(.INIT(64'hFF00F0F0CCCCAAAA)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .I4(S[0]), .I5(S[1]), .O(inst0_O));
LUT6 #(.INIT(64'hFF00F0F0CCCCAAAA)) inst1 (.I0(I[4]), .I1(I[5]), .I2(I[6]), .I3(I[7]), .I4(S[0]), .I5(S[1]), .O(inst1_O));
MUXF7 inst2 (.I0(inst0_O), .I1(inst1_O), .S(S[2]), .O(inst2_O));
assign O = inst2_O;
endmodule

module Mux16 (input [15:0] I, input [3:0] S, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
Mux8 inst0 (.I({I[7],I[6],I[5],I[4],I[3],I[2],I[1],I[0]}), .S({S[2],S[1],S[0]}), .O(inst0_O));
Mux8 inst1 (.I({I[15],I[14],I[13],I[12],I[11],I[10],I[9],I[8]}), .S({S[2],S[1],S[0]}), .O(inst1_O));
MUXF7 inst2 (.I0(inst0_O), .I1(inst1_O), .S(S[3]), .O(inst2_O));
assign O = inst2_O;
endmodule

module Mux16x8 (input [7:0] I0, input [7:0] I1, input [7:0] I2, input [7:0] I3, input [7:0] I4, input [7:0] I5, input [7:0] I6, input [7:0] I7, input [7:0] I8, input [7:0] I9, input [7:0] I10, input [7:0] I11, input [7:0] I12, input [7:0] I13, input [7:0] I14, input [7:0] I15, input [3:0] S, output [7:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
Mux16 inst0 (.I({I15[0],I14[0],I13[0],I12[0],I11[0],I10[0],I9[0],I8[0],I7[0],I6[0],I5[0],I4[0],I3[0],I2[0],I1[0],I0[0]}), .S(S), .O(inst0_O));
Mux16 inst1 (.I({I15[1],I14[1],I13[1],I12[1],I11[1],I10[1],I9[1],I8[1],I7[1],I6[1],I5[1],I4[1],I3[1],I2[1],I1[1],I0[1]}), .S(S), .O(inst1_O));
Mux16 inst2 (.I({I15[2],I14[2],I13[2],I12[2],I11[2],I10[2],I9[2],I8[2],I7[2],I6[2],I5[2],I4[2],I3[2],I2[2],I1[2],I0[2]}), .S(S), .O(inst2_O));
Mux16 inst3 (.I({I15[3],I14[3],I13[3],I12[3],I11[3],I10[3],I9[3],I8[3],I7[3],I6[3],I5[3],I4[3],I3[3],I2[3],I1[3],I0[3]}), .S(S), .O(inst3_O));
Mux16 inst4 (.I({I15[4],I14[4],I13[4],I12[4],I11[4],I10[4],I9[4],I8[4],I7[4],I6[4],I5[4],I4[4],I3[4],I2[4],I1[4],I0[4]}), .S(S), .O(inst4_O));
Mux16 inst5 (.I({I15[5],I14[5],I13[5],I12[5],I11[5],I10[5],I9[5],I8[5],I7[5],I6[5],I5[5],I4[5],I3[5],I2[5],I1[5],I0[5]}), .S(S), .O(inst5_O));
Mux16 inst6 (.I({I15[6],I14[6],I13[6],I12[6],I11[6],I10[6],I9[6],I8[6],I7[6],I6[6],I5[6],I4[6],I3[6],I2[6],I1[6],I0[6]}), .S(S), .O(inst6_O));
Mux16 inst7 (.I({I15[7],I14[7],I13[7],I12[7],I11[7],I10[7],I9[7],I8[7],I7[7],I6[7],I5[7],I4[7],I3[7],I2[7],I1[7],I0[7]}), .S(S), .O(inst7_O));
assign O = {inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module main (output [7:0] LED, input [3:0] SWITCH, input  CLKIN);
wire [7:0] inst0_O;
Mux16x8 inst0 (.I0({1'b0,1'b0,1'b1,1'b0,1'b0,1'b0,1'b0,1'b0}), .I1({1'b0,1'b1,1'b0,1'b0,1'b0,1'b0,1'b0,1'b1}), .I2({1'b0,1'b0,1'b1,1'b0,1'b0,1'b0,1'b1,1'b0}), .I3({1'b0,1'b1,1'b0,1'b0,1'b0,1'b0,1'b1,1'b1}), .I4({1'b0,1'b0,1'b1,1'b0,1'b0,1'b1,1'b0,1'b0}), .I5({1'b0,1'b1,1'b0,1'b0,1'b0,1'b1,1'b0,1'b1}), .I6({1'b0,1'b0,1'b1,1'b0,1'b0,1'b1,1'b1,1'b0}), .I7({1'b0,1'b1,1'b0,1'b0,1'b0,1'b1,1'b1,1'b1}), .I8({1'b0,1'b0,1'b1,1'b0,1'b1,1'b0,1'b0,1'b0}), .I9({1'b0,1'b1,1'b0,1'b0,1'b1,1'b0,1'b0,1'b1}), .I10({1'b0,1'b0,1'b1,1'b0,1'b1,1'b0,1'b1,1'b0}), .I11({1'b0,1'b1,1'b0,1'b0,1'b1,1'b0,1'b1,1'b1}), .I12({1'b0,1'b0,1'b1,1'b0,1'b1,1'b1,1'b0,1'b0}), .I13({1'b0,1'b1,1'b0,1'b0,1'b1,1'b1,1'b0,1'b1}), .I14({1'b0,1'b0,1'b1,1'b0,1'b1,1'b1,1'b1,1'b0}), .I15({1'b0,1'b1,1'b0,1'b0,1'b1,1'b1,1'b1,1'b1}), .S(SWITCH), .O(inst0_O));
assign LED = inst0_O;
endmodule

