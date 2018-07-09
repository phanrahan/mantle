module NAnd8 (input [7:0] I, output  O);
wire  inst0_O5;
wire  inst0_O6;
wire  inst1_O;
wire  inst2_O5;
wire  inst2_O6;
wire  inst3_O;
LUT6_2 #(.INIT(64'h8000800080008000)) inst0 (.I5(1'b1), .O5(inst0_O5), .O6(inst0_O6));
MUXCY inst1 (.DI(inst0_O5), .CI(1'b1), .S(inst0_O6), .O(inst1_O));
LUT6_2 #(.INIT(64'h8000800080008000)) inst2 (.I5(1'b1), .O5(inst2_O5), .O6(inst2_O6));
MUXCY inst3 (.DI(inst2_O5), .CI(inst1_O), .S(inst2_O6), .O(inst3_O));
assign O = inst3_O;
endmodule

module NAnd8x4 (input [3:0] I0, input [3:0] I1, input [3:0] I2, input [3:0] I3, input [3:0] I4, input [3:0] I5, input [3:0] I6, input [3:0] I7, output [3:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
NAnd8 inst0 (.I({I7[0],I6[0],I5[0],I4[0],I3[0],I2[0],I1[0],I0[0]}), .O(inst0_O));
NAnd8 inst1 (.I({I7[1],I6[1],I5[1],I4[1],I3[1],I2[1],I1[1],I0[1]}), .O(inst1_O));
NAnd8 inst2 (.I({I7[2],I6[2],I5[2],I4[2],I3[2],I2[2],I1[2],I0[2]}), .O(inst2_O));
NAnd8 inst3 (.I({I7[3],I6[3],I5[3],I4[3],I3[3],I2[3],I1[3],I0[3]}), .O(inst3_O));
assign O = {inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

