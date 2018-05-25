from magma import *
from mantle import *
from mantle.xilinx.spartan3.RAM import RAM16
from mantle.xilinx.spartan3.CLB import CARRY

__all__ = ['DefineSequencer']

#
# RAM :: A:Array(4,Bit), INCR:Bit, I: Array(4,Bit), WE:Bit -> O:Array(n,Bit)
#
# computes
#
#    O = ram16[A] + INCR
#    if WE:
#       ram16[A] = I
#
def RAM(n):

    # RAM16 + CIN
    def ram16(y):
        CIN = In(Bit)()
        ram = RAM16(0) # initialized to 0s
        O, COUT = CARRY(ram, ram, CIN) 

        return AnonymousCircuit("A",  ram.A,
                                "O", O,
                                "I",  ram.I, 
                                "WE", ram.WE,
                                "CIN",  CIN,
                                "COUT", COUT)

    ram = braid(col(ram16, n), foldargs={"CIN":"COUT"}, forkargs=['A', 'WE'])

    return AnonymousCircuit("A",  ram.A,
                            "INCR", ram.CIN,
                            "O", ram.O,
                            "I",  ram.I,
                            "WE", ram.WE)

#
# Build an sequencer with an n-bit program counter
#
# INCR:Bit, JUMP:Bit, ADDR:Array(n,Bit), PUSH:Bit, POP:Bit -> O : Array(n,Bit)
#
#    newsp = SP+PUSH-POP
#    newpc = ADDR if JUMP else RAM[newsp]+INCR
#    if WE:
#        RAM[newsp] = newpc
#        SP = newsp
#    O = newpc
#


def DefineSequencer(n):

    class _Sequencer(Circuit):
        name = 'Sequencer'+str(n)
        IO = ["incr", In(Bit),
              "jump", In(Bit),
              "addr", In(Array(n, Bit)),
              "push", In(Bit),
              "pop",  In(Bit),
              "we",   In(Bit),
              "pc",   Out(Array(n, Bit))] + ClockInterface()

        @classmethod
        def definition(seq):

            # create a 4-bit updown counter whose output is the next value
            # the value of this counter is the next value (not the current value)
            print('sequencer')
            newsp = UpDownCounter(4, next=True, ce=True)

            # create stack
            stack = RAM(n)

            # create input mux
            newpc = Mux(2,n)

            #  incr = push
            #  decr = pop
            #  return newsp + push - pop
            newsp(seq.push, seq.pop, CE=seq.we)

            #  return stack.O if not jump else addr
            newpc(stack, seq.addr, seq.jump)

            #  A = newsp
            #  I = newpc
            #  return stack[newsp] + incr
            stack(newsp, seq.incr, newpc, seq.we)

            wire(newpc.O, seq.pc)

    return _Sequencer

