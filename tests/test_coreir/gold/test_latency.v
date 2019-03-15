module coreir_reg #(parameter clk_posedge=1, parameter init=1, parameter width=1) (
  input clk,
  input [width-1:0] in,
  output [width-1:0] out
);
  reg [width-1:0] outReg=init;
  wire real_clk;
  assign real_clk = clk_posedge ? clk : ~clk;
  always @(posedge real_clk) begin
    outReg <= in;
  end
  assign out = outReg;

endmodule  // coreir_reg

module coreir_mem #(parameter depth=1, parameter has_init=0, parameter width=1) (
  input clk,
  input [width-1:0] wdata,
  input [$clog2(depth)-1:0] waddr,
  input wen,
  output [width-1:0] rdata,
  input [$clog2(depth)-1:0] raddr
);
  reg [width-1:0] data[depth-1:0];
  always @(posedge clk) begin
    if (wen) begin
      data[waddr] <= wdata;
    end
  end
  assign rdata = data[raddr];

endmodule  // coreir_mem

module RAM256x16 (
  input  CLK,
  input [7:0] RADDR,
  output [15:0] RDATA,
  input [7:0] WADDR,
  input [15:0] WDATA,
  input  WE
);


  // Instancing generated Module: coreir.mem(depth:256, has_init:False, width:16)
  wire  coreir_mem256x16_inst0__clk;
  wire [7:0] coreir_mem256x16_inst0__raddr;
  wire [15:0] coreir_mem256x16_inst0__rdata;
  wire [7:0] coreir_mem256x16_inst0__waddr;
  wire [15:0] coreir_mem256x16_inst0__wdata;
  wire  coreir_mem256x16_inst0__wen;
  coreir_mem #(.depth(256),.has_init(0),.width(16)) coreir_mem256x16_inst0(
    .clk(coreir_mem256x16_inst0__clk),
    .raddr(coreir_mem256x16_inst0__raddr),
    .rdata(coreir_mem256x16_inst0__rdata),
    .waddr(coreir_mem256x16_inst0__waddr),
    .wdata(coreir_mem256x16_inst0__wdata),
    .wen(coreir_mem256x16_inst0__wen)
  );

  // Instancing generated Module: coreir.reg(width:16)
  wire  reg_P_inst0__clk;
  wire [15:0] reg_P_inst0__in;
  wire [15:0] reg_P_inst0__out;
  coreir_reg #(.clk_posedge(1),.init(16'h0000),.width(16)) reg_P_inst0(
    .clk(reg_P_inst0__clk),
    .in(reg_P_inst0__in),
    .out(reg_P_inst0__out)
  );

  assign coreir_mem256x16_inst0__clk = CLK;

  assign coreir_mem256x16_inst0__raddr[7:0] = RADDR[7:0];

  assign reg_P_inst0__in[15:0] = coreir_mem256x16_inst0__rdata[15:0];

  assign coreir_mem256x16_inst0__waddr[7:0] = WADDR[7:0];

  assign coreir_mem256x16_inst0__wdata[15:0] = WDATA[15:0];

  assign coreir_mem256x16_inst0__wen = WE;

  assign reg_P_inst0__clk = CLK;

  assign RDATA[15:0] = reg_P_inst0__out[15:0];


endmodule  // RAM256x16

