module Add8_cin (input CIN, input [7:0] I0, input [7:0] I1, output [7:0] O);
assign O = (({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,CIN}) + I0) + I1;
endmodule

module Sub8_cin (input CIN, input [7:0] I0, input [7:0] I1, output [7:0] O);
wire not_inst0_out;
Add8_cin Add8_cin_inst0(.CIN(not_inst0_out), .I0(I0), .I1(~ I1), .O(O));
corebit_not not_inst0(.in(CIN), .out(not_inst0_out));
endmodule

