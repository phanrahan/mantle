module Mux2 (input [1:0] I, input  S, output  O);
wire  LUT3_inst0_O;
LUT3 #(.INIT(8'hCA)) LUT3_inst0 (.I0(I[0]), .I1(I[1]), .I2(S), .O(LUT3_inst0_O));
assign O = LUT3_inst0_O;
endmodule

module ASR4_1 (input [3:0] I, input  S, output [3:0] O);
wire  Mux2_inst0_O;
wire  Mux2_inst1_O;
wire  Mux2_inst2_O;
wire  Mux2_inst3_O;
Mux2 Mux2_inst0 (.I({I[1],I[0]}), .S(S), .O(Mux2_inst0_O));
Mux2 Mux2_inst1 (.I({I[2],I[1]}), .S(S), .O(Mux2_inst1_O));
Mux2 Mux2_inst2 (.I({I[3],I[2]}), .S(S), .O(Mux2_inst2_O));
Mux2 Mux2_inst3 (.I({I[3],I[3]}), .S(S), .O(Mux2_inst3_O));
assign O = {Mux2_inst3_O,Mux2_inst2_O,Mux2_inst1_O,Mux2_inst0_O};
endmodule

module ASR4_2 (input [3:0] I, input  S, output [3:0] O);
wire  Mux2_inst0_O;
wire  Mux2_inst1_O;
wire  Mux2_inst2_O;
wire  Mux2_inst3_O;
Mux2 Mux2_inst0 (.I({I[2],I[0]}), .S(S), .O(Mux2_inst0_O));
Mux2 Mux2_inst1 (.I({I[3],I[1]}), .S(S), .O(Mux2_inst1_O));
Mux2 Mux2_inst2 (.I({I[3],I[2]}), .S(S), .O(Mux2_inst2_O));
Mux2 Mux2_inst3 (.I({I[3],I[3]}), .S(S), .O(Mux2_inst3_O));
assign O = {Mux2_inst3_O,Mux2_inst2_O,Mux2_inst1_O,Mux2_inst0_O};
endmodule

module ASR4 (input [3:0] I, input [1:0] S, output [3:0] O);
wire [3:0] ASR4_1_inst0_O;
wire [3:0] ASR4_2_inst0_O;
ASR4_1 ASR4_1_inst0 (.I(I), .S(S[0]), .O(ASR4_1_inst0_O));
ASR4_2 ASR4_2_inst0 (.I(ASR4_1_inst0_O), .S(S[1]), .O(ASR4_2_inst0_O));
assign O = ASR4_2_inst0_O;
endmodule

