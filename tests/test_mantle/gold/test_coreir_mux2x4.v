module _Mux2 (input [1:0] I, input  S, output  O);
wire  inst0_out;
coreir_bitmux inst0 (.in0(I[0]), .in1(I[1]), .sel(S), .out(inst0_out));
assign O = inst0_out;
endmodule

module Mux2x4 (input [3:0] I0, input [3:0] I1, input  S, output [3:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
_Mux2 inst0 (.I({I1[0],I0[0]}), .S(S), .O(inst0_O));
_Mux2 inst1 (.I({I1[1],I0[1]}), .S(S), .O(inst1_O));
_Mux2 inst2 (.I({I1[2],I0[2]}), .S(S), .O(inst2_O));
_Mux2 inst3 (.I({I1[3],I0[3]}), .S(S), .O(inst3_O));
assign O = {inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

