from magma import *
from magma.testing import check_files_equal
from mantle import *
import mantle.coreir

def Define_mantle_reg_U6(init):
  class mantle_reg_U6(Circuit):
    name = f"mantle_reg_U6_{init}"
    IO = ["I", Array[ 4,In(Bit) ], "clk", In(Clock), "O", Array[ 4,Out(Bit) ], "en", In(Bit)]
    @classmethod
    def definition(io):
      enMux = mantle.coreir.DefineCoreirMux(width=4)(name="enMux")
      reg0 = mantle.coreir.DefineCoreirReg(init=init, width=4)(name="reg0")
      wire(enMux.I0, reg0.O)
      wire(enMux.I1, io.I)
      wire(reg0.I, enMux.O)
      wire(enMux.S, io.en)
      wire(reg0.CLK, io.clk)
      wire(io.O, reg0.O)
  return mantle_reg_U6

class commonlib_LinebufferMem_U5(Circuit):
  name = "commonlib_LinebufferMem_U5"
  IO = ["clk", In(Clock), "rdata", Array[ 16,Out(Bit) ], "valid", Out(Bit), "wdata", Array[ 16,In(Bit) ], "wen", In(Bit)]
  @classmethod
  def definition(io):
    add_r = mantle.coreir.DefineCoreirAdd(width=4)(name="add_r")
    add_w = mantle.coreir.DefineCoreirAdd(width=4)(name="add_w")
    c1 = mantle.coreir.DefineCoreirConst(value=1, width=4)(name="c1")
    max_const = mantle.coreir.DefineCoreirConst(value=10, width=4)(name="max_const")
    mem = mantle.coreir.DefineCoreirMem(depth=10, width=16)(name="mem")
    raddr = Define_mantle_reg_U6(init=0)()
    raddr_eq = mantle.coreir.DefineCoreirEq(width=4)(name="raddr_eq")
    raddr_mux = mantle.coreir.DefineCoreirMux(width=4)(name="raddr_mux")
    veq = mantle.coreir.DefineCoreirNeq(width=4)(name="veq")
    waddr = Define_mantle_reg_U6(init=0)()
    waddr_eq = mantle.coreir.DefineCoreirEq(width=4)(name="waddr_eq")
    waddr_mux = mantle.coreir.DefineCoreirMux(width=4)(name="waddr_mux")
    zero_const = mantle.coreir.DefineCoreirConst(value=0, width=4)(name="zero_const")
    wire(add_r.I0, raddr.O)
    wire(add_r.I1, c1.O)
    wire(raddr_eq.I0, add_r.O)
    wire(raddr_mux.I0, add_r.O)
    wire(add_w.I0, waddr.O)
    wire(add_w.I1, c1.O)
    wire(waddr_eq.I0, add_w.O)
    wire(waddr_mux.I0, add_w.O)
    wire(raddr_eq.I1, max_const.O)
    wire(waddr_eq.I1, max_const.O)
    wire(mem.clk, io.clk)
    wire(mem.raddr, raddr.O)
    wire(io.rdata, mem.rdata)
    wire(mem.waddr, waddr.O)
    wire(mem.wdata, io.wdata)
    wire(mem.wen, io.wen)
    wire(raddr.clk, io.clk)
    wire(raddr.en, io.wen)
    wire(raddr.I, raddr_mux.O)
    wire(veq.I0, raddr.O)
    wire(raddr_mux.S, raddr_eq.O)
    wire(raddr_mux.I1, zero_const.O)
    wire(waddr.clk, io.clk)
    wire(io.valid, veq.O)
    wire(waddr.en, io.wen)
    wire(veq.I1, waddr.O)
    wire(waddr.I, waddr_mux.O)
    wire(waddr_mux.S, waddr_eq.O)
    wire(waddr_mux.I1, zero_const.O)

class commonlib_Linebuffer_U3(Circuit):
  name = "commonlib_Linebuffer_U3"
  IO = ["clk", In(Clock), "I", Array[ 16,In(Bit) ], "wen", In(Bit), "O", Array[ 2,Array[ 1,Array[ 16,Out(Bit) ] ] ]]
  @classmethod
  def definition(io):
    mem_1 = commonlib_LinebufferMem_U5()
    mem_1_valid_term = mantle.coreir.DefineCorebitTerm()(name="mem_1_valid_term")
    wire(io.O[0][0], mem_1.rdata)
    wire(mem_1_valid_term.I, mem_1.valid)
    wire(mem_1.wdata, io.I)
    wire(mem_1.wen, io.wen)
    wire(io.O[1][0], io.I)

class mantle_wire_U0(Circuit):
  name = "mantle_wire_U0"
  IO = ["I", Array[ 16,In(Bit) ], "O", Array[ 16,Out(Bit) ]]
  @classmethod
  def definition(io):
    wire(io.O, io.I)

class global_DesignTop(Circuit):
  name = "global_DesignTop"
  IO = ["clk", In(Clock), "I", Array[ 1,Array[ 16,In(Bit) ] ], "O", Array[ 16,Out(Bit) ]]
  @classmethod
  def definition(io):
    _336_pt = mantle_wire_U0()
    _341_pt = mantle_wire_U0()
    add_335_339_340 = mantle.coreir.DefineCoreirAdd(width=16)(name="add_335_339_340")
    add_335_343_344 = mantle.coreir.DefineCoreirAdd(width=16)(name="add_335_343_344")
    const0__334 = mantle.coreir.DefineCoreirConst(value=0, width=16)(name="const0__334")
    const7__338 = mantle.coreir.DefineCoreirConst(value=7, width=16)(name="const7__338")
    const7__338__ds__1 = mantle.coreir.DefineCoreirConst(value=7, width=16)(name="const7__338__ds__1")
    lb_p4_clamped_stencil_update_stream = commonlib_Linebuffer_U3()
    lb_p4_clamped_stencil_update_stream_wen = mantle.coreir.DefineCorebitConst(value=1)(name="lb_p4_clamped_stencil_update_stream_wen")
    mul_337_338_339 = mantle.coreir.DefineCoreirMul(width=16)(name="mul_337_338_339")
    mul_342_338_343 = mantle.coreir.DefineCoreirMul(width=16)(name="mul_342_338_343")
    wire(_336_pt.I, lb_p4_clamped_stencil_update_stream.O[0][0])
    wire(mul_337_338_339.I0, _336_pt.O)
    wire(_341_pt.I, lb_p4_clamped_stencil_update_stream.O[1][0])
    wire(mul_342_338_343.I0, _341_pt.O)
    wire(add_335_339_340.I0, const0__334.O)
    wire(add_335_339_340.I1, mul_337_338_339.O)
    wire(add_335_343_344.I0, add_335_339_340.O)
    wire(add_335_343_344.I1, mul_342_338_343.O)
    wire(io.O, add_335_343_344.O)
    wire(mul_337_338_339.I1, const7__338.O)
    wire(mul_342_338_343.I1, const7__338__ds__1.O)
    wire(lb_p4_clamped_stencil_update_stream.clk, io.clk)
    wire(lb_p4_clamped_stencil_update_stream.I, io.I[0])
    wire(lb_p4_clamped_stencil_update_stream.wen, lb_p4_clamped_stencil_update_stream_wen.O)

def test_conv():
    compile("build/test_coreir_conv", global_DesignTop, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_conv.json", "gold/test_coreir_conv.json")
