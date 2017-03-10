from magma import *
from mantle import *

# 
# Ensure that the input is N-bits wide
#
def InputOne(input, N):
    #print('wiring', input)
    if isinstance(input, BitType):
        input = [input] + (N-1)*[GND]
        return array(*input)
    elif len(input) != N:
        return concat(input, (N-len(input))*[GND])
    return input

def Input(N, inputs):

    A = In(Array(N, Bit))()
    if isinstance(inputs, list):
        n = len(inputs)
        assert n in [2, 4, 8]
        for i in range(n): 
            inputs[i] = InputOne(inputs[i], N)
        if   n == 2:
            mux = Mux(2, N)
            mux(inputs[0], inputs[1], A[0])
        elif n == 4:
            mux = Mux(4, N)
            mux(inputs[0], inputs[1], inputs[2], inputs[3], A[0:2])
        elif n == 8:
            mux = Mux(8, N)
            mux(inputs[0], inputs[1], inputs[2], inputs[3],
                inputs[4], inputs[5], inputs[6], inputs[7], A[0:3])
        O = mux.O
    else:
        O = InputOne(inputs,N)

    return AnonymousCircuit("A", A, "O", O)


#
# Generate a register with the same number of bits as the output
#
def OutputOne(input, output, ce):
    #print('wiring', output)
    O = output.I
    if isinstance(O, BitType):
        output(input[0], CE=ce)
    else:
        N = len(O)
        #print('connecting', N, 'bits')
        output(input[0:N], CE=ce)

def Output(N, outputs):

    I = In(Array(N, Bit))()
    A = In(Array(N, Bit))()
    en = In(Bit)()
    wr = In(Bit)()

    if isinstance(outputs, list):
        for i,k in enumerate(outputs):
            ena = Decode(i, N)(A)
            ce = LUT3(I0 & I1 & I2)(en, wr, ena)
            OutputOne(I, k, ce)
    else:
        ce = LUT2(I0 & I1)(en, wr)
        OutputOne(I, outputs, ce)

    return AnonymousCircuit("A", A, "I", I, "EN", en, "WE", wr )

