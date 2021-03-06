module Sub2_cin1_cout (input [1:0] I0, input [1:0] I1, output [1:0] O, output  COUT);
wire  LUT6_2_inst0_O5;
wire  LUT6_2_inst0_O6;
wire  MUXCY_inst0_O;
wire  XORCY_inst0_O;
wire  LUT6_2_inst1_O5;
wire  LUT6_2_inst1_O6;
wire  MUXCY_inst1_O;
wire  XORCY_inst1_O;
LUT6_2 #(.INIT(64'h99999999AAAAAAAA)) LUT6_2_inst0 (.I0(I0[0]), .I1(I1[0]), .I2(1'b0), .I3(1'b0), .I4(1'b0), .I5(1'b1), .O5(LUT6_2_inst0_O5), .O6(LUT6_2_inst0_O6));
MUXCY MUXCY_inst0 (.DI(LUT6_2_inst0_O5), .CI(1'b1), .S(LUT6_2_inst0_O6), .O(MUXCY_inst0_O));
XORCY XORCY_inst0 (.LI(LUT6_2_inst0_O6), .CI(1'b1), .O(XORCY_inst0_O));
LUT6_2 #(.INIT(64'h99999999AAAAAAAA)) LUT6_2_inst1 (.I0(I0[1]), .I1(I1[1]), .I2(1'b0), .I3(1'b0), .I4(1'b0), .I5(1'b1), .O5(LUT6_2_inst1_O5), .O6(LUT6_2_inst1_O6));
MUXCY MUXCY_inst1 (.DI(LUT6_2_inst1_O5), .CI(MUXCY_inst0_O), .S(LUT6_2_inst1_O6), .O(MUXCY_inst1_O));
XORCY XORCY_inst1 (.LI(LUT6_2_inst1_O6), .CI(MUXCY_inst0_O), .O(XORCY_inst1_O));
assign O = {XORCY_inst1_O,XORCY_inst0_O};
assign COUT = MUXCY_inst1_O;
endmodule

module UGT2 (input [1:0] I0, input [1:0] I1, output  O);
wire [1:0] Sub2_cin1_cout_inst0_O;
wire  Sub2_cin1_cout_inst0_COUT;
wire  LUT1_inst0_O;
Sub2_cin1_cout Sub2_cin1_cout_inst0 (.I0(I1), .I1(I0), .O(Sub2_cin1_cout_inst0_O), .COUT(Sub2_cin1_cout_inst0_COUT));
LUT1 #(.INIT(2'h1)) LUT1_inst0 (.I0(Sub2_cin1_cout_inst0_COUT), .O(LUT1_inst0_O));
assign O = LUT1_inst0_O;
endmodule

