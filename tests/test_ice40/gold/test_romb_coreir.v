// Module `SB_RAM40_4K` defined externally
module coreir_const #(parameter width = 1, parameter value = 1) (output [width-1:0] out);
  assign out = value;
endmodule

module corebit_const #(parameter value = 1) (output out);
  assign out = value;
endmodule

module test_romb_coreir (input CLK, output [15:0] RDATAOUT);
wire [15:0] SB_RAM40_4K_inst0_RDATA;
wire bit_const_0_None_out;
wire bit_const_1_None_out;
wire [10:0] const_0_11_out;
wire [15:0] const_0_16_out;
wire [10:0] const_1_11_out;
SB_RAM40_4K #(.INIT_0(256'h0000000000000000000000000000000000000000000000000000000000ff0001), .INIT_1(256'h0000000000000000000000000000000000000000000000000000000000000000), .INIT_2(256'h0000000000000000000000000000000000000000000000000000000000000000), .INIT_3(256'h0000000000000000000000000000000000000000000000000000000000000000), .INIT_4(256'h0000000000000000000000000000000000000000000000000000000000000000), .INIT_5(256'h0000000000000000000000000000000000000000000000000000000000000000), .INIT_6(256'h0000000000000000000000000000000000000000000000000000000000000000), .INIT_7(256'h0000000000000000000000000000000000000000000000000000000000000000), .INIT_8(256'h0000000000000000000000000000000000000000000000000000000000000000), .INIT_9(256'h0000000000000000000000000000000000000000000000000000000000000000), .INIT_A(256'h0000000000000000000000000000000000000000000000000000000000000000), .INIT_B(256'h0000000000000000000000000000000000000000000000000000000000000000), .INIT_C(256'h0000000000000000000000000000000000000000000000000000000000000000), .INIT_D(256'h0000000000000000000000000000000000000000000000000000000000000000), .INIT_E(256'h0000000000000000000000000000000000000000000000000000000000000000), .INIT_F(256'h0000000000000000000000000000000000000000000000000000000000000000), .READ_MODE(0), .WRITE_MODE(0)) SB_RAM40_4K_inst0(.MASK(const_0_16_out), .RADDR(const_1_11_out), .RCLK(CLK), .RCLKE(bit_const_1_None_out), .RDATA(SB_RAM40_4K_inst0_RDATA), .RE(bit_const_1_None_out), .WADDR(const_0_11_out), .WCLK(CLK), .WCLKE(bit_const_0_None_out), .WDATA(const_0_16_out), .WE(bit_const_0_None_out));
corebit_const #(.value(0)) bit_const_0_None(.out(bit_const_0_None_out));
corebit_const #(.value(1)) bit_const_1_None(.out(bit_const_1_None_out));
coreir_const #(.value(11'h000), .width(11)) const_0_11(.out(const_0_11_out));
coreir_const #(.value(16'h0000), .width(16)) const_0_16(.out(const_0_16_out));
coreir_const #(.value(11'h001), .width(11)) const_1_11(.out(const_1_11_out));
assign RDATAOUT = SB_RAM40_4K_inst0_RDATA;
endmodule

