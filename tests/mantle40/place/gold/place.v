module And2x2 (input [1:0] I0, input [1:0] I1, output [1:0] O);
wire  inst0_O;
wire  inst1_O;
SB_LUT4 #(.LUT_INIT(16'h8888)) inst0 (.I0(I0[0]), .I1(I1[0]), .I2(1'b0), .I3(1'b0), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'h8888)) inst1 (.I0(I0[1]), .I1(I1[1]), .I2(1'b0), .I3(1'b0), .O(inst1_O));
assign O = {inst1_O,inst0_O};
endmodule

module main (input  I0, input  I1, input  I2, input  I3, output  D2, output  D1);
wire [1:0] inst0_O;
And2x2 inst0 (.I0({I1,I0}), .I1({I3,I2}), .O(inst0_O));
assign D2 = inst0_O[1];
assign D1 = inst0_O[0];
endmodule

