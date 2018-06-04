module NE2 (input [1:0] I0, input [1:0] I1, output  O);
wire  inst0_O;
wire  inst1_O;
LUT3 #(.INIT(8'hBE)) inst0 (.I0(1'b0), .I1(I0[0]), .I2(I1[0]), .O(inst0_O));
LUT3 #(.INIT(8'hBE)) inst1 (.I0(inst0_O), .I1(I0[1]), .I2(I1[1]), .O(inst1_O));
assign O = inst1_O;
endmodule

