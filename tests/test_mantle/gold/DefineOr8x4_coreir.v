module Or8x4 (input [3:0] I0, input [3:0] I1, input [3:0] I2, input [3:0] I3, input [3:0] I4, input [3:0] I5, input [3:0] I6, input [3:0] I7, output [3:0] O);
wire  inst0_out;
wire  inst1_out;
wire  inst2_out;
wire  inst3_out;
orr inst0 (.in({I7[0],I6[0],I5[0],I4[0],I3[0],I2[0],I1[0],I0[0]}), .out(inst0_out));
orr inst1 (.in({I7[1],I6[1],I5[1],I4[1],I3[1],I2[1],I1[1],I0[1]}), .out(inst1_out));
orr inst2 (.in({I7[2],I6[2],I5[2],I4[2],I3[2],I2[2],I1[2],I0[2]}), .out(inst2_out));
orr inst3 (.in({I7[3],I6[3],I5[3],I4[3],I3[3],I2[3],I1[3],I0[3]}), .out(inst3_out));
assign O = {inst3_out,inst2_out,inst1_out,inst0_out};
endmodule

