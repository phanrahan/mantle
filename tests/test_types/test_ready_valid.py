import magma as m
from mantle.types import ReadyValid

def test_ready_valid():
    data = m.Tuple(a=m.Bit,b=m.Bits(5))
    rv = ReadyValid(data,False,"bits")
    check = m.Tuple(
      ready=m.BitIn,
      valid=m.BitOut,
      bits=m.Tuple(a=m.BitOut,b=m.Out(m.Bits(5)))
    )
    assert rv == check

    data = m.Tuple(a=m.Bit,b=m.Bits(5))
    rv = ReadyValid(data,flatten=True)
    check = m.Tuple(
      ready=m.BitIn,
      valid=m.BitOut,
      a=m.BitOut,
      b=m.Out(m.Bits(5))
    )
    assert rv == check


if __name__ == "__main__":
    test_ready_valid()
