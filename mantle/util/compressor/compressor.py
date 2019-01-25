#
# Implementation of compressor trees
#
from magma import fork, cache_definition, DefineCircuit, EndDefine, In, Out, Bit, wire
from magma import mantle_target
if mantle_target == "ice40":
    from mantle import LUT2, LUT3, I0, I1, I2
else:
    from mantle import XOr, Or, And


__all__ = ['compressor']

n3to2s = 0
n2to2s = 0

if mantle_target == "ice40":
    def compress2to2():
        global n2to2s
        n2to2s = n2to2s + 1
        return fork([LUT2(I0^I1), LUT2((I0&I1)|(I1&I2))])

    def compress3to2():
        global n3to2s
        n3to2s = n3to2s + 1
        return fork([LUT3(I0^I1^I2), LUT3((I0&I1)|(I1&I2)|(I2&I0))])
else:
    def Define3to2Op():
        Op = DefineCircuit("_3to2Op", "I0", In(Bit), "I1", In(Bit), "I2", In(Bit), "O", Out(Bit))
        a = And(2)(Op.I0, Op.I1)
        b = And(2)(Op.I1, Op.I2)
        c = And(2)(Op.I2, Op.I0)
        d = Or(3)(a, b, c)
        wire(d, Op.O)
        EndDefine()
        return Op

    def compress3to2():
        global n3to2s
        n3to2s = n3to2s + 1
        Op = Define3to2Op()
        return fork([XOr(3), Op()])

# compress 2 and 3 bit groups in a column
def compresscolumn2(bits):
    n = len(bits)
    ones = []
    twos = []
    for i in range(0,n,3):
        if i+1 < n:
            c = compress3to2()
            c(bits[i], bits[i+1], 0 if i+2 >= n else bits[i+2])
            ones.append(c.O[0])
            twos.append(c.O[1])
        else:
            while i < n:
                ones.append(bits[i])
                i += 1
            break
    return twos, ones

# compress only 3 bit groups in a column
def compresscolumn3(bits):
    n = len(bits)
    ones = []
    twos = []
    for i in range(0,n,3):
        if i+2 < n:
            c = compress3to2()
            c(bits[i], bits[i+1], bits[i+2])
            ones.append(c.O[0])
            twos.append(c.O[1])
        else:
            while i < n:
                ones.append(bits[i])
                i += 1
            break
    return twos, ones


# compress only 3 bit groups in a column without ripple
def compress3(bits):
    res = []
    lasttwos = []
    for b in bits:
        twos, ones = compresscolumn3(b)
        res.append(ones + lasttwos)
        lasttwos = twos
    if len(lasttwos) > 0:
        res.append(lasttwos)
    return res

# ripple adder - assumes all the columns have at most 2 bits
def ripple(bits):
    res = []
    twos = []
    for b in bits:
        # ripple: combine last column of twos with this column
        b = b + twos
        # should only require fulladders (compress 3 to 2)
        assert len(b) <= 3
        twos, ones = compresscolumn2(b)
        res.append(ones)
    if len(twos) > 0:
        res.append(twos)
    return res


# returns True if there are any columns with more than 2 bits
def iscompressible(bits):
    for b in bits:
         if len(b) > 2:
             return True
    return False

def compressor(r):
    global n2to2s, n3to2s
    n3to2s = 0
    n2to2s = 0
    #print( list(map(len, r)) )
    while iscompressible(r):
        r = compress3(r)
        #print( list(map(len, r)) )
    r = ripple(r)
    #print( list(map(len, r)) )
    #print('n3to2s = {}'.format(n3to2s))
    return sum(r, [])

