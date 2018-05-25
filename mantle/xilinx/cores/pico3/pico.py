from magma import *
from mantle import *
from mantle.xilinx.spartan3.RAMB import ROMB
from mantle.xilinx.spartan3.RAM  import RAM16DxN
from .seq import DefineSequencer
from .alu import DefineLogic, DefineArith
from .io import Input, Output

ADDRN = 10
DATAN = 18
N = 8

Mux2 = DefineMux(2,N)
Sequencer = DefineSequencer(ADDRN)
Logic = DefineLogic(N)
Arith = DefineArith(N)

def pico(mem, inputs, outputs, step=1):

    # program memory
    print('creating program memory')
    rom = ROMB(mem, DATAN)
    inst = rom.O
    addr = inst[0:ADDRN]
    imm = inst[0:8]
    rb = inst[4:8]
    ra = inst[8:12]
    op = inst[14:16]

    # condition code registers
    print('creating z flag')
    z = DFF(ce=True)
    print('creating c flag')
    c = DFF(ce=True)

    print('creating register file')
    reg = RAM16DxN(N)

    print('creating logic unit')
    logicunit = Logic()

    print('creating arith unit')
    arithunit = Arith()

    print('creating sequencer')
    seq = Sequencer()

    # instruction decode
    print('creating insruction decoder')
    arithinst, logicinst, jump, push, pop, iflag, regwr, cwr, zwr, iord, iowr =\
        decode(inst,z,c,step)

    # sequencer
    print('wiring sequencer to program memory')
    rom(seq(1, jump, addr, push, pop, step))

    # register
    print('creating and wiring register omux')
    regomux = Mux2()
    raval, rbval = reg.O0, reg.O1
    regomux(imm, rbval, iflag)

    # alu
    print('creating and wiring arith/logic mux')
    alumux = Mux2()
    logicunit(raval, regomux, op[0], op[1])
    arithunit(raval, regomux, op[0], op[1])
    wire(c, arithunit.CIN )
    alumux(logicunit, arithunit, arithinst)

    # compute new z flag
    zval = Decode(0, N)
    print(zval.interface)

    if inputs:
        print('creating input')
        input = Input(N, inputs)
        input(regomux)

        print('creating and wiring register imux')
        regimux = Mux2()
        regimux(alumux, input, iord)

        print('wiring register file')
        reg(ra, rb, regimux, regwr)

        print('wiring z flag')
        z(zval(regimux), CE=zwr)
    else:
        print('wiring register file')
        reg(ra, rb, alumux, regwr)

        print('wiring z flag')
        z(zval(alumux), CE=zwr)

    if outputs:
        print('creating output')
        output = Output(N, outputs)
        output(regomux, raval, step, iowr)


    # compute new c flag
    cval = Logic2(A0 & A1)

    print('wiring c flag')
    c(cval(arithunit.COUT, arithinst), CE=cwr)



# 
# instruction decoder
#
def decode(inst, z, c, step):
    insttype = inst[16:18]
    op = inst[14:16]

    # ccflag -> test condition 
    # wflag -> write
    ccflag = wflag = inst[13] 

    # iflag determines whether immediate
    iflag = inst[12]  

    nflag = inst[11]  # negates condition
    zcflag = inst[10] # determine whether the condition is z or c

    # type of instruction
    logicinst = ROM2(1 << 0)(insttype) # 00
    arithinst = ROM2(1 << 1)(insttype) # 01
    aluinst   = ROM2((1 << 0) | (1 << 1))(insttype)
    ioinst    = ROM2(1 << 2)(insttype) # 10

    # control flow instructions: 11oo
    retinst  = Logic4(A0 & A1 &  A2 & ~A3) # 1110  
    retinst(insttype[0], insttype[1], op[0], op[1])
    jumpinst = Logic4(A0 & A1 & ~A2 &  A3) # 1101
    jumpinst(insttype[0], insttype[1], op[0], op[1])
    callinst = Logic4(A0 & A1 &  A2 &  A3) # 1111
    callinst(insttype[0], insttype[1], op[0], op[1])

    # is the condition met? 
    #   zcflag - predicate on z vs z
    #   nflag - not z or not c
    #   if zcflag: # predicate on z vs c
    #      return z if not nflag else not z
    #   else:
    #      return c if not nflag else not c
    expr = (~A0 & (A1^A2)) | (A0 & (A1^A3))
    cc = Logic4(expr)(zcflag, nflag, z, c)

    # goto the address 
    expr = (A0 | A1) & (~A2 | (A2 & A3)) # if not ccflag or (ccflag and cc)
    goto = Logic4(expr)(callinst, jumpinst, ccflag, cc)

    # push the current pc onto the stack if callinst and cc are true
    expr = A0 & (~A1 | (A1 & A3)) # if not ccflag or (ccflag and cc)
    push = Logic3(expr)(callinst, ccflag, cc)

    # pop the stack if retinst and conditions codes are true
    expr = A0 & (~A1 | (A1 & A3))
    pop = Logic3(expr)(retinst, ccflag, cc)


    # register write enable
    expr = A0 & ((A1&A2)|(~A1&A3))
    regwr = Logic4(expr)(step, wflag, aluinst, ioinst)

    # z write enable
    zwr = Logic2(A0 & A1)(step, aluinst)

    # c write enable
    cwr = Logic2(A0 & A1)(step, arithinst)

    # io read or write
    iord = Logic2(A0 & ~A1)(ioinst, wflag)
    iowr = Logic2(A0 &  A1)(ioinst, wflag)

    # control signals
    #  arithinst - arithmetic instruction
    #  logicinst - logic instruction
    #  goto - jump/call the address in the control instruction
    #  push - push pc onto the stack
    #  pop - pop pc from the stack
    #  iflag - immediate instruction
    #  regwr - write alu result register
    #  cwr - write carry flag
    #  zwr - write zero flag
    #  iord - read io register
    #  iowr - write to io register
    return arithinst, logicinst, goto, push, pop, iflag, regwr, cwr, zwr, iord, iowr

