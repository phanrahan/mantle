module HalfAdder (input  I0, input  I1, output  O, output  COUT);
wire  inst0_O;
wire  inst1_O;
LUT2 #(.INIT(4'h6)) inst0 (.I0(I0), .I1(I1), .O(inst0_O));
LUT2 #(.INIT(4'h8)) inst1 (.I0(I0), .I1(I1), .O(inst1_O));
assign O = inst0_O;
assign COUT = inst1_O;
endmodule

