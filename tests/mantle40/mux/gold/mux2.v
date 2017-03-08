module main (input  I0, input  I1, input  S, output  D1);
wire  inst0_O;
SB_LUT4 #(.LUT_INIT(16'hCACA)) inst0 (.I0(I0), .I1(I1), .I2(S), .I3(1'b0), .O(inst0_O));
assign D1 = inst0_O;
endmodule

