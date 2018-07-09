module Add8_cout (input [7:0] I0, input [7:0] I1, output [7:0] O, output  COUT);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
wire  inst8_O;
wire  inst9_O;
wire  inst10_O;
wire  inst11_O;
wire  inst12_O;
wire  inst13_O;
wire  inst14_O;
wire  inst15_O;
LUT2 #(.INIT(4'h6)) inst0 (.I0(I0[0]), .I1(I1[0]), .O(inst0_O));
MUXCY inst1 (.DI(I0[0]), .CI(1'b0), .S(inst0_O), .O(inst1_O));
LUT2 #(.INIT(4'h6)) inst2 (.I0(I0[1]), .I1(I1[1]), .O(inst2_O));
MUXCY inst3 (.DI(I0[1]), .CI(inst1_O), .S(inst2_O), .O(inst3_O));
LUT2 #(.INIT(4'h6)) inst4 (.I0(I0[2]), .I1(I1[2]), .O(inst4_O));
MUXCY inst5 (.DI(I0[2]), .CI(inst3_O), .S(inst4_O), .O(inst5_O));
LUT2 #(.INIT(4'h6)) inst6 (.I0(I0[3]), .I1(I1[3]), .O(inst6_O));
MUXCY inst7 (.DI(I0[3]), .CI(inst5_O), .S(inst6_O), .O(inst7_O));
LUT2 #(.INIT(4'h6)) inst8 (.I0(I0[4]), .I1(I1[4]), .O(inst8_O));
MUXCY inst9 (.DI(I0[4]), .CI(inst7_O), .S(inst8_O), .O(inst9_O));
LUT2 #(.INIT(4'h6)) inst10 (.I0(I0[5]), .I1(I1[5]), .O(inst10_O));
MUXCY inst11 (.DI(I0[5]), .CI(inst9_O), .S(inst10_O), .O(inst11_O));
LUT2 #(.INIT(4'h6)) inst12 (.I0(I0[6]), .I1(I1[6]), .O(inst12_O));
MUXCY inst13 (.DI(I0[6]), .CI(inst11_O), .S(inst12_O), .O(inst13_O));
LUT2 #(.INIT(4'h6)) inst14 (.I0(I0[7]), .I1(I1[7]), .O(inst14_O));
MUXCY inst15 (.DI(I0[7]), .CI(inst13_O), .S(inst14_O), .O(inst15_O));
assign O = {inst14_O,inst12_O,inst10_O,inst8_O,inst6_O,inst4_O,inst2_O,inst0_O};
assign COUT = inst15_O;
endmodule

module Register8 (input [7:0] I, output [7:0] O, input  CLK);
wire  inst0_Q;
wire  inst1_Q;
wire  inst2_Q;
wire  inst3_Q;
wire  inst4_Q;
wire  inst5_Q;
wire  inst6_Q;
wire  inst7_Q;
FDRSE #(.INIT(1'h0)) inst0 (.C(CLK), .CE(1'b1), .R(1'b0), .S(1'b0), .D(I[0]), .Q(inst0_Q));
FDRSE #(.INIT(1'h0)) inst1 (.C(CLK), .CE(1'b1), .R(1'b0), .S(1'b0), .D(I[1]), .Q(inst1_Q));
FDRSE #(.INIT(1'h0)) inst2 (.C(CLK), .CE(1'b1), .R(1'b0), .S(1'b0), .D(I[2]), .Q(inst2_Q));
FDRSE #(.INIT(1'h0)) inst3 (.C(CLK), .CE(1'b1), .R(1'b0), .S(1'b0), .D(I[3]), .Q(inst3_Q));
FDRSE #(.INIT(1'h0)) inst4 (.C(CLK), .CE(1'b1), .R(1'b0), .S(1'b0), .D(I[4]), .Q(inst4_Q));
FDRSE #(.INIT(1'h0)) inst5 (.C(CLK), .CE(1'b1), .R(1'b0), .S(1'b0), .D(I[5]), .Q(inst5_Q));
FDRSE #(.INIT(1'h0)) inst6 (.C(CLK), .CE(1'b1), .R(1'b0), .S(1'b0), .D(I[6]), .Q(inst6_Q));
FDRSE #(.INIT(1'h0)) inst7 (.C(CLK), .CE(1'b1), .R(1'b0), .S(1'b0), .D(I[7]), .Q(inst7_Q));
assign O = {inst7_Q,inst6_Q,inst5_Q,inst4_Q,inst3_Q,inst2_Q,inst1_Q,inst0_Q};
endmodule

module Counter8 (output [7:0] O, output  COUT, input  CLK);
wire [7:0] inst0_O;
wire  inst0_COUT;
wire [7:0] inst1_O;
Add8_cout inst0 (.I0(inst1_O), .I1({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b1}), .O(inst0_O), .COUT(inst0_COUT));
Register8 inst1 (.I(inst0_O), .O(inst1_O), .CLK(CLK));
assign O = inst1_O;
assign COUT = inst0_COUT;
endmodule

