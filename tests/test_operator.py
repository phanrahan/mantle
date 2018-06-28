import pytest
import magma as m
m.set_mantle_target("ice40")
import mantle
from magma.testing import check_files_equal


@pytest.mark.parametrize("op_name", [
    "and_",
    "nand",
    "or_",
    "nor",
    "xor",
    "nxor"
])
@pytest.mark.parametrize("N", [4])
@pytest.mark.parametrize("T,TType", [(m.UInt, m.UIntType), (m.SInt, m.SIntType), (m.Bits, m.BitsType)])
def test_binary_logic_op(op_name, N, T, TType):
    op = getattr(mantle, op_name)
    # T = m.Bits
    def to_str(x):
        if callable(x):
            return x.__name__
        return str(x)
    _name = "TestsCircuit_" + "_".join(to_str(x) for x in (op_name, N, T, TType))
    class TestCircuit(m.Circuit):
        name = _name
        IO = ["I0", m.In(T(N)), "I1", m.In(T(N)),
              "O", m.Out(T(N))]
        @classmethod
        def definition(io):
            res = op(io.I0, io.I1)
            assert isinstance(res, TType), type(res)
            m.wire(res, io.O)

    m.compile(f'build/{_name}', TestCircuit)
    assert check_files_equal(__file__,
            f"build/{_name}.v", f"gold/{_name}.v")
