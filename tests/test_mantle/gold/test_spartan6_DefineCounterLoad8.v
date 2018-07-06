module Add8_cout (input [7:0] I0, input [7:0] I1, output [7:0] O, output  COUT);
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
LUT6_2 #(.INIT(64'h1111111111111110)) inst0 (.I0(I0[0]), .I1(I1[0]), .I5(1'b1), .O5(inst0_O5), .O6(inst0_O6));
MUXCY inst1 (.DI(inst0_O5), .S(inst0_O6), .O(inst1_O));
LUT6_2 #(.INIT(64'h1111111111111110)) inst2 (.I0(I0[1]), .I1(I1[1]), .I5(1'b1), .O5(inst2_O5), .O6(inst2_O6));
MUXCY inst3 (.DI(inst2_O5), .CI(inst1_O), .S(inst2_O6), .O(inst3_O));
LUT6_2 #(.INIT(64'h1111111111111110)) inst4 (.I0(I0[2]), .I1(I1[2]), .I5(1'b1), .O5(inst4_O5), .O6(inst4_O6));
MUXCY inst5 (.DI(inst4_O5), .CI(inst3_O), .S(inst4_O6), .O(inst5_O));
LUT6_2 #(.INIT(64'h1111111111111110)) inst6 (.I0(I0[3]), .I1(I1[3]), .I5(1'b1), .O5(inst6_O5), .O6(inst6_O6));
MUXCY inst7 (.DI(inst6_O5), .CI(inst5_O), .S(inst6_O6), .O(inst7_O));
LUT6_2 #(.INIT(64'h1111111111111110)) inst8 (.I0(I0[4]), .I1(I1[4]), .I5(1'b1), .O5(inst8_O5), .O6(inst8_O6));
MUXCY inst9 (.DI(inst8_O5), .CI(inst7_O), .S(inst8_O6), .O(inst9_O));
LUT6_2 #(.INIT(64'h1111111111111110)) inst10 (.I0(I0[5]), .I1(I1[5]), .I5(1'b1), .O5(inst10_O5), .O6(inst10_O6));
MUXCY inst11 (.DI(inst10_O5), .CI(inst9_O), .S(inst10_O6), .O(inst11_O));
LUT6_2 #(.INIT(64'h1111111111111110)) inst12 (.I0(I0[6]), .I1(I1[6]), .I5(1'b1), .O5(inst12_O5), .O6(inst12_O6));
MUXCY inst13 (.DI(inst12_O5), .CI(inst11_O), .S(inst12_O6), .O(inst13_O));
LUT6_2 #(.INIT(64'h1111111111111110)) inst14 (.I0(I0[7]), .I1(I1[7]), .I5(1'b1), .O5(inst14_O5), .O6(inst14_O6));
MUXCY inst15 (.DI(inst14_O5), .CI(inst13_O), .S(inst14_O6), .O(inst15_O));
assign O = {inst14_O6,inst12_O6,inst10_O6,inst8_O6,inst6_O6,inst4_O6,inst2_O6,inst0_O6};
endmodule

module Mux2 (input [1:0] I, input  S, output  O);
wire  inst0_O;
LUT3 #(.INIT(8'hCA)) inst0 (.I0(I[0]), .I1(I[1]), .I2(S), .O(inst0_O));
assign O = inst0_O;
endmodule

module Mux2x8 (input [7:0] I0, input [7:0] I1, input  S, output [7:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
Mux2 inst0 (.I({I1[0],I0[0]}), .S(S), .O(inst0_O));
Mux2 inst1 (.I({I1[1],I0[1]}), .S(S), .O(inst1_O));
Mux2 inst2 (.I({I1[2],I0[2]}), .S(S), .O(inst2_O));
Mux2 inst3 (.I({I1[3],I0[3]}), .S(S), .O(inst3_O));
Mux2 inst4 (.I({I1[4],I0[4]}), .S(S), .O(inst4_O));
Mux2 inst5 (.I({I1[5],I0[5]}), .S(S), .O(inst5_O));
Mux2 inst6 (.I({I1[6],I0[6]}), .S(S), .O(inst6_O));
Mux2 inst7 (.I({I1[7],I0[7]}), .S(S), .O(inst7_O));
assign O = {inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
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
FDRSE #(.INIT(1'h0)) inst0 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(I[0]), .Q(inst0_Q));
FDRSE #(.INIT(1'h0)) inst1 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(I[1]), .Q(inst1_Q));
FDRSE #(.INIT(1'h0)) inst2 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(I[2]), .Q(inst2_Q));
FDRSE #(.INIT(1'h0)) inst3 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(I[3]), .Q(inst3_Q));
FDRSE #(.INIT(1'h0)) inst4 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(I[4]), .Q(inst4_Q));
FDRSE #(.INIT(1'h0)) inst5 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(I[5]), .Q(inst5_Q));
FDRSE #(.INIT(1'h0)) inst6 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(I[6]), .Q(inst6_Q));
FDRSE #(.INIT(1'h0)) inst7 (.CE(1'b1), .R(1'b0), .S(1'b0), .D(I[7]), .Q(inst7_Q));
assign O = {inst7_Q,inst6_Q,inst5_Q,inst4_Q,inst3_Q,inst2_Q,inst1_Q,inst0_Q};
endmodule

module CounterLoad8 (input [7:0] DATA, input  LOAD, output [7:0] O, output  COUT, input  CLK);
wire [7:0] inst0_O;
wire  inst0_COUT;
wire [7:0] inst1_O;
wire [7:0] inst2_O;
Add8_cout inst0 (.I0(inst2_O), .I1({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b1}), .O(inst0_O), .COUT(inst0_COUT));
Mux2x8 inst1 (.I0(inst0_O), .I1(DATA), .S(LOAD), .O(inst1_O));
Register8 inst2 (.I(inst1_O), .O(inst2_O), .CLK(CLK));
assign O = inst2_O;
assign COUT = inst0_COUT;
endmodule

