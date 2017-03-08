module Mux4 (input [3:0] I, input [1:0] S, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
LUT3 #(.INIT(8'hCA)) inst0 (.I0(I[0]), .I1(I[1]), .I2(S[0]), .O(inst0_O));
LUT3 #(.INIT(8'hCA)) inst1 (.I0(I[2]), .I1(I[3]), .I2(S[0]), .O(inst1_O));
MUXF5 inst2 (.I0(inst0_O), .I1(inst1_O), .S(S[1]), .O(inst2_O));
assign O = inst2_O;
endmodule

module Mux4x2 (input [1:0] I0, input [1:0] I1, input [1:0] I2, input [1:0] I3, input [1:0] S, output [1:0] O);
wire  inst0_O;
wire  inst1_O;
Mux4 inst0 (.I({I3[0],I2[0],I1[0],I0[0]}), .S(S), .O(inst0_O));
Mux4 inst1 (.I({I3[1],I2[1],I1[1],I0[1]}), .S(S), .O(inst1_O));
assign O = {inst1_O,inst0_O};
endmodule

module main (output [1:0] LED, input [5:0] SWITCH);
wire [1:0] inst0_O;
Mux4x2 inst0 (.I0({SWITCH[0],SWITCH[0]}), .I1({SWITCH[1],SWITCH[1]}), .I2({SWITCH[2],SWITCH[2]}), .I3({SWITCH[3],SWITCH[3]}), .S({SWITCH[5],SWITCH[4]}), .O(inst0_O));
assign LED = inst0_O;
endmodule

