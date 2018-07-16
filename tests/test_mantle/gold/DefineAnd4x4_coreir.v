module And4x4 (input [3:0] I0, input [3:0] I1, input [3:0] I2, input [3:0] I3, output [3:0] O);
wire  inst0_out;
wire  inst1_out;
wire  inst2_out;
wire  inst3_out;
andr inst0 (.in({I3[0],I2[0],I1[0],I0[0]}), .out(inst0_out));
andr inst1 (.in({I3[1],I2[1],I1[1],I0[1]}), .out(inst1_out));
andr inst2 (.in({I3[2],I2[2],I1[2],I0[2]}), .out(inst2_out));
andr inst3 (.in({I3[3],I2[3],I1[3],I0[3]}), .out(inst3_out));
assign O = {inst3_out,inst2_out,inst1_out,inst0_out};
endmodule

