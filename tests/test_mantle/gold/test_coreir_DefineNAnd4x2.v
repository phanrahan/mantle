module Invert2_wrapped (input [1:0] I, output [1:0] O);
wire [1:0] inst0_out;
coreir_not inst0 (.in(I), .out(inst0_out));
assign O = inst0_out;
endmodule

module And4x2 (input [1:0] I0, input [1:0] I1, input [1:0] I2, input [1:0] I3, output [1:0] O);
wire  inst0_out;
wire  inst1_out;
andr inst0 (.in({I3[0],I2[0],I1[0],I0[0]}), .out(inst0_out));
andr inst1 (.in({I3[1],I2[1],I1[1],I0[1]}), .out(inst1_out));
assign O = {inst1_out,inst0_out};
endmodule

module NAnd42 (input [1:0] I0, input [1:0] I1, input [1:0] I2, input [1:0] I3, output [1:0] O);
wire [1:0] inst0_O;
wire [1:0] inst1_O;
Invert2_wrapped inst0 (.I(inst1_O), .O(inst0_O));
And4x2 inst1 (.I0(I0), .I1(I1), .I2(I2), .I3(I3), .O(inst1_O));
assign O = inst0_O;
endmodule

