from magma import *
from magma.bit_vector import BitVector
from mantle.coreir.MUX import Mux
import coreir


def gen_sim_register(N, init, has_ce):
    def sim_register(self, value_store, state_store):
        """
        Adapted from Brennan's SB_DFF simulation in mantle
        """
        cur_clock = value_store.get_value(self.clk)

        if not state_store:
            state_store['prev_clock'] = cur_clock
            state_store['cur_val'] = BitVector(init, num_bits=N) if N is not None else bool(init)

        # if has_reset:
        #     cur_reset = value_store.get_value(self.rst)
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
            input_val = value_store.get_value(getattr(self, "in"))

            enable = True
            if has_ce:
                enable = value_store.get_value(self.en)

            if enable:
                # if r and sy and cur_r:
                #     new_val = False
                # elif s and sy and cur_s:
                #     new_val = True
                # else:
                #     new_val = input_val
                new_val = input_val

        # if has_reset and not cur_reset:  # Reset is asserted low
        #     if N is not None:
        #         new_val = [False for _ in range(N)]
        #     else:
        #         new_val = None
        # if s and not sy and cur_s:
        #     new_val = True

        state_store['prev_clock'] = cur_clock
        state_store['cur_val'] = BitVector(new_val, num_bits=N) if N is not None else new_val
        value_store.set_value(self.out, new_val)
    return sim_register


def DefineCoreirReg(width, init=0, has_ce=False, has_reset=False, T=Bits):
    if width is None:
        width = 1
    name = "reg_P"  # TODO: Add support for clock interface
    config_args = {"init": coreir.type.BitVector(width, init)}
    gen_args = {"width": width}
    T = T(width)
    io = ["in", In(T), "clk", In(Clock), "out", Out(T)]
    methods = []

    def reset(self, condition):
        wire(condition, self.rst)
        return self

    if has_reset:
        io.extend(["rst", In(Reset)])
        name += "R"  # TODO: This assumes ordering of clock parameters
        methods.append(circuit_type_method("reset", reset))
        gen_args["has_rst"] = True

    def when(self, condition):
        wire(condition, self.en)
        return self

    if has_ce:
        io.extend(["en", In(Enable)])
        name += "E"  # TODO: This assumes ordering of clock parameters
        methods.append(circuit_type_method("when", when))
        gen_args["has_en"] = True

    # default_kwargs = gen_args.copy()
    default_kwargs = {"init": coreir.type.BitVector(width, init)}
    # default_kwargs.update(config_args)

    return DeclareCircuit(
        name,
        *io,
        stateful=True,
        simulate=gen_sim_register(width, init, has_ce),
        circuit_type_methods=methods,
        default_kwargs=default_kwargs,
        coreir_genargs=gen_args,
        coreir_configargs=config_args,
        coreir_name="reg",
        verilog_name="coreir_" + name,
        coreir_lib="mantle"
    )


@cache_definition
def DefineDFF(init=0, has_ce=False, has_reset=False):
    Reg = DefineCoreirReg(None, init, has_ce, has_reset)
    IO = ["I", In(Bit), "O", Out(Bit)] + ClockInterface(has_ce, has_reset)
    circ = DefineCircuit("DFF_init{}_has_ce{}_has_reset{}".format(init, has_ce, has_reset),
        *IO)
    reg = Reg()
    wiredefaultclock(circ, reg)
    wireclock(circ, reg)
    wire(circ.I, getattr(reg, "in")[0])
    wire(reg.out[0], circ.O)
    EndDefine()
    return circ




def DFF(init=0, has_ce=False, has_reset=False, **kwargs):
    return DefineDFF(init, has_ce, has_reset)(**kwargs)

FF = DFF
