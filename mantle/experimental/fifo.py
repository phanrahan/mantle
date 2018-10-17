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
                m.bit(True), mantle.mux([m.bit(False), is_full.O], do_deq & is_full.O)],
                do_enq & ~do_enq & (enq_ptr_inc == deq_ptr_inc))

            enq_ptr(mantle.mux([enq_ptr_inc, enq_ptr.O], do_enq))
            deq_ptr(mantle.mux([deq_ptr_inc, deq_ptr.O], do_deq))

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
