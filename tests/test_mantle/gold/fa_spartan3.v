module FullAdder (input  I0, input  I1, input  I2, output  O, output  COUT);
wire  inst0_O;
wire  inst1_O;
LUT3 #(.INIT(8'h96)) inst0 (.I0(I0), .I1(I1), .I2(I2), .O(inst0_O));
LUT3 #(.INIT(8'hE8)) inst1 (.I0(I0), .I1(I1), .I2(I2), .O(inst1_O));
assign O = inst0_O;
assign COUT = inst1_O;
endmodule

