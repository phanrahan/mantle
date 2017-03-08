from magma import *
from magma.compatibility import IntegerTypes

__all__ = ['DFF']
#__all__   = ['DFF', 'RSFF', 'SRFF', 'JKFF', 'TFF']
__all__  += ['FF', 'FFs']

_DFF = DefineCircuit('DFF', "D", In(Bit), "CLK", In(Bit), "Q", Out(Bit) )
_DFF.verilog = '''\
    always @(posedge CLK) begin
        Q <= D;
    end'''

def DFF(init=0, ce=False, r=False, s=False):
    ff = _DFF()

    args = ['I', ff.D, 'CLK', ff.CLK]
    if ce:
        args += ['CE', ff.E]
    if r:
        args += ['RESET', ff.R]
    if s:
        args += ['SET', ff.S]

    args += ['O', ff.Q]

    return AnonymousCircuit(args)


#
# Create a column of n FFs initialized to init
#
# Each FF may have a ce, r, and s signal.
#
def FFs(n, init=0, ce=False, r=False, s=False):
    if isinstance(init, IntegerTypes):
        init = int2seq(init, n)

    def f(y):
        return FF(init[y], ce=ce, r=r, s=s)

    return col(f, n)

FF = DFF
