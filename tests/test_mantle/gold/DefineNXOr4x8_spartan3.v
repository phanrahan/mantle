module NXOr4 (input [3:0] I, output  O);
wire  inst0_O;
LUT4 #(.INIT(16'h9669)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst0_O));
assign O = inst0_O;
endmodule

module NXOr4x8 (input [7:0] I0, input [7:0] I1, input [7:0] I2, input [7:0] I3, output [7:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
NXOr4 inst0 (.I({I3[0],I2[0],I1[0],I0[0]}), .O(inst0_O));
NXOr4 inst1 (.I({I3[1],I2[1],I1[1],I0[1]}), .O(inst1_O));
NXOr4 inst2 (.I({I3[2],I2[2],I1[2],I0[2]}), .O(inst2_O));
NXOr4 inst3 (.I({I3[3],I2[3],I1[3],I0[3]}), .O(inst3_O));
NXOr4 inst4 (.I({I3[4],I2[4],I1[4],I0[4]}), .O(inst4_O));
NXOr4 inst5 (.I({I3[5],I2[5],I1[5],I0[5]}), .O(inst5_O));
NXOr4 inst6 (.I({I3[6],I2[6],I1[6],I0[6]}), .O(inst6_O));
NXOr4 inst7 (.I({I3[7],I2[7],I1[7],I0[7]}), .O(inst7_O));
assign O = {inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

