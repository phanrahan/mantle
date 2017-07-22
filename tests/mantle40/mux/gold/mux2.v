module Mux2 (input [1:0] I, input  S, output  O);
wire  inst0_O;
SB_LUT4 #(.LUT_INIT(16'hCACA)) inst0 (.I0(I[0]), .I1(I[1]), .I2(S), .I3(1'b0), .O(inst0_O));
assign O = inst0_O;
endmodule

module main (input  I0, input  I1, input  S, output  D1);
wire  inst0_O;
Mux2 inst0 (.I({I1,I0}), .S(S), .O(inst0_O));
assign D1 = inst0_O;
endmodule

