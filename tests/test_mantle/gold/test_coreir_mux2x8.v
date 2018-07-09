module _Mux2 (input [1:0] I, input  S, output  O);
wire  inst0_out;
coreir_bitmux inst0 (.in0(I[0]), .in1(I[1]), .sel(S), .out(inst0_out));
assign O = inst0_out;
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
_Mux2 inst0 (.I({I1[0],I0[0]}), .S(S), .O(inst0_O));
_Mux2 inst1 (.I({I1[1],I0[1]}), .S(S), .O(inst1_O));
_Mux2 inst2 (.I({I1[2],I0[2]}), .S(S), .O(inst2_O));
_Mux2 inst3 (.I({I1[3],I0[3]}), .S(S), .O(inst3_O));
_Mux2 inst4 (.I({I1[4],I0[4]}), .S(S), .O(inst4_O));
_Mux2 inst5 (.I({I1[5],I0[5]}), .S(S), .O(inst5_O));
_Mux2 inst6 (.I({I1[6],I0[6]}), .S(S), .O(inst6_O));
_Mux2 inst7 (.I({I1[7],I0[7]}), .S(S), .O(inst7_O));
assign O = {inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

