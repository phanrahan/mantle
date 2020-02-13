import magma as m
from magma.testing import check_files_equal
import mantle
import pytest


@pytest.mark.parametrize("T", [m.Tuple[m.Bit, m.Bits[2]],
                               m.Array[2, m.Tuple[m.Bit, m.Bits[2]]]])
def test_coreir_mux_complex(T):
    class Main(m.Circuit):
        IO = [
            "I0", m.In(T),
            "I1", m.In(T),
            "S", m.In(m.Bit),
            "O", m.Out(T)
        ]
        @classmethod
        def definition(circuit):
            MuxT = mantle.DefineMux(2, T=type(circuit.I0))
            circuit.O @= MuxT()(circuit.I0, circuit.I1, circuit.S)

    T_str = str(T).replace("[", "").replace("]", "").replace("(", "")\
                  .replace(")", "").replace(",", "").replace(" ", "")
    m.compile(f"build/test_coreir_mux_{T_str}", Main)
    check_files_equal(__file__, f"build/test_coreir_mux_{T_str}.v",
                      f"gold/test_coreir_mux_{T_str}.v")
