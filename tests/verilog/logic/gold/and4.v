module And4 (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_0;
and inst0 (inst0_0, I0, I1, I2, I3);
assign O = inst0_0;
endmodule

module main (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_O;
And4 inst0 (.I0(I0), .I1(I1), .I2(I2), .I3(I3), .O(inst0_O));
assign O = inst0_O;
endmodule

