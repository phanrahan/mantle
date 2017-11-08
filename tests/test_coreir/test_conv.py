import os
os.environ['MANTLE'] = 'coreir'
from magma import *
from magma.testing import check_files_equal
from mantle import *
import mantle.coreir

@cache_definition
def Define_mantle_reg_U6(init):
  class mantle_reg_U6(Circuit):
    name = f"mantle_reg_U6_{init}"
    IO = ["in", Array(4,In(Bit)), "clk", In(Clock), "out", Array(4,Out(Bit)), "en", In(Bit)]
    @classmethod
    def definition(io):
      enMux = mantle.coreir.DefineCoreirMux(width=4)(name="enMux")
      reg0 = mantle.coreir.DefineCoreirReg(init=init, width=4)(name="reg0")
      wire(getattr(enMux, "in0"), getattr(reg0, "out"))
      wire(getattr(enMux, "in1"), getattr(io, "in"))
      wire(getattr(reg0, "in"), getattr(enMux, "out"))
      wire(getattr(enMux, "sel"), getattr(io, "en"))
      wire(getattr(reg0, "clk"), getattr(io, "clk"))
      wire(getattr(io, "out"), getattr(reg0, "out"))
  return mantle_reg_U6

class commonlib_LinebufferMem_U5(Circuit):
  name = "commonlib_LinebufferMem_U5"
  IO = ["clk", In(Clock), "rdata", Array(16,Out(Bit)), "valid", Out(Bit), "wdata", Array(16,In(Bit)), "wen", In(Bit)]
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
    wire(getattr(add_r, "in0"), getattr(raddr, "out"))
    wire(getattr(add_r, "in1"), getattr(c1, "out"))
    wire(getattr(raddr_eq, "in0"), getattr(add_r, "out"))
    wire(getattr(raddr_mux, "in0"), getattr(add_r, "out"))
    wire(getattr(add_w, "in0"), getattr(waddr, "out"))
    wire(getattr(add_w, "in1"), getattr(c1, "out"))
    wire(getattr(waddr_eq, "in0"), getattr(add_w, "out"))
    wire(getattr(waddr_mux, "in0"), getattr(add_w, "out"))
    wire(getattr(raddr_eq, "in1"), getattr(max_const, "out"))
    wire(getattr(waddr_eq, "in1"), getattr(max_const, "out"))
    wire(getattr(mem, "clk"), getattr(io, "clk"))
    wire(getattr(mem, "raddr"), getattr(raddr, "out"))
    wire(getattr(io, "rdata"), getattr(mem, "rdata"))
    wire(getattr(mem, "waddr"), getattr(waddr, "out"))
    wire(getattr(mem, "wdata"), getattr(io, "wdata"))
    wire(getattr(mem, "wen"), getattr(io, "wen"))
    wire(getattr(raddr, "clk"), getattr(io, "clk"))
    wire(getattr(raddr, "en"), getattr(io, "wen"))
    wire(getattr(raddr, "in"), getattr(raddr_mux, "out"))
    wire(getattr(veq, "in0"), getattr(raddr, "out"))
    wire(getattr(raddr_mux, "sel"), getattr(raddr_eq, "out"))
    wire(getattr(raddr_mux, "in1"), getattr(zero_const, "out"))
    wire(getattr(waddr, "clk"), getattr(io, "clk"))
    wire(getattr(io, "valid"), getattr(veq, "out"))
    wire(getattr(waddr, "en"), getattr(io, "wen"))
    wire(getattr(veq, "in1"), getattr(waddr, "out"))
    wire(getattr(waddr, "in"), getattr(waddr_mux, "out"))
    wire(getattr(waddr_mux, "sel"), getattr(waddr_eq, "out"))
    wire(getattr(waddr_mux, "in1"), getattr(zero_const, "out"))

class commonlib_Linebuffer_U3(Circuit):
  name = "commonlib_Linebuffer_U3"
  IO = ["clk", In(Clock), "in", Array(16,In(Bit)), "wen", In(Bit), "out", Array(2,Array(1,Array(16,Out(Bit))))]
  @classmethod
  def definition(io):
    mem_1 = commonlib_LinebufferMem_U5()
    mem_1_valid_term = mantle.coreir.DefineCorebitTerm()(name="mem_1_valid_term")
    wire(getattr(io, "out")[0][0], getattr(mem_1, "rdata"))
    wire(getattr(mem_1_valid_term, "in"), getattr(mem_1, "valid"))
    wire(getattr(mem_1, "wdata"), getattr(io, "in"))
    wire(getattr(mem_1, "wen"), getattr(io, "wen"))
    wire(getattr(io, "out")[1][0], getattr(io, "in"))

class mantle_wire_U0(Circuit):
  name = "mantle_wire_U0"
  IO = ["in", Array(16,In(Bit)), "out", Array(16,Out(Bit))]
  @classmethod
  def definition(io):
    wire(getattr(io, "out"), getattr(io, "in"))

class global_DesignTop(Circuit):
  name = "global_DesignTop"
  IO = ["clk", In(Clock), "in", Array(1,Array(16,In(Bit))), "out", Array(16,Out(Bit))]
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
    wire(getattr(_336_pt, "in"), getattr(lb_p4_clamped_stencil_update_stream, "out")[0][0])
    wire(getattr(mul_337_338_339, "in0"), getattr(_336_pt, "out"))
    wire(getattr(_341_pt, "in"), getattr(lb_p4_clamped_stencil_update_stream, "out")[1][0])
    wire(getattr(mul_342_338_343, "in0"), getattr(_341_pt, "out"))
    wire(getattr(add_335_339_340, "in0"), getattr(const0__334, "out"))
    wire(getattr(add_335_339_340, "in1"), getattr(mul_337_338_339, "out"))
    wire(getattr(add_335_343_344, "in0"), getattr(add_335_339_340, "out"))
    wire(getattr(add_335_343_344, "in1"), getattr(mul_342_338_343, "out"))
    wire(getattr(io, "out"), getattr(add_335_343_344, "out"))
    wire(getattr(mul_337_338_339, "in1"), getattr(const7__338, "out"))
    wire(getattr(mul_342_338_343, "in1"), getattr(const7__338__ds__1, "out"))
    wire(getattr(lb_p4_clamped_stencil_update_stream, "clk"), getattr(io, "clk"))
    wire(getattr(lb_p4_clamped_stencil_update_stream, "in"), getattr(io, "in")[0])
    wire(getattr(lb_p4_clamped_stencil_update_stream, "wen"), getattr(lb_p4_clamped_stencil_update_stream_wen, "out"))

def test_conv():
    compile("build/test_coreir_conv", global_DesignTop, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_conv.json", "gold/test_coreir_conv.json")
