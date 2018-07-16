module NXOr4 (input [3:0] I, output  O);
wire  inst0_O;
SB_LUT4 #(.LUT_INIT(16'h9669)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst0_O));
assign O = inst0_O;
endmodule

module NXOr4x4 (input [3:0] I0, input [3:0] I1, input [3:0] I2, input [3:0] I3, output [3:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
NXOr4 inst0 (.I({I3[0],I2[0],I1[0],I0[0]}), .O(inst0_O));
NXOr4 inst1 (.I({I3[1],I2[1],I1[1],I0[1]}), .O(inst1_O));
NXOr4 inst2 (.I({I3[2],I2[2],I1[2],I0[2]}), .O(inst2_O));
NXOr4 inst3 (.I({I3[3],I2[3],I1[3],I0[3]}), .O(inst3_O));
assign O = {inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

