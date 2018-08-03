import magma as m
from mantle.types import ReadyValid

def test_ready_valid():
    data = m.Tuple(a=m.Bit,b=m.Bits(5))
    rv = ReadyValid(data)
    check = m.Tuple(
      ready=m.BitIn,
      valid=m.BitOut,
      data=m.Tuple(a=m.BitOut,b=m.Out(m.Bits(5)))
    )
    assert rv == check

#if __name__ == "__main__":
#    test_ready_valid()
