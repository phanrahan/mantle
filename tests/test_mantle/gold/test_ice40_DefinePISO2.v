module Mux2 (input [1:0] I, input  S, output  O);
wire  inst0_O;
SB_LUT4 #(.LUT_INIT(16'hCACA)) inst0 (.I0(I[0]), .I1(I[1]), .I2(S), .I3(1'b0), .O(inst0_O));
assign O = inst0_O;
endmodule

module Register2 (input [1:0] I, output [1:0] O, input  CLK);
wire  inst0_Q;
wire  inst1_Q;
SB_DFF inst0 (.C(CLK), .D(I[0]), .Q(inst0_Q));
SB_DFF inst1 (.C(CLK), .D(I[1]), .Q(inst1_Q));
assign O = {inst1_Q,inst0_Q};
endmodule

module PISO2 (input  SI, input [1:0] PI, input  LOAD, output  O, input  CLK);
wire  inst0_O;
wire  inst1_O;
wire [1:0] inst2_O;
Mux2 inst0 (.I({PI[0],SI}), .S(LOAD), .O(inst0_O));
Mux2 inst1 (.I({PI[1],inst2_O[0]}), .S(LOAD), .O(inst1_O));
Register2 inst2 (.I({inst1_O,inst0_O}), .O(inst2_O), .CLK(CLK));
assign O = inst2_O[1];
endmodule

