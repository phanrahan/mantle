module Add8_cin (input [7:0] I0, input [7:0] I1, output [7:0] O, input CIN);
assign O = (({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,CIN}) + I0) + I1;
endmodule

module Sub8_cin (input [7:0] I0, input [7:0] I1, output [7:0] O, input CIN);
Add8_cin Add8_cin_inst0(.I0(I0), .I1(~ I1), .O(O), .CIN(~ CIN));
endmodule

