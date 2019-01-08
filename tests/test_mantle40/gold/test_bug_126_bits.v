module Register2 (input [1:0] I, output [1:0] O, input  CLK);
wire  SB_DFF_inst0_Q;
wire  SB_DFF_inst1_Q;
SB_DFF SB_DFF_inst0 (.C(CLK), .D(I[0]), .Q(SB_DFF_inst0_Q));
SB_DFF SB_DFF_inst1 (.C(CLK), .D(I[1]), .Q(SB_DFF_inst1_Q));
assign O = {SB_DFF_inst1_Q,SB_DFF_inst0_Q};
endmodule

module EQ2 (input [1:0] I0, input [1:0] I1, output  O);
wire  SB_LUT4_inst0_O;
SB_LUT4 #(.LUT_INIT(16'h9009)) SB_LUT4_inst0 (.I0(I0[0]), .I1(I1[0]), .I2(I0[1]), .I3(I1[1]), .O(SB_LUT4_inst0_O));
assign O = SB_LUT4_inst0_O;
endmodule

module Mux2 (input [1:0] I, input  S, output  O);
wire  SB_LUT4_inst0_O;
SB_LUT4 #(.LUT_INIT(16'hCACA)) SB_LUT4_inst0 (.I0(I[0]), .I1(I[1]), .I2(S), .I3(1'b0), .O(SB_LUT4_inst0_O));
assign O = SB_LUT4_inst0_O;
endmodule

module Mux2x2 (input [1:0] I0, input [1:0] I1, input  S, output [1:0] O);
wire  Mux2_inst0_O;
wire  Mux2_inst1_O;
Mux2 Mux2_inst0 (.I({I1[0],I0[0]}), .S(S), .O(Mux2_inst0_O));
Mux2 Mux2_inst1 (.I({I1[1],I0[1]}), .S(S), .O(Mux2_inst1_O));
assign O = {Mux2_inst1_O,Mux2_inst0_O};
endmodule

module combinational_logic (input [1:0] a, output [1:0] O0);
wire  EQ2_inst0_O;
wire [1:0] Mux2x2_inst0_O;
EQ2 EQ2_inst0 (.I0(a), .I1({1'b0,1'b0}), .O(EQ2_inst0_O));
Mux2x2 Mux2x2_inst0 (.I0({1'b0,1'b0}), .I1({1'b0,1'b1}), .S(EQ2_inst0_O), .O(Mux2x2_inst0_O));
assign O0 = Mux2x2_inst0_O;
endmodule

module main (output  LED);
wire [1:0] Register2_inst0_O;
wire [1:0] combinational_logic_inst0_O0;
Register2 Register2_inst0 (.I(combinational_logic_inst0_O0), .O(Register2_inst0_O));
combinational_logic combinational_logic_inst0 (.a(Register2_inst0_O), .O0(combinational_logic_inst0_O0));
assign LED = Register2_inst0_O[0];
endmodule

