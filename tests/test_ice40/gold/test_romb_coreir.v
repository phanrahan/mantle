/* External Modules
module SB_RAM40_4K (
  input [15:0] MASK,
  input [10:0] RADDR,
  input  RCLK,
  input  RCLKE,
  output [15:0] RDATA,
  input  RE,
  input [10:0] WADDR,
  input  WCLK,
  input  WCLKE,
  input [15:0] WDATA,
  input  WE
);

endmodule  // SB_RAM40_4K

*/
module coreir_const #(parameter value=1, parameter width=1) (
  output [width-1:0] out
);
  assign out = value;

endmodule  // coreir_const

module corebit_const #(parameter value=1) (
  output out
);
  assign out = value;

endmodule  // corebit_const

module test_romb_coreir (
  input  CLK,
  output [15:0] RDATAOUT
);


  wire [15:0] SB_RAM40_4K_inst0__MASK;
  wire [10:0] SB_RAM40_4K_inst0__RADDR;
  wire  SB_RAM40_4K_inst0__RCLK;
  wire  SB_RAM40_4K_inst0__RCLKE;
  wire [15:0] SB_RAM40_4K_inst0__RDATA;
  wire  SB_RAM40_4K_inst0__RE;
  wire [10:0] SB_RAM40_4K_inst0__WADDR;
  wire  SB_RAM40_4K_inst0__WCLK;
  wire  SB_RAM40_4K_inst0__WCLKE;
  wire [15:0] SB_RAM40_4K_inst0__WDATA;
  wire  SB_RAM40_4K_inst0__WE;
  SB_RAM40_4K #(.INIT_0(256'h0000000000000000000000000000000000000000000000000000000000ff0001),.INIT_1(256'h0000000000000000000000000000000000000000000000000000000000000000),.INIT_2(256'h0000000000000000000000000000000000000000000000000000000000000000),.INIT_3(256'h0000000000000000000000000000000000000000000000000000000000000000),.INIT_4(256'h0000000000000000000000000000000000000000000000000000000000000000),.INIT_5(256'h0000000000000000000000000000000000000000000000000000000000000000),.INIT_6(256'h0000000000000000000000000000000000000000000000000000000000000000),.INIT_7(256'h0000000000000000000000000000000000000000000000000000000000000000),.INIT_8(256'h0000000000000000000000000000000000000000000000000000000000000000),.INIT_9(256'h0000000000000000000000000000000000000000000000000000000000000000),.INIT_A(256'h0000000000000000000000000000000000000000000000000000000000000000),.INIT_B(256'h0000000000000000000000000000000000000000000000000000000000000000),.INIT_C(256'h0000000000000000000000000000000000000000000000000000000000000000),.INIT_D(256'h0000000000000000000000000000000000000000000000000000000000000000),.INIT_E(256'h0000000000000000000000000000000000000000000000000000000000000000),.INIT_F(256'h0000000000000000000000000000000000000000000000000000000000000000),.READ_MODE(0),.WRITE_MODE(0)) SB_RAM40_4K_inst0(
    .MASK(SB_RAM40_4K_inst0__MASK),
    .RADDR(SB_RAM40_4K_inst0__RADDR),
    .RCLK(SB_RAM40_4K_inst0__RCLK),
    .RCLKE(SB_RAM40_4K_inst0__RCLKE),
    .RDATA(SB_RAM40_4K_inst0__RDATA),
    .RE(SB_RAM40_4K_inst0__RE),
    .WADDR(SB_RAM40_4K_inst0__WADDR),
    .WCLK(SB_RAM40_4K_inst0__WCLK),
    .WCLKE(SB_RAM40_4K_inst0__WCLKE),
    .WDATA(SB_RAM40_4K_inst0__WDATA),
    .WE(SB_RAM40_4K_inst0__WE)
  );

  wire  bit_const_0_None__out;
  corebit_const #(.value(0)) bit_const_0_None(
    .out(bit_const_0_None__out)
  );

  wire  bit_const_1_None__out;
  corebit_const #(.value(1)) bit_const_1_None(
    .out(bit_const_1_None__out)
  );

  // Instancing generated Module: coreir.const(width:11)
  wire [10:0] const_0_11__out;
  coreir_const #(.value(11'h000),.width(11)) const_0_11(
    .out(const_0_11__out)
  );

  // Instancing generated Module: coreir.const(width:16)
  wire [15:0] const_0_16__out;
  coreir_const #(.value(16'h0000),.width(16)) const_0_16(
    .out(const_0_16__out)
  );

  // Instancing generated Module: coreir.const(width:11)
  wire [10:0] const_1_11__out;
  coreir_const #(.value(11'h001),.width(11)) const_1_11(
    .out(const_1_11__out)
  );

  assign SB_RAM40_4K_inst0__MASK[15:0] = const_0_16__out[15:0];

  assign SB_RAM40_4K_inst0__RADDR[10:0] = const_1_11__out[10:0];

  assign SB_RAM40_4K_inst0__RCLK = CLK;

  assign SB_RAM40_4K_inst0__RCLKE = bit_const_1_None__out;

  assign RDATAOUT[15:0] = SB_RAM40_4K_inst0__RDATA[15:0];

  assign SB_RAM40_4K_inst0__RE = bit_const_1_None__out;

  assign SB_RAM40_4K_inst0__WADDR[10:0] = const_0_11__out[10:0];

  assign SB_RAM40_4K_inst0__WCLK = CLK;

  assign SB_RAM40_4K_inst0__WCLKE = bit_const_0_None__out;

  assign SB_RAM40_4K_inst0__WDATA[15:0] = const_0_16__out[15:0];

  assign SB_RAM40_4K_inst0__WE = bit_const_0_None__out;


endmodule  // test_romb_coreir

