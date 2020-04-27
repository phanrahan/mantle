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

module commonlib_muxn__N2__width4 (
    input [3:0] in_data_0,
    input [3:0] in_data_1,
    input [0:0] in_sel,
    output [3:0] out
);
assign out = in_sel[0] ? in_data_1 : in_data_0;
endmodule

module Mux2x4 (
    input [3:0] I0,
    input [3:0] I1,
    input S,
    output [3:0] O
);
commonlib_muxn__N2__width4 coreir_commonlib_mux2x4_inst0 (
    .in_data_0(I0),
    .in_data_1(I1),
    .in_sel(S),
    .out(O)
);
endmodule

module DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse (
    input I,
    output O,
    input CLK
);
wire [0:0] reg_P_inst0_out;
coreir_reg #(
    .clk_posedge(1'b1),
    .init(1'h0),
    .width(1)
) reg_P_inst0 (
    .clk(CLK),
    .in(I),
    .out(reg_P_inst0_out)
);
assign O = reg_P_inst0_out[0];
endmodule

module Register4 (
    input [3:0] I,
    output [3:0] O,
    input CLK
);
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_O;
wire DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_O;
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0 (
    .I(I[0]),
    .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst0_O),
    .CLK(CLK)
);
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1 (
    .I(I[1]),
    .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst1_O),
    .CLK(CLK)
);
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2 (
    .I(I[2]),
    .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst2_O),
    .CLK(CLK)
);
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3 (
    .I(I[3]),
    .O(DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse_inst3_O),
    .CLK(CLK)
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
assign coreir_add5_inst0_out = 5'(({1'b0,I0[3],I0[2],I0[1],I0[0]}) + ({1'b0,I1[3],I1[2],I1[1],I1[0]}));
assign O = {coreir_add5_inst0_out[3],coreir_add5_inst0_out[2],coreir_add5_inst0_out[1],coreir_add5_inst0_out[0]};
assign COUT = coreir_add5_inst0_out[4];
endmodule

module CounterLoad4_COUT (
    input [3:0] DATA,
    input LOAD,
    output [3:0] O,
    output COUT,
    input CLK
);
wire [3:0] Add4_cout_inst0_O;
wire [3:0] Mux2x4_inst0_O;
Add4_cout Add4_cout_inst0 (
    .I0(O),
    .I1(4'h1),
    .O(Add4_cout_inst0_O),
    .COUT(COUT)
);
Mux2x4 Mux2x4_inst0 (
    .I0(Add4_cout_inst0_O),
    .I1(DATA),
    .S(LOAD),
    .O(Mux2x4_inst0_O)
);
Register4 Register4_inst0 (
    .I(Mux2x4_inst0_O),
    .O(O),
    .CLK(CLK)
);
endmodule

