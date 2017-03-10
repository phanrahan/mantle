module Mux4 (input [3:0] I, input [1:0] S, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
LUT3 #(.INIT(8'hCA)) inst0 (.I0(I[0]), .I1(I[1]), .I2(S[0]), .O(inst0_O));
LUT3 #(.INIT(8'hCA)) inst1 (.I0(I[2]), .I1(I[3]), .I2(S[0]), .O(inst1_O));
MUXF5 inst2 (.I0(inst0_O), .I1(inst1_O), .S(S[1]), .O(inst2_O));
assign O = inst2_O;
endmodule

module Mux8 (input [7:0] I, input [2:0] S, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
Mux4 inst0 (.I({I[3],I[2],I[1],I[0]}), .S({S[1],S[0]}), .O(inst0_O));
Mux4 inst1 (.I({I[7],I[6],I[5],I[4]}), .S({S[1],S[0]}), .O(inst1_O));
MUXF6 inst2 (.I0(inst0_O), .I1(inst1_O), .S(S[2]), .O(inst2_O));
assign O = inst2_O;
endmodule

module Mux16 (input [15:0] I, input [3:0] S, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
Mux8 inst0 (.I({I[7],I[6],I[5],I[4],I[3],I[2],I[1],I[0]}), .S({S[2],S[1],S[0]}), .O(inst0_O));
Mux8 inst1 (.I({I[15],I[14],I[13],I[12],I[11],I[10],I[9],I[8]}), .S({S[2],S[1],S[0]}), .O(inst1_O));
MUXF6 inst2 (.I0(inst0_O), .I1(inst1_O), .S(S[3]), .O(inst2_O));
assign O = inst2_O;
endmodule

module main (output [0:0] LED, input [7:0] SWITCH);
wire  inst0_O;
Mux16 inst0 (.I({SWITCH[3],SWITCH[2],SWITCH[1],SWITCH[0],SWITCH[3],SWITCH[2],SWITCH[1],SWITCH[0],SWITCH[3],SWITCH[2],SWITCH[1],SWITCH[0],SWITCH[3],SWITCH[2],SWITCH[1],SWITCH[0]}), .S({SWITCH[7],SWITCH[6],SWITCH[5],SWITCH[4]}), .O(inst0_O));
assign LED = {inst0_O};
endmodule

