module Decode4 (input [3:0] I, output  O);
wire  inst0_O;
LUT4 #(.INIT(16'h0001)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst0_O));
assign O = inst0_O;
endmodule

