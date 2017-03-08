module Decoder3 (input [2:0] I, output [7:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
LUT3 #(.INIT(8'h01)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .O(inst0_O));
LUT3 #(.INIT(8'h02)) inst1 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .O(inst1_O));
LUT3 #(.INIT(8'h04)) inst2 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .O(inst2_O));
LUT3 #(.INIT(8'h08)) inst3 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .O(inst3_O));
LUT3 #(.INIT(8'h10)) inst4 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .O(inst4_O));
LUT3 #(.INIT(8'h20)) inst5 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .O(inst5_O));
LUT3 #(.INIT(8'h40)) inst6 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .O(inst6_O));
LUT3 #(.INIT(8'h80)) inst7 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .O(inst7_O));
assign O = {inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module main (output [7:0] LED, input [2:0] SWITCH);
wire [7:0] inst0_O;
Decoder3 inst0 (.I(SWITCH), .O(inst0_O));
assign LED = inst0_O;
endmodule

