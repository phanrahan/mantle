module Register1 (input [0:0] I, output [0:0] O, input  CLK);
wire  SB_DFF_inst0_Q;
SB_DFF SB_DFF_inst0 (.C(CLK), .D(I[0]), .Q(SB_DFF_inst0_Q));
assign O = {SB_DFF_inst0_Q};
endmodule

module EQNone (input  I0, input  I1, output  O);
wire  SB_LUT4_inst0_O;
SB_LUT4 #(.LUT_INIT(16'h9999)) SB_LUT4_inst0 (.I0(I0), .I1(I1), .I2(1'b0), .I3(1'b0), .O(SB_LUT4_inst0_O));
assign O = SB_LUT4_inst0_O;
endmodule

module Mux2 (input [1:0] I, input  S, output  O);
wire  SB_LUT4_inst0_O;
SB_LUT4 #(.LUT_INIT(16'hCACA)) SB_LUT4_inst0 (.I0(I[0]), .I1(I[1]), .I2(S), .I3(1'b0), .O(SB_LUT4_inst0_O));
assign O = SB_LUT4_inst0_O;
endmodule

module combinational_logic (input  a, output  O0);
wire  EQNone_inst0_O;
wire  Mux2_inst0_O;
EQNone EQNone_inst0 (.I0(a), .I1(1'b0), .O(EQNone_inst0_O));
Mux2 Mux2_inst0 (.I({1'b1,1'b0}), .S(EQNone_inst0_O), .O(Mux2_inst0_O));
assign O0 = Mux2_inst0_O;
endmodule

module main (output  LED);
wire [0:0] Register1_inst0_O;
wire  combinational_logic_inst0_O0;
Register1 Register1_inst0 (.I({combinational_logic_inst0_O0}), .O(Register1_inst0_O));
combinational_logic combinational_logic_inst0 (.a(Register1_inst0_O[0]), .O0(combinational_logic_inst0_O0));
assign LED = Register1_inst0_O[0];
endmodule

