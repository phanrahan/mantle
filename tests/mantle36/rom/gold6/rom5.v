module main (output [0:0] LED, input [4:0] SWITCH);
wire  inst0_O;
LUT5 #(.INIT(32'hAAAAAAAA)) inst0 (.I0(SWITCH[0]), .I1(SWITCH[1]), .I2(SWITCH[2]), .I3(SWITCH[3]), .I4(SWITCH[4]), .O(inst0_O));
assign LED = {inst0_O};
endmodule

