module Mux4 (input [3:0] I, input [1:0] S, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
SB_LUT4 #(.LUT_INIT(16'hCACA)) inst0 (.I0(I[0]), .I1(I[1]), .I2(S[0]), .I3(1'b0), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'hCACA)) inst1 (.I0(I[2]), .I1(I[3]), .I2(S[0]), .I3(1'b0), .O(inst1_O));
SB_LUT4 #(.LUT_INIT(16'hCACA)) inst2 (.I0(inst0_O), .I1(inst1_O), .I2(S[1]), .I3(1'b0), .O(inst2_O));
assign O = inst2_O;
endmodule

module main (input [5:0] J1, output  D1);
wire  inst0_O;
Mux4 inst0 (.I({J1[3],J1[2],J1[1],J1[0]}), .S({J1[5],J1[4]}), .O(inst0_O));
assign D1 = inst0_O;
endmodule

