module Add4 (input [3:0] I0, input [3:0] I1, output [3:0] O);
wire  inst0_O5;
wire  inst0_O6;
wire  inst1_O;
wire  inst2_O5;
wire  inst2_O6;
wire  inst3_O;
wire  inst4_O5;
wire  inst4_O6;
wire  inst5_O;
wire  inst6_O5;
wire  inst6_O6;
wire  inst7_O;
LUT6_2 #(.INIT(64'h1111111111111110)) inst0 (.I0(I0[0]), .I1(I1[0]), .I5(1'b1), .O5(inst0_O5), .O6(inst0_O6));
MUXCY inst1 (.DI(inst0_O5), .S(inst0_O6), .O(inst1_O));
LUT6_2 #(.INIT(64'h1111111111111110)) inst2 (.I0(I0[1]), .I1(I1[1]), .I5(1'b1), .O5(inst2_O5), .O6(inst2_O6));
MUXCY inst3 (.DI(inst2_O5), .CI(inst1_O), .S(inst2_O6), .O(inst3_O));
LUT6_2 #(.INIT(64'h1111111111111110)) inst4 (.I0(I0[2]), .I1(I1[2]), .I5(1'b1), .O5(inst4_O5), .O6(inst4_O6));
MUXCY inst5 (.DI(inst4_O5), .CI(inst3_O), .S(inst4_O6), .O(inst5_O));
LUT6_2 #(.INIT(64'h1111111111111110)) inst6 (.I0(I0[3]), .I1(I1[3]), .I5(1'b1), .O5(inst6_O5), .O6(inst6_O6));
MUXCY inst7 (.DI(inst6_O5), .CI(inst5_O), .S(inst6_O6), .O(inst7_O));
assign O = {inst6_O6,inst4_O6,inst2_O6,inst0_O6};
endmodule

module Arbiter4 (input [3:0] I, output [3:0] O);
wire [3:0] inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
Add4 inst0 (.I0(I), .I1({1'b1,1'b1,1'b1,1'b1}), .O(inst0_O));
LUT2 #(.INIT(4'h2)) inst1 (.I0(I[0]), .I1(inst0_O[0]), .O(inst1_O));
LUT2 #(.INIT(4'h2)) inst2 (.I0(I[1]), .I1(inst0_O[1]), .O(inst2_O));
LUT2 #(.INIT(4'h2)) inst3 (.I0(I[2]), .I1(inst0_O[2]), .O(inst3_O));
LUT2 #(.INIT(4'h2)) inst4 (.I0(I[3]), .I1(inst0_O[3]), .O(inst4_O));
assign O = {inst4_O,inst3_O,inst2_O,inst1_O};
endmodule

