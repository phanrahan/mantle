module RAM16D_2 (input [3:0] A0, input [3:0] A1, output [1:0] O0, output [1:0] O1, input [1:0] I, input  WE, input  CLK);
wire  inst0_SPO;
wire  inst0_DPO;
wire  inst1_SPO;
wire  inst1_DPO;
RAM16X1D #(.INIT(16'h0000)) inst0 (.A0(A0[0]), .A1(A0[1]), .A2(A0[2]), .A3(A0[3]), .DPRA0(A1[0]), .DPRA1(A1[1]), .DPRA2(A1[2]), .DPRA3(A1[3]), .SPO(inst0_SPO), .DPO(inst0_DPO), .D(I[0]), .WE(WE), .WCLK(CLK));
RAM16X1D #(.INIT(16'h0000)) inst1 (.A0(A0[0]), .A1(A0[1]), .A2(A0[2]), .A3(A0[3]), .DPRA0(A1[0]), .DPRA1(A1[1]), .DPRA2(A1[2]), .DPRA3(A1[3]), .SPO(inst1_SPO), .DPO(inst1_DPO), .D(I[1]), .WE(WE), .WCLK(CLK));
assign O0 = {inst1_SPO,inst0_SPO};
assign O1 = {inst1_DPO,inst0_DPO};
endmodule

module main (output [3:0] LED, input  CLKIN, input [6:0] SWITCH);
wire [1:0] inst0_O0;
wire [1:0] inst0_O1;
RAM16D_2 inst0 (.A0({1'b0,1'b0,SWITCH[1],SWITCH[0]}), .A1({1'b0,1'b0,SWITCH[3],SWITCH[2]}), .O0(inst0_O0), .O1(inst0_O1), .I({SWITCH[5],SWITCH[4]}), .WE(SWITCH[6]), .CLK(CLKIN));
assign LED = {inst0_O1[1],inst0_O1[0],inst0_O0[1],inst0_O0[0]};
endmodule

