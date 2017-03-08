module Decoder2 (input [1:0] I, output [3:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
SB_LUT4 #(.LUT_INIT(16'h0001)) inst0 (.I0(I[0]), .I1(I[1]), .I2(1'b0), .I3(1'b0), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'h0002)) inst1 (.I0(I[0]), .I1(I[1]), .I2(1'b0), .I3(1'b0), .O(inst1_O));
SB_LUT4 #(.LUT_INIT(16'h0004)) inst2 (.I0(I[0]), .I1(I[1]), .I2(1'b0), .I3(1'b0), .O(inst2_O));
SB_LUT4 #(.LUT_INIT(16'h0008)) inst3 (.I0(I[0]), .I1(I[1]), .I2(1'b0), .I3(1'b0), .O(inst3_O));
assign O = {inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module main (input [1:0] J1, output [3:0] J3);
wire [3:0] inst0_O;
Decoder2 inst0 (.I(J1), .O(inst0_O));
assign J3 = inst0_O;
endmodule

