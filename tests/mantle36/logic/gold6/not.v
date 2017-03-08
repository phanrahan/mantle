module main (output [0:0] LED, input [0:0] SWITCH);
wire  inst0_O;
LUT1 #(.INIT(2'h1)) inst0 (.I0(SWITCH[0]), .O(inst0_O));
assign LED = {inst0_O};
endmodule

