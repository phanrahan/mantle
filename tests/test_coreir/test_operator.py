import pytest
import magma as m
import mantle
from magma.testing import check_files_equal
from collections import namedtuple
import fault
from bit_vector import BitVector

op = namedtuple("op", ["name", "operator"])


@pytest.mark.parametrize("op", [
    op(name="invert", operator="~"),
    op(name="neg", operator="-"),
])
@pytest.mark.parametrize("N", [4])
@pytest.mark.parametrize("T,TType", [(m.Bit, m.BitType),
                                     (m.UInt, m.UIntType),
                                     (m.SInt, m.SIntType),
                                     (m.Bits, m.BitsType)])
def test_unary_op(op, N, T, TType):
    """
    Tests mantle.operator by using the operator.{op.name} method directly and
    using the overloaded {op.operator} if it is not None.
    """
    if op.name == "neg" and T not in (m.UInt, m.SInt):
        return

    def to_str(x):
        if callable(x):
            return x.__name__
        return str(x)
    _name = "TestsCircuit_" + \
        "_".join(to_str(x) for x in (op.name, N, T, TType))
    # List of comparison ops so we can special case them (output type and
    # wiring 0)
    comparisons = ["lt", "le", "gt", "ge"]
    if op.name in comparisons + ["eq", "ne"] or T is m.Bit:
        out_T = m.Out(m.Bit)
        expected_res_type = m.BitType
    else:
        out_T = m.Out(T(N))
        expected_res_type = TType

    if T is m.Bit:
        in_T = m.Bit
    else:
        in_T = T(N)

    class TestCircuit(m.Circuit):
        name = _name
        IO = ["I", m.In(in_T), "O0", out_T, "O1", out_T]

        @classmethod
        def definition(io):
            # Test using the method directly
            res = getattr(mantle, op.name)(io.I)
            assert isinstance(res, expected_res_type), type(res)
            m.wire(res, io.O0)
            # Test using the operator if it exists, otherwise wire 0 to O1
            if op.operator is None or (
                    op.name in ["sub", "add"] + comparisons and T == m.Bits):
                if op.name in comparisons:
                    m.wire(0, io.O1)
                else:
                    m.wire(m.bits(0, N), io.O1)
            else:
                res_operator = eval(f"{op.operator} io.I")
                m.wire(res_operator, io.O1)

    m.compile(f'build/{_name}', TestCircuit, output="coreir")
    assert check_files_equal(__file__, f"build/{_name}.json",
                             f"gold/{_name}.json")


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
    op(name="mul", operator="*"),
    op(name="udiv", operator="/"),
    op(name="sdiv", operator="/"),
    op(name="umod", operator="%"),
    op(name="smod", operator="%"),
    op(name="eq", operator="=="),
    op(name="ne", operator="!="),
    op(name="lt", operator="<"),
    op(name="le", operator="<="),
    op(name="gt", operator=">"),
    op(name="ge", operator=">="),
])
@pytest.mark.parametrize("N", [4])
@pytest.mark.parametrize("T,TType", [(m.UInt, m.UIntType),
                                     (m.SInt, m.SIntType),
                                     (m.Bits, m.BitsType)])
def test_binary_op(op, N, T, TType):
    """
    Tests mantle.operator by using the operator.{op.name} method directly and
    using the overloaded {op.operator} if it is not None.
    """

    if op.name in ["mul"] and T not in (m.UInt, m.SInt):
        pytest.skip(f"{op.name} only defined for m.UInt and m.SInt")
    if op.name in ["udiv", "umod"] and T != m.UInt:
        pytest.skip(f"{op.name} only defined for m.UInt")
    elif op.name in ["sdiv", "smod"] and T != m.SInt:
        pytest.skip(f"{op.name} only defined for m.SInt")
    def to_str(x):
        if callable(x):
            return x.__name__
        return str(x)
    _name = "TestsCircuit_" + \
        "_".join(to_str(x) for x in (op.name, N, T, TType))
    # List of comparison ops so we can special case them (output type and
    # wiring 0)
    comparisons = ["lt", "le", "gt", "ge"]
    if op.name in comparisons + ["eq", "ne"]:
        out_T = m.Out(m.Bit)
        expected_res_type = m.BitType
    else:
        out_T = m.Out(T(N))
        expected_res_type = TType

    class TestCircuit(m.Circuit):
        name = _name
        IO = ["I0", m.In(T(N)), "I1", m.In(T(N)),
              "O0", out_T, "O1", out_T, "O2", out_T]

        @classmethod
        def definition(io):
            # Test using the method directly
            res = getattr(mantle, op.name)(io.I0, io.I1)
            assert isinstance(res, expected_res_type), type(res)
            m.wire(res, io.O0)
            # Test using the operator if it exists, otherwise wire 0 to O1
            if op.operator is None or (
                    op.name in ["sub", "add"] + comparisons and T == m.Bits):
                if op.name in comparisons:
                    m.wire(0, io.O1)
                else:
                    m.wire(m.bits(0, N), io.O1)
            else:
                res_operator = eval(f"io.I0 {op.operator} io.I1")
                m.wire(res_operator, io.O1)
            # Test integer promotion
            res = getattr(mantle, op.name)(io.I0, 1)
            m.wire(res, io.O2)

    m.compile(f'build/{_name}', TestCircuit, output="coreir")
    assert check_files_equal(__file__, f"build/{_name}.json",
                             f"gold/{_name}.json")


def test_dyanmic_mux_getitem():
    class TestDynamicMuxGetItem(m.Circuit):
        IO = ["I", m.In(m.Bits(2)), "S", m.In(m.Bit), "O", m.Out(m.Bit)]

        @classmethod
        def definition(io):
            m.wire(io.O, io.I[io.S])
    m.compile("build/test_dynamic_mux_getitem", TestDynamicMuxGetItem,
              output="coreir")
    assert check_files_equal(__file__, f"build/test_dynamic_mux_getitem.json",
                             f"gold/test_dynamic_mux_getitem.json")

    tester = fault.Tester(TestDynamicMuxGetItem)
    tester.poke(TestDynamicMuxGetItem.I, BitVector(2, 2))
    tester.poke(TestDynamicMuxGetItem.S, 0)
    tester.expect(TestDynamicMuxGetItem.O, 0)
    tester.eval()
    tester.expect(TestDynamicMuxGetItem.O, 0)
    tester.poke(TestDynamicMuxGetItem.S, 1)
    tester.eval()
    tester.expect(TestDynamicMuxGetItem.O, 1)
    tester.compile_and_run(target='coreir')
