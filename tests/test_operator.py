import pytest
import magma as m
m.set_mantle_target("coreir")
import mantle
from magma.testing import check_files_equal
from collections import namedtuple

op = namedtuple("op", ["name", "operator"])

@pytest.mark.parametrize("op", [
    op(name="and_", operator="&"),
    op(name="nand", operator=None),
    op(name="or_", operator="|"),
    op(name="nor", operator=None),
    op(name="xor", operator="^"),
    op(name="nxor", operator=None),
    op(name="lsl", operator="<<"),
    op(name="lsr", operator=">>"),
    op(name="asr", operator=None),
    op(name="add", operator="+"),
    op(name="sub", operator="-")
])
@pytest.mark.parametrize("N", [4])
@pytest.mark.parametrize("T,TType", [(m.UInt, m.UIntType), (m.SInt, m.SIntType), (m.Bits, m.BitsType)])
def test_binary_op(op, N, T, TType):
    """
    Tests mantle.operator by using the operator.{op.name} method directly and
    using the overloaded {op.operator} if it is not None.
    """
    def to_str(x):
        if callable(x):
            return x.__name__
        return str(x)
    _name = "TestsCircuit_" + "_".join(to_str(x) for x in (op.name, N, T, TType))
    class TestCircuit(m.Circuit):
        name = _name
        IO = ["I0", m.In(T(N)), "I1", m.In(T(N)),
              "O0", m.Out(T(N)), "O1", m.Out(T(N))]
        @classmethod
        def definition(io):
            # Test using the method directly
            res = getattr(mantle, op.name)(io.I0, io.I1)
            assert isinstance(res, TType), type(res)
            m.wire(res, io.O0)
            # Test using the operator if it exists, otherwise wire 0 to O1
            if op.operator is None or op.operator in ["-", "+"] and T == m.Bits:
                m.wire(m.bits(0, N), io.O1)
            else:
                res_operator = eval(f"io.I0 {op.operator} io.I1")
                m.wire(res_operator,io.O1)

    m.compile(f'build/{_name}', TestCircuit)
    assert check_files_equal(__file__,
            f"build/{_name}.v", f"gold/{_name}.v")


@pytest.mark.parametrize("op_name", [
    "eq",
    "lt",
    "le",
    "gt",
    "ge",
])
@pytest.mark.parametrize("N", [4])
@pytest.mark.parametrize("T", [m.UInt, m.SInt, m.Bits])
def test_comparison_op(op_name, N, T):
    op = getattr(mantle, op_name)
    def to_str(x):
        if callable(x):
            return x.__name__
        return str(x)
    _name = "TestsCircuit_" + "_".join(to_str(x) for x in (op_name, N, T))
    class TestCircuit(m.Circuit):
        name = _name
        IO = ["I0", m.In(T(N)), "I1", m.In(T(N)),
              "O", m.Out(m.Bit)]
        @classmethod
        def definition(io):
            res = op(io.I0, io.I1)
            assert isinstance(res, m.BitType), type(res)
            m.wire(res, io.O)

    m.compile(f'build/{_name}', TestCircuit)
    assert check_files_equal(__file__,
            f"build/{_name}.v", f"gold/{_name}.v")
