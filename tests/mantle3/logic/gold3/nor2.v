module main (output [0:0] LED, input [1:0] SWITCH);
wire  inst0_O;
LUT2 #(.INIT(4'h1)) inst0 (.I0(SWITCH[0]), .I1(SWITCH[1]), .O(inst0_O));
assign LED = {inst0_O};
endmodule

