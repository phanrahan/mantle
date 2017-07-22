module And2 (input  I0, input  I1, output  O);
wire  inst0_0;
and inst0 (inst0_0, I0, I1);
assign O = inst0_0;
endmodule

module main (input [1:0] I, output  O);
wire  inst0_O;
And2 inst0 (.I0(I[0]), .I1(I[1]), .O(inst0_O));
assign O = inst0_O;
endmodule

