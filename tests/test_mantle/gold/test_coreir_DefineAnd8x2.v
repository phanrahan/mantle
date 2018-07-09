module And8x2 (input [1:0] I0, input [1:0] I1, input [1:0] I2, input [1:0] I3, input [1:0] I4, input [1:0] I5, input [1:0] I6, input [1:0] I7, output [1:0] O);
wire  inst0_out;
wire  inst1_out;
andr inst0 (.in({I7[0],I6[0],I5[0],I4[0],I3[0],I2[0],I1[0],I0[0]}), .out(inst0_out));
andr inst1 (.in({I7[1],I6[1],I5[1],I4[1],I3[1],I2[1],I1[1],I0[1]}), .out(inst1_out));
assign O = {inst1_out,inst0_out};
endmodule

