module Add4 (input [3:0] I0, input [3:0] I1, output [3:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
LUT2 #(.INIT(4'h6)) inst0 (.I0(I0[0]), .I1(I1[0]), .O(inst0_O));
MUXCY inst1 (.DI(I0[0]), .CI(1'b0), .S(inst0_O), .O(inst1_O));
LUT2 #(.INIT(4'h6)) inst2 (.I0(I0[1]), .I1(I1[1]), .O(inst2_O));
MUXCY inst3 (.DI(I0[1]), .CI(inst1_O), .S(inst2_O), .O(inst3_O));
LUT2 #(.INIT(4'h6)) inst4 (.I0(I0[2]), .I1(I1[2]), .O(inst4_O));
MUXCY inst5 (.DI(I0[2]), .CI(inst3_O), .S(inst4_O), .O(inst5_O));
LUT2 #(.INIT(4'h6)) inst6 (.I0(I0[3]), .I1(I1[3]), .O(inst6_O));
MUXCY inst7 (.DI(I0[3]), .CI(inst5_O), .S(inst6_O), .O(inst7_O));
assign O = {inst6_O,inst4_O,inst2_O,inst0_O};
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

