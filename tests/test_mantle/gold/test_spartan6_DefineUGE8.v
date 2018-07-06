module Sub8_cin1_cout (input [7:0] I0, input [7:0] I1, output [7:0] O, output  COUT);
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
wire  inst8_O5;
wire  inst8_O6;
wire  inst9_O;
wire  inst10_O5;
wire  inst10_O6;
wire  inst11_O;
wire  inst12_O5;
wire  inst12_O6;
wire  inst13_O;
wire  inst14_O5;
wire  inst14_O6;
wire  inst15_O;
LUT6_2 #(.INIT(64'h4444444444444443)) inst0 (.I0(I0[0]), .I1(I1[0]), .I5(1'b1), .O5(inst0_O5), .O6(inst0_O6));
MUXCY inst1 (.DI(inst0_O5), .CI(1'b1), .S(inst0_O6), .O(inst1_O));
LUT6_2 #(.INIT(64'h4444444444444443)) inst2 (.I0(I0[1]), .I1(I1[1]), .I5(1'b1), .O5(inst2_O5), .O6(inst2_O6));
MUXCY inst3 (.DI(inst2_O5), .CI(inst1_O), .S(inst2_O6), .O(inst3_O));
LUT6_2 #(.INIT(64'h4444444444444443)) inst4 (.I0(I0[2]), .I1(I1[2]), .I5(1'b1), .O5(inst4_O5), .O6(inst4_O6));
MUXCY inst5 (.DI(inst4_O5), .CI(inst3_O), .S(inst4_O6), .O(inst5_O));
LUT6_2 #(.INIT(64'h4444444444444443)) inst6 (.I0(I0[3]), .I1(I1[3]), .I5(1'b1), .O5(inst6_O5), .O6(inst6_O6));
MUXCY inst7 (.DI(inst6_O5), .CI(inst5_O), .S(inst6_O6), .O(inst7_O));
LUT6_2 #(.INIT(64'h4444444444444443)) inst8 (.I0(I0[4]), .I1(I1[4]), .I5(1'b1), .O5(inst8_O5), .O6(inst8_O6));
MUXCY inst9 (.DI(inst8_O5), .CI(inst7_O), .S(inst8_O6), .O(inst9_O));
LUT6_2 #(.INIT(64'h4444444444444443)) inst10 (.I0(I0[5]), .I1(I1[5]), .I5(1'b1), .O5(inst10_O5), .O6(inst10_O6));
MUXCY inst11 (.DI(inst10_O5), .CI(inst9_O), .S(inst10_O6), .O(inst11_O));
LUT6_2 #(.INIT(64'h4444444444444443)) inst12 (.I0(I0[6]), .I1(I1[6]), .I5(1'b1), .O5(inst12_O5), .O6(inst12_O6));
MUXCY inst13 (.DI(inst12_O5), .CI(inst11_O), .S(inst12_O6), .O(inst13_O));
LUT6_2 #(.INIT(64'h4444444444444443)) inst14 (.I0(I0[7]), .I1(I1[7]), .I5(1'b1), .O5(inst14_O5), .O6(inst14_O6));
MUXCY inst15 (.DI(inst14_O5), .CI(inst13_O), .S(inst14_O6), .O(inst15_O));
assign O = {inst14_O6,inst12_O6,inst10_O6,inst8_O6,inst6_O6,inst4_O6,inst2_O6,inst0_O6};
endmodule

module UGE8 (input [7:0] I0, input [7:0] I1, output  O);
wire [7:0] inst0_O;
wire  inst0_COUT;
Sub8_cin1_cout inst0 (.I0(I0), .I1(I1), .O(inst0_O), .COUT(inst0_COUT));
assign O = inst0_COUT;
endmodule

