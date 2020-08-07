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

module Mux2x4 (
    input [3:0] I0,
    input [3:0] I1,
    input S,
    output [3:0] O
);
reg [3:0] coreir_commonlib_mux2x4_inst0_out;
always @(*) begin
if (S == 0) begin
    coreir_commonlib_mux2x4_inst0_out = I0;
end else begin
    coreir_commonlib_mux2x4_inst0_out = I1;
end
end

assign O = coreir_commonlib_mux2x4_inst0_out;
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

module Register4 (
    input [3:0] I,
    output [3:0] O,
    input CLK
);
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_I;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_CLK;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_I;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_CLK;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_I;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_CLK;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_I;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_CLK;
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
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_I = I[2];
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_CLK = CLK;
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2 (
    .I(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_I),
    .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_O),
    .CLK(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_CLK)
);
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_I = I[3];
assign DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_CLK = CLK;
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3 (
    .I(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_I),
    .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_O),
    .CLK(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_CLK)
);
assign O = {DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O,DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O};
endmodule

module Add4_cout (
    input [3:0] I0,
    input [3:0] I1,
    output [3:0] O,
    output COUT
);
wire [4:0] coreir_add5_inst0_out;
assign coreir_add5_inst0_out = 5'(({1'b0,I0[3:0]}) + ({1'b0,I1[3:0]}));
assign O = coreir_add5_inst0_out[3:0];
assign COUT = coreir_add5_inst0_out[4];
endmodule

module CounterLoad4_COUT (
    input [3:0] DATA,
    input LOAD,
    output [3:0] O,
    output COUT,
    input CLK
);
wire [3:0] Add4_cout_inst0_I0;
wire [3:0] Add4_cout_inst0_I1;
wire [3:0] Add4_cout_inst0_O;
wire [3:0] Mux2x4_inst0_I0;
wire [3:0] Mux2x4_inst0_I1;
wire Mux2x4_inst0_S;
wire [3:0] Mux2x4_inst0_O;
wire [3:0] Register4_inst0_I;
wire Register4_inst0_CLK;
assign Add4_cout_inst0_I0 = O;
assign Add4_cout_inst0_I1 = 4'h1;
Add4_cout Add4_cout_inst0 (
    .I0(Add4_cout_inst0_I0),
    .I1(Add4_cout_inst0_I1),
    .O(Add4_cout_inst0_O),
    .COUT(COUT)
);
assign Mux2x4_inst0_I0 = Add4_cout_inst0_O;
assign Mux2x4_inst0_I1 = DATA;
assign Mux2x4_inst0_S = LOAD;
Mux2x4 Mux2x4_inst0 (
    .I0(Mux2x4_inst0_I0),
    .I1(Mux2x4_inst0_I1),
    .S(Mux2x4_inst0_S),
    .O(Mux2x4_inst0_O)
);
assign Register4_inst0_I = Mux2x4_inst0_O;
assign Register4_inst0_CLK = CLK;
Register4 Register4_inst0 (
    .I(Register4_inst0_I),
    .O(O),
    .CLK(Register4_inst0_CLK)
);
endmodule

