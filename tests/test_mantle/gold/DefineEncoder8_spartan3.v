module Or4 (input [3:0] I, output  O);
wire  inst0_O;
LUT4 #(.INIT(16'h0001)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(I[3]), .O(inst0_O));
assign O = inst0_O;
endmodule

module Encoder8 (input [7:0] I, output [2:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
Or4 inst0 (.I({I[7],I[5],I[3],I[1]}), .O(inst0_O));
Or4 inst1 (.I({I[7],I[6],I[3],I[2]}), .O(inst1_O));
Or4 inst2 (.I({I[7],I[6],I[5],I[4]}), .O(inst2_O));
assign O = {inst2_O,inst1_O,inst0_O};
endmodule

