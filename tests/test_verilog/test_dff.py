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
wire  DFF_inst0_Q;
DFF DFF_inst0 (.D(I), .CLK(CLK), .Q(DFF_inst0_Q));
assign O = DFF_inst0_Q;
endmodule

'''
  
