import magma as m
from magma.testing import check_files_equal
import fault
from hwtypes import BitVector


def test_dyanmic_mux_getitem():
    class TestDynamicMuxGetItem(m.Circuit):
        io = m.IO(I=m.In(m.Bits[ 2 ]), S=m.In(m.Bit), O=m.Out(m.Bit))

        @classmethod
        def definition(io):
            m.wire(io.O, io.I[io.S])
    m.compile("build/test_dynamic_mux_getitem", TestDynamicMuxGetItem,
              output="coreir")
    assert check_files_equal(__file__, f"build/test_dynamic_mux_getitem.json",
                             f"gold/test_dynamic_mux_getitem.json")

    tester = fault.Tester(TestDynamicMuxGetItem)
    tester.poke(TestDynamicMuxGetItem.I, BitVector[2](2))
    tester.poke(TestDynamicMuxGetItem.S, 0)
    tester.expect(TestDynamicMuxGetItem.O, 0)
    tester.eval()
    tester.expect(TestDynamicMuxGetItem.O, 0)
    tester.poke(TestDynamicMuxGetItem.S, 1)
    tester.eval()
    tester.expect(TestDynamicMuxGetItem.O, 1)
    tester.compile_and_run(target='coreir')
