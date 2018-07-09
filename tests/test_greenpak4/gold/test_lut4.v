module LUT4 (input  I0, input  I1, input  I2, input  I3, output  O);
wire  inst0_OUT;
GP_4LUT #(.INIT(16'h8000)) inst0 (.IN0(I0), .IN1(I1), .IN2(I2), .IN3(I3), .OUT(inst0_OUT));
assign O = inst0_OUT;
endmodule

