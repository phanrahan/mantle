module LUT2 (input  I0, input  I1, output  O);
wire  inst0_OUT;
GP_2LUT #(.INIT(4'h8)) inst0 (.IN0(I0), .IN1(I1), .OUT(inst0_OUT));
assign O = inst0_OUT;
endmodule

