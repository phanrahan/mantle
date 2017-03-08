module And2x2 (input [1:0] I0, input [1:0] I1, output [1:0] O);
wire  inst0_0;
wire  inst1_0;
and inst0 (inst0_0, I0[0], I1[0]);
and inst1 (inst1_0, I0[1], I1[1]);
assign O = {inst1_0,inst0_0};
endmodule

module main (input  I0, input  I1, input  I2, input  I3, output  O0, output  O1);
wire [1:0] inst0_O;
And2x2 inst0 (.I0({I1,I0}), .I1({I3,I2}), .O(inst0_O));
assign O0 = inst0_O[0];
assign O1 = inst0_O[1];
endmodule

