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

module Mux2x2 (
    input [1:0] I0,
    input [1:0] I1,
    input S,
    output [1:0] O
);
reg [1:0] coreir_commonlib_mux2x2_inst0_out;
always @(*) begin
if (S == 0) begin
    coreir_commonlib_mux2x2_inst0_out = I0;
end else begin
    coreir_commonlib_mux2x2_inst0_out = I1;
end
end

assign O = coreir_commonlib_mux2x2_inst0_out;
endmodule

module DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse (
    input I,
    output O,
    input CLK
);
wire reg_P_inst0_clk;
wire [0:0] reg_P_inst0_in;
wire [0:0] reg_P_inst0_out;
assign reg_P_inst0_clk = CLK;
assign reg_P_inst0_in = I;
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

module Register2 (
    input [1:0] I,
    output [1:0] O,
    input CLK
);
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_I;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_CLK;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_I;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_CLK;
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_I = I[0];
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_CLK = CLK;
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0 (
    .I(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_I),
    .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O),
    .CLK(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_CLK)
);
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_I = I[1];
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_CLK = CLK;
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1 (
    .I(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_I),
    .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O),
    .CLK(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_CLK)
);
assign O = {DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O};
endmodule

module Add2_cout (
    input [1:0] I0,
    input [1:0] I1,
    output [1:0] O,
    output COUT
);
wire [2:0] coreir_add3_inst0_out;
assign coreir_add3_inst0_out = 3'(({1'b0,I0[1:0]}) + ({1'b0,I1[1:0]}));
assign O = coreir_add3_inst0_out[1:0];
assign COUT = coreir_add3_inst0_out[2];
endmodule

module CounterLoad2_COUT (
    input [1:0] DATA,
    input LOAD,
    output [1:0] O,
    output COUT,
    input CLK
);
wire [1:0] Add2_cout_inst0_I0;
wire [1:0] Add2_cout_inst0_I1;
wire [1:0] Add2_cout_inst0_O;
wire [1:0] Mux2x2_inst0_I0;
wire [1:0] Mux2x2_inst0_I1;
wire Mux2x2_inst0_S;
wire [1:0] Mux2x2_inst0_O;
wire [1:0] Register2_inst0_I;
wire Register2_inst0_CLK;
assign Add2_cout_inst0_I0 = O;
assign Add2_cout_inst0_I1 = 2'h1;
Add2_cout Add2_cout_inst0 (
    .I0(Add2_cout_inst0_I0),
    .I1(Add2_cout_inst0_I1),
    .O(Add2_cout_inst0_O),
    .COUT(COUT)
);
assign Mux2x2_inst0_I0 = Add2_cout_inst0_O;
assign Mux2x2_inst0_I1 = DATA;
assign Mux2x2_inst0_S = LOAD;
Mux2x2 Mux2x2_inst0 (
    .I0(Mux2x2_inst0_I0),
    .I1(Mux2x2_inst0_I1),
    .S(Mux2x2_inst0_S),
    .O(Mux2x2_inst0_O)
);
assign Register2_inst0_I = Mux2x2_inst0_O;
assign Register2_inst0_CLK = CLK;
Register2 Register2_inst0 (
    .I(Register2_inst0_I),
    .O(O),
    .CLK(Register2_inst0_CLK)
);
endmodule

