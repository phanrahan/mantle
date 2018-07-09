module Add4 (input [3:0] I0, input [3:0] I1, output [3:0] O);
wire [3:0] inst0_out;
coreir_add4 inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

module TestsCircuit_add_4_Bits_BitsType (input [3:0] I0, input [3:0] I1, output [3:0] O0, output [3:0] O1);
wire [3:0] inst0_O;
Add4 inst0 (.I0(I0), .I1(I1), .O(inst0_O));
assign O0 = inst0_O;
assign O1 = {1'b0,1'b0,1'b0,1'b0};
endmodule

