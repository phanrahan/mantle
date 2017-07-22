module And3 (input  I0, input  I1, input  I2, output  O);
wire  inst0_0;
and inst0 (inst0_0, I0, I1, I2);
assign O = inst0_0;
endmodule

module main (input  I0, input  I1, input  I2, output  O);
wire  inst0_O;
And3 inst0 (.I0(I0), .I1(I1), .I2(I2), .O(inst0_O));
assign O = inst0_O;
endmodule

