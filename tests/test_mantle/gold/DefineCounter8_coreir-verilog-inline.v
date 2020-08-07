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

module Add8_cout (
    input [7:0] I0,
    input [7:0] I1,
    output [7:0] O,
    output COUT
);
wire [8:0] coreir_add9_inst0_out;
assign coreir_add9_inst0_out = 9'(({1'b0,I0[7:0]}) + ({1'b0,I1[7:0]}));
assign O = coreir_add9_inst0_out[7:0];
assign COUT = coreir_add9_inst0_out[8];
endmodule

module Counter8_COUT (
    output [7:0] O,
    output COUT,
    input CLK
);
wire [7:0] Add8_cout_inst0_I0;
wire [7:0] Add8_cout_inst0_I1;
wire [7:0] Add8_cout_inst0_O;
wire reg_P_inst0_clk;
wire [7:0] reg_P_inst0_in;
assign Add8_cout_inst0_I0 = O;
assign Add8_cout_inst0_I1 = 8'h01;
Add8_cout Add8_cout_inst0 (
    .I0(Add8_cout_inst0_I0),
    .I1(Add8_cout_inst0_I1),
    .O(Add8_cout_inst0_O),
    .COUT(COUT)
);
assign reg_P_inst0_clk = CLK;
assign reg_P_inst0_in = Add8_cout_inst0_O;
coreir_reg #(
    .clk_posedge(1'b1),
    .init(8'h00),
    .width(8)
) reg_P_inst0 (
    .clk(reg_P_inst0_clk),
    .in(reg_P_inst0_in),
    .out(O)
);
endmodule

