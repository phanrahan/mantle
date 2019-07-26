from magma import *
from hwtypes import BitVector
from magma.frontend.coreir_ import CircuitInstanceFromGeneratorWrapper, GetCoreIRBackend
from .register import register


def gen_sim_mem(depth, width):
    addr_width = getRAMAddrWidth(depth)
    def sim_mem(self, value_store, state_store):
        cur_clk = value_store.get_value(self.clk)

        if not state_store:
            state_store['mem'] = [
                BitVector[width](0) for _ in range(depth)
            ]
            state_store['prev_clk'] = cur_clk


        prev_clk = state_store['prev_clk']
        clk_edge = cur_clk and not prev_clk
        rdata = value_store.get_value(self.rdata)

        if clk_edge:
            index = BitVector[addr_width](value_store.get_value(self.raddr)).as_int()
            rdata = state_store['mem'][index].as_bool_list()
        if clk_edge:
            if value_store.get_value(self.wen):
                index = BitVector[addr_width](value_store.get_value(self.waddr)).as_int()
                state_store['mem'][index] = BitVector[width](value_store.get_value(self.wdata))

        state_store['prev_clk'] = cur_clk
        value_store.set_value(self.rdata, rdata)
    return sim_mem


def DefineCoreirMem(depth, width):
    name = "coreir_mem{}x{}".format(depth,width)
    addr_width = getRAMAddrWidth(depth)
    IO = ["raddr", In(Bits[ addr_width ]),
          "rdata", Out(Bits[ width ]),
          "waddr", In(Bits[ addr_width ]),
          "wdata", In(Bits[ width ]),
          "clk", In(Clock),
          "wen", In(Bit) ]
    return DeclareCircuit(name, *IO, verilog_name="coreir_mem",
            coreir_name="mem", coreir_lib="coreir",
            simulate=gen_sim_mem(depth, width),
            coreir_genargs={"width": width, "depth": depth})
            # coreir_configargs={"init": "0"})

def CoreirMem(depth, width):
    return CircuitInstanceFromGeneratorWrapper(GetCoreIRBackend(), "coreir", "mem", "CoreIRmem_w{}_d{}".format(width, depth),
                                               ["global"], {"width": width, "depth": depth})

def DefineROM(height, width,read_latency=0):
    """
    coreir doesn't have a ROM primitive yet
    """
    raise NotImplementedError()

def getRAMAddrWidth(height):
    return max((height - 1).bit_length(), 1)

def DefineRAM(height, width, read_latency=0):
    addr_width = getRAMAddrWidth(height)
    circ = DefineCircuit("RAM{}x{}".format(height, width),
        "RADDR", In(Bits[ addr_width ]),
        "RDATA", Out(Bits[ width ]),
        "WADDR", In(Bits[ addr_width ]),
        "WDATA", In(Bits[ width ]),
        "CLK",   In(Clock),
        "WE",    In(Bit),
    )
    coreir_mem = DefineCoreirMem(height, width)()
    wire(circ.RADDR, coreir_mem.raddr)
    wire(circ.CLK, coreir_mem.clk)
    wire(circ.WADDR, coreir_mem.waddr)
    wire(circ.WDATA, coreir_mem.wdata)
    wire(circ.WE, coreir_mem.wen)
    
    #Register chain for memory
    rd_out = coreir_mem.rdata
    for i in range(read_latency):
        rd_out = register(rd_out)
    wire(circ.RDATA, rd_out)
    
    EndDefine()
    return circ

def DefineMemory(height, width, readonly=False, read_latency=0):
    if read_latency < 0:
        raise ValueError("read_latency cannot be negative")
    if readonly:
        return DefineROM(height, width, read_latency)
    else:
        return DefineRAM(height, width, read_latency)
