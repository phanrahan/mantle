module And4x8 (input [7:0] I0, input [7:0] I1, input [7:0] I2, input [7:0] I3, output [7:0] O);
wire  inst0_out;
wire  inst1_out;
wire  inst2_out;
wire  inst3_out;
wire  inst4_out;
wire  inst5_out;
wire  inst6_out;
wire  inst7_out;
andr inst0 (.in({I3[0],I2[0],I1[0],I0[0]}), .out(inst0_out));
andr inst1 (.in({I3[1],I2[1],I1[1],I0[1]}), .out(inst1_out));
andr inst2 (.in({I3[2],I2[2],I1[2],I0[2]}), .out(inst2_out));
andr inst3 (.in({I3[3],I2[3],I1[3],I0[3]}), .out(inst3_out));
andr inst4 (.in({I3[4],I2[4],I1[4],I0[4]}), .out(inst4_out));
andr inst5 (.in({I3[5],I2[5],I1[5],I0[5]}), .out(inst5_out));
andr inst6 (.in({I3[6],I2[6],I1[6],I0[6]}), .out(inst6_out));
andr inst7 (.in({I3[7],I2[7],I1[7],I0[7]}), .out(inst7_out));
assign O = {inst7_out,inst6_out,inst5_out,inst4_out,inst3_out,inst2_out,inst1_out,inst0_out};
endmodule

