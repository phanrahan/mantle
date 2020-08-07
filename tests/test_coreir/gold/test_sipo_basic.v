module coreir_reg #(
    parameter width = 1,
    parameter clk_posedge = 1,
    parameter init = 1
) (
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
endmodule

module Register (
    input I,
    output O,
    input CLK
);
wire reg_P_inst0_clk;
wire [0:0] reg_P_inst0_in;
wire [0:0] reg_P_inst0_out;
assign reg_P_inst0_clk = CLK;
assign reg_P_inst0_in[0] = I;
coreir_reg #(
    .clk_posedge(1'b1),
    .init(1'h0),
    .width(1)
) reg_P_inst0 (
    .clk(reg_P_inst0_clk),
    .in(reg_P_inst0_in),
    .out(reg_P_inst0_out)
);
assign O = reg_P_inst0_out[0];
endmodule

module SIPO5 (
    input I,
    output [4:0] O,
    input CLK
);
wire Register_inst0_I;
wire Register_inst0_O;
wire Register_inst0_CLK;
wire Register_inst1_I;
wire Register_inst1_O;
wire Register_inst1_CLK;
wire Register_inst2_I;
wire Register_inst2_O;
wire Register_inst2_CLK;
wire Register_inst3_I;
wire Register_inst3_O;
wire Register_inst3_CLK;
wire Register_inst4_I;
wire Register_inst4_O;
wire Register_inst4_CLK;
assign Register_inst0_I = I;
assign Register_inst0_CLK = CLK;
Register Register_inst0 (
    .I(Register_inst0_I),
    .O(Register_inst0_O),
    .CLK(Register_inst0_CLK)
);
assign Register_inst1_I = Register_inst0_O;
assign Register_inst1_CLK = CLK;
Register Register_inst1 (
    .I(Register_inst1_I),
    .O(Register_inst1_O),
    .CLK(Register_inst1_CLK)
);
assign Register_inst2_I = Register_inst1_O;
assign Register_inst2_CLK = CLK;
Register Register_inst2 (
    .I(Register_inst2_I),
    .O(Register_inst2_O),
    .CLK(Register_inst2_CLK)
);
assign Register_inst3_I = Register_inst2_O;
assign Register_inst3_CLK = CLK;
Register Register_inst3 (
    .I(Register_inst3_I),
    .O(Register_inst3_O),
    .CLK(Register_inst3_CLK)
);
assign Register_inst4_I = Register_inst3_O;
assign Register_inst4_CLK = CLK;
Register Register_inst4 (
    .I(Register_inst4_I),
    .O(Register_inst4_O),
    .CLK(Register_inst4_CLK)
);
assign O = {Register_inst4_O,Register_inst3_O,Register_inst2_O,Register_inst1_O,Register_inst0_O};
endmodule

module test_sipo_basic (
    input I,
    output [4:0] O,
    input CLK
);
wire SIPO5_inst0_I;
wire [4:0] SIPO5_inst0_O;
wire SIPO5_inst0_CLK;
assign SIPO5_inst0_I = I;
assign SIPO5_inst0_CLK = CLK;
SIPO5 SIPO5_inst0 (
    .I(SIPO5_inst0_I),
    .O(SIPO5_inst0_O),
    .CLK(SIPO5_inst0_CLK)
);
assign O = SIPO5_inst0_O;
endmodule

