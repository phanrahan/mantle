module coreir_undriven #(
    parameter width = 1
) (
    output [width-1:0] out
);

endmodule

module coreir_term #(
    parameter width = 1
) (
    input [width-1:0] in
);

endmodule

module corebit_term (
    input in
);

endmodule

module corebit_const #(
    parameter value = 1
) (
    output out
);
  assign out = value;
endmodule

module my_regfile (
    input ASYNCRESET,
    input CLK,
    input [1:0] read_0_addr,
    output [3:0] read_0_data,
    input [1:0] write_0_addr,
    input [3:0] write_0_data
);
wire bit_const_0_None_out;
wire my_regfile_inline_verilog_inst_0_I;
wire [1:0] term_inst0_in;
wire [3:0] term_inst1_in;
wire [1:0] term_inst2_in;
wire [3:0] undriven_inst0_out;
corebit_const #(
    .value(1'b0)
) bit_const_0_None (
    .out(bit_const_0_None_out)
);
assign my_regfile_inline_verilog_inst_0_I = bit_const_0_None_out;
assign term_inst0_in = read_0_addr;
coreir_term #(
    .width(2)
) term_inst0 (
    .in(term_inst0_in)
);
assign term_inst1_in = write_0_data;
coreir_term #(
    .width(4)
) term_inst1 (
    .in(term_inst1_in)
);
assign term_inst2_in = write_0_addr;
coreir_term #(
    .width(2)
) term_inst2 (
    .in(term_inst2_in)
);
coreir_undriven #(
    .width(4)
) undriven_inst0 (
    .out(undriven_inst0_out)
);
assign read_0_data = undriven_inst0_out;

reg [3:0] data [3:0];
always @(posedge CLK) begin
    data[write_0_addr] <= write_0_data;
end
assign read_0_data = write_0_addr == read_0_addr ? write_0_data : data[read_0_addr];


endmodule

module test_regfile_basic_verilog_True (
    input [1:0] write_addr,
    input [3:0] write_data,
    input [1:0] read_addr,
    output [3:0] read_data,
    input CLK,
    input ASYNCRESET
);
wire my_regfile_ASYNCRESET;
wire my_regfile_CLK;
wire [1:0] my_regfile_read_0_addr;
wire [3:0] my_regfile_read_0_data;
wire [1:0] my_regfile_write_0_addr;
wire [3:0] my_regfile_write_0_data;
assign my_regfile_ASYNCRESET = ASYNCRESET;
assign my_regfile_CLK = CLK;
assign my_regfile_read_0_addr = read_addr;
assign my_regfile_write_0_addr = write_addr;
assign my_regfile_write_0_data = write_data;
my_regfile my_regfile (
    .ASYNCRESET(my_regfile_ASYNCRESET),
    .CLK(my_regfile_CLK),
    .read_0_addr(my_regfile_read_0_addr),
    .read_0_data(my_regfile_read_0_data),
    .write_0_addr(my_regfile_write_0_addr),
    .write_0_data(my_regfile_write_0_data)
);
assign read_data = my_regfile_read_0_data;
endmodule

