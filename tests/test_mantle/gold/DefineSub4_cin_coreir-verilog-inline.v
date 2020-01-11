module Add4_cin (input CIN, input [3:0] I0, input [3:0] I1, output [3:0] O);
assign O = (({1'b0,1'b0,1'b0,CIN}) + I0) + I1;
endmodule

module Sub4_cin (input CIN, input [3:0] I0, input [3:0] I1, output [3:0] O);
wire not_inst0_out;
Add4_cin Add4_cin_inst0(.CIN(not_inst0_out), .I0(I0), .I1(~ I1), .O(O));
corebit_not not_inst0(.in(CIN), .out(not_inst0_out));
endmodule

