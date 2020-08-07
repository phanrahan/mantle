module mantle_wire__typeBitIn5 (
    output [4:0] in,
    input [4:0] out
);
assign in = out;
endmodule

module mantle_wire__typeBit5 (
    input [4:0] in,
    output [4:0] out
);
assign out = in;
endmodule

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
    input CLK,
    input I_X,
    input [4:0] I_Y,
    output O_X,
    output [4:0] O_Y
);
wire [4:0] _$_U1_in;
wire [4:0] _$_U1_out;
wire [4:0] _$_U2_in;
wire [4:0] _$_U2_out;
wire reg_P_inst0_clk;
wire [5:0] reg_P_inst0_in;
wire [5:0] reg_P_inst0_out;
assign _$_U1_in = I_Y;
mantle_wire__typeBit5 _$_U1 (
    .in(_$_U1_in),
    .out(_$_U1_out)
);
assign _$_U2_out = reg_P_inst0_out[5:1];
mantle_wire__typeBitIn5 _$_U2 (
    .in(_$_U2_in),
    .out(_$_U2_out)
);
assign reg_P_inst0_clk = CLK;
assign reg_P_inst0_in = {_$_U1_out[4:0],I_X};
coreir_reg #(
    .clk_posedge(1'b1),
    .init(6'h00),
    .width(6)
) reg_P_inst0 (
    .clk(reg_P_inst0_clk),
    .in(reg_P_inst0_in),
    .out(reg_P_inst0_out)
);
assign O_X = reg_P_inst0_out[0];
assign O_Y = _$_U2_in;
endmodule

module SIPO5 (
    input CLK,
    input I_X,
    input [4:0] I_Y,
    output O_0_X,
    output [4:0] O_0_Y,
    output O_1_X,
    output [4:0] O_1_Y,
    output O_2_X,
    output [4:0] O_2_Y,
    output O_3_X,
    output [4:0] O_3_Y,
    output O_4_X,
    output [4:0] O_4_Y
);
wire Register_inst0_CLK;
wire Register_inst0_I_X;
wire [4:0] Register_inst0_I_Y;
wire Register_inst0_O_X;
wire [4:0] Register_inst0_O_Y;
wire Register_inst1_CLK;
wire Register_inst1_I_X;
wire [4:0] Register_inst1_I_Y;
wire Register_inst1_O_X;
wire [4:0] Register_inst1_O_Y;
wire Register_inst2_CLK;
wire Register_inst2_I_X;
wire [4:0] Register_inst2_I_Y;
wire Register_inst2_O_X;
wire [4:0] Register_inst2_O_Y;
wire Register_inst3_CLK;
wire Register_inst3_I_X;
wire [4:0] Register_inst3_I_Y;
wire Register_inst3_O_X;
wire [4:0] Register_inst3_O_Y;
wire Register_inst4_CLK;
wire Register_inst4_I_X;
wire [4:0] Register_inst4_I_Y;
wire Register_inst4_O_X;
wire [4:0] Register_inst4_O_Y;
assign Register_inst0_CLK = CLK;
assign Register_inst0_I_X = I_X;
assign Register_inst0_I_Y = I_Y;
Register Register_inst0 (
    .CLK(Register_inst0_CLK),
    .I_X(Register_inst0_I_X),
    .I_Y(Register_inst0_I_Y),
    .O_X(Register_inst0_O_X),
    .O_Y(Register_inst0_O_Y)
);
assign Register_inst1_CLK = CLK;
assign Register_inst1_I_X = Register_inst0_O_X;
assign Register_inst1_I_Y = Register_inst0_O_Y;
Register Register_inst1 (
    .CLK(Register_inst1_CLK),
    .I_X(Register_inst1_I_X),
    .I_Y(Register_inst1_I_Y),
    .O_X(Register_inst1_O_X),
    .O_Y(Register_inst1_O_Y)
);
assign Register_inst2_CLK = CLK;
assign Register_inst2_I_X = Register_inst1_O_X;
assign Register_inst2_I_Y = Register_inst1_O_Y;
Register Register_inst2 (
    .CLK(Register_inst2_CLK),
    .I_X(Register_inst2_I_X),
    .I_Y(Register_inst2_I_Y),
    .O_X(Register_inst2_O_X),
    .O_Y(Register_inst2_O_Y)
);
assign Register_inst3_CLK = CLK;
assign Register_inst3_I_X = Register_inst2_O_X;
assign Register_inst3_I_Y = Register_inst2_O_Y;
Register Register_inst3 (
    .CLK(Register_inst3_CLK),
    .I_X(Register_inst3_I_X),
    .I_Y(Register_inst3_I_Y),
    .O_X(Register_inst3_O_X),
    .O_Y(Register_inst3_O_Y)
);
assign Register_inst4_CLK = CLK;
assign Register_inst4_I_X = Register_inst3_O_X;
assign Register_inst4_I_Y = Register_inst3_O_Y;
Register Register_inst4 (
    .CLK(Register_inst4_CLK),
    .I_X(Register_inst4_I_X),
    .I_Y(Register_inst4_I_Y),
    .O_X(Register_inst4_O_X),
    .O_Y(Register_inst4_O_Y)
);
assign O_0_X = Register_inst0_O_X;
assign O_0_Y = Register_inst0_O_Y;
assign O_1_X = Register_inst1_O_X;
assign O_1_Y = Register_inst1_O_Y;
assign O_2_X = Register_inst2_O_X;
assign O_2_Y = Register_inst2_O_Y;
assign O_3_X = Register_inst3_O_X;
assign O_3_Y = Register_inst3_O_Y;
assign O_4_X = Register_inst4_O_X;
assign O_4_Y = Register_inst4_O_Y;
endmodule

module test_sipo_product (
    input CLK,
    input I_X,
    input [4:0] I_Y,
    output O_0_X,
    output [4:0] O_0_Y,
    output O_1_X,
    output [4:0] O_1_Y,
    output O_2_X,
    output [4:0] O_2_Y,
    output O_3_X,
    output [4:0] O_3_Y,
    output O_4_X,
    output [4:0] O_4_Y
);
wire SIPO5_inst0_CLK;
wire SIPO5_inst0_I_X;
wire [4:0] SIPO5_inst0_I_Y;
wire SIPO5_inst0_O_0_X;
wire [4:0] SIPO5_inst0_O_0_Y;
wire SIPO5_inst0_O_1_X;
wire [4:0] SIPO5_inst0_O_1_Y;
wire SIPO5_inst0_O_2_X;
wire [4:0] SIPO5_inst0_O_2_Y;
wire SIPO5_inst0_O_3_X;
wire [4:0] SIPO5_inst0_O_3_Y;
wire SIPO5_inst0_O_4_X;
wire [4:0] SIPO5_inst0_O_4_Y;
assign SIPO5_inst0_CLK = CLK;
assign SIPO5_inst0_I_X = I_X;
assign SIPO5_inst0_I_Y = I_Y;
SIPO5 SIPO5_inst0 (
    .CLK(SIPO5_inst0_CLK),
    .I_X(SIPO5_inst0_I_X),
    .I_Y(SIPO5_inst0_I_Y),
    .O_0_X(SIPO5_inst0_O_0_X),
    .O_0_Y(SIPO5_inst0_O_0_Y),
    .O_1_X(SIPO5_inst0_O_1_X),
    .O_1_Y(SIPO5_inst0_O_1_Y),
    .O_2_X(SIPO5_inst0_O_2_X),
    .O_2_Y(SIPO5_inst0_O_2_Y),
    .O_3_X(SIPO5_inst0_O_3_X),
    .O_3_Y(SIPO5_inst0_O_3_Y),
    .O_4_X(SIPO5_inst0_O_4_X),
    .O_4_Y(SIPO5_inst0_O_4_Y)
);
assign O_0_X = SIPO5_inst0_O_0_X;
assign O_0_Y = SIPO5_inst0_O_0_Y;
assign O_1_X = SIPO5_inst0_O_1_X;
assign O_1_Y = SIPO5_inst0_O_1_Y;
assign O_2_X = SIPO5_inst0_O_2_X;
assign O_2_Y = SIPO5_inst0_O_2_Y;
assign O_3_X = SIPO5_inst0_O_3_X;
assign O_3_Y = SIPO5_inst0_O_3_Y;
assign O_4_X = SIPO5_inst0_O_4_X;
assign O_4_Y = SIPO5_inst0_O_4_Y;
endmodule

