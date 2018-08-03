from magma import *
from mantle.types import AxiPort

def test_axi_type():
  t = Tuple(
    S2M=Tuple(
      gp0=Flip(AxiPort(32,32,12)),
      gp1=Flip(AxiPort(32,32,12)),
    ),
    M2S=Tuple(
      gp0=AxiPort(32,32,6),
      gp1=AxiPort(32,32,6),
      hp0=AxiPort(64,32,6),
      hp1=AxiPort(64,32,6),
      hp2=AxiPort(64,32,6),
      hp3=AxiPort(64,32,6),
      acp=AxiPort(64,32,3),
    )
  )
  print(t)
  #Not quite sure exactly what to test other than that it can compile correctly. 
  #Ideally in the future we can hook it up directly to a known axi-port like the ps7


if __name__ == "__main__":
    test_axi_type()
