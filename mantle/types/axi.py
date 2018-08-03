from magma import *
from . import ReadyValid

#Very similar to
#https://github.com/maltanar/axi-in-chisel

def axi_addr(addr_bits, id_bits):
  t = Tuple(
    addr=Bits(addr_bits),
    size=Bits(2),
    len=Bits(4),
    burst=Bits(2),
    id=Bits(id_bits),
    lock=Bits(2),
    cache=Bits(4),
    prot=Bits(3),
    qos=Bits(4),
  )
  return ReadyValid(t)

def axi_read_data(data_bits, id_bits):
  t = Tuple(
    data=Bits(data_bits),
    id=Bits(id_bits),
    last=Bit,
    resp=Bits(2),
  )
  return ReadyValid(t)
  
def axi_write_data(data_bits):
  t = Tuple(
    data=Bits(data_bits),
    strb=Bits(data_bits//8),
    last=Bit,
  )
  return ReadyValid(t)

def axi_write_response(id_bits):
  t = Tuple(
    id=Bits(id_bits),
    resp=Bits(2),
  )
  return ReadyValid(t)

#M2S Direction
def axi_read_port(data_bits,addr_bits,id_bits):
  return Tuple(
    addr=axi_addr(addr_bits,id_bits),
    data=Flip(axi_read_data(data_bits,id_bits))
  )

#M2S Direction
def axi_write_port(data_bits,addr_bits,id_bits):
  return Tuple(
    addr=axi_addr(addr_bits,id_bits),
    data=axi_write_data(data_bits),
    resp=Flip(axi_write_response(id_bits)),
  )


#M2S Direction
def axi_port(data_bits,addr_bits,id_bits):
  return Tuple(
    clk=In(Bit),
    read=axi_read_port(data_bits,addr_bits,id_bits),
    write=axi_write_port(data_bits,addr_bits,id_bits),
  )


