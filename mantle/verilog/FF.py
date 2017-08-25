from magma import DefineCircuit, EndCircuit, In, Out, Bit, Clock

__all__ = ['DFF', 'FF']

_DFF = DefineCircuit('DFF', "D", In(Bit), "CLK", In(Clock), "Q", Out(Bit) )
_DFF.verilog = '''\
    always @(posedge CLK) begin
        Q <= D;
    end'''
EndCircuit()

def DFF(init=0, has_ce=False, has_reset=False, has_set=False):
    ff = _DFF()

    #args = ['I', ff.D, 'CLK', ff.CLK]
    #if has_ce:
    #    args += ['CE', ff.E]
    #if has_reset:
    #    args += ['RESET', ff.R]
    #if has_set:
    #    args += ['SET', ff.S]
    #args += ['O', ff.Q]
    #return AnonymousCircuit(args)

    return ff

FF = DFF
