module And4x2 (input [1:0] I0, input [1:0] I1, input [1:0] I2, input [1:0] I3, output [1:0] O);
wire  inst0_out;
wire  inst1_out;
andr inst0 (.in({I3[0],I2[0],I1[0],I0[0]}), .out(inst0_out));
andr inst1 (.in({I3[1],I2[1],I1[1],I0[1]}), .out(inst1_out));
assign O = {inst1_out,inst0_out};
endmodule

