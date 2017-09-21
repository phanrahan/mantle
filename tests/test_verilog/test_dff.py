from magma import *
from magma.backend.verilog import compile
from mantle.verilog import DFF

def test_dff():
    main = DefineCircuit('main', 'I', In(Bit), "O", Out(Bit), "CLK", In(Clock))
    dff = DFF()
    wire(main.I, dff.D)
    wire(dff.Q, main.O)
    EndCircuit()

    assert compile(main) == '''\
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

'''
  
