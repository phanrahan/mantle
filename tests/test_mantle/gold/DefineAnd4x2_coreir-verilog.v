module coreir_andr #(parameter width = 1) (input [width-1:0] in, output out);
  assign out = &in;
endmodule

module And4x2 (input [1:0] I0, input [1:0] I1, input [1:0] I2, input [1:0] I3, output [1:0] O);
wire andr_inst0_out;
wire andr_inst1_out;
coreir_andr #(.width(4)) andr_inst0(.in({I3[0],I2[0],I1[0],I0[0]}), .out(andr_inst0_out));
coreir_andr #(.width(4)) andr_inst1(.in({I3[1],I2[1],I1[1],I0[1]}), .out(andr_inst1_out));
assign O = {andr_inst1_out,andr_inst0_out};
endmodule

