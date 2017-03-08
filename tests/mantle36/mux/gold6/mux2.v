module main (output [0:0] LED, input [2:0] SWITCH);
wire  inst0_O;
LUT3 #(.INIT(8'hCA)) inst0 (.I0(SWITCH[0]), .I1(SWITCH[1]), .I2(SWITCH[2]), .O(inst0_O));
assign LED = {inst0_O};
endmodule

