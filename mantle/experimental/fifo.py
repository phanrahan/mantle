import magma as m
import mantle


def DefineFIFO(height, width):
    T = m.Bits(width)
    address_width = m.bitutils.clog2(height)
    class FIFO(m.Circuit):
        IO = ["enq_val", m.In(m.Bit),
              "enq_rdy", m.Out(m.Bit),
              "deq_val", m.Out(m.Bit),
              "deq_rdy", m.In(m.Bit),
              "enq_dat", m.In(T),
              "deq_dat", m.Out(T)] + m.ClockInterface()
        @classmethod
        def definition(io):
            enq_ptr = mantle.Register(address_width)
            deq_ptr = mantle.Register(address_width)
            is_full = mantle.FF()
            do_enq = ~is_full.O & io.enq_val

            is_empty = ~is_full.O & (enq_ptr.O == deq_ptr.O)
            do_deq = io.deq_rdy & ~is_empty

            deq_ptr_inc = m.uint(deq_ptr.O) + 1
            enq_ptr_inc = m.uint(enq_ptr.O) + 1
            is_full_next = mantle.mux([
                mantle.mux([is_full.O, m.bit(False)], do_deq & is_full.O), m.bit(True)],
                do_enq & ~do_deq & (enq_ptr_inc == deq_ptr.O))

            enq_ptr(mantle.mux([enq_ptr.O, enq_ptr_inc], do_enq))
            deq_ptr(mantle.mux([deq_ptr.O, deq_ptr_inc], do_deq))

            is_full(is_full_next)
            ram = mantle.DefineMemory(height, width)()
            m.wire(ram.RADDR, deq_ptr.O)
            m.wire(ram.RDATA, io.deq_dat)
            m.wire(ram.WADDR, enq_ptr.O)
            m.wire(ram.WDATA, io.enq_dat)
            m.wire(ram.WE, do_enq)
            m.wire(io.enq_rdy, ~is_full.O)
            m.wire(io.deq_val, ~is_empty)
    return FIFO

FIFO4x8 = DefineFIFO(4, 8)
m.compile('build/FIFO4x8', FIFO4x8)

import fault


tester = fault.Tester(FIFO4x8, FIFO4x8.CLK)

for i in range(0, 4):
    tester.poke(FIFO4x8.enq_val, 1)
    tester.poke(FIFO4x8.enq_dat, i)
    tester.step(2)

tester.poke(FIFO4x8.enq_val, 0)

for i in range(0, 4):
    tester.poke(FIFO4x8.deq_rdy, 1)
    tester.expect(FIFO4x8.deq_val, 1)
    tester.expect(FIFO4x8.deq_dat, i)
    tester.step(2)

tester.compile_and_run(target="verilator")
