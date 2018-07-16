module or_wrapped (input  I0, input  I1, output  O);
wire  inst0_out;
coreir_or inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

module Encoder4 (input [3:0] I, output [1:0] O);
wire  inst0_O;
wire  inst1_O;
or_wrapped inst0 (.I0(I[1]), .I1(I[3]), .O(inst0_O));
or_wrapped inst1 (.I0(I[2]), .I1(I[3]), .O(inst1_O));
assign O = {inst1_O,inst0_O};
endmodule

