import pytest
import magma as m
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
    op(name="sub", operator="-"),
    op(name="eq", operator=None),  # TODO: overload ==, causes issues when == used instead of is
    op(name="lt", operator="<"),
    op(name="le", operator="<="),
    op(name="gt", operator=">"),
    op(name="ge", operator=">="),
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
    # List of comparison ops so we can special case them (output type and
    # wiring 0)
    comparisons = ["eq", "lt", "le", "gt", "ge"]
    if op.name in comparisons:
        out_T = m.Out(m.Bit)
        expected_res_type = m.BitType
    else:
        out_T = m.Out(T(N))
        expected_res_type = TType
    class TestCircuit(m.Circuit):
        name = _name
        IO = ["I0", m.In(T(N)), "I1", m.In(T(N)),
              "O0", out_T, "O1", out_T]
        @classmethod
        def definition(io):
            # Test using the method directly
            res = getattr(mantle, op.name)(io.I0, io.I1)
            assert isinstance(res, expected_res_type), type(res)
            m.wire(res, io.O0)
            # Test using the operator if it exists, otherwise wire 0 to O1
            if op.operator is None or op.name in ["sub", "add"] + comparisons and T == m.Bits:
                if op.name in comparisons:
                    m.wire(0, io.O1)
                else:
                    m.wire(m.bits(0, N), io.O1)
            else:
                res_operator = eval(f"io.I0 {op.operator} io.I1")
                m.wire(res_operator,io.O1)

    m.compile(f'build/{_name}', TestCircuit)
    assert check_files_equal(__file__,
            f"build/{_name}.v", f"gold/{_name}.v")
