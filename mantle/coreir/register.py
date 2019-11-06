import magma as m
from .FF import DefineCoreirReg, DefineDFF
import mantle


@m.cache_definition
def DefineRegister(n, init=0, has_ce=False, has_reset=False,
                   has_async_reset=False, has_async_resetn=False, _type=m.Bits,
                   reset_priority=True, ):
    if has_reset and (has_async_reset or has_async_resetn):
        raise ValueError("Cannot have synchronous and asynchronous reset")
    if has_async_resetn and has_async_reset:
        raise ValueError("Cannot have posedge and negedge asynchronous reset")

    if has_reset or has_ce:
        if n is None:
            T = m.Bit
        else:
            T = _type[n]
        class Register(m.Circuit):
            name = f"Register_has_ce_{has_ce}_has_reset_{has_reset}_" \
                   f"has_async_reset_{has_async_reset}_" \
                   f"has_async_resetn_{has_async_resetn}_" \
                   f"type_{_type.__name__}_n_{n}"
            IO = ["I", m.In(T), "O", m.Out(T)]
            IO += m.ClockInterface(has_ce=has_ce,
                                   has_reset=has_reset,
                                   has_async_reset=has_async_reset,
                                   has_async_resetn=has_async_resetn)

            @classmethod
            def definition(io):
                reg = DefineCoreirReg(n, init, has_async_reset,
                                      has_async_resetn, _type)(name="value")
                I = io.I
                O = reg.O
                if n is None:
                    O = O[0]
                if has_reset and has_ce:
                    if reset_priority:
                        I = mantle.mux([O, I], io.CE, name="enable_mux")
                        I = mantle.mux([I, m.bits(init, n)], io.RESET)
                    else:
                        I = mantle.mux([I, m.bits(init, n)], io.RESET)
                        I = mantle.mux([O, I], io.CE, name="enable_mux")
                elif has_ce:
                    I = mantle.mux([O, I], io.CE, name="enable_mux")
                elif has_reset:
                    I = mantle.mux([I, m.bits(init, n)], io.RESET)
                if n is None:
                    m.wire(I, reg.I[0])
                else:
                    m.wire(I, reg.I)
                m.wire(io.O, O)
                m.wireclock(io, reg)
                m.wiredefaultclock(io, reg)

        return Register
    elif n is None:
        if _type is not m.Bits:
            raise NotImplementedError()
        return DefineDFF(init, has_ce, has_async_reset=has_async_reset)
    else:
        return DefineCoreirReg(n, init, has_async_reset, has_async_resetn,
                               _type)


def Register(n, init=0, has_ce=False, has_reset=False, has_async_reset=False,
             has_async_resetn=False, _type = m.Bits, **kwargs):
    return DefineRegister(n, init, has_ce, has_reset, has_async_reset,
                          has_async_resetn=has_async_resetn, _type=_type)(**kwargs)


def register(I, ce=None, reset=None, async_reset=None, **kwargs):
    has_ce = ce is not None
    has_reset = reset is not None
    has_async_reset = async_reset is not None
    reg = Register(len(I),
                   has_ce=has_ce,
                   has_reset=has_reset,
                   has_async_reset=has_async_reset,
                   **kwargs)
    reg(I)
    if has_ce:
        m.wire(ce, reg.CE)
    if has_reset:
        m.wire(reset, reg.RESET)
    if has_async_reset:
        m.wire(reset, reg.ASYNCRESET)
    return reg.O
