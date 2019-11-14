from magma import *
import magma as m
from mantle.coreir.MUX import Mux
import coreir
from hwtypes import BitVector

from .util import DeclareCoreirCircuit

def gen_sim_register(N, init, has_ce, has_async_reset, has_async_resetn):
    def sim_register(self, value_store, state_store):
        """
        Adapted from Brennan's SB_DFF simulation in mantle
        """
        if has_async_resetn and has_async_reset:
            raise ValueError("Cannot have posedge and negedge asynchronous reset")
        cur_clock = value_store.get_value(self.CLK)

        if not state_store:
            state_store['prev_clock'] = cur_clock
            state_store['cur_val'] = BitVector[N](init) if N is not None else bool(init)

        if has_async_reset or has_async_resetn:
            cur_reset = value_store.get_value(self.arst)
        # if s:
        #     cur_s = value_store.get_value(self.S)

        prev_clock = state_store['prev_clock']
        # if not n:
        #     clock_edge = cur_clock and not prev_clock
        # else:
        #     clock_edge = not cur_clock and prev_clock
        clock_edge = cur_clock and not prev_clock

        new_val = state_store['cur_val'].as_bool_list() if N is not None else state_store['cur_val']

        if clock_edge:
            new_val = value_store.get_value(self.I)

        if has_async_reset and cur_reset or has_async_resetn and not cur_reset:
            new_val = BitVector[N](init) if N is not None else bool(init)
        # if s and not sy and cur_s:
        #     new_val = True

        state_store['prev_clock'] = cur_clock
        state_store['cur_val'] = BitVector[N](new_val) if N is not None else new_val
        value_store.set_value(self.O, new_val)
    return sim_register


@m.cache_definition
def DefineCoreirReg(width, init=0, has_async_reset=False,
                    has_async_resetn=False, T=Bits):
    if width is None:
        width = 1
    name = "reg_P"  # TODO: Add support for clock interface
    config_args = {"init": coreir.type.BitVector[width](init)}
    gen_args = {"width": width}
    T = T[width]
    io = ["I", In(T), "CLK", In(Clock), "O", Out(T)]
    methods = []

    def reset(self, condition):
        wire(condition, self.rst)
        return self

    if has_async_resetn and has_async_reset:
        raise ValueError("Cannot have posedge and negedge asynchronous reset")
    if has_async_reset:
        io.extend(["arst", In(AsyncResetIn)])
        name += "R"  # TODO: This assumes ordering of clock parameters
        config_args["arst_posedge"] = True
    if has_async_resetn:
        io.extend(["arst", In(AsyncResetNIn)])
        name += "R"  # TODO: This assumes ordering of clock parameters
        config_args["arst_posedge"] = False

    def when(self, condition):
        wire(condition, self.en)
        return self

    # if has_ce:
    #     io.extend(["en", In(Enable)])
    #     name += "E"  # TODO: This assumes ordering of clock parameters
    #     methods.append(circuit_type_method("when", when))
    #     gen_args["has_en"] = True

    # default_kwargs = gen_args.copy()
    default_kwargs = {"init": coreir.type.BitVector[width](init)}
    # default_kwargs.update(config_args)

    coreir_name = "reg_arst" if (has_async_reset or has_async_resetn) else "reg"

    return DeclareCoreirCircuit(
        name,
        *io,
        stateful=True,
        simulate=gen_sim_register(width, init, False, has_async_reset,
                                  has_async_resetn),
        circuit_type_methods=methods,
        default_kwargs=default_kwargs,
        coreir_genargs=gen_args,
        coreir_configargs=config_args,
        coreir_name=coreir_name,
        verilog_name="coreir_" + coreir_name,
        coreir_lib="coreir"
    )

def define_wrap(type_, type_name, in_type):
    def sim_wrap(self, value_store, state_store):
        input_val = value_store.get_value(getattr(self, "in"))
        value_store.set_value(self.out, input_val)

    return DeclareCircuit(
        f'coreir_wrap{type_name}',
        "in", In(in_type), "out", Out(type_),
        coreir_genargs = {"type": AsyncReset},
        coreir_name="wrap",
        coreir_lib="coreir",
        simulate=sim_wrap
    )

@m.cache_definition
def DefineDFF(init=0, has_ce=False, has_reset=False, has_async_reset=False, has_async_resetn=False):
    Reg = DefineCoreirReg(None, init, has_async_reset, has_async_resetn)
    IO = ["I", In(Bit), "O", Out(Bit)]
    IO += ClockInterface(has_ce=has_ce, has_reset=has_reset,
                         has_async_reset=has_async_reset,
                         has_async_resetn=has_async_resetn)
    circ = DefineCircuit("DFF_init{}_has_ce{}_has_reset{}_has_async_reset{}".format(
        init, has_ce, has_reset, has_async_reset, has_async_resetn),
        *IO)
    value = Reg()
    wiredefaultclock(circ, value)
    wireclock(circ, value)
    I = circ.I
    if has_reset and (has_async_reset or has_async_resetn):
        raise ValueError("Cannot have synchronous and asynchronous reset")
    if has_async_resetn and has_async_reset:
        raise ValueError("Cannot have posedge and negedge asynchronous reset")
    if has_reset:
        I = Mux()(circ.I, bit(init), circ.RESET)
    if has_ce:
        I = Mux()(value.O[0], I, circ.CE)
    wire(I, value.I[0])
    wire(value.O[0], circ.O)
    EndDefine()
    return circ




def DFF(init=0, has_ce=False, has_reset=False, has_async_reset=False, **kwargs):
    return DefineDFF(init, has_ce, has_reset, has_async_reset)(**kwargs)

FF = DFF
