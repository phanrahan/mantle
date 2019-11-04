module Register1CE (input [0:0] I, output [0:0] O, input  CLK, input  CE);
wire  SB_DFFE_inst0_Q;
SB_DFFE SB_DFFE_inst0 (.C(CLK), .E(CE), .D(I[0]), .Q(SB_DFFE_inst0_Q));
assign O = {SB_DFFE_inst0_Q};
endmodule

module Decoder4 (input [3:0] I, output [15:0] O);
wire  SB_LUT4_inst0_O;
wire  SB_LUT4_inst1_O;
wire  SB_LUT4_inst2_O;
wire  SB_LUT4_inst3_O;
wire  SB_LUT4_inst4_O;
wire  SB_LUT4_inst5_O;
wire  SB_LUT4_inst6_O;
wire  SB_LUT4_inst7_O;
wire  SB_LUT4_inst8_O;
wire  SB_LUT4_inst9_O;
wire  SB_LUT4_inst10_O;
wire  SB_LUT4_inst11_O;
wire  SB_LUT4_inst12_O;
wire  SB_LUT4_inst13_O;
wire  SB_LUT4_inst14_O;
wire  SB_LUT4_inst15_O;
SB_LUT4 #(.LUT_INIT(16'h0001)) SB_LUT4_inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(SB_LUT4_inst0_O));
SB_LUT4 #(.LUT_INIT(16'h0002)) SB_LUT4_inst1 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(SB_LUT4_inst1_O));
SB_LUT4 #(.LUT_INIT(16'h0004)) SB_LUT4_inst2 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(SB_LUT4_inst2_O));
SB_LUT4 #(.LUT_INIT(16'h0008)) SB_LUT4_inst3 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(SB_LUT4_inst3_O));
SB_LUT4 #(.LUT_INIT(16'h0010)) SB_LUT4_inst4 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(SB_LUT4_inst4_O));
SB_LUT4 #(.LUT_INIT(16'h0020)) SB_LUT4_inst5 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(SB_LUT4_inst5_O));
SB_LUT4 #(.LUT_INIT(16'h0040)) SB_LUT4_inst6 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(SB_LUT4_inst6_O));
SB_LUT4 #(.LUT_INIT(16'h0080)) SB_LUT4_inst7 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(SB_LUT4_inst7_O));
SB_LUT4 #(.LUT_INIT(16'h0100)) SB_LUT4_inst8 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(SB_LUT4_inst8_O));
SB_LUT4 #(.LUT_INIT(16'h0200)) SB_LUT4_inst9 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(SB_LUT4_inst9_O));
SB_LUT4 #(.LUT_INIT(16'h0400)) SB_LUT4_inst10 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(SB_LUT4_inst10_O));
SB_LUT4 #(.LUT_INIT(16'h0800)) SB_LUT4_inst11 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(SB_LUT4_inst11_O));
SB_LUT4 #(.LUT_INIT(16'h1000)) SB_LUT4_inst12 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(SB_LUT4_inst12_O));
SB_LUT4 #(.LUT_INIT(16'h2000)) SB_LUT4_inst13 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(SB_LUT4_inst13_O));
SB_LUT4 #(.LUT_INIT(16'h4000)) SB_LUT4_inst14 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(SB_LUT4_inst14_O));
SB_LUT4 #(.LUT_INIT(16'h8000)) SB_LUT4_inst15 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(SB_LUT4_inst15_O));
assign O = {SB_LUT4_inst15_O,SB_LUT4_inst14_O,SB_LUT4_inst13_O,SB_LUT4_inst12_O,SB_LUT4_inst11_O,SB_LUT4_inst10_O,SB_LUT4_inst9_O,SB_LUT4_inst8_O,SB_LUT4_inst7_O,SB_LUT4_inst6_O,SB_LUT4_inst5_O,SB_LUT4_inst4_O,SB_LUT4_inst3_O,SB_LUT4_inst2_O,SB_LUT4_inst1_O,SB_LUT4_inst0_O};
endmodule

module And2 (input [1:0] I, output  O);
wire  SB_LUT4_inst0_O;
SB_LUT4 #(.LUT_INIT(16'h8888)) SB_LUT4_inst0 (.I0(I[0]), .I1(I[1]), .I2(1'b0), .I3(1'b0), .O(SB_LUT4_inst0_O));
assign O = SB_LUT4_inst0_O;
endmodule

module And2x16 (input [15:0] I0, input [15:0] I1, output [15:0] O);
wire  And2_inst0_O;
wire  And2_inst1_O;
wire  And2_inst2_O;
wire  And2_inst3_O;
wire  And2_inst4_O;
wire  And2_inst5_O;
wire  And2_inst6_O;
wire  And2_inst7_O;
wire  And2_inst8_O;
wire  And2_inst9_O;
wire  And2_inst10_O;
wire  And2_inst11_O;
wire  And2_inst12_O;
wire  And2_inst13_O;
wire  And2_inst14_O;
wire  And2_inst15_O;
And2 And2_inst0 (.I({I1[0],I0[0]}), .O(And2_inst0_O));
And2 And2_inst1 (.I({I1[1],I0[1]}), .O(And2_inst1_O));
And2 And2_inst2 (.I({I1[2],I0[2]}), .O(And2_inst2_O));
And2 And2_inst3 (.I({I1[3],I0[3]}), .O(And2_inst3_O));
And2 And2_inst4 (.I({I1[4],I0[4]}), .O(And2_inst4_O));
And2 And2_inst5 (.I({I1[5],I0[5]}), .O(And2_inst5_O));
And2 And2_inst6 (.I({I1[6],I0[6]}), .O(And2_inst6_O));
And2 And2_inst7 (.I({I1[7],I0[7]}), .O(And2_inst7_O));
And2 And2_inst8 (.I({I1[8],I0[8]}), .O(And2_inst8_O));
And2 And2_inst9 (.I({I1[9],I0[9]}), .O(And2_inst9_O));
And2 And2_inst10 (.I({I1[10],I0[10]}), .O(And2_inst10_O));
And2 And2_inst11 (.I({I1[11],I0[11]}), .O(And2_inst11_O));
And2 And2_inst12 (.I({I1[12],I0[12]}), .O(And2_inst12_O));
And2 And2_inst13 (.I({I1[13],I0[13]}), .O(And2_inst13_O));
And2 And2_inst14 (.I({I1[14],I0[14]}), .O(And2_inst14_O));
And2 And2_inst15 (.I({I1[15],I0[15]}), .O(And2_inst15_O));
assign O = {And2_inst15_O,And2_inst14_O,And2_inst13_O,And2_inst12_O,And2_inst11_O,And2_inst10_O,And2_inst9_O,And2_inst8_O,And2_inst7_O,And2_inst6_O,And2_inst5_O,And2_inst4_O,And2_inst3_O,And2_inst2_O,And2_inst1_O,And2_inst0_O};
endmodule

module Mux2 (input [1:0] I, input  S, output  O);
wire  SB_LUT4_inst0_O;
SB_LUT4 #(.LUT_INIT(16'hCACA)) SB_LUT4_inst0 (.I0(I[0]), .I1(I[1]), .I2(S), .I3(1'b0), .O(SB_LUT4_inst0_O));
assign O = SB_LUT4_inst0_O;
endmodule

module Mux2x1 (input [0:0] I0, input [0:0] I1, input  S, output [0:0] O);
wire  Mux2_inst0_O;
Mux2 Mux2_inst0 (.I({I1[0],I0[0]}), .S(S), .O(Mux2_inst0_O));
assign O = {Mux2_inst0_O};
endmodule

module RAM16x1 (input [3:0] RADDR, output [0:0] RDATA, input [3:0] WADDR, input [0:0] WDATA, input  WE, input  CLK);
wire [0:0] Register1CE_inst0_O;
wire [0:0] Register1CE_inst1_O;
wire [0:0] Register1CE_inst2_O;
wire [0:0] Register1CE_inst3_O;
wire [0:0] Register1CE_inst4_O;
wire [0:0] Register1CE_inst5_O;
wire [0:0] Register1CE_inst6_O;
wire [0:0] Register1CE_inst7_O;
wire [0:0] Register1CE_inst8_O;
wire [0:0] Register1CE_inst9_O;
wire [0:0] Register1CE_inst10_O;
wire [0:0] Register1CE_inst11_O;
wire [0:0] Register1CE_inst12_O;
wire [0:0] Register1CE_inst13_O;
wire [0:0] Register1CE_inst14_O;
wire [0:0] Register1CE_inst15_O;
wire [15:0] Decoder4_inst0_O;
wire [15:0] And2x16_inst0_O;
wire [0:0] Mux2x1_inst0_O;
wire [0:0] Mux2x1_inst1_O;
wire [0:0] Mux2x1_inst2_O;
wire [0:0] Mux2x1_inst3_O;
wire [0:0] Mux2x1_inst4_O;
wire [0:0] Mux2x1_inst5_O;
wire [0:0] Mux2x1_inst6_O;
wire [0:0] Mux2x1_inst7_O;
wire [0:0] Mux2x1_inst8_O;
wire [0:0] Mux2x1_inst9_O;
wire [0:0] Mux2x1_inst10_O;
wire [0:0] Mux2x1_inst11_O;
wire [0:0] Mux2x1_inst12_O;
wire [0:0] Mux2x1_inst13_O;
wire [0:0] Mux2x1_inst14_O;
Register1CE Register1CE_inst0 (.I(WDATA), .O(Register1CE_inst0_O), .CLK(CLK), .CE(And2x16_inst0_O[0]));
Register1CE Register1CE_inst1 (.I(WDATA), .O(Register1CE_inst1_O), .CLK(CLK), .CE(And2x16_inst0_O[1]));
Register1CE Register1CE_inst2 (.I(WDATA), .O(Register1CE_inst2_O), .CLK(CLK), .CE(And2x16_inst0_O[2]));
Register1CE Register1CE_inst3 (.I(WDATA), .O(Register1CE_inst3_O), .CLK(CLK), .CE(And2x16_inst0_O[3]));
Register1CE Register1CE_inst4 (.I(WDATA), .O(Register1CE_inst4_O), .CLK(CLK), .CE(And2x16_inst0_O[4]));
Register1CE Register1CE_inst5 (.I(WDATA), .O(Register1CE_inst5_O), .CLK(CLK), .CE(And2x16_inst0_O[5]));
Register1CE Register1CE_inst6 (.I(WDATA), .O(Register1CE_inst6_O), .CLK(CLK), .CE(And2x16_inst0_O[6]));
Register1CE Register1CE_inst7 (.I(WDATA), .O(Register1CE_inst7_O), .CLK(CLK), .CE(And2x16_inst0_O[7]));
Register1CE Register1CE_inst8 (.I(WDATA), .O(Register1CE_inst8_O), .CLK(CLK), .CE(And2x16_inst0_O[8]));
Register1CE Register1CE_inst9 (.I(WDATA), .O(Register1CE_inst9_O), .CLK(CLK), .CE(And2x16_inst0_O[9]));
Register1CE Register1CE_inst10 (.I(WDATA), .O(Register1CE_inst10_O), .CLK(CLK), .CE(And2x16_inst0_O[10]));
Register1CE Register1CE_inst11 (.I(WDATA), .O(Register1CE_inst11_O), .CLK(CLK), .CE(And2x16_inst0_O[11]));
Register1CE Register1CE_inst12 (.I(WDATA), .O(Register1CE_inst12_O), .CLK(CLK), .CE(And2x16_inst0_O[12]));
Register1CE Register1CE_inst13 (.I(WDATA), .O(Register1CE_inst13_O), .CLK(CLK), .CE(And2x16_inst0_O[13]));
Register1CE Register1CE_inst14 (.I(WDATA), .O(Register1CE_inst14_O), .CLK(CLK), .CE(And2x16_inst0_O[14]));
Register1CE Register1CE_inst15 (.I(WDATA), .O(Register1CE_inst15_O), .CLK(CLK), .CE(And2x16_inst0_O[15]));
Decoder4 Decoder4_inst0 (.I(WADDR), .O(Decoder4_inst0_O));
And2x16 And2x16_inst0 (.I0(Decoder4_inst0_O), .I1({WE,WE,WE,WE,WE,WE,WE,WE,WE,WE,WE,WE,WE,WE,WE,WE}), .O(And2x16_inst0_O));
Mux2x1 Mux2x1_inst0 (.I0(Register1CE_inst0_O), .I1(Register1CE_inst1_O), .S(RADDR[0]), .O(Mux2x1_inst0_O));
Mux2x1 Mux2x1_inst1 (.I0(Register1CE_inst2_O), .I1(Register1CE_inst3_O), .S(RADDR[0]), .O(Mux2x1_inst1_O));
Mux2x1 Mux2x1_inst2 (.I0(Register1CE_inst4_O), .I1(Register1CE_inst5_O), .S(RADDR[0]), .O(Mux2x1_inst2_O));
Mux2x1 Mux2x1_inst3 (.I0(Register1CE_inst6_O), .I1(Register1CE_inst7_O), .S(RADDR[0]), .O(Mux2x1_inst3_O));
Mux2x1 Mux2x1_inst4 (.I0(Register1CE_inst8_O), .I1(Register1CE_inst9_O), .S(RADDR[0]), .O(Mux2x1_inst4_O));
Mux2x1 Mux2x1_inst5 (.I0(Register1CE_inst10_O), .I1(Register1CE_inst11_O), .S(RADDR[0]), .O(Mux2x1_inst5_O));
Mux2x1 Mux2x1_inst6 (.I0(Register1CE_inst12_O), .I1(Register1CE_inst13_O), .S(RADDR[0]), .O(Mux2x1_inst6_O));
Mux2x1 Mux2x1_inst7 (.I0(Register1CE_inst14_O), .I1(Register1CE_inst15_O), .S(RADDR[0]), .O(Mux2x1_inst7_O));
Mux2x1 Mux2x1_inst8 (.I0(Mux2x1_inst0_O), .I1(Mux2x1_inst1_O), .S(RADDR[1]), .O(Mux2x1_inst8_O));
Mux2x1 Mux2x1_inst9 (.I0(Mux2x1_inst2_O), .I1(Mux2x1_inst3_O), .S(RADDR[1]), .O(Mux2x1_inst9_O));
Mux2x1 Mux2x1_inst10 (.I0(Mux2x1_inst4_O), .I1(Mux2x1_inst5_O), .S(RADDR[1]), .O(Mux2x1_inst10_O));
Mux2x1 Mux2x1_inst11 (.I0(Mux2x1_inst6_O), .I1(Mux2x1_inst7_O), .S(RADDR[1]), .O(Mux2x1_inst11_O));
Mux2x1 Mux2x1_inst12 (.I0(Mux2x1_inst8_O), .I1(Mux2x1_inst9_O), .S(RADDR[2]), .O(Mux2x1_inst12_O));
Mux2x1 Mux2x1_inst13 (.I0(Mux2x1_inst10_O), .I1(Mux2x1_inst11_O), .S(RADDR[2]), .O(Mux2x1_inst13_O));
Mux2x1 Mux2x1_inst14 (.I0(Mux2x1_inst12_O), .I1(Mux2x1_inst13_O), .S(RADDR[3]), .O(Mux2x1_inst14_O));
assign RDATA = Mux2x1_inst14_O;
endmodule

module FullAdder (input  I0, input  I1, input  CIN, output  O, output  COUT);
wire  SB_LUT4_inst0_O;
wire  SB_CARRY_inst0_CO;
SB_LUT4 #(.LUT_INIT(16'h9696)) SB_LUT4_inst0 (.I0(I0), .I1(I1), .I2(CIN), .I3(1'b0), .O(SB_LUT4_inst0_O));
SB_CARRY SB_CARRY_inst0 (.I0(I0), .I1(I1), .CI(CIN), .CO(SB_CARRY_inst0_CO));
assign O = SB_LUT4_inst0_O;
assign COUT = SB_CARRY_inst0_CO;
endmodule

module Add4 (input [3:0] I0, input [3:0] I1, output [3:0] O);
wire  FullAdder_inst0_O;
wire  FullAdder_inst0_COUT;
wire  FullAdder_inst1_O;
wire  FullAdder_inst1_COUT;
wire  FullAdder_inst2_O;
wire  FullAdder_inst2_COUT;
wire  FullAdder_inst3_O;
wire  FullAdder_inst3_COUT;
FullAdder FullAdder_inst0 (.I0(I0[0]), .I1(I1[0]), .CIN(1'b0), .O(FullAdder_inst0_O), .COUT(FullAdder_inst0_COUT));
FullAdder FullAdder_inst1 (.I0(I0[1]), .I1(I1[1]), .CIN(FullAdder_inst0_COUT), .O(FullAdder_inst1_O), .COUT(FullAdder_inst1_COUT));
FullAdder FullAdder_inst2 (.I0(I0[2]), .I1(I1[2]), .CIN(FullAdder_inst1_COUT), .O(FullAdder_inst2_O), .COUT(FullAdder_inst2_COUT));
FullAdder FullAdder_inst3 (.I0(I0[3]), .I1(I1[3]), .CIN(FullAdder_inst2_COUT), .O(FullAdder_inst3_O), .COUT(FullAdder_inst3_COUT));
assign O = {FullAdder_inst3_O,FullAdder_inst2_O,FullAdder_inst1_O,FullAdder_inst0_O};
endmodule

module Register4 (input [3:0] I, output [3:0] O, input  CLK);
wire  SB_DFF_inst0_Q;
wire  SB_DFF_inst1_Q;
wire  SB_DFF_inst2_Q;
wire  SB_DFF_inst3_Q;
SB_DFF SB_DFF_inst0 (.C(CLK), .D(I[0]), .Q(SB_DFF_inst0_Q));
SB_DFF SB_DFF_inst1 (.C(CLK), .D(I[1]), .Q(SB_DFF_inst1_Q));
SB_DFF SB_DFF_inst2 (.C(CLK), .D(I[2]), .Q(SB_DFF_inst2_Q));
SB_DFF SB_DFF_inst3 (.C(CLK), .D(I[3]), .Q(SB_DFF_inst3_Q));
assign O = {SB_DFF_inst3_Q,SB_DFF_inst2_Q,SB_DFF_inst1_Q,SB_DFF_inst0_Q};
endmodule

module Counter4 (output [3:0] O, input  CLK);
wire [3:0] Add4_inst0_O;
wire [3:0] Register4_inst0_O;
Add4 Add4_inst0 (.I0(Register4_inst0_O), .I1({1'b0,1'b0,1'b0,1'b1}), .O(Add4_inst0_O));
Register4 Register4_inst0 (.I(Add4_inst0_O), .O(Register4_inst0_O), .CLK(CLK));
assign O = Register4_inst0_O;
endmodule

module Add1 (input [0:0] I0, input [0:0] I1, output [0:0] O);
wire  FullAdder_inst0_O;
wire  FullAdder_inst0_COUT;
FullAdder FullAdder_inst0 (.I0(I0[0]), .I1(I1[0]), .CIN(1'b0), .O(FullAdder_inst0_O), .COUT(FullAdder_inst0_COUT));
assign O = {FullAdder_inst0_O};
endmodule

module Register1 (input [0:0] I, output [0:0] O, input  CLK);
wire  SB_DFF_inst0_Q;
SB_DFF SB_DFF_inst0 (.C(CLK), .D(I[0]), .Q(SB_DFF_inst0_Q));
assign O = {SB_DFF_inst0_Q};
endmodule

module Counter1 (output [0:0] O, input  CLK);
wire [0:0] Add1_inst0_O;
wire [0:0] Register1_inst0_O;
Add1 Add1_inst0 (.I0(Register1_inst0_O), .I1({1'b1}), .O(Add1_inst0_O));
Register1 Register1_inst0 (.I(Add1_inst0_O), .O(Register1_inst0_O), .CLK(CLK));
assign O = Register1_inst0_O;
endmodule

module main (output  rdata, input  CLKIN);
wire [0:0] ram_RDATA;
wire [3:0] Counter4_inst0_O;
wire [0:0] Counter1_inst0_O;
wire [3:0] Counter4_inst1_O;
RAM16x1 ram (.RADDR(Counter4_inst1_O), .RDATA(ram_RDATA), .WADDR(Counter4_inst0_O), .WDATA(Counter1_inst0_O), .WE(1'b1), .CLK(CLKIN));
Counter4 Counter4_inst0 (.O(Counter4_inst0_O), .CLK(CLKIN));
Counter1 Counter1_inst0 (.O(Counter1_inst0_O), .CLK(CLKIN));
Counter4 Counter4_inst1 (.O(Counter4_inst1_O), .CLK(CLKIN));
assign rdata = ram_RDATA[0];
endmodule

