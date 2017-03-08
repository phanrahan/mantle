module ROM16x8 (input [3:0] I, output [7:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
LUT4 #(.INIT(16'hD7AD)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst0_O));
LUT4 #(.INIT(16'h279F)) inst1 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst1_O));
LUT4 #(.INIT(16'h2FFB)) inst2 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst2_O));
LUT4 #(.INIT(16'h796D)) inst3 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst3_O));
LUT4 #(.INIT(16'hFD45)) inst4 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst4_O));
LUT4 #(.INIT(16'hDF71)) inst5 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst5_O));
LUT4 #(.INIT(16'hEF7C)) inst6 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst6_O));
LUT4 #(.INIT(16'h0000)) inst7 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst7_O));
assign O = {inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module main (output [7:0] LED, input [3:0] SWITCH);
wire [7:0] inst0_O;
ROM16x8 inst0 (.I(SWITCH), .O(inst0_O));
assign LED = inst0_O;
endmodule

