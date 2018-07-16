module NOr4 (input [3:0] I, output  O);
wire  inst0_O;
SB_LUT4 #(.LUT_INIT(16'h0001)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst0_O));
assign O = inst0_O;
endmodule

module NOr4x2 (input [1:0] I0, input [1:0] I1, input [1:0] I2, input [1:0] I3, output [1:0] O);
wire  inst0_O;
wire  inst1_O;
NOr4 inst0 (.I({I3[0],I2[0],I1[0],I0[0]}), .O(inst0_O));
NOr4 inst1 (.I({I3[1],I2[1],I1[1],I0[1]}), .O(inst1_O));
assign O = {inst1_O,inst0_O};
endmodule

