module Not (input  I0, output  O);
wire  inst0_0;
not inst0 (inst0_0, I0);
assign O = inst0_0;
endmodule

module main (input  I, output  O);
wire  inst0_O;
Not inst0 (.I0(I), .O(inst0_O));
assign O = inst0_O;
endmodule

