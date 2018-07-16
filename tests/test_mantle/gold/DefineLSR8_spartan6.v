module Mux2 (input [1:0] I, input  S, output  O);
wire  inst0_O;
LUT3 #(.INIT(8'hCA)) inst0 (.I0(I[0]), .I1(I[1]), .I2(S), .O(inst0_O));
assign O = inst0_O;
endmodule

module LSR8_1 (input [7:0] I, input  S, output [7:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
Mux2 inst0 (.I({I[1],I[0]}), .S(S), .O(inst0_O));
Mux2 inst1 (.I({I[2],I[1]}), .S(S), .O(inst1_O));
Mux2 inst2 (.I({I[3],I[2]}), .S(S), .O(inst2_O));
Mux2 inst3 (.I({I[4],I[3]}), .S(S), .O(inst3_O));
Mux2 inst4 (.I({I[5],I[4]}), .S(S), .O(inst4_O));
Mux2 inst5 (.I({I[6],I[5]}), .S(S), .O(inst5_O));
Mux2 inst6 (.I({I[7],I[6]}), .S(S), .O(inst6_O));
Mux2 inst7 (.I({1'b0,I[7]}), .S(S), .O(inst7_O));
assign O = {inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module LSR8_2 (input [7:0] I, input  S, output [7:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
Mux2 inst0 (.I({I[2],I[0]}), .S(S), .O(inst0_O));
Mux2 inst1 (.I({I[3],I[1]}), .S(S), .O(inst1_O));
Mux2 inst2 (.I({I[4],I[2]}), .S(S), .O(inst2_O));
Mux2 inst3 (.I({I[5],I[3]}), .S(S), .O(inst3_O));
Mux2 inst4 (.I({I[6],I[4]}), .S(S), .O(inst4_O));
Mux2 inst5 (.I({I[7],I[5]}), .S(S), .O(inst5_O));
Mux2 inst6 (.I({1'b0,I[6]}), .S(S), .O(inst6_O));
Mux2 inst7 (.I({1'b0,I[7]}), .S(S), .O(inst7_O));
assign O = {inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module LSR8_4 (input [7:0] I, input  S, output [7:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
Mux2 inst0 (.I({I[4],I[0]}), .S(S), .O(inst0_O));
Mux2 inst1 (.I({I[5],I[1]}), .S(S), .O(inst1_O));
Mux2 inst2 (.I({I[6],I[2]}), .S(S), .O(inst2_O));
Mux2 inst3 (.I({I[7],I[3]}), .S(S), .O(inst3_O));
Mux2 inst4 (.I({1'b0,I[4]}), .S(S), .O(inst4_O));
Mux2 inst5 (.I({1'b0,I[5]}), .S(S), .O(inst5_O));
Mux2 inst6 (.I({1'b0,I[6]}), .S(S), .O(inst6_O));
Mux2 inst7 (.I({1'b0,I[7]}), .S(S), .O(inst7_O));
assign O = {inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module LSR8 (input [7:0] I, input [2:0] S, output [7:0] O);
wire [7:0] inst0_O;
wire [7:0] inst1_O;
wire [7:0] inst2_O;
LSR8_1 inst0 (.I(I), .S(S[0]), .O(inst0_O));
LSR8_2 inst1 (.I(inst0_O), .S(S[1]), .O(inst1_O));
LSR8_4 inst2 (.I(inst1_O), .S(S[2]), .O(inst2_O));
assign O = inst2_O;
endmodule

