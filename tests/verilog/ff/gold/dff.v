module DFF (input  D, input  CLK, output  Q);
    always @(posedge CLK) begin
        Q <= D;
    end
endmodule

module main (input  I, output  O, input  CLK);
wire  inst0_Q;
DFF inst0 (.D(I), .CLK(CLK), .Q(inst0_Q));
assign O = inst0_Q;
endmodule

