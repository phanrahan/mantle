module or8_wrapped (input [7:0] I0, input [7:0] I1, output [7:0] O);
wire [7:0] inst0_out;
coreir_or inst0 (.in0(I0), .in1(I1), .out(inst0_out));
assign O = inst0_out;
endmodule

