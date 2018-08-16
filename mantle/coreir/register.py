import magma as m
from .util import DeclareCoreirCircuit
from .FF import DefineCoreirReg
import mantle


@m.cache_definition
def DefineRegister(n, init=0, has_ce=False, has_reset=False,
                   has_async_reset=False, _type=m.Bits):
    T = _type(n)
    if has_reset and has_async_reset:
        raise ValueError("Cannot have synchronous and asynchronous reset")

    if has_reset or has_ce:
        class Register(m.Circuit):
            name = f"Register__has_ce_{has_ce}__has_reset_{has_reset}__" \
                   f"has_async_reset__{has_async_reset}__type_{_type.__name__}"
            IO = ["I", m.In(T), "clk", m.In(m.Clock), "O", m.Out(T)]
            @classmethod
            def definition(io):
                reg = DefineCoreirReg(n, init, has_async_reset, _type)()
                I = io.I
                if has_reset:
                    I = mantle.Mux(n)(circ.I, m.bits(init, n), circ.RESET)
                if has_ce:
                    I = Mux(n)(reg.O, I, circ.CE)
                m.wire(I, reg.I)
                m.wire(io.O, reg.O)
        return Register
    else:
        return DefineCoreirReg(n, init, has_async_reset, _type)
