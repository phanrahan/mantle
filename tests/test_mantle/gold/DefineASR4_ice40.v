module Mux2 (input [1:0] I, input  S, output  O);
wire  inst0_O;
SB_LUT4 #(.LUT_INIT(16'hCACA)) inst0 (.I0(I[0]), .I1(I[1]), .I2(S), .I3(1'b0), .O(inst0_O));
assign O = inst0_O;
endmodule

module ASR4_1 (input [3:0] I, input  S, output [3:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
Mux2 inst0 (.I({I[1],I[0]}), .S(S), .O(inst0_O));
Mux2 inst1 (.I({I[2],I[1]}), .S(S), .O(inst1_O));
Mux2 inst2 (.I({I[3],I[2]}), .S(S), .O(inst2_O));
Mux2 inst3 (.I({I[3],I[3]}), .S(S), .O(inst3_O));
assign O = {inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module ASR4_2 (input [3:0] I, input  S, output [3:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
Mux2 inst0 (.I({I[2],I[0]}), .S(S), .O(inst0_O));
Mux2 inst1 (.I({I[3],I[1]}), .S(S), .O(inst1_O));
Mux2 inst2 (.I({I[3],I[2]}), .S(S), .O(inst2_O));
Mux2 inst3 (.I({I[3],I[3]}), .S(S), .O(inst3_O));
assign O = {inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module ASR4 (input [3:0] I, input [1:0] S, output [3:0] O);
wire [3:0] inst0_O;
wire [3:0] inst1_O;
ASR4_1 inst0 (.I(I), .S(S[0]), .O(inst0_O));
ASR4_2 inst1 (.I(inst0_O), .S(S[1]), .O(inst1_O));
assign O = inst1_O;
endmodule

